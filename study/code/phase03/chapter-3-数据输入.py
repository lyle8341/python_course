import os
import sys
import warnings

# 设置Java路径（根据你的实际安装路径修改）
os.environ["JAVA_HOME"] = "E:\jdk-17.0.13"
os.environ["PATH"] = os.environ["JAVA_HOME"] + "/bin;" + os.environ["PATH"]
# 设置Python相关环境变量
os.environ['PYSPARK_PYTHON'] = sys.executable  # 使用当前Python解释器
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

warnings.filterwarnings('ignore')

from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local[*]").setAppName("test_py_spark_app")
# 创建 SparkContext 类对象
sc = SparkContext(conf=conf)

############## 普通python数据容器转 RDD
rdd1 = sc.parallelize([1, 2, 3, 4, 5])
rdd2 = sc.parallelize((1, 2, 3, 4, 5))
rdd3 = sc.parallelize("abcdefg")
rdd4 = sc.parallelize({1, 2, 3, 4, 5})
rdd5 = sc.parallelize({"key1": "value1", "key2": "value2", "key3": "value3"})

"""
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
['a', 'b', 'c', 'd', 'e', 'f', 'g']
[1, 2, 3, 4, 5]
['key1', 'key2', 'key3']
"""
print(rdd1.collect())
print(rdd2.collect())
print(rdd3.collect())
print(rdd4.collect())
print(rdd5.collect())

############## 读取文件转 RDD
rdd = sc.textFile("../../md/day1.md")
print(rdd.collect())

sc.stop()