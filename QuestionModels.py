import pandas as pd
from ortools.linear_solver import pywraplp
from QuestionModel import QuestionModel


class FirstQuestionModel(QuestionModel):

    def __init__(self, dataFilePath):
        QuestionModel.__init__(self, dataFilePath)

    # override method
    def configureModel(self):

        # define model
        self.solver = pywraplp.Solver.CreateSolver("SCIP")
        self.numOfCities = len(self.data)

        # DEFINE VARIABLES

        # distance a parent walks that should be minimized
        infinity = self.solver.infinity()
        self.minDistance = self.solver.NumVar(0, infinity, "")

        # if village i is selected as center
        self.center = []
        for i in range(self.numOfCities):
            self.center.append(self.solver.IntVar(0, 1, ""))

        # x[i, j] is an array of 0-1 variables, which will be 1
        # if center i is assigned village j
        self.centerAssignment = []
        for i in range(self.numOfCities):
            self.centerAssignment.append([])
            for j in range(self.numOfCities):
                self.centerAssignment[i].append(self.solver.IntVar(0, 1, ""))

        # DEFINE CONSTRAINTS

        # There are exactly 4 centers
        self.solver.Add(self.solver.Sum(
            [self.center[i] for i in range(self.numOfCities)]) == 4)

        # If a village is chosen as center
        for i in range(self.numOfCities):
            self.solver.Add(self.solver.Sum(
                [self.centerAssignment[i][j] for j in range(self.numOfCities)]) <= 20 * self.center[i])

        # only a single center is assigned to a village
        for j in range(self.numOfCities):
            self.solver.Add(self.solver.Sum(
                [self.centerAssignment[i][j] for i in range(self.numOfCities)]) == 1)

        # a parent walk distance must be minimized
        for i in range(self.numOfCities):
            for j in range(self.numOfCities):
                self.solver.Add(
                    self.centerAssignment[i][j] * self.data[i][j] <= self.minDistance)

        # OBJECTIVE FUNCTION
        self.solver.Minimize(self.minDistance)

        """
        objective_terms = []
        for i in range(self.numOfCities):
            for j in range(self.numOfCities):
                objective_terms.append(self.center[i] * self.data[i][j])
        self.solver.Minimize(self.solver.Sum(objective_terms))"""

        # FOR REFERANCE
        """self.solver = pywraplp.Solver.CreateSolver('SCIP')
        self.costs = [
            [90, 80, 75, 70],
            [35, 85, 55, 65],
            [125, 95, 90, 95],
            [45, 110, 95, 115],
            [50, 100, 90, 100],
        ]

        self.num_workers = len(self.costs)
        self.num_tasks = len(self.costs[0])

        # x[i, j] is an array of 0-1 variables, which will be 1
        # if worker i is assigned to task j.
        self.x = {}
        for i in range(self.num_workers):
            for j in range(self.num_tasks):
                self.x[i, j] = self.solver.IntVar(0, 1, '')

        # Each worker is assigned to at most 1 task.
        for i in range(self.num_workers):
            self.solver.Add(self.solver.Sum(
                [self.x[i, j] for j in range(self.num_tasks)]) <= 1)

        # Each task is assigned to exactly one worker.
        for j in range(self.num_tasks):
            self.solver.Add(self.solver.Sum(
                [self.x[i, j] for i in range(self.num_workers)]) == 1)

        # Create the objective function
        objective_terms = []
        for i in range(self.num_workers):
            for j in range(self.num_tasks):
                objective_terms.append(self.costs[i][j] * self.x[i, j])
        self.solver.Minimize(self.solver.Sum(objective_terms))"""

    # override method
    def runModel(self, printLock):
        # run the model
        status = self.solver.Solve()

        printLock.acquire()
        print("\n********* Start of Problem 1 *********\n")

        if (status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE):

            print("The minumum distance a parent should work is = ",
                  self.solver.Objective().Value())
            for i in range(self.numOfCities):
                # if chosen as center (with tolerance for floating point arithmetic)
                if (self.center[i].solution_value() > 0.5):
                    print("\nVillage %d is chosen as center" % (i + 1))
                    print("\tAssigned villages are => ", end="")
                for j in range(self.numOfCities):
                    if (self.centerAssignment[i][j].solution_value() > 0.5):
                        print((j + 1), end="  -  ")
        else:
            print(
                "Solver could not solve the problem 1. The given data could be infeasible...\n")
        # print the result
        """status = self.solver.Solve()
        if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
            print('Total cost = ', self.solver.Objective().Value(), '\n')
        for i in range(self.num_workers):
            for j in range(self.num_tasks):
                # Test if x[i,j] is 1 (with tolerance for floating point arithmetic).
                if self.x[i, j].solution_value() > 0.5:
                    print('Worker %d assigned to task %d.  Cost = %d' %
                    (i, j, self.costs[i][j]))
        """
        print("\n\n********* End of Problem 1 *********\n")
        printLock.release()


class SecondQuestionModel(QuestionModel):

    def __init__(self, dataFileArg):
        QuestionModel.__init__(self, dataFileArg)

    # override method
    def configureModel(self):
        print()
        # define model

        # define variables

        # define constraints

        # create objective function

        # abstract method

        # override method
    def runModel(self, printLock):

        printLock.acquire()
        print("\n********* Start of Problem 2 *********\n")
        # run the model

        # print the result

        print("\n********* End of Problem 2 *********\n")
        printLock.release()


class ThirdQuestionModel(QuestionModel):

    def __init__(self, dataFileArg):
        QuestionModel.__init__(self, dataFileArg)

    # override method
    def configureModel(self):
        print()
        # define model

        # define variables

        # define constraints

        # create objective function

        # override method

    def runModel(self, printLock):

        printLock.acquire()
        print("\n********* Start of Problem 3 *********\n")
        # run the model

        # print the result

        print("\n********* End of Problem 3 *********\n")
        printLock.release()


class FourthQuestionModel(QuestionModel):

    def __init__(self, dataFileArg):
        QuestionModel.__init__(self, dataFileArg)

    # override method
    def configureModel(self):
        print()
        # define model

        # define variables

        # define constraints

        # create objective function

        # abstract method

        # override method

    def runModel(self, printLock):

        printLock.acquire()
        print("\n********* Start of Problem 4 *********\n")
        # run the model

        # print the result

        print("\n********* End of Problem 4 *********\n")
        printLock.release()
