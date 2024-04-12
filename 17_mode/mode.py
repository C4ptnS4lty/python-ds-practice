def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    numtracker = {}
    winner = 0
    highscore = 0

    for num in nums:
        if (numtracker.get(num) != None):
            numtracker.update({num: numtracker.get(num) + 1})
        else:
            numtracker.update({num: 1})

    for key in numtracker:
        if(numtracker.get(key) > highscore):
            winner = key
            highscore = numtracker.get(key)
    else:
        return winner
