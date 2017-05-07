# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2017-05-07 22:58:53
# @Last Modified by:   Administrator
# @Last Modified time: 2017-05-07 23:15:27

from http import HTTPClient

class Client(object):
	def __init__(self,caas_url,**kwargs):
		if not caas_url
			caas_url = "default"

		http_client = HTTPClient(caas_url,**kwargs)

		self.projects = projects.ProjectManager(self.http_client
		self.images = images.ImageManager(self.http_client)
		self.containers = containers.ContainerManager(self.http_client)