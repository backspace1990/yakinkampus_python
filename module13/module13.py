import datetime
from imap_tools import MailBox, AND
users = '<users_email>'
users_passwrd = '<users_password>'

mail_box = MailBox('imap.gmail.com')
mail_box.login(users, users_passwrd, initial_folder="INBOX")
print(mail_box.login(users, users_passwrd))

# kriter = AND(date_gte=datetime.date(2022, 2, 1), from_=users)
# 
# for msg in mail_box(kriter):
#     print(msg.text)