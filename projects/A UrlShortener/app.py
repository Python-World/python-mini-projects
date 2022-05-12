from flask import Flask, render_template,request,session,redirect,url_for,g
from pyshorteners import *
# from flaskext.mysqldb import MySQL 
import mysql.connector
# from flask.ext.mysqldb import MySQL 

shortener = Shortener()

app = Flask(__name__)
# app.config['MYSQL_HOST'] = 'japneet-python-db.mysql.database.azure.com'
# app.config['MYSQL_USER'] = '1FcvJ1A4lW'
# app.config['MYSQL_PASSWORD'] = 'Commando@007'
# app.config['MYSQL_DB'] = '1FcvJ1A4lW'
# mysql = MySQL(app)

app.secret_key="japneet"

@app.route('/')
def index():
    return render_template('urlShortener.html')

@app.route('/beforeRegister')
def beforeLogin():
    return render_template('login.html')

@app.route('/login',methods=['POST','GET'])
def login():
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="username"
    )
    mycursor = mydb.cursor()
    if request.method=='POST':
        signup=request.form
        name = signup['name']
        username = signup['username']
        email = signup['email']
        passw = signup['pass']
        rpassw = signup['repass']
        mycursor.execute("insert into users values(%s,%s,%s,%s,%s)",(name,username,email,passw,rpassw))
        mydb.commit()
        mycursor.close()
        return render_template('urlShortener.html')
    

@app.route('/urlShortener',methods=['POST','GET'])
def urlShortener():
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="username"
    )
    mycursor = mydb.cursor()
    if request.method=='POST':
        signnup=request.form
        username = signnup['Username']
        session['username']=username
        passw = signnup['Password']
        # mycursor.execute("TRUNCATE TABLE  link")
        mycursor.execute("select * from users where Username='"+username+"' and Password='"+passw+"'")
        r=mycursor.fetchall()
        count=mycursor.rowcount
        if count ==1:
            return render_template('url.html')
        elif count>1:
            return "More than one user"
        else:
            return "You are not a member please <a href='/register.html'>register</a>"
    else:
        return render_template('url.html')
    mydb.commit()
    mycursor.close()
    
@app.route('/history')
def history():
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="username"
    )
    mycursor = mydb.cursor()
    mycursor.execute("select * from link")
    r=mycursor.fetchall()
    username = session['username']
    len1 = len(r)
    return render_template('history.html',r=r,len1=len1,username=username)

@app.route('/url',methods=['POST','GET'])
def url():
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="username"
    )
    mycursor = mydb.cursor()
    if request.method=='POST':
        result=request.form.to_dict()
        urll = result['Url']
        x = shortener.tinyurl.short(urll)
        result['shortLink']=x
        shortLink = x
        longLink=urll
        username = session['username']
        linkCode = result['linkCode']
        mycursor.execute("insert into link values(%s,%s,%s,%s)",(longLink,shortLink,username,linkCode))
        mydb.commit()
        mycursor.close()
        return render_template('urlResult.html',result=result)

@app.route('/logout')
def logout():
    return "Logged out successfully"

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="127.0.0.1", port=5000)
         
        