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

rdd = sc.parallelize([1, 2, 3, 4, 5, 6])
print(type(rdd.collect()))

print(rdd.take(3))

print(rdd.count())