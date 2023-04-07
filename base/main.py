from setup import *

# Depth-first search
#print(portugal.dfs_get_path(porto, beja, True))

# Uniform-cost search
#print(portugal.ucs_get_path(porto, beja, True))

def menu():
    while True:
        print('\033c', end='')
        print("+{:-^47}+".format("+"))
        print("|{:^47}|".format("Menu de opções"))
        print("+{:-^47}+".format("+"))
        print("|{:<47}|".format("1 - Procurar o caminho entre duas cidades"))
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
        print("|{:^47}|".format("Algoritmos de pesquisa"))
        print("+{:-^47}+".format("+"))
        print("|{:<47}|".format("1 - Em profundidade primeiro (DFS)"))
        print("|{:<47}|".format("2 - Custo uniforme (UCS)"))
        print("|{:<47}|".format("3 - Procura sôfrega"))
        print("|{:<47}|".format("4 - A*"))
        print("|{:<47}|".format("0 - Voltar"))
        print("+{:-^47}+".format("+"))
        op = input('Digite a opção desejada: ')
        if op in ['1', '2', '0']:
            print('\033c', end='')
            return op
        print('\033c', end='')


def main():
    try:
        while True:
            option = menu()
            if option == '1':
                option = search_menu()
                if option == '0':
                    continue
                city = input('Digite o nome da cidade de origem: ')
                destiny = input('Digite o nome da cidade de destino: ')
                print('')
                city = portugal.get_city_by_name(city)
                destiny = portugal.get_city_by_name(destiny)

                if option == '1':
                  portugal.dfs_get_path(city, destiny, True)

                elif option == '2':
                    portugal.ucs_get_path(city, destiny, True)
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
