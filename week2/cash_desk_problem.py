class Bill:

    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return "A {}$ bill".format(self.amount)

    def __int__(self):
        return self.amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(self.amount)


a = Bill(5)
b = Bill(10)
c=Bill(5)

money_holder = {}

money_holder[a] = 1

if c in money_holder:
    money_holder[c] += 1

print(money_holder)
print(hash(b))


class BatchBill(Bill):

    def __init__(self, bills):
        self.bills = bills

    def __len__(self):
        return len(bills)

    def total(self):
        return sum(bills)

    def __getitem__(self, index):
        return self.bills[index]

values = [10, 20, 50, 100]
bills = [Bill(value) for value in values]

batch = BatchBill(bills)

for bill in batch:
    print(bill)


class CashDesk():

    def take_money(self, money):
        for key in money.keys():
            self.money[key] += money[key]

    def total(self):
        sum = 0
        for key in self.money.keys():
            sum += self.money[key] * key
        return sum
