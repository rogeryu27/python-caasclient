# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2017-05-07 22:50:54
# @Last Modified by:   Administrator
# @Last Modified time: 2017-05-10 15:58:46

from caasclient.v1 import base

class Image(base.ApiObject):
    resource_name = 'image'

class ImageManager(base.Manager):
    """Image Manager for CAAS Service API
    	:method create_image_by_step: Create an docker image by a workflow
    	:method create_image_from_dockerfile: Create an docker image with a dockerfile
    	:method search: Search related docker images from Docker Hub with a specified term
    	:method pull: Download an docker image from a registry
    	:method push: Upload an docker image to a registry
    	:method delete: Delete an docker image
    	:method list: List specified docker images
    	:method inspect: Get an image object
    	:method create_registry: Create a local registry
		:method tag: Add a tag to a image
		To be added [tag_related_method]
    """
    resource_class = Image
    api_name = "images"

    def create_image_by_step():
        pass

   	def create_image_from dockerfile():
        pass

   	def search(self, term):
   		return self._get('/images/%s/search' % term)

   	def delete(self, img_id):
   		self._delete('/images/%s' % img_id)

   	def list(self, search_opts=None, limit=None, sort_by=None):
   		return self._list('/images')