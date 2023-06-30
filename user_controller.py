# for handling requests
from app import app
from user_model import user_model
from flask import request, send_file
import datetime

obj = user_model()
@app.route('/user/getall')
def user_getall_controller():
    return obj.user_getall_model()

@app.route("/user/addone", methods = ["POST"])
def user_addone_controller():
    print(request.form)
    return obj.user_addone_model(request.form)

@app.route("/user/update", methods = ["PUT"])
def user_update_controller():
    print(request.form)
    return obj.user_update_model(request.form)

@app.route("/user/<uid>/upload/avatar", methods=["PUT"])
def user_upload_avatar_controller(uid):
    file = request.files['avatar']
    uniqueFilename = str(datetime.now().timestamp()).replace(".", "")
    filenameSplit = file.filename.split["."]
    ext = filenameSplit[len(filenameSplit[:-1])]
    filePath = f"uploads/{uniqueFilename}.{ext}"
    file.save(filePath)
    return obj.user_upload_avatar_model(uid)#"This is user_upload_avatar_controller"

# @app.route(/uploads/<filename>)
# def user_getavatar_controller(filename):


