from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.email import Email

@app.route('/')
def show_form():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_form():
    print(request.form['email'])
    data = {
        'email_add': request.form['email']
    }
    if not Email.validate_email(data):
        return redirect('/')
    # if email is valid, continue to success page
    Email.add(data)
    return redirect('/success')

@app.route('/success')
def show_success():
    return render_template('success.html', all_emails=Email.get_all())

@app.route('/delete/<int:id>')
def delete(id):
    data = {'id': id}
    Email.delete(data)
    return redirect('/success')