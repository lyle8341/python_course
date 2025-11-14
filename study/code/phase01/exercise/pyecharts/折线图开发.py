import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LabelOpts


def zero_fill(num, data):
    zero = [0 for _ in range(num)]
    zero.extend(data)
    return zero


def data_process(data, deadline):
    # us_data = us_data.replace("jsonp_1629344292311_69436(", "")
    us_data = data[26:-2]
    # us_data = us_data[:-2]
    us_dict = json.loads(us_data)

    name = us_dict["data"][0]["name"]
    print(name)
    trend = us_dict["data"][0]["trend"]
    update_date = trend["updateDate"][:deadline]
    print(f"时间: {len(update_date)}, {update_date}")
    list_list = trend["list"]
    确诊数据 = list_list[0]["data"][:deadline]
    print(f"确诊: {len(确诊数据)}, {确诊数据}")
    治愈数据 = list_list[1]["data"][:deadline]
    print(f"治愈: {len(治愈数据)}, {治愈数据}")
    死亡数据 = list_list[2]["data"][:deadline]
    print(f"死亡: {len(死亡数据)}, {死亡数据}")
    新增确诊数据 = list_list[3]["data"][:deadline]
    print(f"新增确诊: {len(新增确诊数据)}, {新增确诊数据}")
    return update_date, 确诊数据, 治愈数据, 死亡数据, 新增确诊数据


f_us = open("sample/美国.txt", "r", encoding="UTF-8")
us_data = f_us.read()
x1, y1a, y1b, y1c, y1d = data_process(us_data, 314)
f_us.close()

f_japan = open("sample/日本.txt", "r", encoding="UTF-8")
japan_data = f_japan.read()
x2, y2a, y2b, y2c, y2d = data_process(japan_data, 315)
f_japan.close()

f_india = open("sample/印度.txt", "r", encoding="UTF-8")
india_data = f_india.read()
x3, y3a, y3b, y3c, y3d = data_process(india_data, 269)
f_india.close()

line = Line()
# x轴 - 选取范围最大的作为x轴
line.add_xaxis(x2)
# y轴 - 数据与x没有对应，补齐
y1a = zero_fill(1, y1a)
y3a = zero_fill(46, y3a)
print(f"填充对齐后数据 ================")
print(f"x轴:{len(x2)}, {x2}")
print(f"y轴:{len(y1a)}, {y1a}")
print(f"y轴:{len(y2a)}, {y2a}")
print(f"y轴:{len(y3a)}, {y3a}")
line.add_yaxis("美国确诊", y1a, label_opts=LabelOpts(is_show=False))
line.add_yaxis("日本确诊", y2a, label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度确诊", y3a, label_opts=LabelOpts(is_show=False))
line.set_global_opts(
    title_opts=TitleOpts(
        title="2020年美日印三国确诊人数折线图",
        pos_left="center",
        pos_bottom="1%"
    )
)

line.render()
