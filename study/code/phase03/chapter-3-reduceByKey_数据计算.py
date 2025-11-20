import os
import sys
from pyspark import SparkConf, SparkContext

os.environ["JAVA_HOME"] = "E:/jdk-17.0.13"
os.environ["PATH"] = os.environ["JAVA_HOME"] + "/bin;" + os.environ["PATH"]
os.environ['PYSPARK_PYTHON'] = sys.executable  # 使用当前Python解释器
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

conf = SparkConf().setMaster("local[*]").setAppName("test_py_spark_app")
# 创建 SparkContext 类对象
sc = SparkContext(conf=conf)

rdd = sc.parallelize([("男", 90), ("女", 30), ("男", 40), ("女", 54)])

rdd2 = rdd.reduceByKey(lambda a, b: a + b)

print(rdd2.collect())
