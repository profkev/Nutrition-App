from flask import Blueprint, render_template

home = Blueprint('home', __name__)  # Define the blueprint

@home.route('/')
def index():
    return render_template('home.html')  # Render a simple template
