# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2017-05-06 23:10:19
# @Last Modified by:   Administrator
# @Last Modified time: 2017-05-07 22:45:23
import 

class HTTPClient(object):
	def __init__(self,endpoint,**kwargs):
		self.endpoint = endpoint
		# Authentication self.auth_token = kwargs.get('auth_token')
		self.api_version = kwargs.get('api_version')
		self.connection_params = self.get('connection_params')

	def get_connection():

	def get(self,):

	def post():

	def patch():

	def delete():


class HTTPSession(object):