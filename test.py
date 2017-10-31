from domain import createTransaction
from functionalities import addTransaction, balance, findTransactions
from validation import validateTransaction
from utils import isFloat, isInt, sumList, maxList

def testTransactionValidation():
    trans = createTransaction(12,34.56,"in","")
    try:
        validateTransaction(trans)
        assert(False)
    except ValueError as ve:
        assert(str(ve) == "Invalid description!!! It must not be empty\n")

def testAddTransaction():
    ls = []
    addTransaction(ls,12,34.45,"in","a")
    trans = createTransaction(12, 34.45, "in", "a")
    assert(ls == [trans])

def testBalance():
    l = []
    addTransaction(l, 12, 1111, "in", "salary")
    addTransaction(l, 23, 33, "out", "gambling")
    addTransaction(l, 22, 12, "in", "found")
    addTransaction(l, 16, 400, "out", "don't know")

    assert balance(l, 20) == 711

def testIsFloat():
    assert isFloat("123s3") == False
    assert isFloat("324") == 324
    assert isFloat("213.53") == 213.53

def testIsInt():
    assert isInt("123s3") == False
    assert isInt("324") == 324
    assert isInt("213.53") == False

def testSumList():
    l = [32, 3, 54, 1]

    assert sumList(l) == 90

def testMaxList():
    l = [32, 3, 54, 1]

    assert maxList(l) == 54

    l = []

    assert maxList(l) == -1

def testFindTransactions():
    pass

def runTests():
    testTransactionValidation()
    testAddTransaction()
    testBalance()
    testFindTransactions()
    testIsFloat()
    testIsInt()
    testSumList()
    testMaxList()