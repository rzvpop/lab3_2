from domain import createTransaction
from utils import *
from validation import validateTransaction

def findTransactions(l, params):
    '''
        Finds transactions in list based on params.
        I: l, params
        O: list of transactions found
    '''
    l_found = []

    if len(params) == 1:
        if params[0] in ["in", "out"]:
            l_found = [x for x in l if x["type"] == params[0]]
        else:
            l_found = [x for x in l if x["day"] == params[0]]
    elif len(params) == 2:
        if isinstance(params[1], int):
            l_found = [x for x in l if x["type"] == params[0] and x["day"] == params[1]]
        elif isinstance(params[1], float):
            l_found = [x for x in l if x["type"] == params[0] and x["amount"] < params[1]]
    elif len(params) == 3:
        l_found = [x for x in l if x["day"] >= params[0] and x["day"] <= params[2]]
    elif len(params) == 5:
        l_found = [x for x in range(len(l)) if l[x]["day"] == params[0] and l[x]["type"] == params[1] and l[x]["desc"] == params[2]]

    return l_found

def removeFiltred(l, l_filter):
    i = 0
    while i < len(l):
        if l[i] not in l_filter:
            remove(l, l[i])
        else:
            i = i + 1

def balance(l, d):
    '''
        Computes the balance of an account until the given day.
        (Adds in amounts and substracts out amounts.
        I: l, d(day)
        O: balance(float)
    '''
    bal = 0
    for x in l:
        if x["day"] <= d:
            if x["type"] == "in":
                bal += x["amount"]
            else:
                bal -= x["amount"]

    return bal

def addTransaction(l,day,amount,type,desc):
    '''
        Creates a transaction and introduces it in the list.
        I:l, day, amount, type, desc
    '''
    trans = createTransaction(day, amount, type, desc)
    validateTransaction(trans)
    add(l, trans)

def printList(l, params):
    '''
        Prints list of transaction depending on the parameters given.
        I: l, params
    '''
    if len(params)==0:
        printAll(l)
    if len(params)==1:
        r = [x for x in l if x["tip"] == params[0]]
        printAll(r)
    if len(params) == 2:
        if params[0] == "balance":
            print(balance(l, params[1]))
        else:
            if params[0] == "<":
                r = [x for x in l if x["amount"] < params[1]]
            elif params[0] == "=":
                r = [x for x in l if x["amount"] == params[1]]
            else:
                r = [x for x in l if x["amount"] > params[1]]
            printAll(r)

