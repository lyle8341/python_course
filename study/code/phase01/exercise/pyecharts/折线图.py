from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts,VisualMapOpts

# 创建折线图对象
line = Line()
# 添加x轴数据
line.add_xaxis(["China", "America", "British"])
# 添加y轴数据
line.add_yaxis("GDP", [20, 30, 5])
# 全局配置
line.set_global_opts(
    title_opts=TitleOpts(is_show=True, title="GDP展示",pos_left="center", pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True)


)

# 生成图像
line.render()
