import time
import unittest

from pacai.bin import capture
from pacai.bin import gridworld
from pacai.bin import pacman

"""
This is a test class to assess the executables of this project.
"""
class BinTest(unittest.TestCase):

    def test_pacman(self):
        agents = ["GreedyAgent", "DepthSearchAgent", "BreadthSearchAgent"]
        with open ('result.csv', 'w') as f:
            f.write('Agent,Scores,milis\n')
        for agent in agents:
            map = 1
            while map <= 100:
                started = time.time()
                games = pacman.main(['-p', agent, '--null-graphics', '-l', 'mapa' + str(map)])
                ended = time.time()
                scores = [game.state.getScore() for game in games]
                score = str(sum(scores))
                milis = str((ended - started) * 1000)
                with open('result.csv', 'a') as f:
                    f.write(agent + ',')
                    f.write(score + ',')
                    f.write(milis + '\n')
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
