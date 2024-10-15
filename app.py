from flask import Flask, render_template, jsonify, request

app = Flask(__name__)
app.debug = True

# Country and phone data
country_phone_mapping = {
    'Canada': '+1 (780) 228-9651',
    'UK': '+44 20 7946 0958',
    'Qatar': '+974 4452 5555',
    'India': '+91 98765 43210'
}

@app.route("/")
def home():
    # Set default to Canada
    default_country = 'Canada'
    return render_template('home.html', country=default_country, phone=country_phone_mapping[default_country])

@app.route("/about-us")
def about():
    return render_template("about.html")

@app.route("/training-courses")
def training():
    return render_template("training.html")

@app.route("/partner-profile")
def partner():
    return render_template("partnerProfile.html")

@app.route('/update_contact', methods=['POST'])
def update_contact():
    # Get the selected country from the request
    data = request.json
    country = data.get('country')

    # Get the corresponding phone number, or return 'Not Available' if not found
    phone = country_phone_mapping.get(country, 'Not Available')

    # Return a JSON response with the updated phone and country
    return jsonify({'country': country, 'phone': phone})

if __name__ == '__main__':
    app.run(debug=True)
