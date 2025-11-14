def str_reverse(s):
    """
    字符串反转
    :param s: 字符串
    :return: 反转后的字符串
    """
    return s[::-1]


def substr(s, x, y):
    """
    根据索引切片
    :param s: 原字符串
    :param x: 起始索引
    :param y: 结束索引
    :return: 切片字符串
    """
    return s[x:y]


# 测试
if __name__ == '__main__':
    print(str_reverse("星期五"))
