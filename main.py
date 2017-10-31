from test import runTests
from UI import *
from copy import deepcopy
from utils import add

def readCommand():
    return input(">>").split()

def run():
    lst = []
    undo_lst = []
    commands = {"add":uiAddTransaction,"insert":uiInsertTransaction, "list":uiListTransactions,
                "remove":uiRemoveTransactions, "replace":uiReplaceTransaction, "sum":uiSum, "max":uiMax, "filter":uiFilter,
                "undo":uiUndo}
    initTransList(lst)
    add(undo_lst, deepcopy(lst))

    while True:
        cmd =readCommand()
        if len(cmd) ==0:
            continue
        if cmd[0]=="exit":
            return
        if cmd[0] in commands:
            try:
                if cmd[0] != "undo":
                    commands[cmd[0]](lst, cmd[1:])
                else:
                    commands[cmd[0]](lst, undo_lst)

                if cmd[0] in ["add", "insert", "remove", "replace", "filter"]:
                    add(undo_lst, deepcopy(lst))
            except ValueError as ve:
                print(ve)
        else:
            print("Invalid command!!!")


runTests()
run()