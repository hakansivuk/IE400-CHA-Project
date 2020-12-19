import sys
from QuestionModels import FirstQuestionModel, SecondQuestionModel, ThirdQuestionModel, FourthQuestionModel
import threading


def main():

    # define your variables here
    defDataName = "data"
    problemIndex = -1
    problemList = []

    noOfArguments = len(sys.argv) - 1
    if (noOfArguments >= 1):
        defFileArg = sys.argv[1]
        if (defFileArg != "def-file"):
            defDataName = defFileArg

    if (noOfArguments >= 2):
        problemIndex = int(sys.argv[2]) - 1

    pathToData = "./DataFolder/" + defDataName + ".xlsx"
    print("\nData file to load is: {}".format(pathToData))
    print("Problem index to run arg: {}".format(problemIndex))

    # prepare the model
    problemList.append(FirstQuestionModel(pathToData))
    problemList.append(SecondQuestionModel(pathToData))
    problemList.append(ThirdQuestionModel(pathToData))
    problemList.append(FourthQuestionModel(pathToData))

    threads = [None, None, None, None]

    printLock = threading.Lock()
    if (problemIndex >= 0):
        threads[problemIndex] = threading.Thread(
            target=problemList[problemIndex].solveProblem, args=(printLock,))
        threads[problemIndex].start()
        return
    else:
        for i in range(4):
            threads[i] = threading.Thread(
                target=problemList[i].solveProblem, args=(printLock,))
            threads[i].start()

    # wait for all problems to execute
    for i in range(4):
        if(threads[i] != None):
            threads[i].join()


if __name__ == '__main__':
    main()
