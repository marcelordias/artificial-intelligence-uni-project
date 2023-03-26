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

    def find_path_custom(self, source, destination):
        path = []
        visited = []
        path.append(Neighbor(source, 0))
        visited.append(source)
        path = self.find_path_to_destiny(source, destination, path, visited)
        return path
        # if source == destination:
        #     print(">> Destination found.")
        #     # self.path.append(destination)
        #     for element in self.path:
        #         print(element.name)
        #     return True

        # else:
        #     if node not in self.cities_visited:
        #         self.cities_visited.append(node)
        #         # self.path.append(node)

        #         neighbors = node.get_neighbors()
        #         skip = True
        #         for neighbor in neighbors:
        #             if neighbor.city not in self.cities_visited:
        #                 skip = False

        #         if not skip:

        #             for neighbor in neighbors:
        #                 # self.path.append(neighbor)
        #                 # print(neighbor['city'].name)
        #                 if self.find_path(neighbor.city, destination):
        #                     return True
        #         else:
        #             # self.path.pop()
        #             print('>> All neighbors of {} have already been visited. The cost must be ignored.'.format(
        #                 node.name))

    def find_path_to_destiny_custom(self, source, destination, path, visited):
        if source == destination or source is None:
            return True
        visited.append(source)
        for neighbor in source.neighbors:
            if neighbor.city not in visited:
                path.append(Neighbor(neighbor.city, neighbor.cost))
                if neighbor.city.name == destination:
                    return path
                teste = self.find_path_to_destiny(
                    neighbor.city, destination, path, visited)
                if teste:
                    return path
                # if path[-1].city.name == destination:
                #     return path
                # path.pop
        return path

    # def find_path(self, origin, destiny):
    #     origin_city = self.find_city(origin)
    #     if origin_city is None:
    #         return
    #     path_to_destiny = []
    #     path_to_destiny.append(Neighbor(origin_city, 0))
    #     visited = []
    #     visited.append(origin_city)
    #     path_to_destiny = self.find_path_to_destiny(origin_city, destiny, path_to_destiny, visited)
        #     return path_to_destiny

    def find_path_to_destiny(self, city, destiny, path_to_destiny, visited):
        if city == destiny:
            return path_to_destiny
        visited.append(city)
        for neighbor in city.neighbors:
            if neighbor.city not in visited:
                path_to_destiny.append(Neighbor(neighbor.city, neighbor.cost))
                if neighbor.city == destiny:
                    return path_to_destiny
                path_to_destiny = self.find_path_to_destiny(
                    neighbor.city, destiny, path_to_destiny, visited)
                if path_to_destiny[-1].city == destiny:
                    return path_to_destiny
                path_to_destiny.pop()
        return path_to_destiny

    def find_path(self, origin, destiny):
        path_to_destiny = []
        path_to_destiny.append(Neighbor(origin, 0))
        visited = []
        visited.append(origin)
        path_to_destiny = self.find_path_to_destiny(
            origin, destiny, path_to_destiny, visited)
        return path_to_destiny

    def find_city_neighborhood(self, neighbors, name, visited):
        for neighbor in neighbors:
            if neighbor.city is None:
                return
            if neighbor.city.name == name:
                return neighbor.city
            if neighbor.city not in visited:
                visited.append(neighbor.city)
                return self.find_city_neighborhood(neighbor.city.neighbors, name, visited)

    def find_city(self, name):
        if self.cities:
            for city in self.cities:
                if city.name == name:
                    return city
                found = self.find_city_neighborhood(city.neighbors, name, [])
                if found:
                    return found


class Neighbor:
    def __init__(self, city, cost):
        self.city = city
        self.cost = cost


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
