# valid_braces.py

# author: awakenedhaki

def validBraces(string: str) -> bool:
    '''
    Determines if valid braces.
    '''
    pair = {'(':')', '{':'}', '[': ']'}
    opening, closing = zip(*pair.items())
    # queue: Dict[str, str]. Closing bracket to be evaluated
    queue = []
    for bracket in string:
        if bracket in opening:
            # add bracket pair into queue
            queue.append(pair[bracket])
        # check if current bracket does not match last bracket in queue
        elif queue == [] or bracket != queue.pop():
            return False
    # if queue = [], then True, otherwise False
    return not queue
