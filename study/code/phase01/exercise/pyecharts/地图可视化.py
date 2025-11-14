from pyecharts.charts import Map
from pyecharts import options as opts

mapObj = Map()
data = [
    ("北京市", 99), #必须带省市字
    ("上海市", 199),
    ("陕西省", 299),
    ("台湾省", 399),
    ("香港特别行政区", 499),
    ("澳门特别行政区", 450)
]
mapObj.add(
    "测试地图",
    data,
    "china"
).set_series_opts(
    label_opts=opts.LabelOpts(is_show=True)  # 关键：显示标签
).set_global_opts(
    title_opts=opts.TitleOpts(title="中国人口分布"),
    visualmap_opts=opts.VisualMapOpts(
        max_=11000,
        min_=1000,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 9, "label": "1-9人", "color": "#CCFFFF"},
            {"min": 10, "max": 99, "label": "10-99人", "color": "#FF6666"},
            {"min": 200, "max": 299, "label": "200-299人", "color": "#990033"},
            {"min": 300, "max": 399, "label": "300-399人", "color": "#4FC3F7"},
            {"min": 400, "label": "400人以上", "color": "#03A9F4"}
        ]
    )
)
mapObj.render()
