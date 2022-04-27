#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    README = readme_file.read()

with open("HISTORY.rst") as history_file:
    HISTORY = history_file.read()

REQUIREMENTS = ["docopt", "python-magic", "beautifulsoup4"]

SETUP_REQUIREMENTS = ["pytest-runner"]

TEST_REQUIREMENTS = ["pytest", "pytest-cov"]

setup(
    author="Victor Cabello",
    author_email="vmeca87@gmail.com",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    description="Convert html and images into an standalone file with inline img in base64",
    entry_points={"console_scripts": ["toStandalone=pystandalonehtml.cli:main"]},
    install_requires=REQUIREMENTS,
    license="MIT license",
    long_description=README + "\n\n" + HISTORY,
    include_package_data=True,
    keywords="html to single html",
    name="pystandalonehtml",
    packages=find_packages(include=["pystandalonehtml"]),
    setup_requires=SETUP_REQUIREMENTS,
    test_suite="tests",
    tests_require=TEST_REQUIREMENTS,
    url="https://github.com/victorcabello/pystandalonehtml",
    version="0.1.0",
    zip_safe=False,
)