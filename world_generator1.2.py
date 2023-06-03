# Mapas para executar com a estratégia A*
import os
import time
import numpy as np
import random
import pathlib

wall = "%"
pill = "."
pacman = "P"
space= " "

#dimensão do mapa 
h = 20
w = 12
#criando uma matriz com números zeros 
matrix = np.zeros ((h,w),dtype=np.float64)
#insere números 1 no interior da matriz
matrix[1:h-1,1:w-1] = 1
world =""
count = 0
num_worlds = 100
count1=0
while count < num_worlds:
    nomearquivo="mapa"
    for i in range(h):
        print("")
        world+="\n"
        for j in range(w):
            if i == h/2 and j == w/2:
               print(pacman, end="")
               world+=pacman
            elif int(matrix[i][j]==1):
                #gerando números aleatório entre 1 e 9 (inclusivo)
                r = random.randint(1,25)
                #toda vez que o número aleatório
                if r == 1 and count1<5:
                    print(pill, end="")
                    world+=pill
                    count1+=1
                elif r == 25 and count1<5:
                    print(pill, end="")
                    world+=pill
                    count1+=1
                elif r == 0:
                    print(wall, end="")
                    world+=wall
                else:
                    if r < 3:
                        print(wall, end="")
                        world+=wall
                    else:
                        print(space, end="")
                        world+=space
            else:
                print(wall,end="")
                world+=wall    
    count+=1
    caminho_base = os.path.dirname(os.path.abspath(__file__))
    nomearquivo = nomearquivo+str(count)            

    caminho_arquivo = f"{caminho_base}/pacai/core/layouts/{nomearquivo}.lay"

    print(world)
    with open(caminho_arquivo, "w") as arquivo:
        arquivo.write(world) 
    world =""    
    count1=0
    print("\n")
    time.sleep(1)
    os.system('clear')
    print("\n")

