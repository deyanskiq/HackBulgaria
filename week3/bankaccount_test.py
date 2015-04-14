import unittest
from bankaccount import BankAccount


class BankAccountTest(unittest.TestCase):

    def test_deposit_money(self):
        account = BankAccount("Rado", 0, "$")
        account.deposit(1000)
        self.assertEqual(int(account), 1000)

    def test_balance(self):
        account = BankAccount("Rado", 467, "$")
        self.assertTrue(account.balance() == 467)

    def test_withdrow(self):
        account = BankAccount("Rado", 900, "$")
        account.withdraw(300)
        self.assertTrue(int(account) == 600)

    def test_create_str_value_from_account(self):
        account = BankAccount("Rado", 467, "$")
        self.assertEqual(
            str(account), "Bank account for Rado with balance of 467$")

    def test_create_new_bankaccount_class(self):
        account = BankAccount("Rado", 0, "$")
        self.assertTrue(isinstance(account== BankAccount))

    def test_value_error_raises_from_invalid_name(self):
        account = BankAccount(12, 0, "$")
        self.assertTrue(isinstance(self.account.getname(), str))

    def test_create_int_value_from_account(self):
        account = BankAccount("Rado", 0, "$")
        self.assertEqual(int(account), 0)

if __name__ == '__main__':
    unittest.main()
