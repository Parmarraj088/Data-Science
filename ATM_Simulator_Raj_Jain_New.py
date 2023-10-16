#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Dictionary to store account information (PIN as key and balance as value)
account_data = {
    "1234": 1500,
    "5678": 2000,
    "9999": 10000
}

# Function to check account balance
def check_balance(pin):
    return account_data.get(pin, "Invalid PIN")

# Function to withdraw money
def withdraw(pin, amount):
    if pin in account_data and account_data[pin] >= amount:
        account_data[pin] -= amount
        return f"Withdrawal successful. Remaining balance: {account_data[pin]}"
    elif pin not in account_data:
        return "Invalid PIN"
    else:
        return "Insufficient funds"

# Function to deposit money
def deposit(pin, amount):
    if pin in account_data:
        account_data[pin] += amount
        return f"Deposit successful. Updated balance: {account_data[pin]}"
    else:
        return "Invalid PIN"

# Main function for ATM simulator
def main():
    pin = input("Enter your 4-digit PIN: ")

    # Validate PIN
    if pin not in account_data:
        print("Invalid PIN")
        return

    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print(f"Your balance: {check_balance(pin)}")
        elif choice == "2":
            amount = float(input("Enter the amount to withdraw: "))
            print(withdraw(pin, amount))
        elif choice == "3":
            amount = float(input("Enter the amount to deposit: "))
            print(deposit(pin, amount))
        elif choice == "4":
            print("Thank you for using the ATM. Have a nice day!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the ATM simulator
if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


def get_user_input(timeout):
    start_time = time.time()
    while True:
        user_input = input("Enter something: ")
        if user_input:
            return user_input
        current_time = time.time()
        if current_time - start_time > timeout:
            print("Idle timeout reached. Exiting...")
            break

# Set the idle timeout in seconds (e.g., 10 seconds)
timeout_seconds = 10

user_input = get_user_input(timeout_seconds)
# Your code continues here after receiving user input or reaching the timeout

