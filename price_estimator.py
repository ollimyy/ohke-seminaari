import numpy as np
from sklearn.linear_model import LinearRegression
from sample_data_generator import generate_sample_data

def estimate_price_from_condition(condition: int):
    if condition < 1 or condition > 5:
        raise ValueError('Condition must be between 1 and 5')

    # TODO: replace with getting the real data, but for now, generate sample data
    data = generate_sample_data(random_seed = np.random.randint(0, 100))

    # separate condition and price columns
    X = data[['condition']]
    y = data['price']

    model = LinearRegression()

    # fit the model with the dataset
    model.fit(X.values, y)

    # make a prediction based on the condition
    result = model.predict([[condition]])

    return int(result[0])
