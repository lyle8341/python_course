class Phone:
    # __ 私有变量
    __current_voltage = 0.2

    # 私有成员方法
    def __keep_single_core(self):
        print("CPU is running as single core")

    def call_by_5g(self):
        if self.__current_voltage >= 1:
            print("5g model is running ...")
        else:
            self.__keep_single_core()
            print("battery is empty")


phone = Phone()
phone.call_by_5g()