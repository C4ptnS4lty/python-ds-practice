def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """

    place_holder = ''
    reversed = ''
    replaced = phrase
    replaced = replaced.replace(" ", "")

    for ltr in replaced:
            place_holder = reversed
            reversed = ltr
            reversed += place_holder

    return (replaced.upper() == reversed.upper())