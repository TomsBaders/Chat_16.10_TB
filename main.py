from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home_page.html")

@app.route("/chat")
def chat():
    return render_template("chat.html")

@app.route("/friends")
def friends():
    return render_template("friends.html")


app.run(host="0.0.0.0", port=80, debug=True)