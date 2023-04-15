from setup import *

# Terminal text colors
W = '\033[0m'  # White
R = '\033[31m'  # Red
G = '\033[32m'  # Green
O = '\033[33m'  # Orange
P = '\033[35m'  # Purple

# Depth-first search
#portugal.get_dfs_path(castelo, portalegre, True)

# Uniform-cost search
#portugal.ucs_get_path(viseu, faro, True)

# Greedy search
# portugal.greedy_get_path(vila, faro, True)
# portugal.greedy_get_path(braganca, faro, True)

def menu():
    while True:
        print('\033c', end='')
        print("+{:-^47}+".format("+"))
        print("|{:^47}|".format("Menu de opções"))
        print("+{:-^47}+".format("+"))
        print("|{:<47}|".format("1 - Executar métodos de procura"))
        print("|{:<47}|".format("0 - Sair"))
        print("+{:-^47}+".format("+"))
        op = input('\n>> Opção desejada: ')
        if op in ['1', '0']:
            print('\033c', end='')
            return op
        print('\033c', end='')


def search_menu():
    while True:
        print("+{:-^47}+".format("+"))
        print("|{:^47}|".format("Métodos de procura"))
        print("+{:-^47}+".format("+"))
        print("|{:<47}|".format("1 - Em profundidade primeiro (DFS)"))
        print("|{:<47}|".format("2 - Custo uniforme (UCS)"))
        print("|{:<47}|".format("3 - Procura sôfrega (Greedy)"))
        print("|{:<47}|".format("4 - A*"))
        print("|{:<47}|".format("0 - Voltar"))
        print("+{:-^47}+".format("+"))
        op = input('\n>> Opção desejada: ')
        if op in ['1', '2', '3', '4', '0']:
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
                source = input('\n>> Cidade de origem: ')
                source = portugal.get_city(source)
                if source == None:
                    input('\n>> ' + R + 'Nenhuma cidade encontrada' + W + '\n\n>> Pressionar ENTER para voltar ao menu de opções...')
                    continue
                if option == '1' or option == '2':
                    destination = input('>> Cidade de destino: ')
                    destination = portugal.get_city(destination)
                    print('')
                    if destination == None:
                        input('>> ' + R + 'Nenhuma cidade encontrada' + W + '\n\n>> Pressionar ENTER para voltar ao menu de opções...')
                        continue
                else:
                    destination = source.straight_neighbor.city
                    print('\n>> Cidade de destino é por omissão \'{}\'\n'.format(destination.name))
                if option == '1':
                    portugal.get_dfs_path(source, destination, True)

                elif option == '2':
                    portugal.get_ucs_path(source, destination, True)

                elif option == '3':
                    portugal.get_greedy_path(source, destination, True)

                elif option == '4':
                    portugal.get_a_star_path(source, destination, True)
                input('>> Pressionar ENTER para voltar ao menu de opções...')
            elif option == '0':
                break
            else:
                print('Opção inválida')
    except KeyboardInterrupt:
        print('Programa interrompido.')


if __name__ == '__main__':
    main()
