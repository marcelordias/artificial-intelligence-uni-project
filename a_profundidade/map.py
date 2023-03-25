import os, io
from city import City
from travel import Travel

class Map:
    def __init__(self):
        path = os.path.abspath("a_profundidade/storage/cidades.txt")
        cities_txt = io.open(path, mode="r", encoding="utf-8")
        self.cities = []
        for line in cities_txt:
            line = line.split(',')
            self.cities.append(self.find_city(line[0]) or City(line[0]))
            for i in range(1, len(line), 2):
                neighbor = self.find_city(line[i]) or City(line[i])
                self.cities[-1].add_neighbor(neighbor, int(line[i+1]))
        cities_txt.close()

    def get_all_neighbors(self, neighbors, level=1, visited=[]):
        for neighbor in neighbors:
            if neighbor.city is None:
                return
            if neighbor.city not in visited:
                for i in range(level):
                    print(' ', end='')
                print('Vizinho {}: {}, Cost: {}, Nº de vizinhos: {}'.format(
                    level, neighbor.city.name, neighbor.cost, neighbor.city.n_neighbors))
                visited.append(neighbor.city)
                self.get_all_neighbors(neighbor.city.neighbors, level+1)

    def get_all_cities(self):
        if self.cities:
            for city in self.cities:
                print('Cidade: {}, Nº de vizinhos: {}'.format(
                    city.name, city.n_neighbors))
                self.get_all_neighbors(city.neighbors)

    def find_city_neighborhood(self, neighbors, name, visited=[]):
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
                return self.find_city_neighborhood(city.neighbors, name)

    def find_path_to_destiny(self, city, destiny, path_to_destiny, visited):
        for neighbor in city.neighbors:
            if neighbor.city is None:
                return
            if neighbor.city not in visited:
                visited.append(neighbor.city)
                path_to_destiny.append(Travel(neighbor.city, neighbor.cost))
                if neighbor.city.name == destiny:
                    return path_to_destiny
                return self.find_path_to_destiny(neighbor.city, destiny, path_to_destiny, visited)
            else:
                continue
        return path_to_destiny

    def find_path(self, origin, destiny):
        origin_city = self.find_city(origin)
        if origin_city is None:
            return
        path_to_destiny = []
        path_to_destiny.append(Travel(origin_city, 0))
        visited = []
        visited.append(origin_city)
        return self.find_path_to_destiny(origin_city, destiny, path_to_destiny, visited)
