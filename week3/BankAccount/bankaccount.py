class BankAccount:

    def __init__(self, name, balance, currency):
        self.__name = str(name)
        self.__balance = balance
        self.__currency = currency

    def __int__(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

    def balance(self):
        return self.__balance

    def __str__(self):
        return "Bank account for {} with balance of {}{}".format(self.__name, self.__balance, self.__currency)

    def withdraw(self, amount):
        self.__balance -= amount
    def getname(self):
        return self.__name
