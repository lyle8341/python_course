
def outer(func):
    def inner():
        print("fall asleep")
        func()
        print("wake up")
    return inner

# 方式二
@outer
def sleep():
    import random
    import time
    print("sleep ...")
    time.sleep(random.randint(1,5))

# 使用方式
# fn = outer(sleep)
# fn()



sleep()