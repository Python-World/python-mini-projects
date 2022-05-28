import yagmail

body = "Hello"

mail = yagmail.SMTP({"yourmail@gmail.com":"Sender Name"},"Auth Password")
mail.send(to="receiver@gmail.com",subject="Test Mail",contents=body)


