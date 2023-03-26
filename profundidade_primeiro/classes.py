class Map:
    def __init__(self, name):
        self.cities = []
        self.name = name

    def add_city(self, city):
        self.cities.append(city)

    def get_cities(self):
        print('>> \'{}\' has {} cities:'.format(
            self.name, len(self.cities)))
        for city in self.cities:
            print('\t>> \'{}\''.format(
                city.name))

    def get_path(self, source, destination):
        path = []
        visited = []
        path_cost = 0
        if source == destination:
            print('>> You already are in \'{}\''.format(source.name))
            return path
        visited.append(source)
        path = self.recursive_get_path(
            source, destination, path, visited)
        print('>> From \'{}\' to \'{}\' path:'.format(path[0].source.name, path[-1].city.name))
        for i in path:
          print('\t>> From \'{}\' to \'{}\' has a cost of {}'.format(i.source.name, i.city.name, i.cost))
          path_cost += i.cost
        print('\t-----------')
        print('\t>> From \'{}\' to \'{}\' has a total cost of {}'.format(path[0].source.name, path[-1].city.name, path_cost))
        return path

    def recursive_get_path(self, source, destination, path, visited):
        if source == destination:
            return path
        visited.append(source)
        for neighbor in source.neighbors:
            if neighbor.city not in visited:
                path.append(Neighbor(neighbor.city, neighbor.cost, source))
                if neighbor.city == destination:
                    return path
                self.recursive_get_path(
                    neighbor.city, destination, path, visited)
                if path[-1].city == destination:
                    return path
                path.pop()
        return path


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
    def get_neighbor(self, city):
        for neighbor in self.neighbors:
            if neighbor.city == city:
                print('>> \'{}\' has \'{}\' as neighbor and has a cost of {}.'.format(
                    self.name, neighbor.city.name, neighbor.cost))
                return neighbor

    # Get a list of neighbors.
    def get_neighbors(self):
        print('>> \'{}\' has {} neighbor(s):'.format(
            self.name, len(self.neighbors)))
        for neighbor in self.neighbors:
            print('\t>> \'{}\' and has a cost of {}.'.format(
                neighbor.city.name, neighbor.cost))
        return self.neighbors
