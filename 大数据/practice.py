from pyspark import SparkContext
from operator import add

sc = SparkContext('local','count app')
words = sc.parallelize(['zhangxin','yanglele','zhangyuanyang','zhangxiaofeng'])
words.collect()

count=words.count()
print('the RDD counts is->%i' %count)

print('/n')
def f(x): print(x)
fore = words.foreach(f)

words_new=words.filter(lambda x:'zhang' in x)
words_new.collect()

words_map=words.map(lambda x:x+' good')
words_map.collect()

adding=words.reduce(add)
print(adding)