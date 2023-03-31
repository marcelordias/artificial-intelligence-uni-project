from map import Map


def menu():
    print("+{:-^47}+".format("+"))
    print("|{:^47}|".format("MENU DE OPÇÕES"))
    print("+{:-^47}+".format("+"))
    print("|{:<47}|".format("1 - Mostrar todas as cidades e seus vizinhos"))
    print("|{:<47}|".format("2 - Mostrar o caminho entre duas cidades"))
    print("|{:<47}|".format("3 - Mostrar o melhor caminho entre duas cidades"))
    print("|{:<47}|".format("4 - Sair"))
    print("+{:-^47}+".format("+"))
    return input('Digite a opção desejada: ')


def main():
    portugal = Map()
    try:
        while True:
            option = menu()
            if option == '1':
                portugal.get_all_cities()
            elif option == '2':
                city = input('Digite o nome da cidade de origem: ')
                destiny = input('Digite o nome da cidade de destino: ')
                path = portugal.find_path(city, destiny)
                if path is None:
                    print('Caminho não encontrado')
                elif path[-1].city.name != destiny:
                    print('Não há caminho entre {} e {}'.format(city, destiny))
                else:
                    total_cost = 0
                    for travel in path:
                        print('-{}- {}'.format(travel.cost, travel.city.name), end=' ')
                        total_cost += travel.cost
                    print('\nTotal: {}'.format(total_cost))
            elif option == '3':
                city = input('Digite o nome da cidade de origem: ')
                destiny = input('Digite o nome da cidade de destino: ')
                path = portugal.find_path(city, destiny, True)
                if path is None:
                    print('Caminho não encontrado')
                # elif path[-1].city.name != destiny:
                #     print('Não há caminho entre {} e {}'.format(city, destiny))
                else:
                    total_cost = 0
                    for travel in path:
                        print('-{}- {}'.format(travel.cost, travel.city.name), end=' ')
                        total_cost += travel.cost
                    print('\nTotal: {}'.format(total_cost))
            elif option == '4':
                break
            else:
                print('Opção inválida')
    except KeyboardInterrupt:
        print('Programa interrompido.')
if __name__ == '__main__':
    main()
