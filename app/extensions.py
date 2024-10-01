from flask_pymongo import PyMongo

# Initialize the extension
mongo = PyMongo()

def configure_extensions(app):
    # Initialize extensions with the app
    mongo.init_app(app)
