from pyspark import *
conf1 = SparkConf().setMaster('local[*]').setAppName('data frame 1')
sc = SparkContext(conf=conf1)
rdd1 = sc.parallelize([1,3,5,8])
print(rdd1.collect())