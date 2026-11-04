
import os
import joblib
import pickle
import pandas as pd

rf_model = joblib.load('rf_model.pkl')
city_le = joblib.load('city_le.pkl')
z_le = joblib.load('z_le.pkl')


def predictions(sqft_living, sqft_lot, city, statezip,
                sqft_above, yr_built):

    # Convert user inputs into the numeric categories
    city_encoded = int(city_le.transform([str(city)])[0])
    zip_encoded = int(z_le.transform([str(statezip)])[0])

    house_price = [[
        sqft_living,
        sqft_lot,
        city_encoded,
        zip_encoded,
        sqft_above,
        yr_built
    ]]

    result = rf_model.predict(house_price)

    return result[0]
