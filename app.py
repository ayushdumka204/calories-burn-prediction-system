import pickle
import pandas as pd
import streamlit as st

# Load the pipeline
with open('pipeline.pkl', 'rb') as f:
    pipeline = pickle.load(f)


# Define the Streamlit app
def main():
    st.title("Calories Burnt Prediction using Machine Learning")

    st.write("Fill in the details below to predict the amount of calories burnt:")

    # Create input fields
    gender = st.selectbox("Select Gender", ['male', 'female'])
    age = st.number_input("Enter Your Age", min_value=0, max_value=120, value=25)
    height = st.number_input("Enter Your Height in Cm", min_value=50.0, max_value=250.0, value=170.0)
    weight = st.number_input("Enter Your Weight in Kg", min_value=20.0, max_value=200.0, value=70.0)
    duration = st.number_input("Duration in Minutes", min_value=1.0, max_value=300.0, value=30.0)
    heart_rate = st.number_input("Heart Rate in Bpm", min_value=30.0, max_value=200.0, value=70.0)
    body_temp = st.number_input("Body Temp in Celsius", min_value=30.0, max_value=45.0, value=36.5)

    if st.button("Predict"):
        sample = pd.DataFrame({
            'Gender': [gender],
            'Age': [age],
            'Height': [height],
            'Weight': [weight],
            'Duration': [duration],
            'Heart_Rate': [heart_rate],
            'Body_Temp': [body_temp],
        }, index=[0])

        result = pipeline.predict(sample)
        st.success(f"Amount of Calories Burnt: {result[0]:.2f}")


# Run the app
if __name__ == '__main__':
    main()
