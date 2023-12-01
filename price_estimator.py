import sys
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from get_data_from_db import get_data_frame

def estimate_price_from_condition(condition: int, item_description: str):
    if condition < 1 or condition > 5:
        raise ValueError('Condition must be between 1 and 5')

    # get data matching the item description
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

def estimate_and_plot(condition: int, item_description: str):

    # Estimate price
    estimated_price = estimate_price_from_condition(condition, item_description)

    print(f"Estimated price for '{item_description}', condition {condition}: {estimated_price}")

    # Plot the linear regression line
    data = get_data_frame(item_description)
    X = data[['condition']]
    y = data['price']

    model = LinearRegression()
    model.fit(X.values, y)

    # Plot the data points
    plt.scatter(X, y, color='blue', label='Data Points')

    # Plot the linear regression line
    x_range = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
    y_range = model.predict(x_range)
    plt.plot(x_range, y_range, color='red', linewidth=3, label='Linear Regression')
    
    # Plot the estimation
    plt.scatter(condition, estimated_price, color='green', marker='o', s=100, zorder=10, label='Estimated Price')

    plt.xticks([1, 2, 3, 4, 5])
    plt.xlabel('Condition')
    plt.ylabel('Price')
    plt.title(f'"{item_description}", condition: {condition}, estimated price: {estimated_price}')
    plt.legend()
    plt.grid(True)

    # Save the plot to a file
    plt.savefig('estimation_plot.png')

# figures can be plotted from the commandline
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python plot_estimation.py <item_description> <condition>")
        sys.exit(1)

    estimate_and_plot(int(sys.argv[2]), sys.argv[1])