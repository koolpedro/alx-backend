#!/usr/bin/env python3

"""
This module implements a Flask app with a timezone selector using Babel.
"""

from flask import Flask, request, render_template, redirect, url_for
import pytz
from babel import dates


app = Flask(__name__)


def get_timezone() -> str:
    """
    Get the selected time zone based on URL parameter or user settings.
    The function checks if the timezone is provided in the URL parameters.
    If not, it find the timezone from user settings.If not available either,
    it defaults to UTC. where it validates provided timezone, pytz.timezone
    catches the UnknownTimeZoneError exception if timezone is invalid,
    falling back to UTC.
    Returns:
        str: The selected time zone as a string.
    """
    # 1. Find timezone parameter in URL parameters
    timezone = request.args.get('timezone')

    # 2. Find time zone from user settings
    if not timezone:
        # You need to replace this part with your user settings logic
        # For example, if using a user object with a timezone attribute:
        # timezone = user.timezone
        pass

    # 3. Default to UTC if timezone is still not set
    if not timezone:
        timezone = 'UTC'

    # 4. Validate the timezone using pytz.timezone
    try:
        pytz.timezone(timezone)
    except pytz.UnknownTimeZoneError:
        # If an invalid timezone is provided, fallback to UTC
        timezone = 'UTC'

    return timezone


# Route for the index page
@app.route('/')
@dates.timezoneselector
def index():
    timezone = get_timezone()
    return render_template('7-index.html',
                           'timezone=timezone')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
