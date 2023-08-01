#!/usr/bin/env python3
"""Task 5"""
from flask import Flask, g, render_template, request

app = Flask(__name__)

# Mock user database table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user(user_id):
    """Return the user dictionary for the given user_id, or None if not found."""
    return users.get(user_id)

@app.before_request
def before_request():
    """Set the logged-in user (if any) as a global on flask.g.user."""
    user_id = request.args.get('login_as')
    g.user = get_user(int(user_id)) if user_id else None

@app.route('/')
def index():
    """Render the index page with a welcome message if logged in, or a default message if not logged in."""
    return render_template('index.html', user=g.user)

if __name__ == '__main__':
    app.run(debug=True)

