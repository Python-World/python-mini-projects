## Program to fetch the HTTP status code

This script is used to fetch the status code of any request.

Input: 
-> URL of a website or an API

Output:
-> Line 1 : Status code of the response followed by emoji (thumbsup/thumbsdown)
-> Line 2 : Relevant message about the status code.
i.e. If status code corresponds to failure, then reason of failure would be shown in the message field.

## Prerequisites

This program uses and external dependency of "emoji" library to display the emojis in output.
This library can be installed easily by using the following command:
pip install -r requirements.txt

## How to use this script?

-> Install the requirements.
->Type the following command:
python fetch_http_status_code.py
->A message asking URL/API would be displayed : Enter any url of choice and check the output
