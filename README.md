# Karada Scanner App

This project is a Flask-based web application that predicts various body metrics based on user input. The application uses a trained machine learning model to make predictions.

## Project Structure

- `flask_app.py`: The main Flask application file.
- `app.py`: Streamlit application for user interaction.
- `templates/`: Directory containing HTML templates.
  - `index.html`: The main input form.
  - `result.html`: The results display page.
- `static/`: Directory for static files like images and CSS.
- `requirements.txt`: List of dependencies required for the project.
- `vercel.json`: Configuration file for deploying the project on Vercel.
- `model.ipynb`: Jupyter Notebook for training the machine learning model.
- `my_model.h5`: The trained machine learning model.
- `scaler.pkl`: The scaler used for data preprocessing.

## Setup Instructions

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- Vercel CLI (for deployment)

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/karada-scanner.git
   cd karada-scanner
   ```

2. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

### Running the Flask Application

1. Set the `FLASK_APP` environment variable:
   For Windows:
   ```sh
   set FLASK_APP=flask_app.py
   ```

   For macOS/Linux:
   ```sh
   export FLASK_APP=flask_app.py
   ```

2. Run the Flask application:
   ```sh
   flask run
   ```

   The application will be available at `http://127.0.0.1:5000/`.

### Running the Streamlit Application

1. Run the Streamlit application:
   ```sh
   streamlit run app.py
   ```

   The application will be available at `http://localhost:8501/`.

### Deploying to Vercel

1. Install Vercel CLI:
   ```sh
   npm install -g vercel
   ```

2. Login to Vercel:
   ```sh
   vercel login
   ```

3. Deploy the project:
   ```sh
   vercel
   ```

   Follow the prompts to complete the deployment process.

## Project Overview

### `flask_app.py`

This file contains the main Flask application. It loads the trained machine learning model and scaler, defines the prediction function, and sets up the routes for the web application.

### `app.py`

This file contains the Streamlit application. It provides a user interface for inputting data and displays the prediction results.

### `templates/index.html`

This file contains the HTML template for the main input form. It includes fields for height, weight, age, and gender.

### `templates/result.html`

This file contains the HTML template for displaying the prediction results. It shows the predicted values for various body metrics.

### `model.ipynb`

This Jupyter Notebook contains the code for training the machine learning model. It includes data preprocessing, model training, and evaluation.

### `vercel.json`

This file contains the configuration for deploying the project on Vercel. It specifies the routes and build settings.

## Commands

- Install dependencies:
  ```sh
  pip install -r requirements.txt
  ```

- Run Flask application:
  ```sh
  flask run
  ```

- Run Streamlit application:
  ```sh
  streamlit run app.py
  ```

- Deploy to Vercel:
  ```sh
  vercel
  ```

## Conclusion

This project demonstrates how to build a web application using Flask and Streamlit, and how to deploy it on Vercel. The application predicts various body metrics based on user input using a trained machine learning model.
