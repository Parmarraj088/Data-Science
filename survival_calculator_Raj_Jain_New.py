#!/usr/bin/env python
# coding: utf-8

# In[10]:


# Function to calculate remaining survival time
def calculate_remaining_time(age, time_unit):
    if time_unit == "months":
        remaining_time = age * 12
    elif time_unit == "weeks":
        remaining_time = age * 52
    elif time_unit == "hours":
        remaining_time = age * 365 * 24
    elif time_unit == "minutes":
        remaining_time = age * 365 * 24 * 60
    elif time_unit == "seconds":
        remaining_time = age * 365 * 24 * 60 * 60
    else:
        return "Invalid time unit"
    
    return remaining_time

# Main function
def main():
    try:
        age = int(input("Enter your age: "))
        time_unit = input("Select time unit (months, weeks, hours, minutes, or seconds): ").lower()
        
        remaining_time = calculate_remaining_time(age, time_unit)
        if isinstance(remaining_time, str):
            print(remaining_time)
        else:
            print(f"Converted time unit: {remaining_time} {time_unit}")
    except ValueError:
        print("Invalid input. Please enter a valid age.")

# Run the program
if __name__ == "__main__":
    main()


# In[ ]:




