import matplotlib.pyplot as plt

from agents.depthSearchAgent import DepthSearchAgent
from agents.greedySearchAgent import GreedySearchAgent
from agents.breadthSearchAgent import BreadthSearchAgent
from helpers import getBasePath, plotGraphic, plotThreeGraphics, plotBarGraphic, createDirectories

depthSearchAgentPath = f'{getBasePath()}/depthSearchAgent.csv'
greedySearchAgentPath = f'{getBasePath()}/greedySearchAgent.csv'
breadthSearchAgentPath = f'{getBasePath()}/breadthSearchAgent.csv'
 
depthSearchAgentGraphicPath = f'{getBasePath()}/graphics/depthSearch/depthSearch'
greedySearchAgentGraphicPath = f'{getBasePath()}/graphics/greedySearch/greedySearch'
breadthSearchAgentGraphicPath = f'{getBasePath()}/graphics/breadthSearch/breadthSearch'
allStrategiesGraphicPath = f'{getBasePath()}/graphics/allStrategies'

createDirectories()

depthSearchAgent = DepthSearchAgent(depthSearchAgentPath)
greedySearchAgent = GreedySearchAgent(greedySearchAgentPath)
breadthSearchAgent = BreadthSearchAgent(breadthSearchAgentPath)

#cost
depthSearchCostY = depthSearchAgent.getAxleYToCost()
greedySearchCostY = greedySearchAgent.getAxleYToCost()
breadthSearchCostY = breadthSearchAgent.getAxleYToCost()

plotGraphic(plt, depthSearchCostY, "Custo da Busca em Profundidade", "Iteração", "Custo", f'{depthSearchAgentGraphicPath}Cost.png')
plotGraphic(plt, greedySearchCostY, "Custo da Busca Gulosa", "Iteração", "Custo", f'{greedySearchAgentGraphicPath}Cost.png')
plotGraphic(plt, breadthSearchCostY, "Custo da Busca em Largura", "Iteração", "Custo", f'{breadthSearchAgentGraphicPath}Cost.png')

plotThreeGraphics(plt, greedySearchCostY, breadthSearchCostY, depthSearchCostY,
                    "Custo", "Iteração", "Custo", 40, f'{allStrategiesGraphicPath}/comparative/cost.png')

#score
depthSearchScoreY = depthSearchAgent.getAxleYToScore()
greedySearchScoreY = greedySearchAgent.getAxleYToScore()
breadthSearchScoreY = breadthSearchAgent.getAxleYToScore()

plotGraphic(plt, depthSearchScoreY, "Pontuação da Busca em Profundidade", "Iteração", "Pontuação",f'{depthSearchAgentGraphicPath}Score.png')
plotGraphic(plt, greedySearchScoreY, "Pontuação da Busca Gulosa", "Iteração", "Pontuação", f'{greedySearchAgentGraphicPath}Score.png')
plotGraphic(plt, breadthSearchScoreY, "Pontuação da Busca em Largura", "Iteração", "Pontuação", f'{breadthSearchAgentGraphicPath}Score.png')

plotThreeGraphics(plt, greedySearchScoreY, breadthSearchScoreY, depthSearchScoreY,
                    "Pontuação", "Iteração", "Pontuação", 40, f'{allStrategiesGraphicPath}/comparative/score.png')

#time(in ms)
depthSearchMilisecondsY = depthSearchAgent.getAxleYToMiliSeconds()
greedySearchMilisecondsY = greedySearchAgent.getAxleYToMiliSeconds()
breadthSearchMilisecondsY = breadthSearchAgent.getAxleYToMiliSeconds()

plotGraphic(plt, depthSearchMilisecondsY, "Tempo de execução da Busca em Profundidade", "Iteração", "Tempo de execução (ms)",f'{depthSearchAgentGraphicPath}Time.png')
plotGraphic(plt, greedySearchMilisecondsY, "Tempo de execução da Busca Gulosa", "Iteração", "Tempo de execução (ms)", f'{greedySearchAgentGraphicPath}Time.png')
plotGraphic(plt, breadthSearchMilisecondsY, "Tempo de execução da Busca em Largura", "Iteração", "Tempo de execução (ms)", f'{breadthSearchAgentGraphicPath}Time.png')

plotThreeGraphics(plt, greedySearchMilisecondsY, breadthSearchMilisecondsY, depthSearchMilisecondsY,
                    "Tempo de Execução", "Iteração", "Tempo de execução (ms)", 10, f'{allStrategiesGraphicPath}/comparative/time.png')

#os arrays agent_costs, agents_scores, agents_times devem seguir a mesma ordem
strategies = ["Profunda", "Gulosa", "Largura"]

#cost average
greedyAgentCostAverage = greedySearchAgent.getCostMean()
breadthSearchCostAverage = breadthSearchAgent.getCostMean()
depthSearchCostAverage = depthSearchAgent.getCostMean()

agents_costs = [depthSearchCostAverage, greedyAgentCostAverage, breadthSearchCostAverage]

plotBarGraphic(plt, strategies, agents_costs, 0.3, "Custo Médio", "Estratégia", "Custo", f'{allStrategiesGraphicPath}/means/meanCostBar.png')

#score average
greedyAgentScoreAverage = greedySearchAgent.getScoreMeans()
breadthSearchScoreAverage = breadthSearchAgent.getScoreMeans()
depthSearchScoreAverage = depthSearchAgent.getScoreMeans()

agents_scores = [depthSearchScoreAverage, greedyAgentScoreAverage, breadthSearchScoreAverage]

#Pode escolher entre linha ou barras
# plotGraphic(plt, agents_scores, "Pontuação Média", "Estratégia", "Pontuação", f'{allStrategiesGraphicPath}/means/meanScore.png', strategies)
plotBarGraphic(plt, strategies, agents_scores, 0.3, "Pontuação Média", "Estratégia", "Pontuação", f'{allStrategiesGraphicPath}/means/meanScoreBar.png')

#time average
greedyAgentMilisecondsAverage = greedySearchAgent.getMiliSecondsMean()
breadthSearchMilisecondsAverage = breadthSearchAgent.getMiliSecondsMean()
depthSearchMilisecondsAverage = depthSearchAgent.getMiliSecondsMean()

agents_times = [depthSearchMilisecondsAverage, greedyAgentMilisecondsAverage, breadthSearchMilisecondsAverage]

plotBarGraphic(plt, strategies, agents_times, 0.3, "Tempo Médio", "Estratégia", "Tempo (Ms)", f'{allStrategiesGraphicPath}/means/meanTimeBar.png')
