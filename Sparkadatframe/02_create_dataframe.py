from pyspark.sql import SparkSession

spark = SparkSession.builder.master('local[*]').appName('dff1').getOrCreate()
data1 = [(1,'Ram',25,20000),
(2,'Sham',29,30000),
(3,'Kiran',31,10000),
(4,'Mina',34,14000)
]
strc1 = ['id','Name','age','salary']
df1 =spark.createDataFrame(data=data1, schema=strc1)
df1.show()