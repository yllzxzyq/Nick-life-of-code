# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 14:31:11 2019

@author: yllzxzyq
"""
from pyspark import SparkContext
logFile = "爬取中国大学.txt"
sc = SparkContext("local", "first app")
logData = sc.textFile(logFile).cache()
numAs = logData.filter(lambda s: 'a' in s).count()
numBs = logData.filter(lambda s: 'b' in s).count()
sc.stop()
print("Line with a:%i,lines with b :%i" % (numAs, numBs))