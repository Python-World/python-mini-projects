from tkinter import *
import time
import requests
import json


root=Tk()

root.geometry("500x250")

match_data=requests.get('http://cricapi.com/api/cricketScore?unique_id=1216519&apikey=B5fGKy2dzmYwzwswez4mdzbLBpE2')
json_data=match_data.json()

def times():
    current_score=json_data['stat']
    current_score1=json_data['score']
    score.configure(text="required : "+current_score)
    score.configure(text="current score : "+current_score1)
    score.after(200,times)



score=Label(root,font=("time",15,"bold"),bg="white")
score.grid(row=2,column=2,pady=25,padx=100)
times()

root.mainloop()