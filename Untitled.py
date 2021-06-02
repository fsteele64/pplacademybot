#!/usr/bin/env python
# coding: utf-8

# In[16]:



import requests
import time

messages = ['Daily Reminder: Update CPP Student Chats \n \n 1. What did you complete with your student today? \n 2. Is your student still on schedule? \n 3. How many hours are left in their package? \n 4. How many estimated hours until course completion?']

time.sleep(10)

for message in messages:
    
    base_url = 'https://api.telegram.org/bot1724131473:AAGd1fzBu4owagZxIRl-sWNzMRxXemzYv7A/sendMessage?chat_id=-546983246&text={}'.format(message)
    print(base_url)
    requests.get(base_url)
    
    
    


# In[ ]:




