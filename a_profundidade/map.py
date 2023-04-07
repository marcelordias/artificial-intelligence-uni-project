import os, io
from city import City
from travel import Travel
from colorama import Fore
class Map:
    def __init__(self):
        # Loads the cities from the file and creates the graph
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
        # Loads the straight lines from the file
        path = os.path.abspath("a_profundidade/storage/linhas_retas.txt")
        straight_lines_txt = io.open(path, mode="r", encoding="utf-8")
        for line in straight_lines_txt:
            line = line.split(',')
            city = self.find_city(line[0])
            city.add_straight_line(self.find_city(line[1]), int(line[2]))
        straight_lines_txt.close()        

    def get_all_neighbors(self, neighbors, visited, level=1):
        for neighbor in neighbors:
            if neighbor.city is None:
                return
            if neighbor.city not in visited:
                for i in range(level):
                    print(' ', end='')
                print('Vizinho {}: {}, Cost: {}, Nº de vizinhos: {}'.format(
                    level, neighbor.city.name, neighbor.cost, neighbor.city.n_neighbors))
                visited.append(neighbor.city)
                self.get_all_neighbors(neighbor.city.neighbors, visited, level+1)

    def get_all_cities(self):
        if self.cities:
            for city in self.cities:
                print('Cidade: {}, Nº de vizinhos: {}'.format(
                    city.name, city.n_neighbors))
                self.get_all_neighbors(city.neighbors,[])

    def find_city_neighborhood(self, neighbors, name, visited):
        for neighbor in neighbors:
            if neighbor.city not in visited:
                if neighbor.city.name == name:
                    return neighbor.city
                visited.append(neighbor.city)
                found = self.find_city_neighborhood(neighbor.city.neighbors, name, visited)
                if found:
                    return found

    def find_city(self, name):
        if self.cities:
            for city in self.cities:
                if city.name == name:
                    return city
                found = self.find_city_neighborhood(city.neighbors, name, [])
                if found:
                    return found
                
    def find_path_to_destiny(self, city, destiny, path_to_destiny, visited):
        visited.append(city)
        for neighbor in city.neighbors:
            if neighbor.city not in visited:
                path_to_destiny.append(Travel(neighbor.city, neighbor.cost + path_to_destiny[-1].cost))
                if neighbor.city.name == destiny:
                    return path_to_destiny
                self.find_path_to_destiny(neighbor.city, destiny, path_to_destiny, visited)
                if path_to_destiny[-1].city.name == destiny:
                    return path_to_destiny
                path_to_destiny.pop()
        return path_to_destiny
    
    def find_path_to_destiny_uniform_cost_search_legacy(self, city, destiny, path, cost, visited):
        visited.append(city)
        if city.name == destiny:
            return path
        possible_paths = []
        for neighbor in city.neighbors:
            if neighbor.city not in visited:
                path.append(Travel(neighbor.city, cost + neighbor.cost))
                new_path = self.find_path_to_destiny_uniform_cost_search_legacy(neighbor.city, destiny, path.copy(), cost + neighbor.cost, visited.copy())
                if new_path:
                    possible_paths.append(new_path)
                path.pop()
        if possible_paths:
            return min(possible_paths, key=lambda x: x[-1].cost)
        return None
    
    def find_path_to_destiny_uniform_cost_search_optimized(self, path, start_city, goal_city):
        frontier = [(0, start_city, path)]
        visited = []

        while frontier:
            frontier.sort(key=lambda x: x[0])
            cost, city, path = frontier.pop(0)
            
            if city.name == goal_city:
                return path
            
            visited.append(city)

            for neighbor in city.neighbors:
                new_cost = cost + neighbor.cost
                if neighbor not in visited:
                    frontier.append((new_cost, neighbor.city, path + [Travel(neighbor.city, new_cost)]))
        return None
    
    def find_path_to_destiny_greedy_search(self, path, start_city, goal_city):
        frontier = [(0, start_city, path)]
        visited = []

        while frontier:
            cost, city, path = frontier.pop(0)
            
            if city.name == goal_city:
                return path
            
            visited.append(city)
            smaller_distance = float('inf')
            for neighbor in city.neighbors:
                new_cost = cost + neighbor.cost
                distance_to_destiny = neighbor.city.straight_line.cost
                if neighbor not in visited and distance_to_destiny < smaller_distance:
                    smaller_distance = distance_to_destiny
                    frontier.append((new_cost, neighbor.city, path + [Travel(neighbor.city, new_cost)]))
        return None

    def find_path_to_destiny_a_star_search(self, path, start_city, goal_city):
        frontier = [(0, start_city, path)]
        visited = []

        while frontier:
            frontier.sort(key=lambda x: x[0])
            cost, city, path = frontier.pop(0)
            
            if city.name == goal_city:
                return path
            
            visited.append(city)
            for neighbor in city.neighbors:
                new_cost = cost + neighbor.cost
                distance_to_destiny = neighbor.city.straight_line.cost
                previous_cost = path[-1].cost
                if neighbor not in visited:
                    frontier.append((new_cost + distance_to_destiny, neighbor.city, path + [Travel(neighbor.city, neighbor.cost + previous_cost)]))
        return None

    def find_path(self, origin, destiny, option):
        origin_city = self.find_city(origin)
        if origin_city is None:
            return
        path_to_destiny = []
        visited = []
        path_to_destiny.append(Travel(origin_city, 0))
        if option == '1': # Procura em profundidade
            path_to_destiny = self.find_path_to_destiny(origin_city, destiny, path_to_destiny, visited)
        elif option == '2': # Busca uniforme (legacy)
            path_to_destiny = self.find_path_to_destiny_uniform_cost_search_legacy(origin_city, destiny, path_to_destiny, 0, visited)
        elif option == '3': # Busca uniforme (otimizada)
            path_to_destiny = self.find_path_to_destiny_uniform_cost_search_optimized(path_to_destiny,origin_city, destiny)
        elif option == '4': # Busca sôfrega
            path_to_destiny = self.find_path_to_destiny_greedy_search(path_to_destiny,origin_city, destiny)
        elif option == '5': # Busca A*
            path_to_destiny = self.find_path_to_destiny_a_star_search(path_to_destiny,origin_city, destiny)
        else:
            return []
        return path_to_destiny
    
    def print_path(self, path):
        if path:
            print(f'De {Fore.GREEN}{path[0].city.name}{Fore.RESET} para {Fore.CYAN}{path[-1].city.name}{Fore.RESET} o custo total é de {Fore.RED}{path[-1].cost}{Fore.RESET} batatas.')
            for i in range(len(path)):
                if i == len(path) - 1:
                    print(path[i].city.name, end='')
                else:
                    print(path[i].city.name, end=' -> ')
        else:
            print('Não foi possível encontrar um caminho')

