#!/usr/bin/python
# -*- coding: utf-8 -*-

from argparse import ArgumentParser  
  
p = ArgumentParser(usage='it is usage tip', description='this is a test')
p.add_argument('--one', default=1, type=int, help='the first argument')
p.add_argument('--two', default=2, type=int, help='the second argument')
p.add_argument('--docs-dir', default="./", help='document directory')
  
args = p.parse_args()  

print args  

print args.one  
print args.docs_dir   #经过parse_args()函数后参数名称去掉了前面的"--"，所有的"-"转换为"_" 