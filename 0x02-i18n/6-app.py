#!/usr/bin/env python3
from flask import Flask, request, render_template


app = Flask(__name__)

SUPPORTED_LOCALES = ['en', 'fr', 'es', 'de']


def get_locale():
    # Check if locale from URL parameters is supported
    url_locale = request.args.get('locale')
    if url_locale and url_locale in SUPPORTED_LOCALES:
        return url_locale

    # Check if locale from user settings is supported
    user_settings_locale = get_user_settings_locale()  

    # Replace this with your function to get user settings
    if user_settings_locale and user_settings_locale in SUPPORTED_LOCALES:
        return user_settings_locale

    # Check if locale from request header is supported
    request_header_locale = request.headers.get('Accept-Language')
    if request_header_locale:
        request_header_locale = request_header_locale.split(',')[0].split('-')[0]
        if request_header_locale in SUPPORTED_LOCALES:
            return request_header_locale

    # Return the default locale if none of the above options are available
    return 'en'

@app.route('/')
def index():
    preferred_locale = get_locale()
    return render_template('6-index.html', preferred_locale=preferred_locale)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port="5000")
