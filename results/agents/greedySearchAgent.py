from agents.base import BaseAgent

class GreedySearchAgent(BaseAgent):
    def __init__(self, file_path):
        super().__init__(file_path)