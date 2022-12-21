# Task 01 – Dictionary
#
# Imagine you have to write a (very simple) bookkeeping system for a bank
# that keeps track of the account balances of each of its customers.
#
#    1. Write a function that spans a dictionary holding a default balance of 0 for an initial list of customers.
#    For simplicity, assume customer names are unique identifier.
#    (optional) Can you express that same functionality using a lambda function?

#    2. What are elegant ways to add or remove single and multiple customers using the functionality of dict?

#    3. Now write two simple functions that allow you to deposit and withdraw money for a given bank customer.

#    4. Include error messages for inputs that are not permissible,
#    e.g., withdrawing negative amounts or overdrawing the account, etc.


# 1.
def get_dict_0():
    customers = ["Jim Halpert", "Pam Beesly", "Michael Scott", "Kevin Malone"]
    customers_dict = dict((name, float(0)) for name in customers)
    return customers_dict


customers_dict = get_dict_0()



# 2.

def remove_customers (customers_dict):
    customers_to_be_removed = []
    rem_custom_user_input = input("Which customer is to be removed? Please provide the first and the last name:\n")
    customers_to_be_removed.append(rem_custom_user_input)
    for name in customers_to_be_removed:
        customers_dict.pop(name, None)


def add_customers(customers_dict):
    customers_to_be_added = []
    add_custom_user_input = input("Which customer is to be added? Please provide the first and the last name:\n")
    customers_to_be_added.append(add_custom_user_input)
    for name in customers_to_be_added:
        customers_dict.update({name: float(0)})


#    3. Now write two simple functions that allow you to deposit and withdraw money for a given bank customer.

def deposit_money(customers_dict):
    deposit_person_name = input("Please enter the first and last name of the person that wants to deposit money:\n")

    while True:
        deposit_amount_input = float(input("Please enter the amount of money that is to be added:\n"))
        if deposit_amount_input <= 0:
            print("Please enter a number bigger than 0.")
            continue
        else:
            break

    if deposit_person_name in customers_dict:
        dep_new_amount = customers_dict[deposit_person_name] + deposit_amount_input
        customers_dict.update({deposit_person_name: dep_new_amount})
    else:
        print("Please enter a valid input.")


def withdraw_money(customers_dict):
    withdraw_person_name = input("Please enter the first and last name of the person that wants to withdraw money:\n")

    while True:
        withdraw_amount_input = float(input("Please enter the amount of money that is to be withdrawn:\n"))
        if withdraw_amount_input <= 0:
            print("Please enter a number bigger than 0.")
            continue
        else:
            break

    if withdraw_person_name in customers_dict:
        with_new_amount = customers_dict[withdraw_person_name] - withdraw_amount_input
        if with_new_amount < 0:
            print("Your account balance is not allowed to be negative. Eat the rich to add money to your account.")
        else:
            customers_dict.update({withdraw_person_name: with_new_amount})
    else:
        print("Please enter a valid input.")



# Task 02 – Classes

# The manager thinks that the simple bookkeeping system you have built is not powerful enough.
# She requests that you start from scratch and use classes instead.

#    1. Write a simple class with appropriate constructor __init__ that initializes an object of class "Customer"
#    tracking the same information as in Task 01.

#    2. Now write two simple methods for class Customer that allow you to deposit and withdraw money
#    for a given customer object.

#    3. Include error messages for inputs that are not permissible, e.g.,
#    withdrawing negative amounts or overdrawing the account.

#    4. (Inheritance) Write a child class SavingsCustomer that inherits its features from the parent class Customer.
#    A savings customer has an extra savings balance for receiving extra interest.
#    The class should have a method to transfer money back and forth between the accounts' main balance
#    as well as the savings balance. Do not forget to add reasonable error messages.



class Customer:
    """The attributes of our customer"""

    def __init__(self, first_name, last_name, account_balance=float(0)):
        self.first_name = first_name
        self.last_name = last_name
        self.account_balance = account_balance

    def full_name(self):
        full_name = self.first_name + " " + self.last_name
        return full_name

    def print_current_balance(self):
        print_current_balance = str(self.full_name() + self.account_balance)
        return print_current_balance

    def deposit_money(self):
        try:
            dep_money_input = float(input("Please enter the amount of money that is to be added to your account:\n"))
            if dep_money_input > 0:
                dep_result = self.account_balance + dep_money_input
                self.account_balance = dep_result
                return f"Thank you! Your current balance is: {dep_result}."

            else:
                return "You can only deposit an amount bigger than 0."
        except ValueError as err:
            print("Invalid input. Please only enter numbers.\n"
                  "Error: ", err)

    def withdraw_money(self):
        try:
            with_money_input = float(input("Please enter the amount of money that is to be withdrawn from your account:\n"))
            if self.account_balance - with_money_input >= 0:
                with_result = self.account_balance - with_money_input
                self.account_balance = with_result
                return f"Thank you! Your current balance is: {with_result}."
            else:
                return "Your account balance is not allowed to be negative. Eat the rich to add money to your account."
        except ValueError as err:
            print("Invalid input. Please only enter numbers.\n"
                  "Error: ", err)



