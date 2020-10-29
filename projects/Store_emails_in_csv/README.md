# Store emails in CSV

This project contains a simple script to extract email messages
from an IMAP server.

The messages are written to a simple four-column CSV file.


## Dependencies

This depends on the BeautifulSoup library and `lxml`
for extracting text from HTML messages.


## Running the script

You will need to have a file `credentials.txt`
with your IMAP server account name and password on separate lines.

Gmail - and many other IMAP providers -
requires you to create a separate "application password"
to allow this code to run, so probably do that first.
Then put that password in `credentials.txt`.

Then simply run

```
python store_emails.py
```

This generates `mails.csv` in the current directory.

The generated CSV file contains the following fields for each message:

* Date
* From (Sender)
* Subject
* Message text


## Development ideas

This hardcodes the IMAP server for Gmail.com and the `"INBOX"` folder.
Perhaps this should be configured outside of the code
for easier customization.

This brutally marks all messages as read.
Perhaps make it `PEEK` so as to not change the message flags.

This will read everything in the `INBOX` folder.
It could be useful to make it remember which messages it has already seen,
and update a CSV file only with information from messages which have
arrived since the previous poll.

It might be useful to be able to specify which messages to fetch,
instead of have it fetch everything every time.

The exception handling is not a good example of how to do this properly.


## Author Name

[Shiv Thakur](https://github.com/ShivSt)
