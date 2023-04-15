from flask import Flask, redirect, url_for, render_template, request, make_response, flash
from flask_wtf import FlaskForm
from flask_mail import Mail, Message
from wtforms import TextAreaField, BooleanField, TextAreaField, SubmitField


app = Flask(__name__)
app.secret_key = 'secretKey'
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'jessicaldoe@gmail.com'
app.config['MAIL_PASSWORD'] = 'komocnxwuhnnmqkv'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True


class ContactForm(FlaskForm):
    name = TextAreaField("Name")
    email = TextAreaField("Email")
    subject = TextAreaField("Subject")
    message = TextAreaField("Message")
    submit = SubmitField("Send")


@app.route("/")
def about():
    return render_template("about/about.html")


@app.route("/experience")
def experience():  # binding to hello_admin call
    return render_template("experience/experience.html")


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio/portfolio.html")


@app.route('/contact', methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        name = request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]
        mail = Mail(app)
        msg = Message(subject, sender='jessicaldoe@gmail.com', recipients=['jldoe@uwaterloo.ca'])
        msg.body = f"CONTACT FORM FILLED FROM PERSONAL WEBSITE! \n\n" \
                   f"From: {name} \n" \
                   f"Email: {email} \n\n" \
                   f"{message}"
        mail.send(msg)
        flash("Message Sent!")
    return render_template('contact/contact.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
