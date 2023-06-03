import matplotlib.pyplot as plt

from agents.aStarSearchAgent import AStarSearchAgent
from agents.depthSearchAgent import DepthSearchAgent
from agents.greedySearchAgent import GreedySearchAgent
from agents.breadthSearchAgent import BreadthSearchAgent
from helpers import getBasePath, plotGraphic, plotFourGraphics, plotBarGraphic, createDirectories

aStarSearchAgentPath = f'{getBasePath()}/aStarSearchAgent.csv'
depthSearchAgentPath = f'{getBasePath()}/depthSearchAgent.csv'
greedySearchAgentPath = f'{getBasePath()}/greedySearchAgent.csv'
breadthSearchAgentPath = f'{getBasePath()}/breadthSearchAgent.csv'
 
aStarSearchAgentGraphicPath = f'{getBasePath()}/graphics/aStarSearch/aStarSearch'
depthSearchAgentGraphicPath = f'{getBasePath()}/graphics/depthSearch/depthSearch'
greedySearchAgentGraphicPath = f'{getBasePath()}/graphics/greedySearch/greedySearch'
breadthSearchAgentGraphicPath = f'{getBasePath()}/graphics/breadthSearch/breadthSearch'
allStrategiesGraphicPath = f'{getBasePath()}/graphics/allStrategies'

createDirectories()

aStarSearchAgent = AStarSearchAgent(aStarSearchAgentPath)
depthSearchAgent = DepthSearchAgent(depthSearchAgentPath)
greedySearchAgent = GreedySearchAgent(greedySearchAgentPath)
breadthSearchAgent = BreadthSearchAgent(breadthSearchAgentPath)

#cost
aStarSearchCostY = aStarSearchAgent.getAxleYToCost()
depthSearchCostY = depthSearchAgent.getAxleYToCost()
greedySearchCostY = greedySearchAgent.getAxleYToCost()
breadthSearchCostY = breadthSearchAgent.getAxleYToCost()

plotGraphic(plt, aStarSearchCostY, "Custo da Busca A*", "Iteração", "Custo", f'{aStarSearchAgentGraphicPath}Cost.png')
plotGraphic(plt, depthSearchCostY, "Custo da Busca em Profundidade", "Iteração", "Custo", f'{depthSearchAgentGraphicPath}Cost.png')
plotGraphic(plt, greedySearchCostY, "Custo da Busca Gulosa", "Iteração", "Custo", f'{greedySearchAgentGraphicPath}Cost.png')
plotGraphic(plt, breadthSearchCostY, "Custo da Busca em Largura", "Iteração", "Custo", f'{breadthSearchAgentGraphicPath}Cost.png')

plotFourGraphics(plt, aStarSearchCostY, greedySearchCostY, breadthSearchCostY, depthSearchCostY,
                    "Custo", "Iteração", "Custo", 40, f'{allStrategiesGraphicPath}/comparative/cost.png')

#score
aStarSearchScoreY = aStarSearchAgent.getAxleYToScore()
depthSearchScoreY = depthSearchAgent.getAxleYToScore()
greedySearchScoreY = greedySearchAgent.getAxleYToScore()
breadthSearchScoreY = breadthSearchAgent.getAxleYToScore()

plotGraphic(plt, aStarSearchScoreY, "Pontuação da Busca A*", "Iteração", "Pontuação",f'{aStarSearchAgentGraphicPath}Score.png')
plotGraphic(plt, depthSearchScoreY, "Pontuação da Busca em Profundidade", "Iteração", "Pontuação",f'{depthSearchAgentGraphicPath}Score.png')
plotGraphic(plt, greedySearchScoreY, "Pontuação da Busca Gulosa", "Iteração", "Pontuação", f'{greedySearchAgentGraphicPath}Score.png')
plotGraphic(plt, breadthSearchScoreY, "Pontuação da Busca em Largura", "Iteração", "Pontuação", f'{breadthSearchAgentGraphicPath}Score.png')

plotFourGraphics(plt, aStarSearchScoreY, greedySearchScoreY, breadthSearchScoreY, depthSearchScoreY,
                    "Pontuação", "Iteração", "Pontuação", 40, f'{allStrategiesGraphicPath}/comparative/score.png')

