import smtplib
import pandas as pd

with open("credentials.txt", "r") as f:
    Email_Address = f.readline()
    Email_Pass = f.readline()

emails_list = pd.read_csv("emails.csv")


# Get Credentials From Environment
"""
Email_Address = os.environ.get("Email_User")
Emial_Pass = os.environ.get("Email_Pass")
print(Email_Address)
"""

# creates SMTP session
s = smtplib.SMTP("smtp.gmail.com", 587)
s.ehlo()
# start TLS for security
s.starttls()
s.ehlo()
# Authentication
s.login(Email_Address, Email_Pass)
print("login")
# message to be sent
subject = "Welcome to python"
body = """Python is an interpreted, high-level,
general-purpose programming language.\n
Created by Guido van Rossum and first released in 1991,
Python's design philosophy emphasizes code readability\n
with its notable use of significant whitespace"""
message = f"Subject : {subject} \n\n {body}"

# sending the mail
for ind in range(len(emails_list)):
    email = emails_list.loc[ind, "Emails"]
    s.sendmail(Email_Address, email, message)
    print("Send To " + email)


# terminating the session
s.quit()
print("sent")
