# Import the create_cd_account and create_savings_account functions
try:
    from Account import cd_account, savings_account
except ImportError:
    print("The module 'account' could not be found. Please ensure it is in the correct directory.")
    exit(1)

# Prompt the user to enter the savings balance, interest rate, and months for the savings account.
savings_balance = float(input("Enter the savings account balance: "))
savings_interest = float(input("Enter the savings account interest rate (as a percentage): "))
savings_maturity = int(input("Enter the number of months for the savings account: "))

# Prompt the user to enter the CD balance, interest rate, and months for the CD account.
cd_balance = float(input("Enter the CD account balance: "))
cd_interest = float(input("Enter the CD account interest rate (as a percentage): "))
cd_maturity = int(input("Enter the number of months for the CD account: "))


# Define the main function
def main(): 
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
savings_balance = float(input("Enter the initial balance for the savings account: "))
interest_rate = float(input("Enter the annual interest rate (in %) for the savings account: "))
months = int(input("Enter the number of months the savings account will earn interest: "))

print(f"Initial Balance: ${savings_balance:.2f}")
print(f"Annual Interest Rate: {interest_rate:.2f}%")
print(f"Number of Months: {months}")

    # Call the create_savings_account function and pass the variables from the user.
updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
print(f"Interest Earned: ${interest_earned:.2f}")   
print(f"Updated Balance: ${updated_savings_balance:.2f}")


    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
cd_balance = float(input("Enter the initial balance for the CD account: "))
interest_rate = float(input("Enter the annual interest rate (in %) for the CD account: "))
months = int(input("Enter the number of months the CD account will earn interest: "))
print(f"Initial Balance: ${cd_balance:.2f}")
print(f"Annual Interest Rate: {interest_rate:.2f}%")
print(f"Number of Months: {months}")

    # Call the create_cd_account function and pass the variables from the user.
updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)


    # Print out the interest earned and updated CD account balance with interest earned for the given months.
print(f"Interest Earned: ${interest_earned:.2f}")
print(f"Updated Balance: ${updated_cd_balance:.2f}")
    # ADD YOUR CODE HERE
if __name__ == "__main__":
    if __name__ == "__main__":
    # Call the main function.
        main()
