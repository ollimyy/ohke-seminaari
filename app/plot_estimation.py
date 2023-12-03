import sys
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from app.database import get_dataframe_for_item

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

# make an estimation and plot it, can be ran from the commandline
def estimate_and_plot(condition: int, item_description: str):

    # get data matching the item description and remove outliers
    data = remove_outliers(get_dataframe_for_item(item_description))

    # separate condition and price columns
    X = data[['condition']]
    y = data['price']

    model = LinearRegression()

    # fit the model with the dataset
    model.fit(X.values, y)

    # make a prediction based on the condition
    estimation = model.predict([[condition]])
    estimated_price = estimation[0]

    print(f"Estimated price for '{item_description}', condition {condition}: {estimated_price}")
    
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
    plt.savefig('app/estimation_plot.png')
    print("Plot saved to estimation_plot.png.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python plot_estimation.py <item_description> <condition>")
        sys.exit(1)

    estimate_and_plot(int(sys.argv[2]), sys.argv[1])