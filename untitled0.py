# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 16:32:07 2024

@author: kb290
"""

from flask import Flask, render_template, request
import pickle
import numpy as np

# Initialize the Flask app
app = Flask(__name__)

# Load the trained model
model = pickle.load(open('Model.pkl', 'rb'))

@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Get input features from the form
            Route_Name = float(request.form['Route_Name'])
            Operated_Day = float(request.form['Operated_Day'])
            Sch_Trip_Start_Hour = float(request.form['Sch_Trip_Start_Hour'])
            Sch_Trip_Start_Minute = float(request.form['Sch_Trip_Start_Minute'])
            Sch_Trip_Start_Day = float(request.form['Sch_Trip_Start_Day'])
            Sch_Trip_Start_Month = float(request.form['Sch_Trip_Start_Month'])
            Sch_Trip_DayOfWeek = float(request.form['Sch_Trip_DayOfWeek'])
            Sch_Trip_Weekend = float(request.form['Sch_Trip_Weekend'])

            # Create the feature array
            features = np.array([[Route_Name, Operated_Day, Sch_Trip_Start_Hour, Sch_Trip_Start_Minute,
                                  Sch_Trip_Start_Day, Sch_Trip_Start_Month, Sch_Trip_DayOfWeek, Sch_Trip_Weekend]])

            # Predict using the loaded model
            prediction = model.predict(features)[0]

            # Render the prediction
            return render_template('index.html', prediction_text=f"Predicted Trip Duration: {prediction:.2f} minutes")
        
        except ValueError:
            return render_template('index.html', prediction_text="Please enter valid input values.")
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
