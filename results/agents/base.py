import pandas as pd

from abc import ABC
	
class BaseAgent(ABC):

    dataframe = pd.DataFrame()

    def __init__(self, file_path):
        self.dataframe = pd.read_csv(file_path)

    def getCost(self):
        return self.dataframe["Cost"]
    
    def getCostMean(self):
        cost = self.getCost()

        return cost.mean()

    def getMiliSeconds(self):
        return self.dataframe["Milis"]

    def getMiliSecondsMean(self):
        miliseconds = self.getMiliSeconds()

        return miliseconds.mean()

    def getScore(self):
        return self.dataframe["Scores"]

    def getScoreMeans(self):
        score = self.getScore()

        return score.mean()

    def getAxleX(self):
        x = []

        for i in range(0,100):
            x.append(i)

        return x

    def getAxleYToCost(self):
        cost = self.getCost()
        costAxleY = []

        for i in range(0,100):
            costAxleY.append(cost[i])

        return costAxleY

    def getAxleYToMiliSeconds(self):
        cost = self.getMiliSeconds()
        costAxleY = []

        for i in range(0,100):
            costAxleY.append(cost[i])

        return costAxleY

    def getAxleYToScore(self):
        cost = self.getScore()
        costAxleY = []

        for i in range(0,100):
            costAxleY.append(cost[i])

        return costAxleY
