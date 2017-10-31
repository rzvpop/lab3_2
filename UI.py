from datetime import datetime
from copy import deepcopy
from functionalities import addTransaction, printList, findTransactions, remove
from utils import isFloat, isInt, sumList, maxList, printAll


def initTransList(l):
    addTransaction(l, 12, 423.43, "in", "salary")
    addTransaction(l, 23, 33, "out", "gambling")
    addTransaction(l, 22, 12, "in", "found")
    addTransaction(l, 16, 1111, "out", "don't know")
    addTransaction(l, 4, 2000, "out", "help abandoned birds")
    addTransaction(l, 25, 53.45, "out", "yoooo")
    addTransaction(l, 8, 23, "in", "stuff")
    addTransaction(l, 31, 42, "out", "gambling")
    addTransaction(l, 12, 200, "in", "ex")
    addTransaction(l, 23, 300, "in", "photo shooting")

def uiAddTransaction(l, params):
    if len(params)<3:
        print("Wrong number of parameters!!! Required usage: add <value> <type> <description> \n")
        return

    day = datetime.now().day

    if not isFloat(params[0]):
        print("Wrong amount!!! It must be a decimal value. \n")
        return
    amount = isFloat(params[0])
    tip = params[1]
    desc = " ".join(params[2:])
    addTransaction(l, day, amount, tip, desc)
    print("Transaction added successfully!!!\n")

def uiInsertTransaction(l, params):
    if len(params) < 4:
        print("Wrong number of parameters!!! Required usage: insert <day> <value> <type> <description> \n")
        return

    if not isInt(params[0]):
        print("Wrong date!!! It must be an integer value between 1 and 31. \n")
        return
    day = isInt(params[0])

    if not isFloat(params[1]):
        print("Wrong amount!!! It must be a decimal value. \n")
        return
    amount = isFloat(params[1])
    tip = params[2]
    desc = " ".join(params[3:])
    addTransaction(l, day, amount, tip, desc)
    print("Transaction inserted successfully!!!\n")

def uiRemoveTransactions(l, params):
    l_to_remove = []

    if len(params) == 1:
        if (params[0] not in ["in", "out"]) and isInt(params[0]) == False:
            print("Wrong parameters!!! Required usage: remove <day> or remove <start_day> to <end_day> "
                  "or remove in/out \n")
            return

        if isInt(params[0]) != False:
            params[0] = isInt(params[0])

    elif len(params) == 3:
        if isInt(params[0]) != False and isInt(params[2]) != False and params[1] == "to":
            params[0] = isInt(params[0])
            params[2] = isInt(params[2])
        else:
            print("Wrong parameters!!! Required usage: remove <day> or remove <start_day> to <end_day> "
                  "or remove in/out \n")
            return
    else:
        print("Wrong number of parameters!!! Required usage: remove <day> or remove <start_day> to <end_day> "
              "or remove in/out \n")
        return

    l_to_remove = findTransactions(l, params)

    for x in l_to_remove:
        remove(l, x)
    print("The operatiom worked well!")

def uiReplaceTransaction(l, params):
    if len(params) > 5:
        for i in range(len(params) - 5):
            params[2] += " " + params[3]
            remove(params, params[3])

    if len(params) != 5:
        print("Wrong parameters!!! Required usage: repalce <day> <type> <description> with <new_amount> \n")
        return

    params[0] = isInt(params[0])

    replace = True
    replace = replace and  params[0] != False and 1 <= params[0] and 31 >= params[0]
    replace = replace and params[1] in ["in", "out"]
    replace = replace and params[2] != ""
    replace = replace and params[3] == "with"
    replace = replace and isFloat(params[4]) != False

    if replace:
        params[0] = isInt(params[0])
        params[4] = isFloat(params[4])
        pos_to_repalce = findTransactions(l, params)
        l[pos_to_repalce[0]]["amount"] = params[4]
        print("Successful operation!")
    else:
        print("Wrong parameters!!! Required usage: repalce <day> <amount> <type> <description> \n")
        return

def uiSum(l, params):
    if len(params) != 1:
        print("Wrong number of parameters!!! Required usage: sum <type>\n")
        return

    if params[0] in ["in", "out"]:
        sum = 0
        l_sum = findTransactions(l, params)
        for i in range(len(l_sum)):
            l_sum[i] = l_sum[i]["amount"]
        sum = sumList(l_sum)
        print(sum)
    else:
        print("Wrong parameters!!! Required usage: sum <type>\n")
        return

def uiMax(l, params):
    if len(params) != 2:
        print("Wrong number of parameters!!! Required usage: max <type> <day>\n")
        return

    params[1] = isInt(params[1])

    if (params[0] in ["in", 'out']) and params[1] != False and 1 <= params[1] and 31 >= params[1]:
        l_max = findTransactions(l, params)
        for i in range(len(l_max)):
            l_max[i] = l_max[i]["amount"]
        max = maxList(l_max)

        if max == -1:
            print("No transaction found found!")
            return
        print(max)
    else:
        print("Wrong parameters!!! Required usage: sum <type> <day>\n")
        return

def uiFilter(l, params):
    if len(params) < 1 or len(params) > 2:
        print("Wrong number of parameters!!! Required usage: filter <type> or filter <type> <day>\n")
        return

    if len(params) == 2:
        params[1] = isFloat(params[1])
        if (params[0] in ["in", 'out']) and params[1] != False:
            l_filter = findTransactions(l, params)

            i = 0
            while i < len(l):
                if l[i] not in l_filter:
                    remove(l, l[i])
                else:
                    i = i + 1
        else:
            print("Wrong number of parameters!!! Required usage: filter <type> or filter <type> <day>\n")
            return
    elif len(params) == 1:
        if params[0] in ["in", 'out']:
            l_filter = findTransactions(l, params)

            i = 0
            while i < len(l):
                if l[i] not in l_filter:
                    remove(l, l[i])
                else:
                    i = i + 1

        else:
            print("Wrong number of parameters!!! Required usage: filter <type> or filter <type> <day>\n")
            return

def uiUndo(l, undo_l):
    if len(undo_l) >= 2:
        l = deepcopy(undo_l[len(undo_l) - 2])
        remove(undo_l, undo_l[len(undo_l) - 1])
    else:
        l = []
        undo_l = []

def uiListTransactions(l, params):
    if len(params)>2:
        print("Invalid no of parameters!!!")
    if len(params)==0:
        print("The current list of transactions is:")

    if len(params)==1:
        if params[0] not in ["in","out"]:
            print("Invalid parameter!!! Proper usage list <type>")
            return
        print("The current list of "+params[0]+" transactions is:")
    if len(params)==2:
        if params[0] not in ["<", "=",">", "balance"]:
            print("Invalid parameter!!! Proper usage: list [>,=,<] <type> balance <end_day>")
            return
        if params[0] == "balance":
            params[1] = isInt(params[1])
        else:
            params[1] = isFloat(params[1])

    printList(l, params)