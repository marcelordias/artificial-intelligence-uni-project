from map import Map

def menu():
    while True:
        print('\033c', end='')
        print("+{:-^47}+".format("+"))
        print("|{:^47}|".format("MENU DE OPÇÕES"))
        print("+{:-^47}+".format("+"))
        print("|{:<47}|".format("1 - Mostrar todas as cidades e seus vizinhos"))
        print("|{:<47}|".format("2 - Procurar caminho entre duas cidades"))
        print("|{:<47}|".format("0 - Sair"))
        print("+{:-^47}+".format("+"))
        op = input('Digite a opção desejada: ')
        if op in ['1', '2', '0']:
            print('\033c', end='')
            return op
        print('\033c', end='')

def search_menu():
    while True:
        print("+{:-^47}+".format("+"))
        print("|{:^47}|".format("ALGORITMOS DE PESQUISA"))
        print("+{:-^47}+".format("+"))
        print("|{:<47}|".format("1 - Busca em profundidade"))
        print("|{:<47}|".format("2 - Busca custo uniforme [LEGACY]"))
        print("|{:<47}|".format("3 - Busca custo uniforme [OPTIMIZED]"))
        print("|{:<47}|".format("4 - Busca sôfrega"))
        print("|{:<47}|".format("5 - Busca A*"))
        print("|{:<47}|".format("0 - Voltar"))
        print("+{:-^47}+".format("+"))
        op = input('Digite a opção desejada: ')
        if op in ['1', '2', '3', '4', '5', '0']:
            print('\033c', end='')
            return op
        print('\033c', end='')

def main():
    portugal = Map()
    try:
        while True:
            option = menu()
            if option == '1':
                portugal.get_all_cities()
                print('\nPressione ENTER para continuar...')
                input()
            elif option == '2':
                option = search_menu()
                if option == '0':
                    continue
                city = input('Digite o nome da cidade de origem: ')
                if option == '4' or option == '5':
                    print('Esta procura irá apenas ter como destino: Faro')
                    destiny = 'Faro'
                else:
                    destiny = input('Digite o nome da cidade de destino: ')

                path = portugal.find_path(city, destiny, option)
                portugal.print_path(path)
                print('\nPressione ENTER para continuar...')
                input()
            elif option == '0':
                break
            else:
                print('Opção inválida')
    except KeyboardInterrupt:
        print('Programa interrompido.')

if __name__ == '__main__':
    main()
