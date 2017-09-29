import logging
from flask import Blueprint, render_template, abort, session, request, flash, url_for, redirect
from logic.movie import MovieService

logger = logging.getLogger(__name__)
movie_api = Blueprint('movie_api', __name__)

FILE_API = 'http://127.0.0.1:8000/'
RESOURCE_FOLDER='/Users/liliang/work/six/testdata'

@movie_api.route('/show_movie_list')
def show_movie_list():
    if session.get('logged_in'):
        movie_list = MovieService.get_all_movie()
        return render_template('movie_list.html', movie_list=movie_list, file_url_prefix=FILE_API)
    else:
        redirect(url_for('login'))

@movie_api.route('/show_movie_detail/<movie_id>')
def show_movie_detail(movie_id):
    print('movie detail for {}'.format(movie_id))
    pass