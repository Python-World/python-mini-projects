'''
Python Gdrive uploader using pydrive
It will upload all files in a "Dir_Path" folder
'''
'''
INSTRUCTION TO USE


#Authentication

Drive API requires OAuth2.0 for authentication. PyDrive makes your life much easier by handling complex authentication steps for you.

1.Go to APIs Console and make your own project.
2.Search for ‘Google Drive API’, select the entry, and click ‘Enable’.
3.Select ‘Credentials’ from the left menu, click ‘Create Credentials’, select ‘OAuth client ID’.
4.Now, the product name and consent screen need to be set -> click ‘Configure consent screen’ and follow the instructions. Once finished:
5.Select ‘Application type’ to be Web application.
6.Enter an appropriate name.
7.Input http://localhost:8080 for ‘Authorized JavaScript origins’.
8.Input http://localhost:8080/ for ‘Authorized redirect URIs’.
9.Click ‘Save’.
10.Click ‘Download JSON’ on the right side of Client ID to download client_secret_<really long ID>.json.
The downloaded file has all authentication information of your application. Rename the file to “client_secrets.json” and place it in the directory where your py script is there.

'''



import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

Dir_Path = r"C:\Users\Admin\Desktop\Test"

for x in os.listdir(Dir_Path): 
   
    f = drive.CreateFile({'title': x}) 
    f.SetContentFile(os.path.join(Dir_Path, x)) 
    f.Upload() 
