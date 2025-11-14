import json

f = open("sample/1960-2019全球GDP数据.csv", "r", encoding="UTF-8")

year_country_gdp = {}

header = 0
for line in f:
    if header == 0:
        header += 1
        continue
    list_line = line.split(",")
    year = list_line[0].strip()
    country = list_line[1].strip()
    gdp = list_line[2].strip()
    gdp = int(gdp)
    # 如果有该年份
    country_gdp = year_country_gdp.get(year)
    if country_gdp:
        country_gdp[country] = gdp
    else:
        year_country_gdp[year] = {country: gdp}

print(json.dumps(year_country_gdp, ensure_ascii=False))

f.close()
