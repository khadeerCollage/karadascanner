import numpy as np
import streamlit as st
# from streamlit_extras.app_logo import add_logo
import pickle, joblib
from tensorflow import keras
from sklearn.preprocessing import StandardScaler

model = keras.models.load_model('my_model.h5')

scaler = joblib.load('scaler.pkl')

def predict_values(height_inch, Weight, Age, Gender):

    input_data = np.array([[height_inch, Weight, Age, Gender]]) 

    predictions = model.predict(input_data)
    
    input_data_scaled = scaler.transform(input_data)

    predictions = model.predict(input_data_scaled)

    # predictions =  predictions.flatten()
    
    Bmi =                         predictions[0][0]
    body_fat =                    predictions[0][1]  
    Neck =                        predictions[0][2]
    Chest =                       predictions[0][3]
    Abdomen =                     predictions[0][4]
    Hip =                         predictions[0][5]
    Thigh =                       predictions[0][6]
    Knee =                        predictions[0][7]
    Ankle =                       predictions[0][8]
    Biceps =                      predictions[0][9]
    Forearm =                     predictions[0][10]
    Wrist =                       predictions[0][11]
    Bmi_score =                   predictions[0][12]
    lean_body_mass =              predictions[0][13]
    fat_mass =                    predictions[0][14]
    fat_type =                    predictions[0][15]
    skeleton_mass_muscle_kg =     predictions[0][16]

    
    return Bmi, body_fat,Neck, Chest,Abdomen, Hip, Thigh, Knee, Ankle, Biceps, Forearm,Wrist, Bmi_score, lean_body_mass, fat_mass,fat_type,skeleton_mass_muscle_kg

# add_logo('logo.png')

# Add a logo at the left side of the title
col1, col2 = st.columns([1, 8])
with col1:
    st.image('logo.png', width=50)
with col2:
    st.title("Karada Scanner App")

st.sidebar.header("User Input for Prediction")

height = st.sidebar.text_input("Height (cm)", value="170")
weight = st.sidebar.text_input("Weight (kg)", value="70")
age = st.sidebar.text_input("Age", value="30")
gender = st.sidebar.selectbox("Gender", options=["Male", "Female"])

gender_numeric = 1 if gender == "Male" else 0

if st.sidebar.button("Predict"):
    try:
        # Convert inputs to appropriate types
        height = float(height)
        weight = float(weight)
        age = int(age)

        # Get predictions
        results = predict_values(height, weight, age, gender_numeric)

        # Ensure results unpacking matches the predict_values return
        bmi, body_fat, Neck, Chest, Abdomen, Hip,\
        Thigh, Knee, Ankle, Biceps,\
        Forearm, Wrist, Bmi_score,\
        lean_body_mass, fat_mass,\
        fat_type, skeleton_mass_muscle_kg = results

        # Display predictions
        st.success(f"Predicted BMI: {bmi:.2f}")
        st.success(f"Predicted Body Fat: {body_fat:.2f}%")
        st.success(f"Predicted Neck: {Neck:.2f} cm")
        st.success(f"Predicted Chest: {Chest:.2f} cm")
        st.success(f"Predicted Abdomen: {Abdomen:.2f} cm")
        st.success(f"Predicted Hip: {Hip:.2f} cm")
        st.success(f"Predicted Thigh: {Thigh:.2f} cm")
        st.success(f"Predicted Knee: {Knee:.2f} cm")
        st.success(f"Predicted Ankle: {Ankle:.2f} cm")
        st.success(f"Predicted Biceps: {Biceps:.2f} cm")
        st.success(f"Predicted Forearm: {Forearm:.2f} cm")
        st.success(f"Predicted Wrist: {Wrist:.2f} cm")
        st.success(f"Predicted BMI Score: {Bmi_score:.2f}")
        st.success(f"Predicted Lean Body Mass: {lean_body_mass:.2f} kg")
        st.success(f"Predicted Fat Mass: {fat_mass:.2f} kg")
        st.success(f"Predicted Fat Type: {fat_type}")
        st.success(f"Predicted Skeleton Mass Muscle (kg): {skeleton_mass_muscle_kg:.2f}")

    except Exception as e:
        st.error(f"Error during prediction: {str(e)}")
