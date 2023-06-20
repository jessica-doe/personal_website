from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = 'secretKey'


@app.route("/")
def about():
    return render_template("about/about.html")


if __name__ == '__main__':
    app.run(debug=True)