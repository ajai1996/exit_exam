# Airbnb Price Prediction Web Application

## Project Overview

This project is a Machine Learning based web application that predicts the estimated price of an Airbnb listing based on several property and host features. The application uses a trained regression model to analyze listing characteristics such as neighbourhood, property type, room type, number of beds, reviews, and host experience.

The project demonstrates the complete machine learning workflow including data preprocessing, feature engineering, model training, evaluation, and deployment using Flask.

The final output provides a **predicted price range** rather than a single value, giving hosts a more realistic estimate for setting listing prices.

---

## How It Works

1. **Data Preprocessing**

   * Cleaned the dataset and handled missing values.
   * Converted `Host Since` into a numerical feature called **Host Tenure (days)**.
   * Encoded categorical variables such as:

     * Neighbourhood
     * Property Type
     * Room Type

2. **Feature Engineering**

   * Created a new interaction feature:

     ```
     Neighbourhood + Room Type
     ```

     This helps capture location-specific pricing patterns.

3. **Model Training**

   * A regression model (Random Forest Regressor) was trained to predict Airbnb prices.
   * Model performance was evaluated using:

     * RMSE
     * R² Score

4. **Deployment**

   * The trained model was saved as `model.pkl`.
   * A Flask backend (`app.py`) loads the model and handles predictions.
   * The frontend form (`index.html`) collects user inputs.

5. **Prediction Output**

   * The model predicts a base price.
   * A **price range (±10%)** is displayed to represent realistic pricing variation.

---

## Project Structure

```
project/
│
├── app.py                # Flask backend application
├── model.pkl             # Trained machine learning model
├── scaler.pkl            # Feature scaler
├── requirements.txt      # Required Python libraries
│
├── templates/
│    └── index.html       # User input web interface
│
└── README.md             # Project documentation
```

---

## How to Run the Project

### 1. Clone the Repository

```
git clone https://github.com/your-username/airbnb-price-prediction.git
cd airbnb-price-prediction
```

---

### 2. Install Required Libraries

```
pip install -r requirements.txt
```

---

### 3. Run the Flask Application

```
python app.py
```

---

### 4. Open the Web Application

Open your browser and go to:

```
http://127.0.0.1:5000
```

Enter the property details in the form and click **Predict Price** to see the estimated price range.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Flask
* HTML

---

## Model Output Example

Example prediction output:

```
Estimated Price Range: $120 - $145
```

This range helps hosts make flexible pricing decisions based on market conditions.

---

## Future Improvements

* Add advanced feature engineering
* Improve prediction accuracy using ensemble models
* Deploy the application on a cloud platform (Heroku / Render / AWS)
* Integrate interactive UI styling

