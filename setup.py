# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name="jsroutes",
    version="0.1.3",
    packages=["jsroutes", "jsroutes.management",
              "jsroutes.management.commands"],
    install_requires=[
        "django",
    ],
    package_data = {
        "jsroutes": ["templates/jsroutes.js"],
    },
    author="Viktor Kotseruba",
    author_email="barbuzaster@gmail.com",
    description="use 'reverse' from javascript",
    license="MIT",
    keywords="web django",
    zip_safe=False
)
