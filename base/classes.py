# Terminal text colors
W = '\033[0m'  # White
R = '\033[31m'  # Red
G = '\033[32m'  # Green
O = '\033[33m'  # Orange
P = '\033[35m'  # Purple


class Map:
    def __init__(self, name):
        self.cities = []
        self.name = name

    def add_city(self, city):
        self.cities.append(city)

    def get_city(self, name):
        for city in self.cities:
            if city.name.lower() == name.lower():
                return city

    def print_cities(self):
        print('\n>> ' + P + self.name + W + ' tem ' + O +
              str(len(self.cities)) + W + ' cidade(s):')
        for city in self.cities:
            print('\t>> ' + G + city.name + W)
        print('')

    # Depth-first search
    def get_dfs_path(self, source, destination, debug=False):
        path = self.recursive_get_dfs_path(source, destination)
        if debug:
            path.print_path('Em profundidade primeiro')
        return path

    def recursive_get_dfs_path(self, source, destination, path=[], visited=[], cost=0, costs=[]):
        if source == destination:
            return Path(path, cost)
        visited.append(source)
        for neighbor in source.neighbors:
            if neighbor.city not in visited:
                path.append(Neighbor(neighbor.city, neighbor.cost, source))
                cost += neighbor.cost
                # Lista para armazenar os custos calculados ao longo do percurso.
                costs.append(cost)
                if neighbor.city == destination:
                    return Path(path, costs[-1])
                self.recursive_get_dfs_path(
                    neighbor.city, destination, path, visited, cost)
                if path[-1].city == destination:
                    return Path(path, costs[-1])
                removed = path.pop()
                cost -= removed.cost

    # Uniform-cost search
    def ucs_get_path(self, source, destination, debug=False):
        explored_nodes = [(0, source, [])]
        visited = []
        while explored_nodes:
            explored_nodes.sort(key=lambda x: x[0])
            cost, city, path = explored_nodes.pop(0)
            if city == destination:
                path = Path(path, cost)
                if debug:
                    path.print_path('Custo uniforme')
                return path
            if city not in visited:
                visited.append(city)
            for neighbor in city.neighbors:
                if neighbor.city not in visited:
                    explored_nodes.append(
                        (cost + neighbor.cost, neighbor.city, path + [Neighbor(neighbor.city, neighbor.cost, city)]))

    # Greedy search
    def greedy_get_path(self, source, destination, debug=False):
        explored_nodes = [(0, source, [], 0)]
        visited = []

        while explored_nodes:
            explored_nodes.sort(key=lambda x: x[0])
            cost, city, path, total_cost = explored_nodes.pop(0)
            if city == destination:
                path = Path(path, total_cost)
                if debug:
                    path.print_path('Procura sôfrega')
                return path
            if city not in visited:
                visited.append(city)
            for neighbor in city.neighbors:
                if neighbor.city not in visited:
                    cost = neighbor.city.straight_neighbor.cost
                    explored_nodes.append(
                        (cost, neighbor.city, path + [Neighbor(neighbor.city, neighbor.cost, city)], total_cost + neighbor.cost))

    # A* search
    def a_star_get_path(self, source, destination, debug=False):
        explored_nodes = [(0, source, [], 0)]
        visited = []

        while explored_nodes:
            explored_nodes.sort(key=lambda x: x[0])
            cost, city, path, total_cost = explored_nodes.pop(0)
            if city == destination:
                path = Path(path, total_cost)
                if debug:
                    path.print_path('A*')
                return path
            if city not in visited:
                visited.append(city)
            for neighbor in city.neighbors:
                if neighbor.city not in visited:
                    cost = neighbor.city.straight_neighbor.cost + neighbor.cost
                    explored_nodes.append(
                        (cost, neighbor.city, path + [Neighbor(neighbor.city, neighbor.cost, city)], total_cost + neighbor.cost))


class Neighbor:
    def __init__(self, city, cost, source=None):
        self.city = city
        self.cost = cost
        self.source = source


class City:
    def __init__(self, name):
        self.name = name
        self.neighbors = []
        self.straight_neighbor = None

    def add_neighbor(self, city, cost):
        if self.get_neighbor(city) == None:
            neighbor = Neighbor(city, cost)
            self.neighbors.append(neighbor)
        if city.get_neighbor(self) == None:
            neighbor = Neighbor(self, cost)
            city.neighbors.append(neighbor)

    # Returns the given city, or None if the given city is not a neighbor.
    def get_neighbor(self, city):
        for neighbor in self.neighbors:
            if neighbor.city == city:
                return neighbor

    def add_straight_neighbor(self, city, cost):
        self.straight_neighbor = Neighbor(city, cost, self)

    def print_neighbors(self):
        print('\n>> ' + G + self.name + W + ' tem ' + O +
              str(len(self.neighbors)) + W + ' vizinho(s):')
        for neighbor in self.neighbors:
            print('\t>> ' + G + neighbor.city.name + W +
                  ', com um custo de ' + O + str(neighbor.cost) + W)
        print('')


class Path:
    def __init__(self, path, cost):
        self.path = path
        self.cost = cost

    def print_path(self, algorithm):
        if len(self.path) > 0:
            print('\n>> De ' + G + self.path[0].source.name + W + ' para ' + G + self.path[-1].city.name + W +
                  ', usando o algoritmo ' + P + algorithm + W + ', o custo total é de ' + O + str(self.cost) + W + ':')
            for i in self.path:
                print('\t>> De ' + G + i.source.name + W + ' para ' + G +
                      i.city.name + W + ', o custo é de ' + O + str(i.cost) + W)
            print('')
        else:
            print(
                '\n>> ' + R + 'Não existe nenhum caminho entre as cidades de origem e de destino\n' + W)
