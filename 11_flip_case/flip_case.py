def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    flipped = ''

    for ltr in phrase:
        if (to_swap.upper() == ltr.upper()):
            flipped += ltr.swapcase()
        else:
            flipped += ltr
    
    return flipped
