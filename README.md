# Jupyter XBlock

This is an [XBlock](https://edx.readthedocs.io/projects/xblock-tutorial/en/latest/overview/introduction.html) to integrate JupyterHub notebooks to your [Open edX](https://openedx.org) learning management system (LMS).

Features:

* Integrate [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/) notebooks to the Open edX courseware.
* Fully editable notebooks and student workspaces.
* Simple integration of notebooks from public git repositories.

Here is a screenshot of the Jupyter XBlock in action:

![](https://raw.githubusercontent.com/overhangio/jupyter-xblock/main/static/screenshots/lms.png)

## Usage

Install this xblock with [Tutor](https://docs.tutor.overhang.io/) (Olive release):

    echo "jupyter-xblock>=15.0.0,<16.0.0" >> "$(tutor config printroot)/env/build/openedx/requirements/private.txt"
    tutor images build openedx
    tutor local start -d

In your course "Advanced Settings", add "jupyter" to the "Advanced Module List":

![Studio advanced module list](https://raw.githubusercontent.com/overhangio/jupyter-xblock/main/static/screenshots/studio-advanced-settings.png)

## Configuration

### JupyterHub base URL

The JupyterHub cluster can be configured separately for every XBlock, but this can be quite tedious for course instructors. Instead, a default JupyterHub cluster URL can be defined globally by adding the `LTI_DEFAULT_JUPYTER_HUB_URL` setting to both the LMS and CMS settings.

For instance:

    LTI_DEFAULT_JUPYTER_HUB_URL = "https://hub.myopenedx.com"

If this setting is undefined, the base URL will default to `https://hub.LMS_HOST`.

### LTI passport ID

Similarly, the LTI passport ID can be defined globally for all Jupyter XBlock instances. When a passport ID is not explicitely defined in an XBlock, it will default to the `LTI_DEFAULT_JUPYTER_PASSPORT_ID` setting. If this setting is also undefined, then it will default to `LTI_DEFAULT_PASSPORT_ID`. The fallback value is "jupyterhub".

To define a global LTI passport ID to be used by all Jupyter XBlock instances, add to your LMS/CMS settings:

    LTI_DEFAULT_JUPYTER_PASSPORT_ID = "myjupyterhub"

Then, the corresponding passport must be created in the course advanced settings, as described in the [Open edX documentation](https://edx.readthedocs.io/projects/open-edx-building-and-running-a-course/en/latest/exercises_tools/lti_component.html#creating-an-lti-passport-string):

![Studio advanced LTI settings](https://raw.githubusercontent.com/overhangio/jupyter-xblock/main/static/screenshots/studio-advanced-settings-lti.png)

## Configuring JupyterHub

You will have to launch your own JupyterHub cluster separately from Open edX. Your cluster should support:

- LTI authentication via [ltiauthenticator](https://github.com/jupyterhub/ltiauthenticator/).
- LTI authentication must accept the key and secret defined in the course LTI passport (see above).
- Pulling git repositories via [nbgitpuller](https://github.com/jupyterhub/nbgitpuller).
- Iframe embedding in your LMS/CMS, via the ["Content-Security-Policy"](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/frame-ancestors) header.

## Known limitations

* Grading is not supported at the moment.
* It is not possible to pull notebooks from a raw URL -- only from a public git repository.

## Troubleshooting

This XBlock was kickstarted by Matthew Brett ([@matthew-brett](https://github.com/matthew-brett)) and funded by a grant from the [Chan Zuckerberg Initiative](https://chanzuckerberg.com/). This project is maintained by Régis Behmo from [Overhang.IO](https://overhang.io). Community support is available from the official [Open edX forum](https://discuss.openedx.org).

## License

This work is licensed under the terms of the [GNU Affero General Public License (AGPL)](https://github.com/overhangio/jupyter-xblock/blob/master/LICENSE.txt).
