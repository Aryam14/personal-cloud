from flask import make_response, render_template, request, redirect
from pymongo import MongoClient
import mysql.connector
import json
import os


class user_model():
    def __init__(self):
        try:
            self.con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Password123#@!",
                database="users"
            )
            self.cur = self.con.cursor(dictionary=True)
            self.con.autocommit = True
            print("Connection Successful")
        
        except:
            print("Some error")

    # signup model
    def user_signup_model(self, data):
        self.cur.execute(f"INSERT INTO table1(First Name='{data['First Name']}',Last Name='{data['Last Name']}', email='{data['email']}', password={data['password']})")
        if self.cur.rowcount>0:
            return make_response(f"Yayyy, you are user now {data['username']}", 200)
        else:
            return make_response({"message" : "User not created", 
                                  "error" : 400}, 400)
        
    # login model
    def user_login_model(self, data):
        password_in_db = self.cur.execute(f"SELECT password FROM table1 WHERE id='{data['uid']}'")

        # if self.rowcount == 0:
        #     return redirect("/signup")

        if data['password'] == password_in_db:
            return redirect(f"/{data['uid']}/upload")
        
        else:
            return redirect("/login")
        
    # file upload 
    def user_upload_avatar_model(self, uid, filepath):
        self.cur.execute(f"UPDATE user SET avatar='{filepath}' WHERE id={uid}")
        if self.cur.rowcount>0:
            return make_response({"message":"FILE_UPLOADED_SUCCESSFULLY"}, 200)
        else:
            return make_response({"message":"ERROR_WHILE_UPLOADING"}, 400)

    # # user data update
    # def user_update_model(self, data):
    #     self.cur.execute(f"UPDATE users SET username='{data['name']}', email='{data['email']}', password='{data['password']}'")
    #     if self.cur.rowcount>0:
    #         return make_response(f"All fileds updated successfully\n{data['username']}", {"updated_data":data}, 200)
    #     else:
    #         return make_response("User not created", 400)
    
    # delete user