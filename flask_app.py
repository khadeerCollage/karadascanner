from flask import Flask, render_template, request, redirect, url_for, flash
import numpy as np
import joblib
from tensorflow import keras

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.static_folder = 'static'

model = keras.models.load_model('my_model.h5')
scaler = joblib.load('scaler.pkl')

def predict_values(height_inch, Weight, Age, Gender):
    input_data = np.array([[height_inch, Weight, Age, Gender]])
    input_data_scaled = scaler.transform(input_data)
    predictions = model.predict(input_data_scaled)
    return predictions[0]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            height = float(request.form['height'])
            weight = float(request.form['weight'])
            age = int(request.form['age'])
            gender = 1 if request.form['gender'] == 'Male' else 0

            results = predict_values(height, weight, age, gender)
            return render_template('result.html', results=results)
        except Exception as e:
            flash(f"Error during prediction: {str(e)}")
            return redirect(url_for('index'))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
