def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    vowels = ['a','e','i','o','u']
    indexes = []
    reversed = []

    for ltr in s:
        if(vowels.count(ltr.lower()) >0):
            indexes.append(ltr)
        reversed.append(ltr)

    indexes.reverse()

    x = 0
    while x < len(reversed):
        if(vowels.count(reversed[x].lower()) > 0):
            reversed[x] = indexes.pop(0)
        x += 1

    return ''.join(str(e) for e in reversed)
