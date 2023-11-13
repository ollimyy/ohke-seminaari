import numpy as np
from sklearn.linear_model import LinearRegression

from sample_data_generator import generate_sample_data
from get_data_from_db import get_data_frame

def estimate_price_from_condition(condition: int, item_description: str):
    if condition < 1 or condition > 5:
        raise ValueError('Condition must be between 1 and 5')

    # TODO: replace with getting the real data, but for now, generate sample data
    data = get_data_frame(item_description)

    # separate condition and price columns
    X = data[['condition']]
    y = data['price']

    model = LinearRegression()

    # fit the model with the dataset
    model.fit(X.values, y)

    # make a prediction based on the condition
    result = model.predict([[condition]])

    return int(result[0])
