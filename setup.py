import io
import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(here, "README.md"), "rt", encoding="utf8") as f:
    readme = f.read()

setup(
    name="jupyter-xblock",
    version="15.0.3",
    description="Jupyter XBlock for Open edX",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Overhang.IO",
    author_email="contact@overhang.io",
    maintainer="Overhang.IO",
    maintainer_email="regis@overhang.io",
    project_urls={
        "Documentation": "https://github.com/overhangio/jupyter-xblock",
        "Code": "https://github.com/overhangio/jupyter-xblock",
        "Issue tracker": "https://github.com/overhangio/jupyter-xblock/issues",
        "Community": "https://discuss.openedx.com",
    },
    packages=["jupyterxblock"],
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=["xblock", "web-fragments"],
    entry_points={"xblock.v1": ["jupyter = jupyterxblock.xblock:JupyterXBlock"]},
    license="AGPLv3",
    classifiers=["License :: OSI Approved :: GNU Affero General Public License v3"],
)
