from flask import Flask, request, session, redirect, render_template, flash, url_for
from api.movie import movie_api

app = Flask(__name__)
app.config.update(dict(
    SECRET_KEY='key',
    USERNAME='liliang',
    PASSWORD='rock'
))

@app.route('/ping')
def ping():
    return 'True'

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('movie_api.show_entries'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('login'))

app.register_blueprint(movie_api, url_prefix='/movie')

if __name__ == '__main__':
    app.run(debug=True)