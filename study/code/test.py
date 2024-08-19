def test_func(compute):
    result = compute(1, 2)
    print(result)

def compute(x, y):
    return x + y



if __name__ == '__main__':
    test_func(compute)