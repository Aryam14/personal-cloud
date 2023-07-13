from flask import (
    Blueprint, flash, g, redirect, render_template, session, request, url_for, send_file, current_app
)
from werkzeug.exceptions import abort
from werkzeug.utils import secure_filename

from src.auth import login_required, dirname
from src.db import get_db

import os

bp = Blueprint('store', __name__)

# user_id = session.get('user_id')
@bp.route('/')
def index():
    return render_template("store/index.html")

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
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        
    return redirect(url_for('index'))


@bp.route('/download/<path:filename>')
@login_required
def download(filename):
    path = os.path.join(current_app.config['UPLOAD_FOLDER'],filename)
    return send_file(path)

