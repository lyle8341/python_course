def print_file_info(file_name):
    """
    输出文件内容
    :param file_name: 文件名
    :return: 无
    """
    f = None
    try:
        f = open(file_name, 'r', encoding="UTF-8")
    except FileNotFoundError as e:
        print(f"{file_name} 文件不存在")
        print(e)
    else:
        for line in f:
            print(line, end="")
    finally:
        if f:
            f.close()


def append_to_file(file_name, data):
    f = None
    try:
        f = open(file_name, 'a', encoding="UTF=8")
    except Exception as e:
        print(f"{file_name} 文件不存在")
        print(e)
    else:
        f.write(data)
        f.write("\n")
        f.flush()
    finally:
        if f:
            f.close()


# 测试
if __name__ == '__main__':
    print_file_info("../../../../../output.txt")
