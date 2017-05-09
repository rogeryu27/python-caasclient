# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2017-05-07 22:29:31
# @Last Modified by:   Administrator
# @Last Modified time: 2017-05-09 17:01:57


class Manager(object):
	
	def __init__(self,api):
		self.api = api

	def make_path(self, id):
		return '/' + self.api.api_version + '/' + \
			self.api_name + '/%s' % id if id else \
			'/' + self.api.api_version + '/' + self.api_name

	def list(self):
		return {"a":"a"}

	def get(self, id):
		pass

	def create(self, id):
		self.api.post()

	def filter(self, id):
		pass
		
	def delete(self, id):
		self.api.delete(self.make_path(id))


	
