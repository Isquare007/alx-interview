def bracket(s : str) -> bool:
    """_summary_

    Args:
        s (str): the parenthesis to be checked
        if they are closing each other

    Returns:
        bool: true if it's properly arranged or otherwise
    """
    parenthesis = {'(': ')', '{' : '}', '[': ']'}
    stack = []
    
    for p in s:
        if p in parenthesis.keys():
            stack.append(p)
        elif p in parenthesis.values():
            if not stack or parenthesis[stack.pop()] != p:
                return False
    return len(stack) == 0

s = "[({))]"
print(bracket(s))