from QuestionModel import QuestionModel


class FirstQuestionModel(QuestionModel):

    def __init__(self, dataFileArg):
        QuestionModel.__init__(self, dataFileArg)

    # abstract method
    def configureModel(self):
        print("Overriding parent setup model question 1")

    # abstract method
    def runModel(self):
        print("Overriding parent run model question 1")


class SecondQuestionModel(QuestionModel):

    def __init__(self, dataFileArg):
        QuestionModel.__init__(self, dataFileArg)

    # abstract method
    def configureModel(self):
        print("Overriding parent setup model question 2")

    # abstract method
    def runModel(self):
        print("Overriding parent run model question 2")


class ThirdQuestionModel(QuestionModel):

    def __init__(self, dataFileArg):
        QuestionModel.__init__(self, dataFileArg)

    # abstract method
    def configureModel(self):
        print("Overriding parent setup model question 3")

    # abstract method
    def runModel(self):
        print("Overriding parent run model question 3")


class FourthQuestionModel(QuestionModel):

    def __init__(self, dataFileArg):
        QuestionModel.__init__(self, dataFileArg)

    # abstract method
    def configureModel(self):
        print("Overriding parent setup model question 4")

    # abstract method
    def runModel(self):
        print("Overriding parent run model question 4")
