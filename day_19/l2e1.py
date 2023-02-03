# Extract all incoming email addresses as a list from the email_exchange_big.txt file.

import re

mails=[]

with open('day_19/data/email_exchange_big.txt',encoding='utf-8') as f:
    lines = f.readlines()

for line in lines:
    if line.startswith("From"):
        mail = re.findall(r'[\w\.-]+@[\w\.-]+\.[\w]+',line)
        print(mail)
        if mail:
            mails.extend(mail)

print(mails)    