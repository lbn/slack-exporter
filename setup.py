#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pip

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

links = []
requires = []

requirements = pip.req.parse_requirements(
    "requirements.txt", session=pip.download.PipSession())

for item in requirements:
    # we want to handle package names and also repo urls
    if getattr(item, "url", None):  # older pip has url
        links.append(str(item.url))

    if getattr(item, "link", None):  # newer pip has link
        links.append(str(item.link))

    if item.req:
        requires.append(str(item.req))

config = {
    "description": "Export data from Slack as a non-admin user",
    "author": "Lee Archer",
    "url": "http://blog.archer.onl/article/" +
    "export-all-slack-logs-as-a-non-admin-user/",

    "download_url": "https://github.com/lbn/slack-exporter",
    "author_email": "lee+github@archer.onl",
    "version": "0.0.1",
    "packages": [],
    "scripts": [
        "bin/slack-exporter"
    ],
    "name": "slack-exporter",
    "install_requires": requires,
    "dependency_links": links
}

setup(**config)
