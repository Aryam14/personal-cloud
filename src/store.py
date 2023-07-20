from flask import (
    Blueprint, flash, g, redirect, render_template, session, request, url_for, send_file, current_app, jsonify
)
from werkzeug.exceptions import abort
from werkzeug.utils import secure_filename

from src.auth import login_required
from src.db import get_db

import os
import pandas as pd

from src.deDuplicator import deDuplicator

bp = Blueprint('store', __name__)


# get the data in the user folder
def get_download_data(path):
    directory_data = []
    file_list = os.listdir(path)

    for file in file_list:
        file_path = os.path.join(path,file)

        ext = file.rsplit('.', 1)[1].lower()
        size = os.stat(file_path).st_size/1024
        filename = file.rsplit('.', 1)[0]
        
        file_data = {'filename':filename, 'ext':ext, 'size':size}
        directory_data.append(file_data)

    return directory_data

# user_id = session.get('user_id')
@bp.route('/')
@login_required
def index():
    return render_template("index.html")

# upload logic for an IOT device
# @bp.route('/iot_upload/<path:filename>', methods=('POST','GET'))
# def iot_upload():
#     if request.method == 'POST':
#         user_id = session.get('user_id')
#         db = get_db()
#         user = db.execute(
#             'SELECT * FROM user WHERE id = ?', (user_id,)
#         ).fetchone()

#         file = request.files['files']
#         filename = secure_filename(file.filename)

#         path = os.path.join(current_app.config['UPLOAD_FOLDER'],user['username'],filename)
#         file.save(path)


# upload the file to the user folder
@bp.route('/upload', methods=('GET', 'POST'))
@login_required
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            # upload logic
            user_id = session.get('user_id')
            db = get_db()
            user = db.execute(
                'SELECT * FROM user WHERE id = ?', (user_id,)
            ).fetchone()
            
            filename = secure_filename(file.filename)
            path = os.path.join(current_app.config['UPLOAD_FOLDER'],user['username'],filename)
            file.save(path)

    return redirect(url_for('index'))

# display the files in the user folder
@bp.route('/downloads')
@login_required
def download_data():
    db = get_db()
    user = db.execute(
        'SELECT * FROM user WHERE id = ?', (session.get('user_id'),)
    ).fetchone()
    path = os.path.join(current_app.config['UPLOAD_FOLDER'],user['username'])
    data = get_download_data(path)

    # return data
    return render_template('downloads.html', data = data)


# download the file in the user folder
@bp.route('/download/<path:filename>')
@login_required
def download(filename):
    user_id = session.get('user_id')
    db = get_db()
    user = db.execute(
        'SELECT * FROM user WHERE id = ?', (user_id,)
    ).fetchone

    path = os.path.join(current_app.config['UPLOAD_FOLDER'],user['username'],filename)

    return send_file(path, as_attachment=True)

