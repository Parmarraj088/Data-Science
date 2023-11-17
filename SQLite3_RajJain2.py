#!/usr/bin/env python
# coding: utf-8

# In[46]:


import sqlite3

# Connect to SQLite database (creates a new one if not exists)
conn = sqlite3.connect('raj.db')
cur = conn.cursor()

# Create the "Ages" table
cur.execute('''
CREATE TABLE IF NOT EXISTS raj (
    name VARCHAR(128),
    age INTEGER
)''')

# Delete any existing rows
cur.execute('DELETE FROM raj')

# Insert rows into the "Ages" table
cur.execute("INSERT INTO Ages (name, age) VALUES ('Mara', 28)")
cur.execute("INSERT INTO Ages (name, age) VALUES ('Otto', 33)")
cur.execute("INSERT INTO Ages (name, age) VALUES ('Fyn', 31)")
cur.execute("INSERT INTO Ages (name, age) VALUES ('Neshawn', 17)")

# Commit the changes
conn.commit()

# Retrieve and print the result
cur.execute("SELECT hex(name || age) AS X FROM Ages ORDER BY X")
row = cur.fetchone()
result = row[0]

# Close the database connection
conn.close()

print(f"The first row in the resulting record set: {result}")


# In[ ]:





# In[ ]:




