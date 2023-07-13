import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# application factory function
def create_app(test_config=None):    
    app = Flask(__name__, instance_relative_config=True, template_folder='templates')
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        UPLOAD_FOLDER = '/home/user/personal-cloud/src/uploads',
        # points where the db file will be saveed.
        DATABASE = os.path.join(app.instance_path, 'src.sqlite'),
    )

    # load the config file (if exstis or )
    # if test_config is None:
    #     app.config.from_pyfile('config.py', silent=True)
    # else:
    #     app.config.from_mapping(test_config)

    # # creates the instance folder
    # try:
    #     os.makedirs(app.instance_path)
    # except OSError:
    #     pass

    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    # register with application
    from . import db
    db.init_app(app)

    from . import auth, store
    app.register_blueprint(auth.bp)
    app.register_blueprint(store.bp)
    app.add_url_rule('/', endpoint='index') # allows index to appear without /blog prefix

    
    return app