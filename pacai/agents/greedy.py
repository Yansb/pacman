import random

from pacai.agents.base import BaseAgent
from pacai.core.directions import Directions
from pacai.util import reflection

class GreedyAgent(BaseAgent):
    """
    An agent that greedily takes the available move with the best score at the time.
    """
    def __init__(self, index, evalFn = "pacai.core.eval.score", **kwargs):
        self.totalCost = 0
        super().__init__(index, **kwargs)

        self.evaluationFunction = reflection.qualifiedImport(evalFn)
        assert(self.evaluationFunction is not None)

    def getAction(self, state):
        # lista todas as ações possíveis
        legal = state.getLegalPacmanActions()
        # remove a ação STOP
        if (Directions.STOP in legal):
            legal.remove(Directions.STOP)
        # Lista o estados sucessores e suas ações
        successors = [(state.generateSuccessor(0, action), action) for action in legal]
        # Calcula o score de cada estado sucessor
        scored = [(self.evaluationFunction(state), action) for state, action in successors]
        # Escolhe a melhor ação
        bestScore = max(scored)[0]
        # Lista todas as melhores ações
        bestActions = [pair[1] for pair in scored if pair[0] == bestScore]
        # Atualiza o custo total
        self.totalCost += 1
        # Retorna uma ação aleatória entre as melhores
        return random.choice(bestActions)
