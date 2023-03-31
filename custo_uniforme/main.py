def uniform_cost_search(start_city, goal_city, graph):
    frontier = [(0, start_city, [])]  # list with (cost, city, path) tuples
    visited = set()

    while frontier:
        frontier.sort()  # sort by cost
        cost, city, path = frontier.pop(0)
        if city == goal_city:
            return path + [city]
        visited.add(city)
        for neighbor, neighbor_cost in graph[city].items():
            new_cost = cost + neighbor_cost
            if neighbor not in visited:
                frontier.append((new_cost, neighbor, path + [city]))
    return None

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
    'Portalegre': {"Évora":131,"Castelo Branco":80},
    'Santarém': {"Lisboa":78,"Évora":117,"Leiria":70},
    'Vila Real': {'Viseu': 110, 'Braga': 106, 'Bragança': 137, 'Guarda': 157},
    'Viana do Castelo': {'Porto': 71, 'Braga': 48},
    'Viseu': {'Aveiro': 95, 'Guarda': 85, 'Vila Real': 110, 'Coimbra': 96}
}

path = uniform_cost_search(start_city, goal_city, graph)
print(path)