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
        if debug:
            print('>> De ' + G + source.name + W + ' para ' + G + destination.name + W + ', usando o algoritmo ' + P + 'Em profundidade primeiro' + W + ', as iterações são: ')
        path = self.recursive_get_dfs_path(source, destination, debug=True)
        if debug:
            path.print_path('Em profundidade primeiro')
        return path

    def recursive_get_dfs_path(self, source, destination, path=None, visited=None, cost=0, costs=None, debug=False):
        # Set empty arrays
        if path == None:
            path = []
        if visited == None:
            visited = []
        if costs == None:
            costs = []

        if source == destination:  # Check if the source city is the same as destination city
            return Path(path, cost)
        visited.append(source)  # Add the source to the visited cities list

        for neighbor in source.neighbors:  # Loop over each source neighbor
            if neighbor.city not in visited:  # Process only not yet visited cities
                if debug:
                    print('\t>> De ' + G + source.name +
                          W + ' para ' + G + neighbor.city.name + W)
                # Add it to the path list
                path.append(Neighbor(neighbor.city, neighbor.cost, source))
                cost += neighbor.cost  # Increment the cost with the cost from source to neighbor
                # Add to costs list (useful to get the total cost)
                costs.append(cost)

                if neighbor.city == destination:  # Check if the destination was found
                    return Path(path, costs[-1])

                self.recursive_get_dfs_path(  # Recursive function call if the destination was not found
                    neighbor.city, destination, path, visited, cost, costs, debug=debug)
                if path[-1].city == destination: # When destination was found, check if the last city in path list is the destination
                    return Path(path, costs[-1])
                removed = path.pop() # If not, remove the last city from path list
                if debug:
                    print('\t>> A ' + R + 'sair' + W + ' de ' + G + removed.city.name + W + ', sem cidades novas por visitar')
                cost -= removed.cost # Remove the cost associated to the removed city
        return Path(path, costs[-1])

    # Uniform-cost search
    def get_ucs_path(self, source, destination, debug=False):
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
            print()
            for neighbor in city.neighbors:
                if neighbor.city not in visited:
                    if debug:
                        print('>> A processar de ' + G + city.name + W + ' para ' + G + neighbor.city.name +
                              W + ', o custo total é de ' + O + str(cost + neighbor.cost) + W)
                    explored_nodes.append(
                        (cost + neighbor.cost, neighbor.city, path + [Neighbor(neighbor.city, neighbor.cost, city)]))

    # Greedy search
    def get_greedy_path(self, source, destination, debug=False):
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
            print()
            for neighbor in city.neighbors:
                if neighbor.city not in visited:
                    cost = neighbor.city.straight_neighbor.cost
                    if debug:
                        print('>> A processar de ' + G + city.name + W + ' para ' + G + neighbor.city.name + W + ', o custo é de ' + O + str(neighbor.cost) + W + ' + ' + O + str(city.straight_neighbor.cost) +
                              W + ' = ' + O + str(neighbor.cost + city.straight_neighbor.cost) + W + ' de ' + G + city.name + W + ' até ' + G + neighbor.city.straight_neighbor.city.name + W)
                        print(
                            "Esta formatação deve ir para o A+, o sofrega não olha para o caminho local!")
                    explored_nodes.append(
                        (cost, neighbor.city, path + [Neighbor(neighbor.city, neighbor.cost, city)], total_cost + neighbor.cost))

    # A* search
    def get_a_star_path(self, source, destination, debug=False):
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
            print()
            for neighbor in city.neighbors:
                if neighbor.city not in visited:
                    if debug:
                        print('>> A processar de ' + G + city.name + W + ' para ' + G + neighbor.city.name + W + ', o custo é de ' + O + str(neighbor.cost) + W + ' + ' + O + str(city.straight_neighbor.cost) +
                              W + ' de ' + G + city.name + W + ' até ' + G + neighbor.city.straight_neighbor.city.name + W + ' = ' + O + str(neighbor.cost + city.straight_neighbor.cost) + W)
                        #print('>> A processar de ' + G + city.name + W + ' para ' + G + neighbor.city.name + W + ', o custo total é de ' + O + str(cost + neighbor.cost) + W)
                        #print('>> A processar de ' + G + city.name + W + ' para ' + G + neighbor.city.name + W + ', o custo é de ' + O + str(neighbor.cost) + W + ' + ' + O + str(cost) + W +' de ' + G + neighbor.city.straight_neighbor.city.name + W + ')')
                    cost = neighbor.city.straight_neighbor.cost + neighbor.cost + total_cost
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
