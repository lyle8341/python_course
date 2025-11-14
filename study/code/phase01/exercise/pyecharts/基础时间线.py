from pyecharts.charts import Timeline, Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType

bar1 = Bar()
bar1.add_xaxis(["China", "America", "British"])
bar1.add_yaxis("GDB", [20, 30, 5], label_opts=LabelOpts(position="right"))
bar1.reversal_axis()

bar2 = Bar()
bar2.add_xaxis(["China", "America", "British"])
bar2.add_yaxis("GDB", [25, 32, 7], label_opts=LabelOpts(position="right"))
bar2.reversal_axis()

bar3 = Bar()
bar3.add_xaxis(["China", "America", "British"])
bar3.add_yaxis("GDB", [19, 28, 15], label_opts=LabelOpts(position="right"))
bar3.reversal_axis()

# 创建时间线
tl = Timeline(
    {"theme": ThemeType.LIGHT},

)
tl.add(bar1, "2021年GDP")
tl.add(bar2, "2022年GDP")
tl.add(bar3, "2023年GDP")

tl.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True
)

tl.render("基础柱状图-时间线.html")
