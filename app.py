from flask import Flask, request, render_template

app = Flask(__name__)
app.debug=True

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about-us")
def about():
    return render_template("about.html")

@app.route("/training-courses")
def training():
    return render_template("training.html")

@app.route("/partner-profile")
def partner():
    return render_template("partnerProfile.html")

app.run()