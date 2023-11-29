#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# 
# ### 1. Find the Cartesian Product of the below given sets in the below cell. (In Python Code)
# 
# A = set(['a','b','c'])
# 
# S = {1,2,3}
# 

# In[7]:


from itertools import product
A = set(['a', 'b', 'c'])
S = {1, 2, 3}

cartesian_product = set(product(A, S))

print("Cartesian Product:", cartesian_product)


# ### 2. Find all the possible permutations and number of permutations of A
# 
# A = {'Red','Green','Blue'}
# 

# In[3]:


from itertools import permutations

A = {'Red', 'Green', 'Blue'}

# Find all possible permutations
all_permutations = list(permutations(A))

# Print all permutations
print("All Permutations:")
for perm in all_permutations:
    print(perm)

# Find the number of permutations
num_permutations = len(all_permutations)
print("\nNumber of Permutations:", num_permutations)


# In[ ]:





# ### 3. Research Question on Hypothesis Testing
# 
# In previous years, 52% of parents believed that electronics and social media was the cause of their teenager’s lack of sleep. Do more parents today believe that their teenager’s lack of sleep is caused due to electronics and social media?
# 
# **Population**: Parents with a teenager (age 13-18)  
# **Parameter of Interest**: p  
# 
# **Null Hypothesis:** p = 0.52  
# **Alternative Hypthosis:** p > 0.52 (note that this is a one-sided test)
# 
# **Data**: 1018 people were surveyed. 56% of those who were surveyed believe that their teenager’s lack of sleep is caused due to electronics and social media.

# ### Hint: Use  `proportions_ztest()` from `statsmodels`
# 
# Note the argument `alternative="larger"` indicating a one-sided test. The function returns two values - the z-statistic and the corresponding p-value.

# In[4]:


import statsmodels.api as sm

# Given data
total_surveyed = 1018
sample_proportion = 0.56
previous_proportion = 0.52

# Set up the hypothesis test
z_statistic, p_value = sm.stats.proportions_ztest(
    int(total_surveyed * sample_proportion), total_surveyed, previous_proportion, alternative='larger'
)

# Print the results
print(f"Z-Statistic: {z_statistic}")
print(f"P-Value: {p_value}")

# Check if the p-value is less than the significance level (e.g., 0.05) to decide whether to reject the null hypothesis
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis. There is evidence that more parents today believe their teenager's lack of sleep is caused by electronics and social media.")
else:
    print("Fail to reject the null hypothesis. There is not enough evidence to conclude that more parents today believe their teenager's lack of sleep is caused by electronics and social media.")


# ### What is your Conclusion of the hypothesis test
# 

# The conclusion of the hypothesis test depends on the calculated p-value and the chosen significance level (alpha). Let's assume a common significance level of 0.05:
# 
# Given:
# - Null Hypothesis (\(H_0\)): \(p = 0.52\) (proportion of parents believing their teenager's lack of sleep is caused by electronics and social media has not increased)
# - Alternative Hypothesis (\(H_1\)): \(p > 0.52\) (proportion has increased)
# 
# Results from the test:
# - \(Z\)-Statistic: Calculated value from the test
# - \(P\)-Value: Probability of observing a test statistic as extreme as the one computed, assuming the null hypothesis is true
# 
# Conclusion:
# - If the \(P\)-Value is less than the chosen significance level (0.05), you would reject the null hypothesis.
# - If the \(P\)-Value is greater than or equal to 0.05, you would fail to reject the null hypothesis.
# 
# Assuming a significance level of 0.05:
# - If \(P\)-Value \(< 0.05\): Reject the null hypothesis.
# - If \(P\)-Value \(\geq 0.05\): Fail to reject the null hypothesis.
# 
# Please note that the actual \(P\)-Value obtained from the test is needed to make a specific conclusion. If you have that value, you can compare it with the significance level to make the decision.

# ### 4. Calculate the set difference between the 2 sets (set1 - multipes of 3 upto a range of 31 and set2 - multiples of upto a range of 31)

# In[5]:


# Define the sets
range_limit = 31
set1 = set(range(3, range_limit + 1, 3))  # Multiples of 3 up to a range of 31
set2 = set(range(1, range_limit + 1))  # Numbers up to a range of 31

# Calculate the set difference
result_set = set1 - set2

# Print the result
print("Set Difference:", result_set)


# In[ ]:





# ### 5. Calculate a function to generate random arrays with range of (1,100) and the naive functions to calculate Mean, Varience and Standard deviation for the array generated

# In[6]:


import numpy as np

def generate_random_array(size):
    """Generate a random array with values ranging from 1 to 100."""
    return np.random.randint(1, 101, size)

def calculate_mean(array):
    """Calculate the mean of the array."""
    return sum(array) / len(array)

def calculate_variance(array):
    """Calculate the variance of the array."""
    mean = calculate_mean(array)
    return sum((x - mean) ** 2 for x in array) / len(array)

def calculate_standard_deviation(array):
    """Calculate the standard deviation of the array."""
    variance = calculate_variance(array)
    return np.sqrt(variance)

# Example: Generate a random array and calculate mean, variance, and standard deviation
random_array = generate_random_array(100)
mean_value = calculate_mean(random_array)
variance_value = calculate_variance(random_array)
std_deviation_value = calculate_standard_deviation(random_array)

# Print the results
print("Generated Random Array:", random_array)
print("Mean:", mean_value)
print("Variance:", variance_value)
print("Standard Deviation:", std_deviation_value)


# In[ ]:




