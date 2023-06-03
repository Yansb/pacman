import os

def getBasePath():
    absolutePath = os.path.dirname(os.path.abspath(__file__))
    return absolutePath

def createDirectories():
    graphicsDirectory = f'{getBasePath()}/graphics'
    aStarSearchGraphicsDirectory = f'{graphicsDirectory}/aStarSearch'
    depthSearchGraphicsDirectory = f'{graphicsDirectory}/depthSearch'
    greedySearchGraphicsDirectory = f'{graphicsDirectory}/greedySearch'
    breadthSearchGraphicsDirectory = f'{graphicsDirectory}/breadthSearch'
    allStrategiesGraphicsDirectory = f'{graphicsDirectory}/allStrategies'
    allStrategiesComparativeGraphicsDirectory = f'{graphicsDirectory}/allStrategies/comparative'
    allStrategiesMeansGraphicsDirectory = f'{graphicsDirectory}/allStrategies/means'

    directories = [graphicsDirectory, aStarSearchGraphicsDirectory, depthSearchGraphicsDirectory, greedySearchGraphicsDirectory,
                   breadthSearchGraphicsDirectory, allStrategiesGraphicsDirectory, allStrategiesComparativeGraphicsDirectory,
                   allStrategiesMeansGraphicsDirectory]

    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)


def getAxleX():
    x = []
    
    for i in range(0,100):
        x.append(i)
    
    return x

def getAxleY(y_max):
    y = []

    for i in range(0,100):
        y.append(i*y_max)
    
    return y

def plotGraphic(plt, axle_y, title, x_label, y_label, graphic_path_save, axle_x = []):
    if len(axle_x) == 0:
        axle_x = getAxleX()

    plt.clf()

    plt.plot(axle_x, axle_y, "-g")
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid()

    plt.savefig(graphic_path_save, format='png')

def plotFourGraphics(plt, a_star_agent_cost_y, greedy_agent_cost_y, breadth_search_cost_y, 
                      depth_search_agent_cost_y, title, x_label, y_label, max_y, graphic_path_save):
   
    plt.plot(getAxleX(), getAxleY(max_y), "-w")
    plt.plot(getAxleX(), a_star_agent_cost_y, "-k", label="a estrela")
    plt.plot(getAxleX(), greedy_agent_cost_y, "-b", label="busca gulosa")
    plt.plot(getAxleX(), breadth_search_cost_y, "-g", label="busca em largura")
    plt.plot(getAxleX(), depth_search_agent_cost_y, "-r", label="busca profunda")

    plt.legend(loc="upper right")
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    plt.savefig(graphic_path_save, format='png')

def plotBarGraphic(plt, x, y, width, title, x_label, y_label, graphic_path_save):
    plt.clf()

    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    plt.bar(x, y, width)

    plt.savefig(graphic_path_save, format='png')
