from pyecharts.charts import Map
from pyecharts.options import TitleOpts, VisualMapOpts

map = Map()
city_data = [
    ("上城区", 1256.8),
    ("下城区", 987.3),
    ("西湖区", 1567.2),
    ("拱墅区", 1123.4),
    ("江干区", 1345.6),
    ("滨江区", 1890.5),
    ("萧山区", 2156.7),
    ("余杭区", 1987.4),
    ("富阳区", 876.5),
    ("临安区", 765.3),
    ("桐庐县", 456.2),
    ("淳安县", 342.8),
    ("建德市", 398.7)
]
# map.add("浙江省地图",data, "浙江" )
map.add("杭州市地图", city_data, "杭州")

map.set_global_opts(
    title_opts=TitleOpts(title="杭州市疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 99, "label": "1-99人", "color": "#CCFFFF"},
            {"min": 100, "max": 199, "label": "100-199人", "color": "#FF6666"},
            {"min": 200, "max": 499, "label": "200-499人", "color": "#990033"},
            {"min": 500, "max": 999, "label": "500-999人", "color": "#4FC3F7"},
            {"min": 1000, "label": "1000人以上", "color": "#03A9F4"}
        ]
    )
)

map.render("杭州市疫情地图.html")
