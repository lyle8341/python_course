import os
import sys
from pyspark import SparkConf, SparkContext

os.environ["JAVA_HOME"] = "E:/jdk-17.0.13"
os.environ["PATH"] = os.environ["JAVA_HOME"] + "/bin;" + os.environ["PATH"]
os.environ['PYSPARK_PYTHON'] = sys.executable  # 使用当前Python解释器
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

conf = SparkConf().setMaster("local[*]").setAppName("test_py_spark_app")
# 全局并行度设置
# conf.set('spark.default.parallelism', "1")

# 创建 SparkContext 类对象
sc = SparkContext(conf=conf)

# parallelize方法传入numSlices，设置分区数量
rdd = sc.parallelize([1, 2, 3, 4, 5, 6], numSlices=1)
rdd2 = sc.parallelize([("hello", 3), ("Spark", 1), ("world", 5)])
rdd3 = sc.parallelize([[1, 3, 5], [6, 7, 9], [11, 2, 34]])

"""
os.environ('HADOOP_HOME') = "....."
http://archive.apache.org/dist/hadoop/common/hadoop-3.0.0/hadoop-3.0.0.tar.gz
https://raw.githubusercontent.com/steveloughran/winutils/master/hadoop-3.0.0/bin/winutils.exe
https://raw.githubusercontent.com/steveloughran/winutils/master/hadoop-3.0.0/bin/hadoop.dll
"""
rdd.saveAsTextFile("../../sample/rdd1")
rdd2.saveAsTextFile("../../sample/rdd2")
rdd3.saveAsTextFile("../../sample/rdd3")
