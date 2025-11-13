def func(_calculate):
    result = _calculate(1, 2)
    print(f"参数类型: {type(_calculate)}")
    print(result)


def calculate(x, y):
    return x + y


func(calculate)
