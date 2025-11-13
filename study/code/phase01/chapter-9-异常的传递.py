def f1():
    print("f1 execute ...")
    num = 1 / 0
    print("f1 finished")


def f2():
    print("f2 execute ...")
    f1()
    print("f2 finished")


def main():
    try:
        f2()
    except Exception as e:
        print(e)


main()
