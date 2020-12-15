from abc import ABC, abstractmethod
import pandas as pd


class QuestionModel(ABC):

    # use self.data to access data sheet
    # use self.probs to access probabilities sheet

    def __init__(self, pathToFile):
        self.pathToFile = pathToFile
        dfs = pd.read_excel(
            self.pathToFile, sheet_name=None, header=None, engine="openpyxl")
        self.data = dfs["d"]
        self.probs = dfs["p"]

    def solveProblem(self):
        self.configureModel()
        self.runModel()

    # abstract method
    def configureModel(self):
        pass

    # abstract method
    def runModel(self):
        pass
