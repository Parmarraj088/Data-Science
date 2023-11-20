#!/usr/bin/env python
# coding: utf-8

# In[1]:


def calculate_emi(principal, interest_rate, tenure_years):
    # Calculate monthly interest rate
    monthly_interest_rate = interest_rate / (12 * 100)
    
    # Calculate total number of installments
    total_installments = tenure_years * 12
    
    # Calculate EMI using the formula
    emi = principal * monthly_interest_rate * ((1 + monthly_interest_rate) ** total_installments) / ((1 + monthly_interest_rate) ** total_installments - 1)
    
    return emi

def main():
    try:
        # Get user input for loan amount, interest rate, and tenure
        principal = float(input("Enter the loan amount: "))
        interest_rate = float(input("Enter the annual interest rate (in percentage): "))
        tenure_years = float(input("Enter the loan tenure (in years): "))
        
        # Calculate EMI
        emi = calculate_emi(principal, interest_rate, tenure_years)
        
        # Print the EMI amount
        print(f"Your Equated Monthly Installment (EMI) is: {emi:.2f}")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()


# In[ ]:




