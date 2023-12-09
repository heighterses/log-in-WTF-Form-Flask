from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField

# <--------------Class-WTF-Forms--------------->
class MyForm(FlaskForm):
    email = StringField('Email')
    password = StringField('Password')

# <--------------App--------------->
app = Flask(__name__)

# Disable CSRF protection
app.config['WTF_CSRF_ENABLED'] = False

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/login')
def login_wtf():
    loginForm = MyForm()
    return render_template('login-wtf.html', form=loginForm)

if __name__ == '__main__':
    app.run(debug=True)
