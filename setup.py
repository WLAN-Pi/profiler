# -*- coding: utf-8 -*-

import os
from codecs import open

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

# load the package's __version__.py module as a dictionary
about = {}
with open(os.path.join(here, "profiler", "__version__.py"), "r", "utf-8") as f:
    exec(f.read(), about)

try:
    with open("README.md", "r") as f:
        readme = f.read()
except FileNotFoundError:
    readme = about["__description__"]

packages = ["profiler"]

requires = ["tox==3.23.1", "coverage-badge==1.0.1", "scapy==2.4.5", "manuf==1.1.1"]

setup(
    name=about["__title__"],
    version=about["__version__"],
    description=about["__description__"],
    long_description=readme,
    long_description_content_type="text/markdown",
    author=about["__author__"],
    author_email=about["__author_email__"],
    url=about["__url__"],
    python_requires="~=3.7,",
    license=about["__license__"],
    classifiers=[
        "Natural Language :: English",
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.7",
        "Intended Audience :: System Administrators",
        "Topic :: Utilities",
    ],
    packages=packages,
    project_urls={
        "Documentation": "https://docs.wlanpi.com",
        "Source": "https://github.com/wlan-pi/profiler",
    },
    include_package_data=True,
    install_requires=requires,
    entry_points={"console_scripts": ["profiler=profiler.__main__:main"]},
)
