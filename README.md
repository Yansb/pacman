## Pacman

### Para rodar com o agente de busca A*

```bash
python3 -m pacai.bin.pacman --fps=20 -p AStarFoodSearchAgent -l pacman_map_0
```

### Para rodar com o agente de busca gulosa

```bash
python3 -m pacai.bin.pacman --fps=20 -p GreedyAgent -l pacman_map_0
```

### Para rodar com o agente de busca com os outros

ps: lembra de trocar o algoritmo de busca dentro da classe `ClosestDotSearchAgent` no searchAgents.py

```bash
python3 -m pacai.bin.pacman --fps=20 -p ClosestDotSearchAgent -l pacman_map_1
```
