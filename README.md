python-caasclient
======

Python client for caas

Brief Introduction

Features
--------
* HTTP interface using requests
* Python native quering for CAAS API objects

Installation
------------

	git clone https://github.com/rogeryu27/python-caasclient.git
	cd caasclient
	python setup.py

Usage
-----

Query for all ready containers [in a custom namespace]:

.. code:: python
	
	from python-caasclient import client

	container_list = client(<caas url>).containers.list()

Create a self-defined image:

.. code:: python
	
	import os

	from python-caasclient import client

	image = client(<caas url>).image.create_by_dockerfile(os.open('path/to/dockerfile','w+'))

Requirements
------------

* Python 2.7
* requests

