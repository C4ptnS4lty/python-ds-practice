def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """

    phrase_breakdown = {}

    for ltr in phrase:
        if (phrase_breakdown.get(ltr) != None):
            phrase_breakdown.update({ltr: phrase_breakdown.get(ltr) + 1})
        else:
            phrase_breakdown.update({ltr: 1})

    return phrase_breakdown

