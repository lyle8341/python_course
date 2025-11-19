"""
pip install pyspark
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyspark
"""
import os
import sys

# 设置Java路径（根据你的实际安装路径修改）
os.environ["JAVA_HOME"] = "E:\jdk-17.0.13"
os.environ["PATH"] = os.environ["JAVA_HOME"] + "/bin;" + os.environ["PATH"]
# 设置Python相关环境变量
os.environ['PYSPARK_PYTHON'] = sys.executable  # 使用当前Python解释器
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

import warnings

warnings.filterwarnings('ignore')

from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local[*]").setAppName("test_py_spark_app")
# 创建 SparkContext 类对象
sc = SparkContext(conf=conf)

print(sc.version)

# 停止 SparkContext对象的运行(停止 PySpark程序)
sc.stop()
