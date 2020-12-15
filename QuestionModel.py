from abc import ABC, abstractmethod


class QuestionModel(ABC):

    def __init__(self, pathToFile):
        self.pathToFile = pathToFile

    def solveProblem(self):
        self.configureModel()
        self.runModel()

    # abstract method
    def configureModel(self):
        pass

    # abstract method
    def runModel(self):
        pass
