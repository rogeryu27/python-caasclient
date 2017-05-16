# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2017-05-16 10:38:02
# @Last Modified by:   Administrator
# @Last Modified time: 2017-05-16 11:23:39

import argparse
from ..utils import utils

@utils.arg('--name,
			metavar='<name>',
			help="Name of the project to create.")
def do_test(cli,args):
	print args.name