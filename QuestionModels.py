import pandas as pd
from ortools.linear_solver import pywraplp
from QuestionModel import QuestionModel
import time


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
                [self.centerAssignment[i][j] for j in range(self.numOfCities)]) <= self.numOfCities * self.center[i])

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

        # print the result
        printLock.acquire()
        print("\n********* Start of Problem 1 *********\n")

        if (status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE):

            print("The minumum distance a parent should walk is = ",
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

        print("\n\n********* End of Problem 1 *********\n")
        printLock.release()


class SecondQuestionModel(QuestionModel):

    def __init__(self, dataFileArg):
        QuestionModel.__init__(self, dataFileArg)

    # override method
    def configureModel(self):

        # DEFINE MODEL
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

        # road must not be blocked
        for i in range(self.numOfCities):
            for j in range(self.numOfCities):
                self.solver.Add(
                    self.centerAssignment[i][j] * self.probs[i][j] <= 0.60)

        # a parent walk distance must be minimized
        for i in range(self.numOfCities):
            for j in range(self.numOfCities):
                self.solver.Add(
                    self.centerAssignment[i][j] * self.data[i][j] <= self.minDistance)

        # OBJECTIVE FUNCTION
        self.solver.Minimize(self.minDistance)

    # override method
    def runModel(self, printLock):

        # run the model
        status = self.solver.Solve()

        # print the result
        printLock.acquire()
        print("\n********* Start of Problem 2 *********\n")

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

        print("\n\n********* End of Problem 2 *********\n")
        printLock.release()


class ThirdQuestionModel(QuestionModel):

    def __init__(self, dataFileArg):
        QuestionModel.__init__(self, dataFileArg)

    # override method
    def configureModel(self):
        # define model
        self.solver = pywraplp.Solver.CreateSolver("SCIP")
        self.numOfCities = len(self.data)
        # define variables
        self.x = {}
        for i in range(self.numOfCities):
            for j in range(self.numOfCities):
                self.x[i, j] = self.solver.IntVar(0, 1, '')

        self.u = {}
        for j in range(1, self.numOfCities):
            self.u[j] = self.solver.IntVar(1, self.numOfCities - 1, '')

        # define constraints
        # each city entered once.
        for i in range(self.numOfCities):
            self.solver.Add(self.solver.Sum(
                [self.x[i, j] for j in range(self.numOfCities)]) == 1)

        # each city exited once.
        for j in range(self.numOfCities):
            self.solver.Add(self.solver.Sum(
                [self.x[i, j] for i in range(self.numOfCities)]) == 1)

        # diagonal must be 0
        self.solver.Add(self.solver.Sum(
            [self.x[i, i] for i in range(self.numOfCities)]) == 0)

        # MTZ constraint
        for i in range(1, self.numOfCities):
            for j in range(1, self.numOfCities):
                if i != j:
                    self.solver.Add(
                        self.u[i] - self.u[j] + self.numOfCities*self.x[i, j] <= self.numOfCities - 1)

        # Blocked roads
        for i in range(self.numOfCities):
            for j in range(self.numOfCities):
                self.solver.Add(self.x[i, j] * self.probs[i][j] <= 0.6)

        # create objective function
        objective_terms = []
        for i in range(self.numOfCities):
            for j in range(self.numOfCities):
                objective_terms.append(self.x[i, j] * self.data[i][j])
        self.solver.Minimize(self.solver.Sum(objective_terms))

    # override method
    def runModel(self, printLock):

        # run the model
        status = self.solver.Solve()

        printLock.acquire()
        print("\n********* Start of Problem 3 *********\n")
        # print the result
        if (status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE):

            print("Minimum time of travels is = ",
                  self.solver.Objective().Value() / 40, "hours\n")
            a = 0
            for i in range(self.numOfCities):
                for j in range(self.numOfCities):
                    # if chosen as center (with tolerance for floating point arithmetic)
                    if (self.x[a, j].solution_value() > 0.5 and a != j):
                        print("Santa travelled from %d to %d" % (a + 1, j + 1))
                        a = j
                        break
        else:
            print(
                "Solver could not solve the problem. The given data could be infeasible...\n")

        print("\n********* End of Problem 3 *********\n")
        printLock.release()


class FourthQuestionModel(QuestionModel):

    def __init__(self, dataFileArg):
        QuestionModel.__init__(self, dataFileArg)

    # override method
    def configureModel(self):

        # define model
        self.solver = pywraplp.Solver.CreateSolver(
            "SCIP")
        self.numOfCities = len(self.data)  # 30

        self.speedOfSnowplow = 40  # Speed of the snowplow
        self.timeLimit = 10  # Santa wants volunteer to return to node 1 at most 10 hours
        self.maxDistanceLimit = self.speedOfSnowplow * self.timeLimit

        # DEFINE VARIABLES
        infinity = self.solver.infinity()

        # to minimize
        self.numOfVolunteers = self.solver.IntVar(1, self.numOfCities - 1, "")

        # i stole it from abe
        #self.u = {}
        # for j in range(1, self.numOfCities):
        #    self.u[j] = self.solver.NumVar(0, infinity, '')

        # decision
        #self.y = self.solver.IntVar(0, 1, "")
        #self.M = 1

        # inventory
        #self.travelCost = []
        # for j in range(self.numOfCities):
        #    self.travelCost.append(
        #        self.solver.NumVar(0, infinity, ''))

        # if city j is visited after visiting city i, if we arrive city j from city i => fromToCity[i][j] = 1
        self.fromCityToCity = []
        self.remDistance = []
        for i in range(self.numOfCities):
            self.fromCityToCity.append([])
            self.remDistance.append([])
            for j in range(self.numOfCities):
                self.fromCityToCity[i].append(self.solver.IntVar(0, 1, ""))
                self.remDistance[i].append(self.solver.NumVar(0, infinity, ''))

        # DEFINE CONSTRAINTS

        # we enter each city once except the route node
        for i in range(1, self.numOfCities):
            self.solver.Add(self.solver.Sum(
                [self.fromCityToCity[i][j] for j in range(self.numOfCities)]) == 1)

        # we leave each city once except route node
        for j in range(1, self.numOfCities):
            self.solver.Add(self.solver.Sum(
                [self.fromCityToCity[i][j] for i in range(self.numOfCities)]) == 1)

        # diagonal must be 0
        self.solver.Add(self.solver.Sum(
            [self.fromCityToCity[i][i] for i in range(self.numOfCities)]) <= 0)

        # if m vehcles leave
        self.solver.Add(self.solver.Sum(
            [self.fromCityToCity[0][j] for j in range(self.numOfCities)]) == self.numOfVolunteers)

        # m vehicles return
        self.solver.Add(self.solver.Sum(
            [self.fromCityToCity[i][0] for i in range(self.numOfCities)]) == self.numOfVolunteers)

        # DISTANCE CONSTRAINTS

        for i in range(self.numOfCities):
            for j in range(self.numOfCities):
                self.solver.Add(
                    self.remDistance[i][j] <= self.maxDistanceLimit * self.fromCityToCity[i][j])

        for i in range(1, self.numOfCities):
            self.solver.Add(self.remDistance[0][i] == (self.maxDistanceLimit *
                                                       self.fromCityToCity[0][i]) - (self.data[0][i] * self.fromCityToCity[0][i]))

        for i in range(1, self.numOfCities):
            rowSum = [self.remDistance[i][j]
                      for j in range(self.numOfCities) if j != i]
            colSum = [self.remDistance[j][i]
                      for j in range(self.numOfCities) if j != i]
            distance = [self.fromCityToCity[i][j] * self.data[i][j]
                        for j in range(self.numOfCities)]
            self.solver.Add(self.solver.Sum(
                rowSum) - self.solver.Sum(colSum) + self.solver.Sum(distance) == 0)

        # inventory constraints
        # for i in range(self.numOfCities):
        #    for j in range(1, self.numOfCities):
        #        self.solver.Add(
        #            self.travelCost[j] - (self.data[i][j] * self.fromCityToCity[i][j] + self.travelCost[i]) <= self.M * self.y)
        #        self.solver.Add(
        #            self.fromCityToCity[i][j] <= self.M * (self.y - 1))

        # MTZ
        # for i in range(1, self.numOfCities):
        #    for j in range(1, self.numOfCities):
        #        if i != j:
        #            self.solver.Add(
        #                self.u[i] - self.u[j] + self.numOfCities*self.fromCityToCity[i][j] <= self.numOfCities - 1)

        # base travel cost
        # self.solver.Add(
        #    self.travelCost[0] == 0)

        # for i in range(self.numOfCities):
        #    self.solver.Add(
        #        self.distanceLimit - (self.fromCityToCity[i][0] * self.data[i][0] + self.travelCost[i]) <= self.M * self.y)
        #    self.solver.Add(
        #        self.fromCityToCity[i][0] <= self.M * (self.y - 1))

        # create objective function
        # self.solver.Minimize(self.numOfVolunteers)

        # self.solver.Minimize(self.solver.Sum(
        #    [self.fromCityToCity[0][j] * 3000 for j in range(self.numOfCities)]))

        objective_terms = []
        for i in range(self.numOfCities):
            for j in range(self.numOfCities):
                objective_terms.append(
                    self.fromCityToCity[i][j] * self.data[i][j])
        # for i in range(1, self.numOfCities):
        #    objective_terms.append(self.travelCost[i])

        for i in range(self.numOfCities):
            objective_terms.append(self.fromCityToCity[i][0])

        print('Number of constraints = ', self.solver.NumConstraints())

        self.solver.Minimize(self.numOfVolunteers)
        # self.solver.Minimize(self.solver.Sum(
        #    objective_terms) + self.numOfVolunteers * 5000)

        self.solver.SetNumThreads(4)

    # override method
    def runModel(self, printLock):

        init_time = time.time()
        # run the model
        status = self.solver.Solve()

        # print the result
        printLock.acquire()
        print("\n********* Start of Problem 4 *********\n")

        if (status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE):

            end_time = time.time()
            print('Elapsed time:', end_time - init_time)

            print("The minumum number of helpers is = ",
                  self.solver.Objective().Value())

            for i in range(self.numOfCities):
                for j in range(self.numOfCities):
                    if (self.fromCityToCity[i][j].solution_value() > 0.5):
                        print("Road from %d to %d" % (i, j))

        else:
            print(
                "Solver could not solve the problem 4. The given data could be infeasible...\n")

        print("\n\n********* End of Problem 4 *********\n")
        printLock.release()
