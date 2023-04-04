from flask import Flask, redirect, url_for, render_template, request, make_response
from flask_wtf import FlaskForm
from wtforms import TextAreaField, BooleanField, TextAreaField, SubmitField
import pandas as pd


app = Flask(__name__)
app.secret_key = 'secretKey'


class ContactForm(FlaskForm):
    name = TextAreaField("Name")
    email = TextAreaField("Email")
    subject = TextAreaField("Subject")
    message = TextAreaField("Message")
    submit = SubmitField("Send")


@app.route("/")
def about():
    return render_template("about/index.html")


@app.route("/experience")
def experience():  # binding to hello_admin call
    return "Experiences"


@app.route("/portfolio")
def portfolio():
    return 'Portfolio!'


@app.route('/contact', methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        name = request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]
        res = pd.DataFrame({'name': name, 'email': email, 'subject': subject,'message': message}, index=[0])
        res.to_csv('contactusMessage.csv')
        print("The data are saved !")
        return redirect("/")
    else:
        return render_template('contact/index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
