#!/usr/bin/python3


"""Dictionary to DataFrame (1)
Pandas is an open source library, providing high-performance, easy-to-use data
structures and data analysis tools for Python. Sounds promising!

The DataFrame is one of Pandas' most important data structures.
It's basically a way to store tabular data where you can label the rows and
the columns.
One way to build a DataFrame is from a dictionary.

"""


# Pre-defined lists
import pandas as pd
names = ['United States', 'Australia', 'Japan',
         'India', 'Russia', 'Morocco', 'Egypt']

dr = [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd


# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {
    'country': names,
    'drives_right':  dr,
    'cars_per_cap':  cpc,


}


# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)

# Print cars
print(cars)


# Build cars DataFrame
names = ['United States', 'Australia', 'Japan',
         'India', 'Russia', 'Morocco', 'Egypt']
dr = [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
cars_dict = {'country': names, 'drives_right': dr, 'cars_per_cap': cpc}
cars = pd.DataFrame(cars_dict)
print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels


# Print cars again
print(cars)
