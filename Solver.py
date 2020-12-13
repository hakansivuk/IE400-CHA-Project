import sys
import pandas as pd


def main():

    # define your variables here
    defDataName = "data.xlsx"
    problemIndex = -1
    problemList = [problem1, problem2, problem3, problem4]

    noOfArguments = len(sys.argv) - 1
    if (noOfArguments >= 1):
        defFileArg = sys.argv[1]
        if (defFileArg != "def-file"):
            defDataName = defFileArg

    if (noOfArguments >= 2):
        problemIndex = int(sys.argv[2]) - 1

    pathToData = "./DataFolder/" + defDataName
    print("Data file to load is: {}".format(pathToData))
    print("Problem index to run arg: {}".format(problemIndex))

    # prepare the model
    solverModel = prepareModel(pathToData)

    if (problemIndex > 0):
        problemList[problemIndex](solverModel)
        return
    else:
        for i in range(4):
            problemList[i](solverModel)


def prepareModel(pathToData):
    print("Preparing model")
    return None


def problem1(solver):
    print("Problem 1")


def problem2(solver):
    print("Problem 2")


def problem3(solver):
    print("Problem 3")


def problem4(solver):
    print("Problem 4")


if __name__ == '__main__':
    main()
