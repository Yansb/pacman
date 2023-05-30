"""
This file contains incomplete versions of some agents that can be selected to control Pacman.
You will complete their implementations.

Good luck and happy searching!
"""

import logging

from pacai.core.actions import Actions
from pacai.core.directions import Directions
from pacai.core.distance import manhattan
from pacai.core.distance import maze
from pacai.core.search.food import FoodSearchProblem
from pacai.core.search.position import PositionSearchProblem
from pacai.core.search.problem import SearchProblem
from pacai.agents.base import BaseAgent
from pacai.agents.search.base import SearchAgent

class CornersProblem(SearchProblem):
    """
    This search problem finds paths through all four corners of a layout.

    You must select a suitable state space and successor function.
    See the `pacai.core.search.position.PositionSearchProblem` class for an example of
    a working SearchProblem.

    Additional methods to implement:

    `pacai.core.search.problem.SearchProblem.startingState`:
    Returns the start state (in your search space,
    NOT a `pacai.core.gamestate.AbstractGameState`).

    `pacai.core.search.problem.SearchProblem.isGoal`:
    Returns whether this search state is a goal state of the problem.

    `pacai.core.search.problem.SearchProblem.successorStates`:
    Returns successor states, the actions they require, and a cost of 1.
    The following code snippet may prove useful:
    ```
        successors = []

        for action in Directions.CARDINAL:
            x, y = currentPosition
            dx, dy = Actions.directionToVector(action)
            nextx, nexty = int(x + dx), int(y + dy)
            hitsWall = self.walls[nextx][nexty]

            if (not hitsWall):
                # Construct the successor.

        return successors
    ```
    """

    def __init__(self, startingGameState):
        super().__init__()

        self.walls = startingGameState.getWalls()
        self.startingPosition = startingGameState.getPacmanPosition()
        top = self.walls.getHeight() - 2
        right = self.walls.getWidth() - 2

        self.corners = ((1, 1), (1, top), (right, 1), (right, top))
        for corner in self.corners:
            if not startingGameState.hasFood(*corner):
                logging.warning('Warning: no food in corner ' + str(corner))

    def startingState(self):
        return (self.startingPosition, [])

    def isGoal(self, state):
        node = state[0]
        visited_corners = state[1]

        if node in self.corners:
            if node not in visited_corners:
                visited_corners.append(node)
            return len(visited_corners) == 4
        return False

    def successorStates(self, state):
        x, y = state[0]
        visited_corners = state[1]
        successors = []
        for action in Directions.CARDINAL:
            dx, dy = Actions.directionToVector(action)
            next_x, next_y = int(x + dx), int(y + dy)
            hitsWall = self.walls[next_x][next_y]
            if not hitsWall:
                successor_visited_corners = list(visited_corners)
                next_node = (next_x, next_y)
                if next_node in self.corners:
                    if next_node not in successor_visited_corners:
                        successor_visited_corners.append(next_node)
                successor = ((next_node, successor_visited_corners), action, 1)
                successors.append(successor)
        self._numExpanded += 1

        return successors

    def actionsCost(self, actions):
        """
        Returns the cost of a particular sequence of actions.
        If those actions include an illegal move, return 999999.
        This is implemented for you.
        """

        if (actions is None):
            return 999999

        x, y = self.startingPosition
        for action in actions:
            dx, dy = Actions.directionToVector(action)
            x, y = int(x + dx), int(y + dy)
            if self.walls[x][y]:
                return 999999

        return len(actions)

def cornersHeuristic(state, problem):
    """
    A heuristic for the CornersProblem that you defined.

    This function should always return a number that is a lower bound
    on the shortest path from the state to a goal of the problem;
    i.e. it should be admissible.
    (You need not worry about consistency for this heuristic to receive full credit.)
    """

    corners = problem.corners
    node = state[0]
    visited_corners = state[1]
    corners_left = []
    for corner in corners:
        if corner not in visited_corners:
            corners_left.append(corner)
    if len(corners_left) == 0:
        return 0
    nearest_corners = []
    for corner in corners_left:
        nearest_corners.append(manhattan(corner, node))
        corners_left.remove(corner)
    return min(nearest_corners)

def foodHeuristic(state, problem):
    # pega a posição atual e o grid com comidas
    position, foodGrid = state
    # pega o estado atual do jogo
    gameState = problem.startingGameState
    # inicializa o custo heuristico
    heuristic_cost = 0
    # pega a lista de comidas
    food_left = foodGrid.asList()
    # percorre todas as comidas
    for food in food_left:
        # se o custo heuristico para a comida atual for maior que o custo heuristico
        if heuristic_cost < maze(position, food, gameState):
            # atualiza o custo heuristico
            heuristic_cost = maze(position, food, gameState)
    # retorna o custo heuristico
    return heuristic_cost

class AnyFoodSearchProblem(PositionSearchProblem):
    def __init__(self, gameState, start = None):
        # Passa os parametros para a classe pai
        super().__init__(gameState, goal = None, start = start)
        # Pega a comida do estado
        self.food = gameState.getFood()

    def isGoal(self, state):
        if state in self.food.asList():
            return True
        else:
            return False
