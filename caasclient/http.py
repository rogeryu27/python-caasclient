# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2017-05-06 23:10:19
# @Last Modified by:   Administrator
# @Last Modified time: 2017-05-08 09:28:33
import requests

class HTTPClient(object):
	def __init__(self,endpoint,**kwargs):
		self.endpoint = endpoint
		# Authentication self.auth_token = kwargs.get('auth_token')
		self.api_version = kwargs.get('api_version')
		self.connection_params = self.get('connection_params')

	def session(self):
		return requests.Session

	def get_connection():

	def make_uri(self,**kwargs):
		pass

	def get(self, *args, **kwargs):
		return self.session.get(*args,endpoint)
		
	def post(self, *args, **kwargs):
		return self.session.pos(*args,endpoint)

	def put(self, *args, **kwargs):
		return self.session.put(*args,endpoint)

	def patch(self, *args, **kwargs):
		return self.session.patch(*args,endpoint)

	def delete(self, *args, **kwargs):

		return self.session.delete(*args,endpoint)

# class HTTPSession(object):