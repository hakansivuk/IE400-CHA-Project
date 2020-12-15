import sys
import pandas as pd
from ortools.linear_solver import pywraplp
from QuestionModels import FirstQuestionModel, SecondQuestionModel, ThirdQuestionModel, FourthQuestionModel


def main():

    # define your variables here
    defDataName = "data.xlsx"
    problemIndex = -1
    problemList = []

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
    problemList.append(FirstQuestionModel(pathToData))
    problemList.append(SecondQuestionModel(pathToData))
    problemList.append(ThirdQuestionModel(pathToData))
    problemList.append(FourthQuestionModel(pathToData))

    if (problemIndex > 0):
        problemList[problemIndex].solveProblem()
        return
    else:
        for i in range(4):
            problemList[i].solveProblem()


if __name__ == '__main__':
    main()
