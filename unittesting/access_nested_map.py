def access_nested_map(nested_map, path):
    """
    Accesses a value in a nested dictionary using a sequence of keys.

    :param nested_map: The dictionary potentially containing nested dictionaries.
    :param path: A list or tuple of keys representing the path to the desired value.
    :return: The value found at the specified path.
    """
    for key in path:
        nested_map = nested_map[key]
    return nested_map

path = [ 'a', 'c', 'd', 'e']
print(access_nested_map(
    {
        'a' :{
            'b': 1,
            'c' : {
                'd' : {
                    'e' : 2
                }
            }
        }
    }
, path))