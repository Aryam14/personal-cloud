# for handling requests
from app import app
from user_model import user_model
from flask import request, send_file, render_template
import datetime

obj = user_model()

@app.route('/signup', methods=["POST"] )
def user_signup():
    return obj.user_signup_model(request.form)


@app.route('/login', methods = ['POST'])
def user_login():
    return obj.user_login_model(request.form)


# @app.route('/user/getall')
# def user_getall_controller():
#     return obj.user_getall_model()

# @app.route("/user/addone", methods = ["POST"])
# def user_addone_controller():
#     print(request.form)
#     return obj.user_addone_model(request.form)

# @app.route("/user/update", methods = ["PUT"])
# def user_update_controller():
#     print(request.form)
#     return obj.user_update_model(request.form)

@app.route("/<uid>/upload", methods=['PUT'])
def user_upload_controller(uid):
    file = request.files['avatar']
    uniqueFilename = str(datetime.now().timestamp()).replace(".", "")
    filenameSplit = file.filename.split["."]
    ext = filenameSplit[len(filenameSplit[:-1])]
    filePath = f"uploads/{uniqueFilename}.{ext}"
    file.save(filePath)
    return obj.user_upload_avatar_model(uid, filePath)#"This is user_upload_avatar_controller"

# @app.route("/<uid>/download", methods=['GET'])
# def user_download_controller(uid):
    
# @app.route(/uploads/<filename>)
# def user_getavatar_controller(filename)