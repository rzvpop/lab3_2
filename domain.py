def createTransaction(day,amount,type,desc):
    '''
        Creates a transaction.
        I: day, amount, type, desc(description)
        O: transaction(a dictionary)
    '''
    return {"day":day,
            "amount":amount,
            "type":type,
            "desc":desc}