from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Lucas'}
    posts = [
        {
            'autor': {'username': 'John'}
            'body': 'Beautiful day in Portland'
        },
        {
            'autor': {'username': 'Susan'}
            'body': 'The Avengers movie was so cool!'    
        }
    ]

    return render_template('index.html', title='Home', user=user)