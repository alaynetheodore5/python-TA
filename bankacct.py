class BankAccount:
    def __init__(self, int_rate = 0, balance = 0):
        self.int = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawl(self, amount):
        if self.balance >= 5:
            self.balance -= 5
        else:
            self.balance -= amount
            print("Insufficient Funds: Charging a $5 fee")
        return self

    def yield_interest(self):
        if self.balance >= 0:
            self.balance = self.balance + self.balance * self.int
        return self

    def display_account_balance(self):
        print("balance: $ {}".format(self.balance))
        return self
class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account = BankAccount(int_rate = 0.02, balance = 0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrwal(self, amount):
        self.account.withdrawl(amount)
        return self

    def display_user_balance(self):
        self.account.display_account_balance()
        return self

eric= BankAccount(.10, 0)

eric = User("Eric Doe", "emailaddress1")
kaitlin = User("Kaitlin Doe", "emailaddress2")
ryan = User("Ryan Doe", "emailaddress3")

# eric.make_deposit(100).make_deposit(50).make_deposit(1000).make_withdrwal(500).account.yield_interest().display_account_balance()

#kaitlin.make_deposit(100).make_deposit(500).make_withdrwal(300).make_withdrwal(100).yield_interest().display_account_balance()

#ryan.make_deposit(1000).make_withdrwal(100).make_withdrwal(200).make_withdrwal(300).yield_interest().display_account_balance()