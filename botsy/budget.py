"""
Module to store the budget object info
"""


class Budget:
    """
    Main class to Handle the monthly budget
    """
    EXTRA_INCOME = []
    RECORDS = []

    def __init__(self, income):
        self.income = income

    @property
    def income(self):
        return self._income

    @income.setter
    def income(self, amount):
        if amount <= 0:
            raise ValueError('Out of balance! needs to be greater than 0!')
        self._income = amount

    def expense(self, amount, item, category='Unknown'):
        record = dict(
            amount=amount,
            item=item,
            category=category
        )
        Budget.RECORDS.append(record)
        self.income -= amount
        return record

    def extra_income(self, amount, source, reason='Unknown'):
        record = dict(
            amount=amount,
            source=source,
            reason=reason
        )
        Budget.EXTRA_INCOME.append(record)
        self.income += amount
        return record

    def get_balance(self):
        return self.income

    def get_expenses(self):
        return Budget.RECORDS

    def get_extra_incomes(self):
        return Budget.EXTRA_INCOME
