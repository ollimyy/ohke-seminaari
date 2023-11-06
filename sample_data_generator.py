import numpy as np
import pandas as pd

# slope = rate of price increasing with condition
# intercept = starting point of price
def generate_sample_data(num_samples=200, slope=20, intercept=20, random_seed=0):
    # same random numbers for a certain seed
    np.random.seed(random_seed)

    condition = np.random.randint(1, 6, size=num_samples)

    # add randomness to price
    noise = np.random.normal(0, 20, size=num_samples)

    # calculate price, add noise and round to two decimals
    price = np.round(slope * condition + intercept + noise).astype(int)

    data = pd.DataFrame({'price': price, 'condition': condition})

    return data