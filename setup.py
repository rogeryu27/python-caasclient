# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2017-05-08 11:27:55
# @Last Modified by:   Administrator
# @Last Modified time: 2017-05-08 11:38:30

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst')) as f:
    long_description = f.read()

setup(
	name="caasclient",
	version="1.0.2b1",
	description="Python client for CAAS",
    long_description=long_description,
	author="rogeryu",
	author_email="roger.leo.yu@gmail.com",
	url="https://github.com/rogeryu27/python-caasclient",
	zip_safe=False,
	classifiers=[
		'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 2.7',
    ],
    keywords="client caas",
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
	install_requires=[
		"requests>=2.12",
	],
	entry_points={
        'console_scripts': [
        ],
    },
)
