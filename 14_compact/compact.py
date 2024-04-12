def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """

    only_truth = []

    for item in lst:
        if(bool(item)):
            only_truth.append(item)

    return only_truth