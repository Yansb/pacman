import logging
from pacai.agents.search.base import SearchAgent
from pacai.core.search.position import PositionSearchProblem
from pacai.student import search
from pacai.student.searchAgents import AnyFoodSearchProblem

class BreadthSearchAgent(SearchAgent):
    """
    Search for all food using a sequence of searches.

    Estrutura semelhante a busca profunda mudando apenas a função de busca utilizada
    no momento de encontrar o caminho para o ponto mais próximo.
    """

    def __init__(self, index, **kwargs):
        super().__init__(index, **kwargs)

    def registerInitialState(self, state):
        self._actions = []
        self._actionIndex = 0

        currentState = state

        while (currentState.getFood().count() > 0):
            nextPathSegment = self.findPathToClosestDot(currentState)
            self._actions += nextPathSegment

            for action in nextPathSegment:
                legal = currentState.getLegalActions()
                if action not in legal:
                    raise Exception('findPathToClosestDot returned an illegal move: %s!\n%s' %
                            (str(action), str(currentState)))

                currentState = currentState.generateSuccessor(0, action)
        self.totalCost = len(self._actions)
        logging.info('Path found with cost %d.' % len(self._actions))

    def findPathToClosestDot(self, gameState):
        """
        Returns a path (a list of actions) to the closest dot, starting from gameState.
        """
        problem = AnyFoodSearchProblem(gameState)
        return search.breadthFirstSearch(problem)

