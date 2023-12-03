from sklearn.linear_model import LinearRegression
from .get_data_from_db import get_data_frame

def remove_outliers(data):
    # https://saturncloud.io/blog/how-to-detect-and-exclude-outliers-in-a-pandas-dataframe/
    Q1 = data['price'].quantile(0.25)
    Q3 = data['price'].quantile(0.75)
    IQR = Q3 - Q1

    # identify outliers in data
    threshold = 1.5
    outliers = data[(data['price'] < Q1 - threshold * IQR) | (data['price'] > Q3 + threshold * IQR)]

    # remove outliers from data
    processed_data = data.drop(outliers.index)

    return processed_data

def estimate_price_from_condition(condition: int, item_description: str):
    if condition < 1 or condition > 5:
        raise ValueError('Condition must be between 1 and 5')

    # get data matching the item description and remove outliers
    data = remove_outliers(get_data_frame(item_description))

    # separate condition and price columns
    X = data[['condition']]
    y = data['price']

    model = LinearRegression()

    # fit the model with the dataset
    model.fit(X.values, y)

    # make a prediction based on the condition
    estimation = model.predict([[condition]])

    return int(estimation[0])