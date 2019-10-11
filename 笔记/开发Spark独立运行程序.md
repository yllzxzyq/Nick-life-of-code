#### 开发Spark独立运行程序

使用Maven或者sbt

sc.textFile("hdfs:-")

文件读取方法

#### RDD转换操作

sc.filter(line=>line.contains("spark"))操作

在RDD的每个元素都执行filter中的函数，留下符合函数要求的元素，过滤其他

sc.map(line=>line.split(" "))操作

在RDD的每个元素都执行一遍函数

sc.flatMap(line=>line.split(" "))

也是执行一遍func再进行一次flat操作，即将所有元素的结果再进行一次打包

sc.groupByKey()

将key相同的键对形成分组

sc.reduceByKey((a,b)=>a+b)

将Key相同的键值对形成分组，并且进行一次函数操作

如上面的表达式，将进行（a,b)即分组形成的Array依次求和，将最后的和作为对应的函数值

#### RDD动作操作

rdd.count()统计RDD中元素个数

rdd.collect()以数组形式返回所有元素

rdd.first()取出第一个元素

rdd.take()以数组形式返回前n个元素

rdd.foreach(func)遍历元素，执行func

rdd.reduce((a,b)=>a+b)即每个元素按住公式读入，求和

rdd.persist()对一个RDD标记为持久化

遇到相关动作类型操作就会真正去持久化

参数选择：MEMORY_ONLY只记录在内存，内存满了会更新   MEMORY_AND_DISK会记录到磁盘

rdd.presist(MEMORY_ONLY)=rdd.cache()

都是缓存rdd到内存

rdd.makeString(",")以“，”为分隔符构建字符串

#### 分区

并行计算

减少通信开销

分区原则：最好接近集群中的cup总核数

不同的布置模式都可以设置参数值可以来调整分区

分区语法：sc.textFile(textpath,num)设置num个分区

rdd.repartition(n)重新进行分区

自定义分区方法：

定义新的Partitioner类，继承原来的org.apache.spark.Partitioner类，

numPartitions:Int返回创建的分区数

getPartition(key:any):Int返回给定键值对的分区号

Partitoner只支持键值对

```scala
class Mypartitioner(numParts:Int) extends Partitioner{

//覆盖分区数

override def numPatition(key:Any):Int={

key.toString,toInt%10}
object TestPartitioner{
    def main(args:Array|String){
        val conf=new SparkConf()
        val sc=new SparkContext(conf)
        //模拟5个分区的数据
        val data=sc.parallelize(1 to 10,5)
        //根据尾号转变为10个分区，分别写到10个文件
        data.map((_,1)).partitionBy(new My Partitioner(10)).map(_._1).saveAsTextFile("file:///usr/local/spark/mycode/rdd/partitioner")
    }
}
```



#### 键值对RDD

创建

val pairRDD=lines.flatMap(line=>line,split(" "))map(word=>(word,1))

利用map方法生成键值对RDD

```scala
val words=Array("one","two","three","three","two")

val rdd=sc.parallelize(words),map(word=>(word,1))
//把key相同的项汇总求和形成新的RDD
val Nrdd=rdd.reduceByKey(_+_)
val Nrdd=rdd.groupByKey().map(t=>(t._1,t._2.sum))

```

```scala
rdd.key()
```

```scala
rdd.values()
```

```scala
rdd.sortByKey()
```

根据键排序默认参数是true升序，如果使用False则降序

```scala
rdd.sortBy(_._2,false).collect
```

根据值排序

```scala
//使用参数中的函数对象对RDD中的元素进行操作
rdd.mapValues(x=>(x,1))


//负责RDD操作构建
rdd.reduceByKey((x,y)=>(x._1=y._1,x._2+y._2))
("spark",(2,1))("spark",(6,1))——>("spark",(8,2))

#此时，调用下面的语句
rdd.mapValues(x=>x._1/x._2)
得到("spark",4)
//只要值相同，就组合起来
rdd.join()
比如,rdd1("spark",1)rdd2("spark","fast")
则rdd1.join(rdd2)
结果("spark",(1,"fast"))
```

