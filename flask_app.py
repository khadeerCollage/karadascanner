from flask import Flask, render_template, request, redirect, url_for, flash
import numpy as np
import joblib
from tensorflow import keras
import pandas as pd

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.static_folder = 'static'

# Load the trained model and scaler
model = keras.models.load_model('my_model.h5')
scaler = joblib.load('scaler.pkl')

# Define the BMI score decoding function
def bmi_score(data):
    if data <= 18.5:
        return 'UnderWeight'
    elif 18.5 <= data <= 24.5:
        return 'Healthy'
    elif 24.5 <= data <= 29.5:
        return 'OverWeight'
    else:
        return 'Obesity'

# Define the fat type categorization function
def categorize_fat(body_fat):
    if body_fat < 10:
        return 'Essential Fat'
    elif body_fat < 20:
        return 'Subcutaneous Fat'
    elif body_fat < 30:
        return 'White Fat'
    elif body_fat < 35:
        return 'Visceral Fat'
    elif body_fat >= 35:
        return 'Obesity (High Visceral Fat)'
    else:
        return 'Unknown'

# Prediction function
def predict_values(height_inch, weight, age, gender):
    input_data = np.array([[height_inch, weight, age, gender]])
    input_data_scaled = scaler.transform(input_data)
    predictions = model.predict(input_data_scaled)
    
    # Define column names for the prediction output
    column_names = ['Bmi', 'BodyFat', 'Neck', 'Chest', 'Abdomen', 'Hip', 'Thigh', 
                    'Knee', 'Ankle', 'Biceps', 'Forearm', 'Wrist', 'Bmi_score', 
                    'lean_body_mass', 'fat_mass', 'fat_type', 'skeleton_mass_muscle_kg']
    
    # Convert predictions to DataFrame
    pred_df = pd.DataFrame(predictions, columns=column_names)
    
    # Decode the BMI score
    pred_df['Bmi_score_decoded'] = pred_df['Bmi'].apply(bmi_score)
    
    # Decode the fat_type based on predicted BodyFat
    pred_df['fat_type_decoded'] = pred_df['BodyFat'].apply(categorize_fat)
    
    # Return the predictions as a list including decoded values
    return pred_df.iloc[0].tolist()  # Convert first row to list

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            height = float(request.form['height'])  # Height in inches
            weight = float(request.form['weight'])  # Weight in kg
            age = int(request.form['age'])
            gender = 1 if request.form['gender'] == 'Male' else 0

            # Get predictions including decoded BMI score and fat type
            results = predict_values(height, weight, age, gender)
            return render_template('result.html', results=results)
        except Exception as e:
            flash(f"Error during prediction: {str(e)}")
            return redirect(url_for('index'))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    