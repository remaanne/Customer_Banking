"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account

# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

        Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
       # Create an Account instance
    savings_account = Account(balance, interest_rate)

    # Calculate monthly interest rate
    monthly_interest_rate = interest_rate / 100 / 12

    # Calculate total interest earned
    interest_earned = balance * monthly_interest_rate * months

    # Update the balance with interest
    updated_balance = balance + interest_earned
    savings_account.set_balance(updated_balance)

    return updated_balance, interest_earned

    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
def create_savings_account(balance, interest_rate, months):
    savings_account = Account(balance, interest_rate)
    

# Calculate interest earned
# ADD YOUR CODE HERE
def update_balance_with_interest():
    interest_earned = balance * (interest_rate / 100) / 12 * months
    return interest_earned


# Update the savings account balance by adding the interest earned
# ADD YOUR CODE HERE
def set_balance(updated_balance):
    balance = updated_balance
    return balance

# Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
# ADD YOUR CODE HERE
def set_balance(updated_balance):
    balance = updated_balance
    return balance


# Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
# ADD YOUR CODE HERE
def set_interest(interest_earned):
    interest = interest_earned
    return interest

# Return the updated balance and interest earned.
def interest_earned():
    return balance, interest_earned

  
