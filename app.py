from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
import csv


# <--------------Class-WTF-Forms--------------->
class MyForm(FlaskForm):
    email = StringField(label='Email',
                        validators=[DataRequired(), Email(message='Invalid email format. Please include "@" symbol.')])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8,
                                                                                  message='Password must be at least 8 characters long.')])
    submit = SubmitField(label='Log In')


# <--------------Login Forms List--------------->
data = []

# <--------------App--------------->
app = Flask(__name__)

# Disable CSRF protection
app.config['WTF_CSRF_ENABLED'] = False


@app.route('/', methods=["GET", "POST"])
def login_page():
    loginForm = MyForm()
    if loginForm.validate_on_submit():
        print(loginForm.email.data)
        print(loginForm.password.data)
        email_in = loginForm.email.data
        password_in = loginForm.password.data
        with open('data.csv', mode='a', newline='') as csvfile:
            fieldnames = ['email', 'password']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Check if the file is empty, write header if necessary
            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow({"email": email_in, "password": password_in})
        return render_template('login-success.html')
    else:
        render_template('no-data.html')



    return render_template('login.html', form=loginForm)


if __name__ == '__main__':
    app.run(debug=True)
