# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2017-05-07 22:50:49
# @Last Modified by:   Administrator
# @Last Modified time: 2017-05-10 16:02:17

from caasclient.v1 import base

class Project(base.ApiObject):
	resource_name = 'project'

class ProjectManager(base.Manager):
    """Project Manager for CAAS Service API
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

    api_name = "projects"
    resource_class = Project

   	def delete(self, p_id):
   		self.api._delete('/projects/%s' % p_id)