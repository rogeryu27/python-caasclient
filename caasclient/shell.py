# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2017-05-06 23:13:12
# @Last Modified by:   Administrator
# @Last Modified time: 2017-05-10 22:04:07

'''
Command-line interface for the CAAS API.
'''

import argparse
import logging
import os
import sys

import six

from caasclient.v1 import client as caas_client

class CaasClientArgumentParser(argparse.ArgumentParser):

	def __init__(self, *args, **kwargs):
		super(MagnumClientArgumentParser, self).__init__(*args, **kwargs)

class CaasShell(object):
	def get_base_parser(self):
		parser = CaasClientArgumentParser(
			proc='caas'
		)

		parser.add_argument('-h', '--help',
							action='store_true'
							help='')

		return parser


	def main(self, agrv):

		self.client = caas_client.Client(<url>)

		args.func(self.client, args)

def main():
	try:
		CaasShell().main()
	except Exception as e:
		raise e
if __name__ == "__main__":
	main()