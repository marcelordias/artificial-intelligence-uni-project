start_city = 'Bragança'
goal_city = 'Évora'


graph = {
    'Aveiro': {'Porto': 68, 'Viseu': 95, 'Coimbra': 68, 'Leiria': 115},
    'Braga': {'Viana do Castelo': 48, 'Vila Real': 106, 'Porto': 53},
    'Bragança': {'Vila Real': 137, 'Guarda': 202},
    'Beja': {'Évora': 78, 'Faro': 152, 'Setúbal': 142},
    'Castelo Branco': {'Coimbra': 159, 'Guarda': 106, 'Portalegre': 80, 'Évora': 203},
    'Coimbra': {'Viseu': 96, 'Leiria': 67, 'Aveiro': 68, 'Castelo Branco': 159, 'Évora': 203},
    'Évora': {'Lisboa': 150, 'Santarém': 117, 'Portalegre': 131, 'Beja': 78, 'Castelo Branco': 203, 'Coimbra': 203},
    'Setúbal': {'Lisboa': 50, 'Beja': 142, 'Faro': 249, 'Santarém': 103},
    'Faro': {'Setúbal': 249, 'Lisboa': 299, 'Beja': 152},
    'Guarda': {'Vila Real': 157, 'Viseu': 85, 'Bragança': 202, 'Castelo Branco': 106},
    'Leiria': {'Lisboa': 129, 'Santarém': 70, 'Aveiro': 115, 'Coimbra': 67},
    'Lisboa': {'Santarém': 78, 'Setúbal': 50, 'Leiria': 129, 'Évora': 150, 'Faro': 299},
    'Porto': {'Viana do Castelo': 71, 'Braga': 53, 'Aveiro': 68},
    'Portalegre': {"Évora": 131, "Castelo Branco": 80},
    'Santarém': {"Lisboa": 78, "Évora": 117, "Leiria": 70},
    'Vila Real': {'Viseu': 110, 'Braga': 106, 'Bragança': 137, 'Guarda': 157},
    'Viana do Castelo': {'Porto': 71, 'Braga': 48},
    'Viseu': {'Aveiro': 95, 'Guarda': 85, 'Vila Real': 110, 'Coimbra': 96}
}


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
            
    def get_city_by_name(self, name):
        for city in self.cities:
            if city.name == name:
                return city

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
        print('>> From \'{}\' to \'{}\' path:'.format(
            path[0].source.name, path[-1].city.name))
        for i in path:
            print('\t>> From \'{}\' to \'{}\' has a cost of {}'.format(
                i.source.name, i.city.name, i.cost))
            path_cost += i.cost
        print('\t-----------')
        print('\t>> From \'{}\' to \'{}\' has a total cost of {}'.format(
            path[0].source.name, path[-1].city.name, path_cost))
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

    def uniform_cost_search(self, start_city, goal_city):
        source = start_city.name
        viz = ""
        cid = ""
        goal_cid = ""
        total_cost = 0
        frontier = [(0, source, [])]  # list with (cost, city, path) tuples
        visited = set()

        while frontier:
            frontier.sort()  # sort by cost
            cost, city, path = frontier.pop(0)
            print(">>>COST >>> ", cost)
            if isinstance(city, City):
                cid = city.name
            else:
                cid = city
            if isinstance(goal_city, City):
                goal_cid = goal_city.name
            else:
                goal_cid = goal_city
            if cid == goal_cid:
                return path + [cid]
            visited.add(cid)
            objeto = self.get_city_by_name(cid)
            
            for neighbor in objeto.get_neighbors():
                new_cost = cost + neighbor.cost
                if neighbor not in visited:
                    if isinstance(neighbor.city, City):
                        viz = neighbor.city.name
                    else:
                        viz = neighbor.city
                    if isinstance(city, City):
                        cid = city.name
                    else:
                        cid = city
                    total_cost += new_cost
                    frontier.append((new_cost, viz, path + [cid]))
        return None


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


portugal = Map('Portugal')

aveiro = City('Aveiro')
braga = City('Braga')
braganca = City('Bragança')
beja = City('Beja')
castelo = City('Castelo Branco')
coimbra = City('Coimbra')
evora = City('Évora')
faro = City('Faro')
guarda = City('Guarda')
leiria = City('Leiria')
lisboa = City('Lisboa')
porto = City('Porto')
vila = City('Vila Real')
viseu = City('Viseu')
viana = City('Viana do Castelo')
setubal = City('Setúbal')
portalegre = City('Portalegre')
santarem = City('Santarém')

portugal.add_city(aveiro)
portugal.add_city(braga)
portugal.add_city(braganca)
portugal.add_city(beja)
portugal.add_city(castelo)
portugal.add_city(coimbra)
portugal.add_city(evora)
portugal.add_city(faro)
portugal.add_city(guarda)
portugal.add_city(leiria)
portugal.add_city(lisboa)
portugal.add_city(porto)
portugal.add_city(vila)
portugal.add_city(viseu)
portugal.add_city(viana)
portugal.add_city(setubal)
portugal.add_city(portalegre)
portugal.add_city(santarem)

aveiro.add_neighbor(porto, 68)
aveiro.add_neighbor(viseu, 95)
aveiro.add_neighbor(coimbra, 68)
aveiro.add_neighbor(leiria, 115)

braga.add_neighbor(viana, 48)
braga.add_neighbor(vila, 106)
braga.add_neighbor(porto, 53)

braganca.add_neighbor(vila, 137)
braganca.add_neighbor(guarda, 202)

beja.add_neighbor(evora, 78)
beja.add_neighbor(faro, 152)
beja.add_neighbor(setubal, 142)

castelo.add_neighbor(coimbra, 159)
castelo.add_neighbor(guarda, 106)
castelo.add_neighbor(portalegre, 80)
castelo.add_neighbor(evora, 203)

coimbra.add_neighbor(viseu, 96)
coimbra.add_neighbor(leiria, 67)

evora.add_neighbor(lisboa, 150)
evora.add_neighbor(santarem, 117)
evora.add_neighbor(portalegre, 131)
evora.add_neighbor(setubal, 103)

faro.add_neighbor(setubal, 249)
faro.add_neighbor(lisboa, 299)

guarda.add_neighbor(vila, 157)
guarda.add_neighbor(viseu, 85)

leiria.add_neighbor(lisboa, 129)
leiria.add_neighbor(santarem, 70)

lisboa.add_neighbor(santarem, 78)
lisboa.add_neighbor(setubal, 50)

porto.add_neighbor(viana, 71)
porto.add_neighbor(vila, 116)
porto.add_neighbor(viseu, 133)

vila.add_neighbor(viseu, 110)

path = portugal.uniform_cost_search(lisboa, castelo)

print(path)
