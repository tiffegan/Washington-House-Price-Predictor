import streamlit as st
from my_functions import predictions

st.title(" WASHINGTON STATE Housing Price Predictor App")
sqft_living = st.number_input("Enter Living Square Footage")
sqft_lot = st.number_input("Enter Lot Square Footage")
city = st.text_input("Enter city")
statezip = st.text_input("Enter state zip code (like WA 00000)")
sqft_above = st.number_input("Enter square footage above first floor")
yr_built = st.slider("Year Built", min_value = 1900, max_value = 2026, value = 2000, step =1)

if st.button("Predict"):
    price = predictions(sqft_living,sqft_lot,city,statezip,sqft_above,yr_built)
    
    st.success("Calculation Complete!")
    st.write("Price $ ", f"${price:,.2f})
