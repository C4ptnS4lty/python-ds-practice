def min_max_keys(d):
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings:

        >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """
    min = list(d.keys())[0]
    max = list(d.keys())[0]


    for key in d:
        if(isinstance(key, str)):
            if(len(max) < len(key)):
                max = key
            elif(len(min) > len(key)):
                min = key
        else:
            if(key > max):
                max = key
            elif(key < min):
                min = key
    return (min, max)

print(min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"}))
print(min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'}))