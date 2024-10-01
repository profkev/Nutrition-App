from flask import Flask
from .config import Config  # Ensure this imports correctly from the config.py file
from .extensions import configure_extensions
from .controllers.home_controller import home  # Import the home blueprint
from .api.recipe_routes import recipe_api  # Import the recipe API blueprint
from .api.user_routes import user_routes  # Import the user routes separately

def create_app():
    """
    Create a Flask application using the app factory pattern.

    :return: Flask app
    """
    app = Flask(__name__)
    app.config.from_object(Config)  # Load configuration from Config class

    configure_extensions(app)  # Initialize Flask extensions with the app instance

    register_blueprints(app)  # Register all blueprints for the application

    # Optionally, setup error handlers here if needed
    setup_error_handlers(app)

    return app

def register_blueprints(app):
    """
    Registers all blueprints for the application.

    :param app: Flask application instance
    """
    app.register_blueprint(home)  # Home page routes
    app.register_blueprint(recipe_api, url_prefix='/api/recipes')  # Recipe-related API routes
    app.register_blueprint(user_routes, url_prefix='/api/users')  # User-related API routes

def setup_error_handlers(app):
    """
    Setup error handlers for the application.

    :param app: Flask application instance
    """
    @app.errorhandler(404)
    def not_found_error(error):
        return "Resource not found.", 404

    @app.errorhandler(500)
    def internal_error(error):
        return "An internal error occurred.", 500

# Run the application with debug enabled
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
