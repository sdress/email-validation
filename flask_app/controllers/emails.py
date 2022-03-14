from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.email import Email

@app.route('/')
def show_form():
    return render_template('index.html')

@app.route('/process')
def process_form():
    data = {
        'email_add': request.form('email')
    }
    Email.create(data)
    return redirect('/')

@app.route('/some-page/<int:id>')
def show_something_else(id):
    data = {
        'id': id
    }
    return render_template('something.html', data)
