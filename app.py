from flask import Flask, render_template, request, g

app = Flask(__name__)
app.debug = True

# Country and phone data
country_phone_mapping = {
    'Canada': '+1 (780) 228-9651',
    'UK': '+44 20 7946 0958',
    'Qatar': '+974 4452 5555',
    'India': '+91 98765 43210'
}

# Function to get phone number
def get_phone_number(selected_country):
    return country_phone_mapping.get(selected_country, '+1 (780) 228-9651')  # Default is Canada

@app.before_request
def set_phone_number():
    # Default country and phone
    g.selected_country = 'Canada'
    g.phone = get_phone_number('Canada')

    # Check if a new country is selected
    if request.method == "POST" and request.form.get("country"):
        g.selected_country = request.form.get("country")
        g.phone = get_phone_number(g.selected_country)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template('index.html', country=g.selected_country, phone=g.phone)

@app.route("/about-us")
def about():
    return render_template("about.html", country=g.selected_country, phone=g.phone)

@app.route("/training-courses")
def training():
    return render_template("training.html", country=g.selected_country, phone=g.phone)

@app.route("/partner-profile")
def partner():
    return render_template("partnerProfile.html", country=g.selected_country, phone=g.phone)

if __name__ == '__main__':
    app.run(debug=True)
