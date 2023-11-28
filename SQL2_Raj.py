#!/usr/bin/env python
# coding: utf-8

# In[8]:


import sqlite3
import re

# Function to create or connect to the database
def create_connection(db_file):
    conn = sqlite3.connect(db_file)
    return conn

# Function to create the table if it doesn't exist
def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Counts (
            org TEXT,
            count INTEGER
        )
    ''')
    conn.commit()

# Function to update or insert data into the database
def update_database(conn, org):
    cursor = conn.cursor()
    cursor.execute('SELECT count FROM Counts WHERE org = ?', (org,))
    row = cursor.fetchone()

    if row is None:
        cursor.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org,))
    else:
        cursor.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))

    conn.commit()

# Function to extract email addresses from mbox.txt and update the database
def process_file(file_name, conn):
    try:
        with open(file_name, 'r') as file:
            for line in file:
                if line.startswith('From'):
                    email = re.findall('@([^ ]+)', line)
                    if email:
                        update_database(conn, email[0])
    except FileNotFoundError:
        print(f"Error: {file_name} not found.")

# Function to display the counts
def display_counts(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT org, count FROM Counts ORDER BY count DESC')
    print("Counts:")
    for row in cursor.fetchall():
        print(row[0], row[1])

# Main function
def main():
    file_name = input("Enter file name: ")
    db_file = 'email_counts.db'

    conn = create_connection(db_file)
    create_table(conn)

    process_file(file_name, conn)
    display_counts(conn)

    conn.close()

if __name__ == "__main__":
    main()


# In[ ]:


# I checked manually in the mbox document, it were showing the total 27 domains from: and @. 
#Request you to check from your end as well. Above is the correct answer.

