import os
import csv
import datetime


class Tracker:

    expenses = []
    csv_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tracker.csv')
    # {'date': <YYYY-MM-DD>, 'category': <str>, 'amount': <float>, 'description': <str>}

    def __init__(self):
        self.load_expenses()

    def load_expenses(self):
        if os.path.exists(self.csv_file):
            with open(self.csv_file, newline='') as csv_file:
                reader = csv.reader(csv_file, delimiter=' ', quotechar='|')
                for row in reader:
                    try:
                        local_dict = {'date': datetime.datetime.strptime(row[0], '%Y-%m-%d'), 'category': str(row[1]),
                                      'amount': float(row[2]), 'description': str(row[3])
                                      }
                        self.expenses.append(local_dict)
                    except Exception as err:
                        print(f'Not able to load row! {err}')
                        continue

    def save_expenses(self):
        if os.path.exists(self.csv_file):
            os.remove(self.csv_file)

        with open(self.csv_file, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)

            for row in self.expenses:
                writer.writerow([row['date'].strftime('%Y-%m-%d'), row['category'], row['amount'], row['description']])

    def add_expense(self, **kwargs):
        self.expenses.append({'date': kwargs['date'], 'category': kwargs['category'], 'amount': kwargs['amount'],
                              'description': kwargs['description']})

    def input_expense(self):
        current_date = datetime.datetime.now().date()
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))
        description = input("Enter description: ")
        self.add_expense(date=current_date, category=category, amount=amount, description=description)

    def view_expenses(self):
        if not self.expenses:
            print("No expenses are added!")

        for expense in self.expenses:
            if expense['date'] and expense['category'] and expense['amount'] and expense['description']:
                print(f"Date: {expense['date'].date()}, Category: {expense['category']}, Amount: {expense['amount']}, Description: {expense['description']}")
            else:
                print(f"Invalid expense entry! {expense}")

    def track_budget(self):
        monthly_budget = float(input("Enter monthly budget: "))

        total_expense = 0.0
        for expense in self.expenses:
            if isinstance(expense['amount'], float):
                total_expense += float(expense['amount'])

        print(f"Total expense = {total_expense}")

        if total_expense > monthly_budget:
            print(f"WARNING: Total expense amount {total_expense} had breached the monthly budget of {monthly_budget}!")
        else:
            print(f"Remaining Balance: {monthly_budget - total_expense}")

