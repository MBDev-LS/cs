import datetime

class Account():
	def __init__(self, name: str, balance: int) -> None:
		name = [name]
		balance = 0


class Transaction():
	def __init__(self, datestamp: datetime.datetime) -> None:
		datestamp = datestamp

class Deposit(Transaction):
	def __init__(self, datestamp: datetime.datetime, amount: float) -> None:
		super().__init__(datestamp)
		amount = amount

	def __str__(self) -> str:
		return f'<Deposit: {self.super().datestamp}, {self.amount}'

class Withdrawal(Transaction):
	def __init__(self, datestamp: datetime.datetime, amount: float) -> None:
		super().__init__(datestamp)
		amount = amount

	def __str__(self) -> str:
		return f'<Withdrawal: {self.super().datestamp}, {self.amount}'#