#time(in ms)
aStarSearchMilisecondsY = aStarSearchAgent.getAxleYToMiliSeconds()
depthSearchMilisecondsY = depthSearchAgent.getAxleYToMiliSeconds()
greedySearchMilisecondsY = greedySearchAgent.getAxleYToMiliSeconds()
breadthSearchMilisecondsY = breadthSearchAgent.getAxleYToMiliSeconds()

plotGraphic(plt, aStarSearchMilisecondsY, "Tempo de execução da Busca A*", "Iteração", "Tempo de execução (ms)",f'{aStarSearchAgentGraphicPath}Time.png')
plotGraphic(plt, depthSearchMilisecondsY, "Tempo de execução da Busca em Profundidade", "Iteração", "Tempo de execução (ms)",f'{depthSearchAgentGraphicPath}Time.png')
plotGraphic(plt, greedySearchMilisecondsY, "Tempo de execução da Busca Gulosa", "Iteração", "Tempo de execução (ms)", f'{greedySearchAgentGraphicPath}Time.png')
plotGraphic(plt, breadthSearchMilisecondsY, "Tempo de execução da Busca em Largura", "Iteração", "Tempo de execução (ms)", f'{breadthSearchAgentGraphicPath}Time.png')

plotFourGraphics(plt,aStarSearchMilisecondsY, greedySearchMilisecondsY, breadthSearchMilisecondsY, depthSearchMilisecondsY,
                    "Tempo de Execução", "Iteração", "Tempo de execução (ms)", 10, f'{allStrategiesGraphicPath}/comparative/time.png')

#os arrays agent_costs, agents_scores, agents_times devem seguir a mesma ordem
strategies = ["Profunda", "Gulosa", "Largura", "A*"]

#cost average
aStarAgentCostAverage = aStarSearchAgent.getCostMean()
greedyAgentCostAverage = greedySearchAgent.getCostMean()
breadthSearchCostAverage = breadthSearchAgent.getCostMean()
depthSearchCostAverage = depthSearchAgent.getCostMean()

agents_costs = [depthSearchCostAverage, greedyAgentCostAverage, breadthSearchCostAverage, aStarAgentCostAverage]

plotBarGraphic(plt, strategies, agents_costs, 0.3, "Custo Médio", "Estratégia", "Custo", f'{allStrategiesGraphicPath}/means/meanCostBar.png')

#score average
aStarAgentScoreAverage = aStarSearchAgent.getScoreMeans()
greedyAgentScoreAverage = greedySearchAgent.getScoreMeans()
breadthSearchScoreAverage = breadthSearchAgent.getScoreMeans()
depthSearchScoreAverage = depthSearchAgent.getScoreMeans()

agents_scores = [depthSearchScoreAverage, greedyAgentScoreAverage, breadthSearchScoreAverage, aStarAgentScoreAverage]

#Pode escolher entre linha ou barras
# plotGraphic(plt, agents_scores, "Pontuação Média", "Estratégia", "Pontuação", f'{allStrategiesGraphicPath}/means/meanScore.png', strategies)
plotBarGraphic(plt, strategies, agents_scores, 0.3, "Pontuação Média", "Estratégia", "Pontuação", f'{allStrategiesGraphicPath}/means/meanScoreBar.png')

#time average
aStarAgentMilisecondsAverage = aStarSearchAgent.getMiliSecondsMean()
greedyAgentMilisecondsAverage = greedySearchAgent.getMiliSecondsMean()
breadthSearchMilisecondsAverage = breadthSearchAgent.getMiliSecondsMean()
depthSearchMilisecondsAverage = depthSearchAgent.getMiliSecondsMean()

agents_times = [depthSearchMilisecondsAverage, greedyAgentMilisecondsAverage, breadthSearchMilisecondsAverage, aStarAgentMilisecondsAverage]

plotBarGraphic(plt, strategies, agents_times, 0.3, "Tempo Médio", "Estratégia", "Tempo (Ms)", f'{allStrategiesGraphicPath}/means/meanTimeBar.png')
