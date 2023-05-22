import logging
import os
import urllib.parse

from django.conf import settings
from lti_consumer.lti_xblock import LtiConsumerXBlock, _
from xblock.core import Scope, String, XBlock
from xblockutils.resources import ResourceLoader


logger = logging.getLogger(__name__)


class JupyterXBlock(LtiConsumerXBlock):
    # Advanced component name
    display_name = String(
        display_name=_("Display Name"),
        help=_(
            "Enter the name that students see for this component. "
            "Analytics reports may also use the display name to identify this component."
        ),
        scope=Scope.settings,
        default=_("Jupyter notebook"),
    )

    # Jupyter git repo attributes
    nb_git_repo = String(
        display_name=_("Notebook git repository"),
        help="For example: https://github.com/overhangio/jupyter-xblock.git",
        default="https://github.com/overhangio/jupyter-xblock.git",
        scope=Scope.settings,
    )
    nb_git_branch = String(
        display_name=_("Notebook git branch"),
        default="main",
        scope=Scope.settings,
    )
    nb_git_file = String(
        display_name=_("Notebook file"),
        help="Path relative to the repository root",
        default="static/notebooks/hello.ipynb",
        scope=Scope.settings,
    )

    # LTI attributes
    lti_id = String(
        display_name=_("LTI ID"),
        help=LtiConsumerXBlock.lti_id.help,
        default=getattr(
            settings,
            "LTI_DEFAULT_JUPYTER_PASSPORT_ID",
            getattr(settings, "LTI_DEFAULT_PASSPORT_ID", "jupyterhub"),
        ),
        scope=Scope.settings,
    )
    hub_url = String(
        display_name=_("JupyterHub base URL"),
        help="""For example: https://hub.myopenedx.com""",
        default=getattr(
            settings,
            "LTI_DEFAULT_JUPYTER_HUB_URL",
            f"https://hub.{settings.LMS_BASE}",
        ),
        scope=Scope.settings,
    )

    # Limit the number of editable fields
    editable_field_names = (
        "display_name",
        "launch_target",
        "hub_url",
        "lti_id",
        "nb_git_repo",
        "nb_git_branch",
        "nb_git_file",
    )

    # Override base attributes
    @property
    def launch_url(self):
        """Infer launch URL from JupyterHub URL"""
        return f"{self.hub_url}/hub/lti/launch"

    @property
    def lti_version(self):
        """Always use LTI 1.1"""
        return "lti_1p1"

    @property
    def hub_url_base_path(self):
        path = urllib.parse.urlparse(self.hub_url).path
        return path.strip("/")

    @property
    def prefixed_custom_parameters(self):
        custom_parameters = super().prefixed_custom_parameters

        # Override `next=` custom parameter to follow the specs from nbgitpuller.
        # See: https://hub.jupyter.org/nbgitpuller/link
        next_query_params = {
            "repo": self.nb_git_repo,
            "branch": self.nb_git_branch,
            "urlpath": f"lab/tree/{os.path.basename(self.nb_git_repo)}/{self.nb_git_file}",
        }
        logger.info(
            "Fetching git repo=%s, branch=%s, urlpath=%s",
            next_query_params["repo"],
            next_query_params["branch"],
            next_query_params["urlpath"],
        )
        next_url = f"{self.hub_url_base_path}/hub/user-redirect/git-pull?{urllib.parse.urlencode(next_query_params)}"
        custom_parameters["next"] = next_url

        return custom_parameters

    # Fix student view
    @XBlock.supports("multi_device")
    def student_view(self, context):
        """
        Fix CSS, as the CSS rules defined in the base LTI XBlock do not apply to this
        one.
        """
        fragment = super().student_view(context)
        loader = ResourceLoader(__name__)
        fragment.add_css(loader.load_unicode("static/css/student.css"))
        return fragment
