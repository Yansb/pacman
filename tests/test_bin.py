import os
import time
import unittest

from pacai.bin import pacman

"""
This is a test class to assess the executables of this project.
"""
class BinTest(unittest.TestCase):

    def writeInSpecificFile(self, path, agent, score, miliSecond, totalCost = 0):
        with open(path, 'a') as f:
            f.write(agent + ',')
            f.write(score + ',')
            f.write(str(totalCost) + ',')
            f.write(miliSecond + '\n')

    def writeFileHeader(self, path):
        with open (path, 'w') as f:
            f.write('Agent,Scores,Cost,Milis\n')

    def test_pacman(self):
        agents = ["GreedyAgent","DepthSearchAgent", "BreadthSearchAgent", "AStarAgent"]

        absolutePath = os.path.dirname(os.path.abspath(__file__))
        basePath = absolutePath.replace('tests', 'results/')

        resultPath = basePath + 'result.csv'
        breadthSearchPath = basePath + 'breadthSearchAgent.csv'
        depthSearchPath = basePath + 'depthSearchAgent.csv'
        greedyPath = basePath + 'greedySearchAgent.csv'
        aStarPath = basePath + 'aStarSearchAgent.csv'

        self.writeFileHeader(resultPath)
        self.writeFileHeader(greedyPath)
        self.writeFileHeader(depthSearchPath)
        self.writeFileHeader(breadthSearchPath)
        self.writeFileHeader(aStarPath)

        with open (resultPath, 'w') as f:
            f.write('Agent,Scores,Cost,Milis\n')
        for agent in agents:
            map = 1
            while map <= 100:
                started = time.time()
                games = pacman.main(['-p', agent, '--null-graphics', '-l', 'mapa' + str(map)])
                ended = time.time()
                totalCost = 0
                for game in games:
                    for a in game.agents:
                        totalCost += a.totalCost
                scores = [game.state.getScore() for game in games]
                score = str(sum(scores))
                miliSecond = str((ended - started) * 1000)
                totalCost = str(totalCost)

                self.writeInSpecificFile(resultPath, agent, score, totalCost, miliSecond)

                if agent == 'BreadthSearchAgent':
                    self.writeInSpecificFile(breadthSearchPath, agent, score, miliSecond, totalCost)
                elif agent == 'DepthSearchAgent':
                    self.writeInSpecificFile(depthSearchPath,agent, score, miliSecond, totalCost)
                elif agent == 'GreedyAgent':
                    self.writeInSpecificFile(greedyPath,agent, score, miliSecond, totalCost)
                elif agent == 'AStarAgent':
                    self.writeInSpecificFile(aStarPath,agent, score, miliSecond, totalCost)

                map += 1


        # Raise exception for passing in invalid agent for game of pacman.
        try:
            pacman.main(['-p', 'WhatAgent', '--null-graphics'])
            self.fail("Test did not raise expected exception.")
        except LookupError:
            # Expected exception.
            pass
if __name__ == '__main__':
    unittest.main()
