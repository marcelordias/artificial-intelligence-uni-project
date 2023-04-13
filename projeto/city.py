# Description: This class represents a city
from travel import Travel
from config import Config
class City:
    # Constructor of the class City
    def __init__(self, name):
        self.name = name # Name of the city
        self.neighbors = [] # List of neighbors
        self.n_neighbors = 0 # Number of neighbors
        self.straight_line: Travel = Travel(None, 0) # Straight line to one City

    # This method pushes a neighbor to the list of neighbors
    def push(self, city, cost):
        self.neighbors.append(Travel(city, cost)) # Adds the neighbor to the list of neighbors
        self.n_neighbors += 1 # Increments the number of neighbors
    # This method adds a neighbor to the list of neighbors and vice-versa (bidirectional)
    def add_neighbor(self, city, cost):
        self.push(city, cost) # Adds the neighbor to the list of neighbors
        print('Cidade {} adicionada como vizinha de {}'.format(city.name, self.name)) if Config.DEBUG else None # Prints the message if the program is in testing mode
        city.push(self, cost) # Adds the city to the list of neighbors of the neighbor
        print('Cidade {} adicionada como vizinha de {}'.format(self.name, city.name)) if Config.DEBUG else None # Prints the message if the program is in testing mode

    # This method adds a straight line to the city
    def add_straight_line(self, city, cost):
        self.straight_line = Travel(city, cost) # Adds the straight line to the city
        print('Cidade {} adicionada como linha reta de {}'.format(city.name, self.name)) if Config.DEBUG else None # Prints the message if the program is in testing mode