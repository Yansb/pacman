import logging
from pacai.agents.search.base import SearchAgent
from pacai.core.search.position import PositionSearchProblem
from pacai.student import search
from pacai.student.searchAgents import AnyFoodSearchProblem

class DepthSearchAgent(SearchAgent):
    """
    Search for all food using a sequence of searches.
    """

    def __init__(self, index, **kwargs):
        super().__init__(index, **kwargs)

    def registerInitialState(self, state):
        self._actions = []
        self._actionIndex = 0

        currentState = state
        # Enquanto ainda houver comida
        while (currentState.getFood().count() > 0):
            # Encontra o caminho para o ponto mais próximo
            nextPathSegment = self.findPathToClosestDot(currentState)
            # Adiciona o caminho encontrado ao caminho total
            self._actions += nextPathSegment
            # Para cada ação no caminho encontrado
            for action in nextPathSegment:
                # Verifica se a ação é legal
                legal = currentState.getLegalActions()
                if action not in legal:
                    raise Exception('findPathToClosestDot returned an illegal move: %s!\n%s' %
                            (str(action), str(currentState)))
                # Gera o próximo estado
                currentState = currentState.generateSuccessor(0, action)
        self.totalCost = len(self._actions)
        logging.info('Path found with cost %d.' % len(self._actions))

    def findPathToClosestDot(self, gameState):
        """
        Returns a path (a list of actions) to the closest dot, starting from gameState.
        """
        # Cria o problema de busca
        problem = AnyFoodSearchProblem(gameState)
        return search.depthFirstSearch(problem)

