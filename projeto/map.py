# Description: This class represents the map of the cities and the graph of the cities
import os, io
from city import City
from travel import Travel
from colorama import Fore
from custom_exeptions import CityNotFound, PathNotFound, OriginAndDestinyAreTheSame
class Map:
    # Constructor of the class Map
    def __init__(self): 
        path = os.path.abspath("storage/cidades.txt") # Gets the path of the file cidades.txt in the storage folder
        cities_txt = io.open(path, mode="r", encoding="utf-8") # Opens the file cidades.txt in the storage folder in read mode with utf-8 encoding
        self.cities = [] # List of cities
        for line in cities_txt: # Iterates over the lines of the file cidades.txt
            line = line.split(',') # Splits the line by the comma
            self.cities.append(self.find_city(line[0]) or City(line[0])) # Adds the city to the list of cities if it is not already in the list of cities or finds the city in the list of cities
            for i in range(1, len(line), 2): # Iterates over the neighbors of the city
                neighbor = self.find_city(line[i]) or City(line[i]) # Finds the neighbor in the list of cities or creates a new city if it is not in the list of cities yet
                self.cities[-1].add_neighbor(neighbor, int(line[i+1])) # Adds the neighbor to the list of neighbors of the city and vice-versa (bidirectional)
        cities_txt.close() # Closes the file cidades.txt
        
        path = os.path.abspath("storage/linhas_retas.txt") # Gets the path of the file linhas_retas.txt in the storage folder
        straight_lines_txt = io.open(path, mode="r", encoding="utf-8") # Opens the file linhas_retas.txt in the storage folder in read mode with utf-8 encoding
        for line in straight_lines_txt: # Iterates over the lines of the file linhas_retas.txt
            line = line.split(',') # Splits the line by the comma
            city = self.find_city(line[0]) # Finds the city in the list of cities
            city.add_straight_line(self.find_city(line[1]), int(line[2])) # Adds the straight line to the city
        straight_lines_txt.close() # Closes the file linhas_retas.txt

    # Prints the cities and the neighbors of the cities in the map in a tree-like structure (recursive)
    def print_all_neighbors(self, neighbors, visited, level=1):
        for neighbor in neighbors: # Iterates over the neighbors of the city
            if neighbor.city is None: # If the neighbor is None, do not print it
                return None # Returns None to the caller function (print_all_neighbors)
            if neighbor.city not in visited: # If the neighbor is not in the list of visited cities, print it
                for i in range(level): # Prints the level of the neighbor
                    print(' ', end='') # Prints a space
                print('Vizinho {}: {}, Cost: {}, Nº de vizinhos: {}'.format(level, neighbor.city.name, neighbor.cost, neighbor.city.n_neighbors)) # Prints the neighbor
                visited.append(neighbor.city) # Adds the neighbor to the list of visited cities
                self.print_all_neighbors(neighbor.city.neighbors, visited, level+1) # Calls the function print_all_neighbors recursively with the neighbors of the neighbor as the neighbors of the city

    # Prints the cities and the neighbors of the cities in the map in a tree-like structure (recursive)
    def print_all_cities(self): 
        if self.cities: # If the list of cities is not empty
            for city in self.cities: # Iterates over the cities in the list of cities
                print('Cidade: {}, Nº de vizinhos: {}'.format(city.name, city.n_neighbors)) # Prints the city and the number of neighbors of the city
                self.print_all_neighbors(city.neighbors,[]) # Calls the function print_all_neighbors with the neighbors of the city as the neighbors of the city

    # Finds the city in the list of cities (recursive)
    def find_city_neighborhood(self, neighbors, name, visited):
        for neighbor in neighbors: # Iterates over the neighbors of the city
            if neighbor.city not in visited: # If the neighbor is not in the list of visited cities
                if neighbor.city.name == name: # If the name of the neighbor is the same as the name of the city to be found
                    return neighbor.city # Returns the neighbor to the caller function (find_city)
                visited.append(neighbor.city) # Adds the neighbor to the list of visited cities
                found = self.find_city_neighborhood(neighbor.city.neighbors, name, visited) # Calls the function find_city_neighborhood recursively with the neighbors of the neighbor as the neighbors of the city
                if found: # If the city was found
                    return found # Returns the city to the caller function (find_city)

    # Finds the city in the list of cities
    def find_city(self, name):
        if self.cities: # If the list of cities is not empty
            for city in self.cities: # Iterates over the cities in the list of cities
                if city.name == name: # If the name of the city is the same as the name of the city to be found
                    return city # Returns the city
                found = self.find_city_neighborhood(city.neighbors, name, []) # Calls the function find_city_neighborhood with the neighbors of the city as the neighbors of the city
                if found: # If the city was found
                    return found # Returns the city

    # Finds the path to the destiny city using depth-first search (recursive)
    def find_path_to_destiny_depth_first_search(self, origin_city, destiny_city, path_to_destiny, visited_path):
        visited_path.append(origin_city) # Adds the city to the list of visited cities
        for neighbor in origin_city.neighbors: # Iterates over the neighbors of the city
            if neighbor.city not in visited_path: # If the neighbor is not in the list of visited cities
                path_to_destiny.append(Travel(neighbor.city, neighbor.cost + path_to_destiny[-1].cost)) # Adds the neighbor to the path to the destiny city
                if neighbor.city.name == destiny_city: # If the neighbor is the destiny city
                    return path_to_destiny # Returns the path to the destiny city
                self.find_path_to_destiny_depth_first_search(neighbor.city, destiny_city, path_to_destiny, visited_path) # Calls the function find_path_to_destiny_depth_first_search recursively with the neighbor as the city
                if path_to_destiny[-1].city.name == destiny_city: # If the last city in the path to the destiny city is the destiny city
                    return path_to_destiny # Returns the path to the destiny city
                path_to_destiny.pop() # Removes the last city in the path to the destiny city
        return path_to_destiny # Returns the path to the destiny city
    
    # Finds the path to the destiny city using uniform-cost search search (recursive) (brute force)
    def find_path_to_destiny_uniform_cost_search_legacy(self, origin_city, destiny_city, path_to_destiny, cost, visited_path):
        visited_path.append(origin_city) # Adds the city to the list of visited cities
        if origin_city.name == destiny_city: # If the city is the destiny city
            return path_to_destiny # Returns the path to the destiny city
        possible_paths = [] # Creates a list of possible paths to the destiny city
        for neighbor in origin_city.neighbors: # Iterates over the neighbors of the city
            if neighbor.city not in visited_path: # If the neighbor is not in the list of visited cities
                path_to_destiny.append(Travel(neighbor.city, cost + neighbor.cost)) # Adds the neighbor to the path to the destiny city
                new_path = self.find_path_to_destiny_uniform_cost_search_legacy(neighbor.city, destiny_city, path_to_destiny.copy(), cost + neighbor.cost, visited_path.copy()) # Calls the function find_path_to_destiny_uniform_cost_search_legacy recursively with the neighbor as the city
                if new_path: # If the path to the destiny city was found
                    possible_paths.append(new_path) # Adds the path to the list of possible paths to the destiny city
                path_to_destiny.pop() # Removes the last city in the path to the destiny city
        if possible_paths: # If there are possible paths to the destiny city
            return min(possible_paths, key=lambda x: x[-1].cost) # Returns the path with the lowest cost
        return None # Returns None
    
    # Finds the path to the destiny city using uniform-cost search (interactive) (optimized)
    def find_path_to_destiny_uniform_cost_search_optimized(self, path_to_destiny, origin_city, destiny_city):
        current_path = [(0, origin_city, path_to_destiny)] # Creates a list of current paths to the destiny city
        visited_path = [] # Creates a list of visited cities

        while current_path: # While there are current paths to the destiny city to be explored
            current_path.sort(key=lambda x: x[0]) # Sorts the list of current paths to the destiny city by the cost of the path (ascending order)
            cost, city, path_to_destiny = current_path.pop(0) # Removes the first path in the list of current paths to the destiny city and assigns the cost, city and path to the destiny city to the variables cost, city and path_to_destiny
            
            if city.name == destiny_city: # If the city is the destiny city
                return path_to_destiny # Returns the path to the destiny city
            
            visited_path.append(city) # Adds the city to the list of visited cities

            for neighbor in city.neighbors: # Iterates over the neighbors of the city
                if neighbor.city not in visited_path: # If the neighbor is not in the list of visited cities
                    new_cost = cost + neighbor.cost # Calculates the new cost
                    current_path.append((new_cost, neighbor.city, path_to_destiny + [Travel(neighbor.city, new_cost)])) # Adds the neighbor to the list of current paths to the destiny city 
        return None
    
    # Finds the path to the destiny city using greedy-search (interactive)
    def find_path_to_destiny_greedy_search(self, path_to_destiny, origin_city, destiny_city):
        current_path = [(0, origin_city, path_to_destiny)] # Creates a list of current paths to the destiny city
        visited_path = [] # Creates a list of visited cities

        while current_path: # While there are current paths to the destiny city to be explored
            current_path.sort(key=lambda x: x[0]) # Sorts the list of current paths to the destiny city by the cost of the path (ascending order)
            cost, city, path_to_destiny = current_path.pop(0) # Removes the first path in the list of current paths to the destiny city and assigns the cost, city and path to the destiny city to the variables cost, city and path_to_destiny
            
            if city.name == destiny_city: # If the city is the destiny city
                return path_to_destiny # Returns the path to the destiny city
            
            visited_path.append(city) # Adds the city to the list of visited cities
            
            for neighbor in city.neighbors: # Iterates over the neighbors of the city
                if neighbor.city not in visited_path: # If the neighbor is not in the list of visited cities
                    distance_to_destiny = neighbor.city.straight_line.cost # Get the distance to the destiny city from the neighbor
                    previous_cost = path_to_destiny[-1].cost # Get the cost of the previous city in the path to the destiny city
                    current_cost = neighbor.cost
                    current_path.append((distance_to_destiny, neighbor.city, path_to_destiny + [Travel(neighbor.city, current_cost + previous_cost)])) # Adds the neighbor to the list of current paths to the destiny city
        return None

    # Finds the path to the destiny city using A* search (interactive)
    def find_path_to_destiny_a_star_search(self, path_to_destiny, origin_city, destiny_city):
        current_path = [(0, origin_city, path_to_destiny)] # Creates a list of current paths to the destiny city
        visited_path = [] # Creates a list of visited cities

        while current_path: # While there are current paths to the destiny city to be explored
            current_path.sort(key=lambda x: x[0]) # Sorts the list of current paths to the destiny city by the cost of the path (ascending order)
            _, city, path_to_destiny = current_path.pop(0) # Removes the first path in the list of current paths to the destiny city and assigns the cost, city and path to the destiny city to the variables cost, city and path_to_destiny
            
            if city.name == destiny_city: # If the city is the destiny city
                return path_to_destiny # Returns the path to the destiny city
            
            visited_path.append(city) # Adds the city to the list of visited cities
            
            for neighbor in city.neighbors: # Iterates over the neighbors of the city
                if neighbor.city not in visited_path: # If the neighbor is not in the list of visited cities
                    distance_to_destiny = neighbor.city.straight_line.cost # Get the distance to the destiny city from the neighbor
                    previous_cost = path_to_destiny[-1].cost # Get the cost of the previous city in the path to the destiny city
                    current_cost = neighbor.cost # Get the cost of the neighbor
                    current_path.append((previous_cost + current_cost + distance_to_destiny, neighbor.city, path_to_destiny + [Travel(neighbor.city, current_cost + previous_cost)])) # Adds the neighbor to the list of current paths to the destiny city
        return None # Returns None
    
    # Find the path using the informed search algorithm 
    def find_path(self, origin_city_name, destiny_city_name, option):
        if origin_city_name == destiny_city_name: # If the origin city is the same as the destiny city
            raise OriginAndDestinyAreTheSame("Cidade de origem e destino são iguais") # Raises an exception

        origin_city = self.find_city(origin_city_name) # Finds the origin city
        if origin_city is None: # If the origin city is not found
            raise CityNotFound("Cidade de origem não encontrada") # Raises an exception
        if self.find_city(destiny_city_name) is None: # If the destiny city is not found
            raise CityNotFound("Cidade de destino não encontrada") # Raises an exception
        
        path_to_destiny = [] # Creates a list of paths to the destiny city
        visited = [] # Creates a list of visited cities
        
        path_to_destiny.append(Travel(origin_city, 0)) # Adds the origin city to the list of paths to the destiny city
        if option == '1': # Depth-first search
            path_to_destiny = self.find_path_to_destiny_depth_first_search(origin_city, destiny_city_name, path_to_destiny, visited)
        elif option == '2': # Uniform-cost search (legacy)
            path_to_destiny = self.find_path_to_destiny_uniform_cost_search_legacy(origin_city, destiny_city_name, path_to_destiny, 0, visited)
        elif option == '3': # Uniform-cost search (optimized)
            path_to_destiny = self.find_path_to_destiny_uniform_cost_search_optimized(path_to_destiny,origin_city, destiny_city_name)
        elif option == '4': # Greedy search
            path_to_destiny = self.find_path_to_destiny_greedy_search(path_to_destiny,origin_city, destiny_city_name)
        elif option == '5': # A* search
            path_to_destiny = self.find_path_to_destiny_a_star_search(path_to_destiny,origin_city, destiny_city_name)
        return path_to_destiny # Returns the path to the destiny city
    
    # Prints the path to the destiny city
    def print_path(self, path, algorithm_name): # Prints the path to the destiny city
        if path: # If the path is not empty
            print() # Prints a blank line
            print(f'Algoritmo: {Fore.MAGENTA}{algorithm_name}{Fore.RESET}') # Prints the name of the algorithm in green
            print() # Prints a blank line
            for i in range(len(path)): # Iterates over the path
                if i == 0: # If it is the first city in the path
                    print(f'{Fore.GREEN}{path[i].city.name}{Fore.RESET}', end='') # Prints the name of the city in green
                elif i < len(path) - 1:
                    print(f' -({Fore.RED}{path[i].cost - path[i-1].cost}{Fore.RESET})-> {Fore.YELLOW}{path[i].city.name}{Fore.RESET}', end='') # Prints the name of the city in yellow and the cost of the path in red
                else:
                    print(f' -({Fore.RED}{path[i].cost - path[i-1].cost}{Fore.RESET})-> {Fore.CYAN}{path[i].city.name}{Fore.RESET}', end='') # Prints the name of the city in cyan and the cost of the path in red
            print(f'\nValor total: {Fore.RED}{path[-1].cost}{Fore.RESET}') # Prints the total cost of the path in red
        else: # If the path is empty
            raise PathNotFound("Caminho não encontrado") # Raises an exception