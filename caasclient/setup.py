# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2017-05-08 11:27:55
# @Last Modified by:   Administrator
# @Last Modified time: 2017-05-08 11:38:30

from setuptools import setup, find_packages

setup(
	name="caasclient",
	version="1.0",
	description="Python client for CAAS",
    long_description=open("README.rst").read(),
	author="rogeryu",
	author_email="roger.leo.yu@gmail.com",
	url="https://github.com/rogeryu27/python-caasclient",
	packages=find_packages(),
	zip_safe=False,
	classifiers=[
        'Programming Language :: Python :: 2.7',
    ],
	install_requires=[
		"requests>=2.12",
	],
)