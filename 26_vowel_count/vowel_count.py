def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    counts = {}
    vowels = ['a','e','i','o','u']
    for ltr in phrase:
        if ltr.lower() in vowels:
            if ltr.lower() in counts:
                counts[ltr.lower()] = counts[ltr.lower()] + 1
            else:
                counts[ltr.lower()] = 1

    return counts