def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    trackleft = 0
    trackright = 0

    for paren in parens:
        if(paren == '('):
            trackleft += 1
        else:
            trackright += 1
        if(trackright > trackleft):
            return False
    
    return (trackleft == trackright)
