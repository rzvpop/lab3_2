def add(l, x):
    '''
        Appends an element to a list.
        I: l, x(element)
    '''
    l.append(x)

def remove(l, x):
    '''
        Removes an element from a list.
        I: l, x(element)
    '''
    l.remove(x)

def printAll(l):
    '''
        Prints elements of a list.
        I: l
    '''
    s=""
    if len(l) > 0:
        for x in l:
            s+=str(x)+"\n"
        print(s)
    else:
        print("Empty list.")

def isFloat(x):
    '''
        Checks if a give string can be converted into a float number.
        If yes, then it returns the value.
        I: x(string)
        O: x(float) or False
    '''
    try:
        return float(x)
    except ValueError:
        return False

def isInt(x):
    '''
            Checks if a give string can be converted into a integer.
            If yes, then it returns the value.
            I: x(string)
            O: x(integer) or False
        '''
    try:
        return int(x)
    except ValueError:
        return False

def sumList(l):
    '''
        Adds the elements of a list and returns the sum.
        I: l
        O: sum
    '''
    s = 0
    for x in l:
        s += x
    return s

def maxList(l):
    '''
        Finds the maximum value in a list and returns it.
        If the list is empty it returns -1.
        I: l
        O: max
    '''
    max = -1
    for x in l:
        if x > max:
            max = x

    return max