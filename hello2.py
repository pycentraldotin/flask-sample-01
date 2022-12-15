from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index2.html')


@app.route("/login", methods=['POST'])
def login():
    user = request.form['nm']
    age = request.form['age']
    # html_string = "<p>Hello {}<p>".format(user)
    # return html_string
    return render_template("welcome.html", inp_user=user, inp_age=age)


if __name__ == "__main__":
    app.run()