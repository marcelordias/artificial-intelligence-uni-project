class Map:
    def __init__(self, name):
        self.cities = []
        self.name = name

    def add_city(self, city, debug=False):
        self.cities.append(city)
        if debug:
            print('>> \'{}\' added to \'{}\''.format(city.name, self.name))

    def get_cities(self, debug=False):
        if debug:
            print('>> \'{}\' has {} cities:'.format(
                self.name, len(self.cities)))
            for city in self.cities:
                print('\t>> \'{}\''.format(
                    city.name))
        return self.cities

    # Depth-first search
    def dfs_get_path(self, source, destination, debug=False):
        path = []
        visited = []
        visited.append(source)
        path = self.recursive_dfs_get_path(
            source, destination, path, visited)
        result = Path(path)
        result.set_path_cost()
        if debug:
            result.print_path('DFS')
        return result

    def recursive_dfs_get_path(self, source, destination, path, visited):
        if source == destination:
            return path
        visited.append(source)
        for neighbor in source.neighbors:
            if neighbor.city not in visited:
                path.append(Neighbor(neighbor.city, neighbor.cost, source))
                if neighbor.city == destination:
                    return path
                self.recursive_dfs_get_path(
                    neighbor.city, destination, path, visited)
                if path[-1].city == destination:
                    return path
                path.pop()
        return path

    # Uniform-cost search
    def ucs_get_path(self, source, destination, debug=False):
        neighbors = [(0, source, [])]
        visited = []

        while neighbors:
            neighbors.sort(key=lambda x: x[0])
            cost, city, path = neighbors.pop(0)
            if city == destination:
                path = Path(path, cost)
                if debug:
                    path.print_path('UCS')
                return path
            if city not in visited:
                visited.append(city)
            for neighbor in city.get_neighbors():
                if neighbor.city not in visited:
                    neighbors.append(
                        (cost + neighbor.cost, neighbor.city, path + [Neighbor(neighbor.city, neighbor.cost, city)]))


class Neighbor:
    def __init__(self, city, cost, source=None):
        self.city = city
        self.cost = cost
        self.source = source


class City:
    def __init__(self, name):
        self.neighbors = []
        self.name = name

    def add_neighbor(self, city, cost):
        if self.get_neighbor(city) == None:
            neighbor = Neighbor(city, cost)
            self.neighbors.append(neighbor)
        if city.get_neighbor(self) == None:
            neighbor = Neighbor(self, cost)
            city.neighbors.append(neighbor)

    # Returns the given city, or None if the given city is not a neighbor.
    def get_neighbor(self, city, debug=False):
        for neighbor in self.neighbors:
            if neighbor.city == city:
                if debug:
                    print('>> \'{}\' has \'{}\' as neighbor and has a cost of {}.'.format(
                        self.name, neighbor.city.name, neighbor.cost))
                return neighbor

    # Get a list of neighbors.
    def get_neighbors(self, debug=False):
        if debug:
            print('>> \'{}\' has {} neighbor(s):'.format(
                self.name, len(self.neighbors)))
            for neighbor in self.neighbors:
                print('\t>> \'{}\' and has a cost of {}.'.format(
                    neighbor.city.name, neighbor.cost))
        return self.neighbors


class Path:
    def __init__(self, path, cost=0):
        self.path = path
        self.cost = cost

    def print_path(self, algorithm):
        if len(self.path) > 0:
            print('>> From \'{}\' to \'{}\' path, using {} algorithm:'.format(
                self.path[0].source.name, self.path[-1].city.name, algorithm))
            for i in self.path:
                print('\t>> From \'{}\' to \'{}\' has a cost of {}'.format(
                    i.source.name, i.city.name, i.cost))
            print('\t-----------')
            print('\t>> From \'{}\' to \'{}\' has a total cost of {}'.format(
                self.path[0].source.name, self.path[-1].city.name, self.cost))
        else:
            print('>> There is no path to print')

    def set_path_cost(self):
        cost = 0
        for i in self.path:
            cost += i.cost
        self.cost = cost
