# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 13:21:44 2019

@author: yllzxzyq
"""

import pymysql
 
conn = pymysql.connect(host='localhost',port=8800, user="root",password="zhangxin22",database="train_data",charset="utf8")
cursor = conn.cursor()