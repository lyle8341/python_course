from study.code.phase01.exercise.my_utils.str_util import *
from study.code.phase01.exercise.my_utils.file_util import *

source = "xylophone"
target = str_reverse(source)
print(f"原字符串: {source}，反转后: {target}")

target = substr(source, 4, 9)
print(f"原字符串: {source}，切片后: {target}")

print_file_info("../../../../../output.txt")
print_file_info("../../../../../output1.txt")

content = """闻说双溪春尚好，也拟泛轻舟。\n只恐双溪舴艋舟，载不动许多愁。"""
append_to_file("../../../../../output.txt", content)
