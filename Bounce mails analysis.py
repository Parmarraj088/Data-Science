#!/usr/bin/env python
# coding: utf-8

# In[1]:


import imaplib
import email
from email.header import decode_header

def get_reply_count(username, password, search_sender):
    # Connect to Gmail server
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    
    # Log in to your Gmail account
    mail.login(username, password)
    
    # Select the mailbox (inbox in this case)
    mail.select("inbox")
    
    # Search for emails from the specified sender
    result, data = mail.search(None, '(FROM "{}")'.format(search_sender))
    
    # Get the list of email IDs matching the search criteria
    email_ids = data[0].split()

    # Count the number of emails
    num_emails = len(email_ids)

    # Print the count
    print("Number of emails from '{}': {}".format(search_sender, num_emails))

    # Logout and close the connection
    mail.logout()

# Replace 'your_username@gmail.com', 'your_password', and 'mailer-daemon@googlemail.com' with your Gmail credentials and the desired sender
get_reply_count('your email id', 'your password', 'mailer-daemon@googlemail.com')


# In[ ]:





# In[ ]:




