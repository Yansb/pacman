import os
import time
import numpy as np
import random
import pathlib

wall = "%"
pill = "."
pacman = "P"

#dimensão do papa
h = 20
w = 12
#criando uma matriz com números zeros
matrix = np.zeros ((h,w),dtype=np.float64)
#insere números 1 no interior da matriz
matrix[1:h-1,1:w-1] = 1
world =""
count = 0
num_worlds = 1
while count < num_worlds:
    nomearquivo="mapa"
    for i in range(h):
        print("")
        #world.append("\\n")
        world+="\n"
        for j in range(w):
            if i == h/2 and j==w/2:
               print(pacman, end="")
               #world.append(pacman)
               world+=pacman
            elif int(matrix[i][j]==1):
                #gerando números aleatório entre 1 e 9 (inclusivo)
                r = random.randint(1,9)
                #toda vez que o número aleatório
                if r == 1:
                   print(wall, end="")
                   world+=wall
                else:
                    print(pill, end="")
                    #world.append(pill)
                    world+=pill
            else:
                print(wall,end="")
                #world.append(wall)
                world+=wall
    count+=1
    nomearquivo = nomearquivo+str(count)
    print(world)
    with open(nomearquivo+".lay", "w") as arquivo:
        arquivo.write(world)
    world =""
    print("\n")
    time.sleep(1)
    os.system('clear')
    print("\n")
