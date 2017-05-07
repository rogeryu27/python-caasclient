# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2017-05-07 22:50:49
# @Last Modified by:   Administrator
# @Last Modified time: 2017-05-07 22:58:14

from caasclient.v1 import base
import os
import tempfile
import random

class ProjectManager():

    def __init__(self,client):
        self.client = client

    def create(self,container):
        #TODO: random p_id
        p_id = "11111assd"
        self.client.start(container=container.container_id)
        Project.objects.create(p_id=p_id,name=container.name,container=container)

        return p_id

    def delete(self,p_id,force=True):
        self.client.remove_container(container=self._get(p_id),force=force)
        Project.objects.filter(p_id=p_id).delete()
        container.object.filter(container_id=self._get(p_id))

    def stop(self,p_id,timeout=10000):
        self.client.stop(container=self._get(p_id),timeout=timeout)
        Project.objects.filter(p_id=p_id).update(state=False)

    def start(self,p_id):
        self.client.start(container=self._get(p_id))
        Project.objects.filter(p_id=p_id).update(state=True)

    def _get(self,p_id):
        project = Project.objects.filter(p_id=p_id)
        return project.container.container_id