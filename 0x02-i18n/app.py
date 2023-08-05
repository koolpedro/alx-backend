#!/usr/bin/env python3
"""web application to display the current time in different languages."""

from flask import Flask, render_template
import datetime
import pytz


app = Flask(__name__)


def get_current_time() -> str:
    """Get the current time in the inferred time zone."""
    # Replace 'YOUR_TIMEZONE' with the inferred time zone, desired time zone
    tz = pytz.timezone('YOUR_TIMEZONE')
    current_time = datetime.datetime.now(tz).strftime('%b %d, %Y, %I:%M:%S %p')
    return current_time


@app.route('/')
def index() -> str:
    """Render the home page with the current time."""
    # Get the current time in the inferred time zone
    current_time = get_current_time()
    return render_template('index.html',
                           'current_time=current_time')


if __name__ == '__main__':
    app.run(debug=True)
