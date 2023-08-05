#!/usr/bin/env python3

from flask import Flask, g, render_template, request
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)

# Mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user(user_id: int) -> dict:
    """Get a user dictionary by user ID.

    Args:
        user_id (int): The ID of the user.

    Returns:
        dict: A dictionary representing the user information if found, or None if not found.
    """
    return users.get(user_id)

@app.before_request
def before_request():
    """Before request function to set the user as a global variable."""
    user_id = request.args.get("login_as")
    if user_id is not None:
        user_id = int(user_id)
        user = get_user(user_id)
        g.user = user

@babel.localeselector
def get_locale() -> str:
    """Select the locale for the user.

    Returns:
        str: The locale string, either 'fr' or 'en', based on the user's preference.
             If the user's locale is not supported, it falls back to 'en'.
    """
    user_locale = getattr(g, 'user', None) and g.user.get('locale')
    return user_locale if user_locale in ["fr", "en"] else "en"  # Fallback to English

@app.route('/')
def home():
    """Render the home page template.

    Returns:
        str: The rendered HTML template for the home page.
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

