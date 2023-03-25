class City:
    def init(self, name):
        self.neighbors = []
        self.name = name

    def add_neighbor(self, city, cost):
        self.neighbors.append({'city':city, 'cost':cost})

    def get_neighbors(self):
        return self.neighbors

    def get_neighbor(self, city): # Returns the neighbor, or None if the given city is not a neighbor.
        for element in self.neighbors:
            if element['city'] == city:
                return element['city']

aveiro = City('Aveiro')
viseu = City('Viseu')
aveiro.add_neighbor(viseu, 1)
aveiro.get_neighbor(viseu)

## Nota: falta fazer a parte contraria, se aveiro tem viseu como vizinho, viseu tbm deve ter aveiro como vizinho