#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = {key: a_dictionary[key] * 2 for key in a_dictionary}
    return new_dic


a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
new = {key: a_dictionary[key] * 2 for key in a_dictionary}
print(new)
