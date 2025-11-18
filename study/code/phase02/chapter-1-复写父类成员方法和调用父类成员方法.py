class Phone:
    IMEI = None
    producer = "CN"

    def manual_control(self):
        print("手动控制")


class LittleSwan(Phone):
    producer = "USA"

    def manual_control(self):
        # 方式一
        print(Phone.producer)
        Phone.manual_control(self)  # 必须传递self
        # 方式二
        print(super().producer)
        super().manual_control()  # 必须不能有self

        print("已经升级为全自动")


ls = LittleSwan()
ls.manual_control()
print(ls.producer)
