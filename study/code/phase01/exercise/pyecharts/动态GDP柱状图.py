from pyecharts.charts import Timeline, Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType
import json

f = open("sample/1960-2019全球GDP数据.csv", "r", encoding="UTF-8")

year_country_gdp = {}

"""
将数据转为字典格式如下：
{
    1960: [
        [国家, GDP],
        [国家, GDP],
        [国家, GDP],
        ...
    ],
    1961: [
        [国家, GDP],
        [国家, GDP],
        [国家, GDP],
        ...
    ],
    1962: [
        [国家, GDP],
        [国家, GDP],
        [国家, GDP],
        ...
    ],
    ...
}
"""
header = 0
for line in f:
    if header == 0:
        header += 1
        continue
    list_line = line.split(",")
    year = int(list_line[0].strip())
    country = list_line[1].strip()
    gdp = list_line[2].strip()
    gdp = float(gdp)
    # 如果有该年份
    country_gdp = year_country_gdp.get(year)
    if country_gdp:
        country_gdp.append([country, gdp])
    else:
        year_country_gdp[year] =[[country, gdp]]
# print(json.dumps(year_country_gdp, ensure_ascii=False))
# 关闭文件
f.close()

# 时间线
tl = Timeline(
    {"theme": ThemeType.LIGHT},
)

# 如果要万无一失，对key进行排序，然后再取
for key in sorted(year_country_gdp.keys()):
    country_gdp_s = year_country_gdp[key]
    country_gdp_s.sort(key=lambda ele:ele[1],reverse=True)
    result = country_gdp_s[:10]
    xes = []
    yes = []
    for i in result:
        xes.append(i[0])
        yes.append(i[1] / 100000000)
    bar = Bar()
    xes.reverse()
    yes.reverse()
    bar.add_xaxis(xes)
    bar.add_yaxis("GDP(亿)", yes, label_opts=LabelOpts(position="right"))
    bar.reversal_axis()
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{key}年全球前10GDP数据")
    )

    tl.add(bar, str(key))

tl.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True
)

tl.render("动态GDP柱状图.html")
