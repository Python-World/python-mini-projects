# Send Emails from CSV File

This project contains a simple bulk email script
which sends the same message to a list of recipients.


## Dependencies

This project only requires the Python standard library
(more specifically, the `csv`, `email`, and `smtplib` modules).


## Running the script

The script requires two configuration files:

* `emails.csv` should contain the email addresses to send the message to.
* `credentials.txt` should contain your SMTP server login credentials,
  with your user name and your password on sepate lines,
  with no additional whitespace or other decorations.

The project's directory contains two example files which you'll
probably both want and need to edit.

Once you have these files set up, simply

```
python Send_emails.py
```


## Development ideas

A proper email sender would use `Cc:` or `Bcc:` and send the same
message just once.

Don't play frivolously with this; your email provider,
and/or the recipient's,
may have automatic filters which quickly block anyone who sends
multiple identical messages.

The script simply hardcodes the conventions for Gmail.com.
Other providers may use a different port number and authentication regime.
