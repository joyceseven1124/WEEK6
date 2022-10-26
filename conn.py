# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 19:00:13 2022

@author: 劉佳怡
"""

import mysql.connector

mydb = mysql.connector.connect(
     host="",
     user="",
     password="",
     port  = 3306,
     database="website"
   )
    
mycursor = mydb.cursor()

def filt (input_username):     
    mycursor.execute("SELECT * FROM member WHERE username= %s ",(input_username,)) 
    myresult = mycursor.fetchone() 
    return myresult
        
def add(input_name,input_username,input_password):
    mycursor.execute("INSERT INTO member (name,username,password) VALUES(%s,%s,%s)",(input_name,input_username,input_password))
    mydb.commit()
    
    
def confirm(input_username,input_password):
    mycursor.execute("SELECT * FROM member WHERE username=%s ",(input_username,))
    myresult = mycursor.fetchone()
    
    if myresult != None:
        if myresult[2] == input_username and myresult[3] == input_password:
            return "correct"
        else:
            return "wrong"
    else: 
        return "wrong"
   
def message_content():
    mycursor.execute("SELECT member.name,message.content,message.time FROM member INNER JOIN message ON member.id = message.member_id  ORDER BY message.time DESC ")
    myresult = mycursor.fetchall()
    return myresult

def message_send(id,content):
    mycursor.execute("INSERT INTO message(member_id,content) VALUES(%s,%s)",(id,content))
    mydb.commit()
    