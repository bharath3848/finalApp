import streamlit as st
import pickle
import numpy as np

# Load the model
with open("./Thyroid_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Define the prediction function
def predict_thyroid(Age, Sex, TSH, TT4, FTI, on_thyroxine, on_antithyroid_medication, goitre, hypopituitary, psych, T3_measured):
    # Convert categorical variables to numerical
    Sex = 1 if Sex == "Male" else 0
    on_thyroxine = 1 if on_thyroxine == "True" else 0
    on_antithyroid_medication = 1 if on_antithyroid_medication == "True" else 0
    goitre = 1 if goitre == "True" else 0
    hypopituitary = 1 if hypopituitary == "True" else 0
    psych = 1 if psych == "True" else 0
    T3_measured = 1 if T3_measured == "True" else 0
    
    # Make prediction
    arr = np.array([[Age, Sex, TSH, TT4, FTI, on_thyroxine, on_antithyroid_medication, goitre, hypopituitary, psych, T3_measured]])
    pred = model.predict(arr)

    if pred == 0:
        return "Compensated Hypothyroid"
    elif pred == 1:
        return "No Thyroid"
    elif pred == 2:
        return "Primary Hypothyroid"
    elif pred == 3:
        return "Secondary Hypothyroid"

# Streamlit app
def main():    
    # Title and Image
    st.title("Thyroid Disorder Prediction")
    st.markdown('<style>h1 {color: red; text-align: center;font-size:100px; font-weight:bold;}</style>', unsafe_allow_html=True)
    st.markdown('<style>body {background-color: yellow;}</style>', unsafe_allow_html=True)
    st.image("./banner_img.png", use_column_width=True)

    # Input fields
    st.subheader("Patient Information")
    st.markdown('<style>h1 {color: green; text-align: center;font-size:40px; font-weight:bold;}</style>', unsafe_allow_html=True)
    Age = st.number_input("Age", min_value=0, max_value=100, value=0)
    Sex = st.selectbox("Sex", ["Male", "Female"])
    TSH = st.number_input("Level of Thyroid Stimulating Hormone (TSH)")
    TT4 = st.number_input("Total Thyroxine (TT4)")
    FTI = st.number_input("Free Thyroxine Index (FTI)")
    on_thyroxine = st.selectbox("On Thyroxine", ["True", "False"])
    on_antithyroid_medication = st.selectbox("On Antithyroid Medication", ["True", "False"])
    goitre = st.selectbox("Goitre", ["True", "False"])
    hypopituitary = st.selectbox("Hypopituitary", ["True", "False"])
    psych = st.selectbox("Psychological Symptoms", ["True", "False"])
    T3_measured = st.selectbox("Is T3 measured?", ["True", "False"])

    if st.button("Predict"):
        prediction = predict_thyroid(Age, Sex, TSH, TT4, FTI, on_thyroxine, on_antithyroid_medication, goitre, hypopituitary, psych, T3_measured)
        st.subheader("Prediction")
        st.markdown(f"<p style='color:red; font-size:60px; font-weight:bold;'>Patient has {prediction}</p>", unsafe_allow_html=True)

    # Footer
    st.markdown(
        """
        <style>
            .footer {
                position: fixed;
                left: 0;
                bottom: 0;
                width: 100%;
                background-color: #333;
                color: #fff;
                text-align: center;
                padding: 10px 0;
            }
        </style>
        <div class="footer">
            <p>Developed by Bharath</p>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
