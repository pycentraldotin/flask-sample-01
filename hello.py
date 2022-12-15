from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!<p>"


@app.route("/hulk")
def hello_hulk():
    html_string = "<p>Hello, Hulk!<p>"
    return html_string

@app.route("/hello/<name>")
def hello_name(name):
    html_string = "<p>Hello {}<p>".format(name)
    return html_string

if __name__ == "__main__":
    app.run()
