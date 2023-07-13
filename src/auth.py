import functools
import os

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app
)
from werkzeug.security import check_password_hash, generate_password_hash

from src.db import get_db

# creates a blueprint named auth
bp = Blueprint('auth', __name__, url_prefix='/auth')
# Flask Blueprint is an object that works very similarly to a 
# Flask application. They both can have resources, 
# such as static files, templates, and views that are associated with routes. 
# However, a Flask Blueprint is not actually an application. 
# It needs to be registered in an application before you can run it.

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password))
                )
                db.commit()
                # make a new directory for the new user
                dirname = os.path.join(current_app.config['UPLOAD_FOLDER'], username)
                os.makedir(dirname)
            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                return redirect(url_for("auth.login"))
        
        flash(error)

    return render_template('auth/register.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?',(username,)
        ).fetchone() # returns one row from the query.

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            # session is a dict that stores data across requests.
            # the data is stored in a 'cookie' that is sent to the browser, 
            # and the browser sends it back with subsequent requests.
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('store.index'))
        
        flash(error)
    
    return render_template('auth/login.html')


# registers a function that runs before the view function,
# no matter what the URL is requested.
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.register'))

def login_required(view):
    @functools.wraps(view)
    def wrapper_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        
        return view(**kwargs)
    
    return wrapper_view