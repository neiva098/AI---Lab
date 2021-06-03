# Exercicio 1 - Busca A*
# Christian Medeiros Cantarino - 201722040130 e Cristiano Neiva Abrantes - 201722040467
class City:
    def __init__(self, name, roads=[], distance_to_destination=0):
        self.name = name
        self.roads = roads
        self.distance_to_destinstion = distance_to_destination
        self.visited = False

    def get_nearby_cities(self):
        return [road.destination for road in self.roads]

    def get_nearby_cities_with_distance(self):
        return [(road.destination, road.distance) for road in self.roads]


class Road:
    def __init__(self, destination, distance=0):
        self.destination = destination
        self.distance = distance


class Path:
    def __init__(self, current_city_key, distance=0, path_cost=0, has_reached_destination=False, past_cities=[]):
        self.current_city_key = current_city_key
        self.path_cost = path_cost
        self.distance = distance
        self.has_reached_destination = has_reached_destination
        self.past_cities = past_cities

    def cost(self):
        return self.path_cost + self.distance

    def get_cities_path(self):
        if (len(self.past_cities) == 0):
            return [self.current_city_key]
        return self.past_cities + [self.current_city_key]


def cities_setup():
    return {
        'Arad': City('Arad', [Road('Zerind', 75), Road('Sibiu', 140),
                              Road('Timisoara', 118)], 366),
        'Bucareste': City('Bucareste', [Road('Fagaras', 211), Road('Pitesti', 101),
                                        Road('Giurgiu', 90), Road('Urziceni', 85)]),
        'Craiova': City('Craiova', [Road('Drobeta', 120), Road('Rumnicu Vilcea', 146),
                                    Road('Pitesti', 138)], 160),
        'Drobeta': City('Drobeta', [Road('Mehadia', 75), Road('Craiova', 120)], 242),
        'Eforie': City('Eforie', [Road('Hirsova', 161)], 161),
        'Fagaras': City('Fagaras', [Road('Sibiu', 99), Road('Bucareste', 211)], 176),
        'Giurgiu': City('Giurgiu', [Road('Bucareste', 90)], 77),
        'Hirisova': City('Hirisova', [Road('Urziceni', 98), Road('Eforie', 86)], 151),
        'Iasi': City('Iasi', [Road('Neamt', 87), Road('Vaslui', 92)], 226),
        'Lugoj': City('Lugoj', [Road('Timisoara', 111), Road('Mehadia', 70)], 244),
        'Mehadia': City('Mehadia', [Road('Lugoj', 70), Road('Drobeta', 75)], 241),
        'Neamt': City('Neamt', [Road('Iasi', 87)], 234),
        'Oradea': City('Oradea', [Road('Zerind', 71), Road('Sibiu', 151)], 380),
        'Pitesti': City('Pitesti', [Road('Rumnicu Vilcea', 97), Road('Bucareste', 101)], 100),
        'Rumnicu Vilcea': City('Rumnicu Vilcea', [Road('Sibiu', 80), Road('Craiova', 146),
                                                  Road('Pitesti', 97)], 193),
        'Sibiu': City('Sibiu', [Road('Arad', 140), Road('Rumnicu Vilcea', 80), Road('Fagaras', 99),
                                Road('Oradea', 151)], 253),
        'Timisoara': City('Timisoara', [Road('Arad', 118), Road('Lugoj', 111)], 329),
        'Urziceni': City('Urziceni', [Road('Bucareste', 85), Road('Vaslui', 142),
                                      Road('Hirisova', 98)], 80),
        'Vaslui': City('Vaslui', [Road('Iasi', 92), Road('Urziceni', 142)], 80),
        'Zerind': City('Zerind', [Road('Arad', 75), Road('Oradea', 71)], 374),
    }


def display_cities(cities):
    for key in cities.keys():
        city = cities[key]
        print('City: ' + city.name)
        print('Nearby: ' + str(city.get_nearby_cities_with_distance()))
        print('Distance to destination: ' + str(city.distance_to_destinstion))
        print('\n')


def get_path_cost(path):
    return path.cost()


def a_star_shortest_path(starting_city_key, destination_city_key, cities):
    # Seleciona a estrada inicial
    starting_city = cities[starting_city_key]
    current_path = Path(starting_city_key, starting_city.distance_to_destinstion, 0,
                        starting_city_key == destination_city_key)
    next_paths = []

    while not current_path.has_reached_destination:
        # Seleciona a cidade atual
        current_city = cities[current_path.current_city_key]
        current_city.visited = True

        # Adiciona as proximas estradas em cidades nao visitadas e organiza pelo custo
        next_paths.extend(
            Path(city, cities[city].distance_to_destinstion, current_path.path_cost + path_cost,
                 city == destination_city_key, current_path.get_cities_path())
            for (city, path_cost) in current_city.get_nearby_cities_with_distance()
            if not cities[city].visited)
        next_paths.sort(key=get_path_cost)

        # Imprime os caminhos disponiveis
        # display_paths(next_paths)

        # Seleciona o proximo caminho
        current_path = next_paths.pop(0)

    return current_path


def display_paths(paths):
    for path in paths:
        print(path.current_city_key + '->' + str(path.cost()))
        # display_path(path)
    print('\n')


def display_path(path):
    cities = path.past_cities
    route = ''
    for city in cities:
        route = route + city + ' -> '

    route = route + path.current_city_key
    print(route)
    print('Custo: ' + str(path.cost()))


if __name__ == '__main__':
    # Inicia o dicionario de cidades
    cities = cities_setup()

    # Mostra todas as cidades e as estradas
    # display_cities(cities)

    # Faz a busca comecando em Arad e terminando em Bucareste
    starting_city_key = 'Arad'
    destination_city_key = 'Bucareste'
    path = a_star_shortest_path(
        starting_city_key, destination_city_key, cities)

    # Imprime os resultados
    display_path(path)
