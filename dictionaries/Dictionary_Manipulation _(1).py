#!/usr/bin/python3

"""Create dicts examples"""
# Definition of countries and capital
# Definition of dictionary
# Definition of dictionary
europe = {'spain': 'madrid', 'france': 'paris',
          'germany': 'berlin', 'norway': 'oslo'}

# Add italy to europe
europe['italy'] = 'rome'


# Print out italy in europe
print('italy' in europe)

# Dictionary of dictionaries
europe = {'spain': {'capital': 'madrid', 'population': 46.77},
          'france': {'capital': 'paris', 'population': 66.03},
          'germany': {'capital': 'berlin', 'population': 80.62},
          'norway': {'capital': 'oslo', 'population': 5.084}}


# Print out the capital of France
print(europe['france']['capital'])


# Create sub-dictionary data
data = {

    'capital': 'rome',
    'population': 59.83
}


# Add data to europe under key 'italy'
europe['italy'] = data


# Print europe
print(europe)
