from pyecharts.charts import Bar
from pyecharts.options import LabelOpts

bar = Bar()

bar.add_xaxis(["China", "America", "British"])

bar.add_yaxis("GDP", [20, 30, 5], label_opts=LabelOpts(
    position="right"
))

# 反转
bar.reversal_axis()

bar.render("基础柱状图.html")
