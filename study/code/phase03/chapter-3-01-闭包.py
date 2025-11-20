
def outer(logo):
    def inner(msg):
        nonlocal logo
        logo += logo
        print(f"<{logo}>{msg}<{logo}>")

    return inner


fn1 = outer("Hello")
fn1("world")
fn1("oooo")
fn1("!!!")


def account_create(init_amount=0):
    def atm(num, deposit=True):
        nonlocal init_amount
        if deposit:
            init_amount += num
            print(f"存款: {num}，账户余额: {init_amount}")
        else:
            init_amount -= num
            print(f"取款: {num}，账户余额: {init_amount}")
    return atm


atm = account_create()
atm(200)