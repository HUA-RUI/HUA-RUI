# auther zjs
# data 2019/7/19 15:44
# file_name BAM
 
# 银行账户管理系统（BAM）
# 写一个账户类(Account)：
# 属性: id:账户号码 长整数
# password:账户密码
# name:真实姓名
# person_id:身份证号码 字符串类型
# email:客户的电子邮箱
# balance:账户余额
# 方法:
# deposit: 存款方法,参数是浮点数型的金额
# withdraw:取款方法,参数是浮点数型的金额
# 添加新的银行的客户类：储蓄账户(Saving_Account)和信用账户(Credit_Account),区别在于储蓄账户不允许透支,而信用账户可以透支,并允许用户设置自己的透支额度.
import random
 
 
class Account:
    ''''''
 
    def __init__(self, pwd, name, person_id, email, balance) -> None:
        super().__init__()
        self.__id = random.randint(1000000000000000, 9999999999999999)
        self.pwd = pwd
        self.__name = name
        self.__person_id = person_id
        self.email = email
        self._balance = balance
 
    @property
    def id(self):
        return self.__id
 
    @property
    def name(self):
        return self.__name
 
    @property
    def person_id(self):
        return self.__person_id
 
    @property
    def balance(self):
        return self._balance
 
    @property
    def pwd(self):
        return self.__pwd
 
    @pwd.setter
    def pwd(self, value):
        self.__pwd = value
        pass
 
    @property
    def email(self):
        return self.__email
 
    @email.setter
    def email(self, value):
        self.__email = value
        pass
 
    def deposit(self, money):
        if money < 0:
            print("存款异常")
            return
        self._balance += money
        return money
 
    def withdraw(self, money):
        if money > self._balance:
            print("余额不足")
            return
        self._balance -= money
        return money
 
 
# 添加新的银行的客户类：储蓄账户(Saving_Account)和信用账户(Credit_Account),区别在于储蓄账户不允许透支,而信用账户可以透支,并允许用户设置自己的透支额度.
# 注意:Credit_Account需要多一个属性 ceiling 透支额度
 
class Saving_Account(Account):
    pass
 
 
class Credit_Account(Account):
    def __init__(self, password, name, person_id, email, balance, ceiling) -> None:
        super().__init__(password, name, person_id, email, balance)
        self.ceiling = ceiling
 
    @property
    def ceiling(self):
        return self.__ceiling
 
    @ceiling.setter
    def ceiling(self, value):
        self.__ceiling = value
        pass
 
    # 重写父类取钱方法
    def withdraw(self, money):
        if money < 0:
            print("取款异常")
            return 0
        if money > self._balance + self.ceiling:
            print("额度不足！")
            return 0
        if money < self._balance:
            super().withdraw(money)
            return money
        else:
            self.__ceiling -= (money - self._balance)
            super().withdraw(self._balance)
            return money
 
 
# 编写Bank类
# 属性:
# 1.当前所有的账户对象存放在列表中
# 2.当前登录用户
#
# 方法:
# 1.用户开户,由用户输入需要的参数:id,密码,密码确认,姓名,身份证号码,邮箱,账户类型(int),将新创建的Account对象放入账户列表中
# 2.用户登录,从用户输入中获取:id,密码 提示 检测用户列表内是否有此用户，若登录成功，将匹配到的对象放入当前登录用户中
# 3.用户存款,判断用户是否登录，若登录，输入:存款数额,修改当前登录的Account对象，若未登录，提示登录
# 4.用户取款,判断用户是否登录，若登录，输入:取款数额,修改当前登录的Account对象，若未登录，提示登录
# 5.统计银行所有账户余额总数
# 用户会通过调用Bank对象以上的方法来操作自己的账户,请分析各个方法需要的参数
 
class Bank:
    def __init__(self) -> None:
        super().__init__()
        self.__acss = []
        self.__login = None
 
    def create_account(self):
        while True:
            password = input("密码：")
            password2 = input("确认密码：")
            if password == password2:
                break
 
        name = input("姓名：")
        person_id = input("身份证号：")
        email = input("邮箱：")
        acc_type = input("账户类型(1.储蓄账户；2.信用账户)：")
        if acc_type == "1":
            self.__acss.append(Saving_Account(password, name, person_id, email, 0))
        else:
            self.__acss.append(Credit_Account(password, name, person_id, email, 0, 10000))
 
        print("您的账号为：", self.__acss[-1].id, "请牢记")
 
    def login(self):
        # 检测是否登录
        if self.__login is not None:
            print("请勿重复登录!")
            return
        in_id = int(input("请输入ID:"))
        in_password = input("请输入密码：")
        for i in range(len(self.__acss)):
            if in_id == self.__acss[i].id and in_password == self.__acss[i].pwd:
                self.__login = self.__acss[i]
                break
 
        if self.__login == None:
            print("登陆失败")
        else:
            print("登录成功！请进行下一步操作")
 
    # 用户存钱方法
    def save(self):
        # 检测是否登录
        if self.__login == None:
            print("请先登录")
            self.login()
            return 0
        save_money = int(input("要存的钱数："))
        self.__login.deposit(save_money)
        print("余额为：", self.__login._balance)
 
    # 用户取钱方法
    def get(self):
        # 检测是否登录
        if self.__login == None:
            print("请先登录")
            self.login()
            return 0
        get_money = int(input("要取的金额："))
        self.__login.withdraw(get_money)
        print("本次交易：", get_money, " 余额为：", self.__login.balance)
 
    # 统计银行所有账户金额
    def total(self):
        t = 0
        for i in range(len(self.__acss)):
            t += self.__acss[i].balance
        print("银行用户总金额为：", t)
        return t
 
 
# 测试
bank1 = Bank()
bank1.create_account()
bank1.login()
bank1.save()
bank1.get()
bank1.total()