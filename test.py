#!/usr/bin/env python

import sys
import pprint

pprint.pprint(sys.path)

import os
path = os.path.dirname(pprint.__file__)
print path

import catkin_pkg
path = os.path.dirname(catkin_pkg.__file__)
# from catkin_pkg.topological_order import topological_order
# path = os.path.dirname(topological_order.__file__)
print path

import modules
path = os.path.dirname(modules.__file__)
print path

import roslaunch
path = os.path.dirname(roslaunch.__file__)
print path

# output:
# ['C:\\Users\\gyzhao\\Desktop',
#  'C:\\Python27\\lib\\site-packages\\distribute-0.6.27-py2.7.egg',
#  'C:\\Windows\\system32\\python27.zip',
#  'C:\\Python27\\DLLs',
#  'C:\\Python27\\lib',
#  'C:\\Python27\\lib\\plat-win',
#  'C:\\Python27\\lib\\lib-tk',
#  'C:\\Python27',
#  'C:\\Python27\\lib\\site-packages',
#  'C:\\Python27\\lib\\site-packages\\setuptools-0.6c11-py2.7.egg-info']