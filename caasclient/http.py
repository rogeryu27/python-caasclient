# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2017-05-06 23:10:19
# @Last Modified by:   Administrator
# @Last Modified time: 2017-05-09 22:20:28
import requests

class HTTPClient(requests.Session):
	def __init__(self,endpoint,**kwargs):
		self.endpoint = endpoint
		# Authentication self.auth_token = kwargs.get('auth_token')
		self.api_version = kwargs.get('api_version')
		self.connection_params = kwargs.get('connection_params')

	def make_url(self,**kwargs):
		pass

	def _get(self, url, **kwargs):
		return self.get(url)
		
	def _post(self, url, **kwargs):
		return self.post(url)

	def _put(self, url, **kwargs):
		return self.put(url)

	def _patch(self, url, **kwargs):
		return self.patch(url)

	def _delete(self, url, **kwargs):
		return self.delete(url)

	def _raise_for_status(self, response):
		'''
			To be completed: Error and Exception Class
		'''
		try:
			response.raise_for_status()
		except request.exceptions.HTTPError as e:
			raise e

	def _url(self, )


# class HTTPSession(object):