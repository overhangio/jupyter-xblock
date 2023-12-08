import io
import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(here, "README.md"), "rt", encoding="utf8") as f:
    readme = f.read()

setup(
    name="jupyter-xblock",
    version="17.0.0",
    description="Jupyter XBlock for Open edX",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Overhang.IO",
    author_email="contact@overhang.io",
    maintainer="Edly",
    maintainer_email="mhassan.eeng@gmail.com",
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
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
