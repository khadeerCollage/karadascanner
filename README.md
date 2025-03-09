<div align="center">
  <h1>🔬 Karada Scanner</h1>
  <p>An AI-powered body metrics prediction tool</p>
  
  ![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
  ![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
  ![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0+-orange.svg)
  ![License](https://img.shields.io/badge/License-MIT-yellow.svg)
</div>

## 📋 Overview

Karada Scanner is a Flask-based web application that predicts various body metrics based on user input. The application utilizes a trained deep learning model to provide accurate estimates of body measurements from simple inputs like height, weight, age, and gender.

## 🚀 Features

- **Body Metrics Prediction**: Estimate multiple body measurements from basic inputs
- **BMI Classification**: Automatically categorize BMI into health categories
- **Body Fat Analysis**: Calculate body fat percentage and distribution type
- **Dual Interfaces**: Access via Flask web app or interactive Streamlit dashboard
- **Responsive Design**: User-friendly interface works across devices

## 🗂️ Project Structure

```
karada-scanner/
├── flask_app.py           # Main Flask application 
├── app.py                 # Streamlit interactive dashboard
├── templates/             # HTML templates
│   ├── index.html         # Input form template
│   └── result.html        # Results display page
├── static/                # Static assets (CSS, images)
├── my_model.h5            # Trained neural network model
├── scaler.pkl             # Feature scaling preprocessor
├── model.ipynb            # Model training notebook
├── requirements.txt       # Project dependencies
└── vercel.json            # Vercel deployment configuration
```

## 🛠️ Installation & Setup

### Prerequisites

- Python 3.7+
- pip (Python package installer)
- Git
- Vercel CLI (for deployment)

### Local Setup

1. **Clone the repository**
   ```sh
   git clone https://github.com/yourusername/karada-scanner.git
   cd karada-scanner
   ```

2. **Create a virtual environment (recommended)**
   ```sh
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the Flask application**
   ```sh
   # Windows
   set FLASK_APP=flask_app.py
   set FLASK_ENV=development
   flask run

   # macOS/Linux
   export FLASK_APP=flask_app.py
   export FLASK_ENV=development
   flask run
   ```
   Access at http://127.0.0.1:5000/

5. **Run the Streamlit dashboard (alternative)**
   ```sh
   streamlit run app.py
   ```
   Access at http://localhost:8501/

### Deployment on Vercel

1. **Install Vercel CLI**
   ```sh
   npm install -g vercel
   ```

2. **Login to Vercel**
   ```sh
   vercel login
   ```

3. **Deploy the project**
   ```sh
   vercel
   ```
   Follow the prompts to complete deployment.

## 🧠 Machine Learning Model

The prediction model used in Karada Scanner is a deep neural network developed using TensorFlow and Keras.

### Model Architecture
- **Input Layer**: 4 neurons (height, weight, age, gender)
- **Hidden Layers**: Multiple dense layers with dropout for regularization
- **Output Layer**: 17 neurons (various body measurements)
- **Activation**: ReLU for hidden layers
- **Regularization**: L1_L2 regularization and dropout to prevent overfitting

### Training Process
The model was trained on an annotated dataset of body measurements with:
- Feature scaling using StandardScaler
- Train-test split (80% training, 20% validation)
- Early stopping to prevent overfitting
- Learning rate reduction on plateau
- Mean squared error loss function

### Model Performance
- **Mean Absolute Error**: Typically under 2-3% for most metrics
- **Validation Strategy**: Cross-validation to ensure generalizability

## 📘 User Guide

### Using the Flask Web Interface

1. Access the application at http://127.0.0.1:5000/ (local) or your deployed URL
2. Enter your measurements:
   - Height (in inches)
   - Weight (in kilograms)
   - Age
   - Gender (Male/Female)
3. Click "Predict" to generate results
4. Review your results on the detailed results page
5. Interpret the predictions:
   - BMI Category: Classification based on your calculated BMI
   - Body Fat Percentage: Estimate of total body fat
   - Fat Type: Classification of predominant fat type
   - Body Measurements: Estimated circumference of various body parts

### Using the Streamlit Dashboard

1. Launch the Streamlit app and access via http://localhost:8501/
2. Adjust the input values using the sidebar sliders and inputs
3. See real-time prediction updates in the main panel
4. Explore different scenarios by changing inputs to see how predictions change

### API Integration

#### Request Format:
```json
{
  "height": 72.0,       // inches
  "weight": 78.5,       // kilograms
  "age": 30,            // years
  "gender": "Male"      // "Male" or "Female"
}
```

## 🛠️ Technologies Used

- **Backend**: Flask, Python 3
- **Machine Learning**: TensorFlow, Keras, scikit-learn
- **Data Processing**: NumPy, Pandas
- **Visualization**: Streamlit, Bootstrap
- **Deployment**: Vercel

## 🔮 Future Improvements

- **Mobile Application**: Native iOS/Android apps
- **User Accounts**: Save and track progress over time
- **Additional Models**: Support for specialized demographics
- **Image Input**: Allow users to upload photos for enhanced predictions
- **Exercise Recommendations**: Personalized fitness suggestions based on predictions

## 👥 Contributors

- Your Name - Shaik.Khadeer 

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

<div align="center">
  <p>© 2023 Karada Scanner. All rights reserved.</p>
  <p>
    <a href="https://github.com/yourusername/karada-scanner">GitHub</a> •
    <a href="https://yourusername.github.io/karada-scanner">Documentation</a> •
    <a href="mailto:your.email@example.com">Contact</a>
  </p>
</div>
