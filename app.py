# import streamlit as st
# import pickle


# ## To Load Model and Label Encoder
# # rb = Run Binary

# reg=pickle.load(open("car_model.pkl","rb"))
# le=pickle.load(open("label_encoder.pkl","rb"))

# st.title("Car Price Prediction App")

# car_model = st.selectbox("Select Car Model", le.classes_)

# mileage = st.number_input("Enter Mileage (in miles)",min_value=0)

# age=st.slider("Car Age(year)",0,12)

# encoded_model = le.transform([car_model])



# if st.button("Prediction Price"):
#     input_data=[[encoded_model,mileage,age]]
#     predicted_price=reg.predict(input_data)
#     st.success(f"Estimated Selling Price: {predicted_price[0]}")

import streamlit as st
import pickle

## To load Model and label encoder

# rb = Run binary


reg=pickle.load(open("car_model.pkl","rb"))
le=pickle.load(open("label_encoder.pkl","rb"))

st.title("Car Price Prediction App!")

car_model = st.selectbox("Select Car Model", le.classes_)

mileage = st.number_input("Ener Mileage (In Miles)", min_value=0)

age = st.slider("Car Age(year)",0,12)

encoded_model = le.transform([car_model])[0]

if st.button("Prediction Price"):
    input_data=[[encoded_model,mileage,age]]
    predicted_price=reg.predict(input_data)
    st.success(f"Estimated Selling Price: {predicted_price[0]}")