#!/usr/bin/env python3
"""Flask App
"""
from flask import Flask, render_template, redirect, request, abort, url_for
from db import DB

app = Flask(__name__, template_folder='.')
db = DB()


@app.route('/', strict_slashes=False)
def index():
    """Index route
    """
    return render_template('index.html')


@app.route('/<shorturl>', strict_slashes=False)
def get_url(shorturl: str):
    """ route
    """
    url = db.get_url(shorturl)
    if not url:
        abort(404)
    return redirect(url)


@app.route('/', methods=['POST'], strict_slashes=False)
def create_shorturl():
    """Creates a new shorturl
    """
    url = request.form.get('url')
    shorturl = db.create_shorturl(url)
    return render_template('index.html', shorturl=shorturl)


@app.route('/shorturls', strict_slashes=False)
def get_shorturls():
    """Lists every shorturl in the database
    """
    shorturls = db.get_shorturls()
    return render_template('shorturls.html', shorturls=shorturls)

@app.route('/shorturls', methods=['DELETE'], strict_slashes=False)
def delete_shorturl():
    """Deletes a shorturl
    """
    shorturl = request.args.get('shorturl')
    db.delete_shorturl(shorturl)
    shorturls = db.get_shorturls()
    return render_template('shorturls.html', shorturls=shorturls)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
