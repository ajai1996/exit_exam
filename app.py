from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    # Get form values
    features = [float(x) for x in request.form.values()]
    features = np.array(features).reshape(1, -1)

    # Scale input
    features_scaled = scaler.transform(features)

    # Predict price
    prediction = model.predict(features_scaled)[0]

    # ADD PRICE RANGE HERE
    lower_price = prediction * 0.9
    upper_price = prediction * 1.1

    return render_template(
        "index.html",
        prediction_text=f"Estimated Price Range: ${lower_price:.2f} - ${upper_price:.2f}"
    )


if __name__ == "__main__":
    app.run(debug=True)