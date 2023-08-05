#!/usr/bin/env python3

from flask import Flask, request, render_template

app = Flask(__name__)

SUPPORTED_LOCALES = ['en', 'fr']



def get_locale() -> str:

    """
    Get the user's preferred locale based on priority:
    1. Locale from URL parameters
    2. Locale from user settings
    3. Locale from request header
    4. Default locale

    Returns:
        str: The user's preferred locale.
    """
    # Check if the locale is provided in the URL parameters
    locale = request.args.get('locale')
    if locale and locale in SUPPORTED_LOCALES:
        return locale

    # Check if the locale is set in the user settings (you should implement this logic)
    # Replace `get_user_locale()` with the appropriate function to get the user's locale from settings
    user_locale = get_user_locale()
    if user_locale and user_locale in SUPPORTED_LOCALES:
        return user_locale

    # Check if the locale is provided in the request header
    # For example, if you are using 'Accept-Language' header to specify locale
    header_locale = request.headers.get('Accept-Language')
    if header_locale:
        # Extract the first part of the header value as it contains the locale
        header_locale = header_locale.split(',')[0].split(';')[0].lower()
        if header_locale in SUPPORTED_LOCALES:
            return header_locale

    # If no preferred locale is found, return the default locale
    return 'en'  # Replace 'en' with your default locale

@app.route('/')
def index():
    """
    Render the index template with the user's preferred locale.
    """
    locale = get_locale()
    return render_template('6-index.html', locale=locale)

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = "5000")
