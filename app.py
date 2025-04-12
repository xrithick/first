from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/first")
def first():
    return render_template("first.html")

@app.route("/redirect-wait")
def redirect_wait():
    return render_template("redirect_wait.html")

if __name__ == "__main__":
    app.run(debug=True)