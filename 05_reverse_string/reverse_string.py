def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    place_holder = ''
    reversed = ''

    for ltr in phrase:
        place_holder = reversed
        reversed = ltr
        reversed += place_holder

    return reversed