def validateTransaction(trans):
    '''
        Validates transaction, rasing errors if the user doesn't give proper parameters.
        I: trans
    '''
    errors = ""
    if trans["day"]<1 or trans["day"]>31:
        errors +="Invalid day!!! It must be an integer between 1 and 31\n"
    if trans["amount"]<0:
        errors += "Invalid amount!!! It must be a positive float value\n"
    if trans["type"] not in ["in","out"]:
        errors += "Invalid type!!! It must be either in or out\n"
    if len(trans["desc"])== 0:
        errors += "Invalid description!!! It must not be empty\n"
    if len(errors) > 0:
        raise ValueError(errors)