class SavingsCustomer(Customer):
    def __init__(self, first_name, last_name, account_balance=float(0), saving_balance=float(0)):
        super().__init__(first_name, last_name, account_balance)
        self.saving_balance = saving_balance

    def deposit_money_savings(self):
        try:
            dep_money_input_savings = float(input("Please enter the amount of money that is to be added to your savings account:\n"))
            if dep_money_input_savings > 0:
                dep_result_savings = self.saving_balance + dep_money_input_savings
                self.saving_balance = dep_result_savings
                return f"Thank you! Your current balance is: {dep_result_savings}."

            else:
                return "You can only deposit an amount bigger than 0."
        except ValueError as err:
            print("Invalid input. Please only enter numbers.\n"
                  "Error: ", err)

    def withdraw_money_savings(self):
        try:
            with_money_input_savings = float(input("Please enter the amount of money that is to be withdrawn from your savings account:\n"))
            if self.saving_balance - with_money_input_savings >= 0:
                with_result_savings = self.saving_balance - with_money_input_savings
                self.saving_balance = with_result_savings
                return f"Thank you! Your current balance is: {with_result_savings}."
            else:
                return "Your account balance is not allowed to be negative. Eat the rich to add money to your account."
        except ValueError as err:
            print("Invalid input. Please only enter numbers.\n"
                  "Error: ", err)

    def deposit_and_withdraw_account_savings(self):
        while True:

            try:
                deposit_or_withdraw = input("Do you want to deposit or withdraw money from one account to the other?\n").lower()
                if deposit_or_withdraw == "deposit" or deposit_or_withdraw == "withdraw":
                    pass
                else:
                    print("Please enter a valid input: 'deposit' or 'withdraw'")
                    continue
            except (ValueError, TypeError):
                print("Please enter a valid input: 'deposit' or 'withdraw'")
                continue

            try:
                amount_money = float(input("Please enter the amount of money: \n"))
                amount_money = int(amount_money)
            except (ValueError, TypeError):
                print("Please enter a valid number.")
                continue

            try:
                to_which_account = input("To/from which account? For your main account enter 'main', for your savings account enter 'savings'\n").lower()
                if to_which_account == "main" or to_which_account == "savings":
                    pass
                else:
                    print("Please enter either 'main' or 'savings'.")
                    continue
            except (ValueError, TypeError):
                print("Please enter either 'main' or 'savings'.")
                continue

            make_sure = input(f"""
            Are these options correct: 
            You want to {deposit_or_withdraw} {amount_money} to/from your {to_which_account} account. 
            Correct? 'yes' or 'no'\n""")
            try:
                if make_sure.lower() == "yes":
                    if deposit_or_withdraw.lower() == "deposit" and to_which_account.lower() == "main":
                        new_account_balance = self.account_balance + amount_money
                        self.account_balance = new_account_balance
                        new_savings_balance = self.saving_balance - amount_money
                        self.saving_balance = new_savings_balance
                        if new_account_balance >= 0 and new_savings_balance >= 0:
                            print(f"Thank you! Your main account's balance is: {new_account_balance} and your savings account's balance is: {new_savings_balance}.")
                            break
                        else:
                            print("Neither of your accounts can be negative.")
                            continue

                    if deposit_or_withdraw.lower() == "deposit" and to_which_account.lower() == "savings":
                        new_account_balance = self.account_balance - amount_money
                        self.account_balance = new_account_balance
                        new_savings_balance = self.saving_balance + amount_money
                        self.saving_balance = new_savings_balance
                        if new_account_balance >= 0 and new_savings_balance >= 0:
                            print(f"Thank you! Your main account's balance is: {new_account_balance} and your savings account's balance is: {new_savings_balance}.")
                            break
                        else:
                            print("Neither of your accounts can be negative.")
                            continue

                    if deposit_or_withdraw.lower() == "withdraw" and to_which_account.lower() == "main":
                        new_account_balance = self.account_balance - amount_money
                        self.account_balance = new_account_balance
                        new_savings_balance = self.saving_balance + amount_money
                        self.saving_balance = new_savings_balance
                        if new_account_balance >= 0 and new_savings_balance >= 0:
                            print(
                            f"Thank you! Your main account's balance is: {new_account_balance} and your savings account's balance is: {new_savings_balance}.")
                            break
                        else:
                            print("Neither of your accounts can be negative.")
                            continue

                    if deposit_or_withdraw.lower() == "withdraw" and to_which_account.lower() == "savings":
                        new_account_balance = self.account_balance + amount_money
                        self.account_balance = new_account_balance
                        new_savings_balance = self.saving_balance - amount_money
                        self.saving_balance = new_savings_balance
                        if new_account_balance >= 0 and new_savings_balance >= 0:
                            print(
                            f"Thank you! Your main account's balance is: {new_account_balance} and your savings account's balance is: {new_savings_balance}.")
                            break
                        else:
                            print("Neither of your accounts can be negative.")
                            continue

                else:
                    print("Please try again with correct input.")
            except (ValueError, TypeError) as err:
                print("Enter valid input." 
                      "The error we encountered was: ", err)

            break







