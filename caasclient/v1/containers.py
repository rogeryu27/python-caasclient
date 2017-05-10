# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2017-05-07 22:51:03
# @Last Modified by:   Administrator
# @Last Modified time: 2017-05-10 16:02:38

from caasclient.v1 import base

class Container(base.ApiObject):
	resource_name = 'container'

class ContainerManager(base.Manager):
    """Container Manager for CAAS Service API
    	:method create_image_by_step: Create an docker image by a workflow
    	:method create_image_from_dockerfile: Create an docker image with a dockerfile
    	:method search: Search related docker images from Docker Hub with a specified term
    	:method pull: Download an docker image from a registry
    	:method push: Upload an docker image to a registry
    	:method delete: Delete an project
    	:method list: List specified docker images
    	:method inspect: Get an image object
    	:method create_registry: Create a local registry
		:method tag: Add a tag to a image
		To be added [tag_related_method]
    """
	api_name = "containers"
	resource_class = Container

	def delete(self, c_id):
		self.api._delete('/containers/%s' % c_id)