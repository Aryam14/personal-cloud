import sqlite3
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import create_engine
import click
from flask import current_app, g # g is special object, stores data so 
                                 # multiple functions may access it. (basically makes something a global variable)

# connect to a Database
def get_db():
    if 'db' not in g:
        # connecting to SQLite database
        g.db = sqlite3.connect(
            # current_app - special object, points to the 
            # flask app that is handling a request.
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )

        # tells connection to return rows in dict format.
        g.db.row_factory = sqlite3.Row

    return g.db

# to terminate the connection if already exists.
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    
    db = get_db() # returns a db connection

    # open_resource - opens a file relative to the src package
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

# for commandline 
@click.command('init-db')
def init_db_command():
    """Clear the existing data and creating new tables."""
    init_db()
    click.echo('Initialized the database.')

# Register with the Application

def init_app(app):
    app.teardown_appcontext(close_db) # tells flask to call that function when cleaning up after returning the response
    app.cli.add_command(init_db_command) # adds a new command that can be called with flask command