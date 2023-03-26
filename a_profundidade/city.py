from travel import Travel
from config import Config
class City:
    def __init__(self, name):
        self.name = name
        self.neighbors = []
        self.n_neighbors = 0

    def push(self, city, cost):
        self.neighbors.append(Travel(city, cost))
        self.n_neighbors += 1

    def add_neighbor(self, city, cost):
        self.push(city, cost)
        print('Cidade {} adicionada como vizinha de {}'.format(city.name, self.name)) if Config.TESTING else None
        city.push(self, cost)        
        print('Cidade {} adicionada como vizinha de {}'.format(self.name, city.name)) if Config.TESTING else None
