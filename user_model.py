from flask import make_response, render_template, request
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
            # self.con = MongoClient(
            #     "localhost",
            #     username = "root",
            #     password="Password123#@!",
            #     authSource="myshinydb"
            # )
            self.cur = self.con.cursor(dictionary=True)
            self.con.autocommit = True
            print("Connection Successful")
        
        except:
            print("Some error")

    # signup
    def user_signup_model(self, data):
        self.cur.execute(f"INSERT INTO table1(name='{data['username']}', email='{data['email']}', password={data['password']})")
        if self.cur.rowcount>0:
            return make_response(f"Yayyy, you are user now {data['username']}", 200)
        else:
            return make_response("User not created", 400)
        # return render_template("user_signup_page.html")

    # user data update
    def user_update_model(self, data):
        self.cur.execute(f"UPDATE users SET username='{data['name']}', email='{data['email']}', password='{data['password']}'")
        if self.cur.rowcount>0:
            return make_response(f"All fileds updated successfully\n{data['username']}", {"updated_data":data}, 200)
        else:
            return make_response("User not created", 400)
    
    # delete user

    # file upload
 

    # file download
    def user_upload_avatar_model(self, uid, filepath):
        self.cur.execute("UPDATE user SET avatar='{filepath}' WHERE id={uid}")
        if self.cur.rowcount>0:
            return make_response({"message":"FILE_UPLOADED_SUCCESSFULLY"})
        else:
            return make_response("User not created", 400)
