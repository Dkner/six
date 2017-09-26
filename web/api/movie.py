import os
import logging
from flask import Blueprint, render_template, abort, session, request, flash, url_for, redirect, send_from_directory

logger = logging.getLogger(__name__)
movie_api = Blueprint('movie_api', __name__)

RESOURCE_FOLDER='/Users/liliang/work/six/testdata/movie1'

@movie_api.route('/show_entries')
def show_entries():
    if session.get('logged_in'):
        entries = os.listdir(RESOURCE_FOLDER)
        return render_template('show_entries.html', entries=entries)
    else:
        redirect(url_for('login'))

@movie_api.route('/open_file/<filename>')
def open_file(filename):
    return send_from_directory(RESOURCE_FOLDER, filename)