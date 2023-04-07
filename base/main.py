from setup import *

# Depth-first search
#portugal.get_dfs_path(braganca, evora, True)
#portugal.get_dfs_path(porto, santarem, True)
#viseu.print_neighbors()
# Uniform-cost search
#portugal.ucs_get_path(viseu, faro, True)

# Greedy search
portugal.greedy_get_path(vila, faro, True) # TO CHECK IF OK
portugal.greedy_get_path(braganca, faro, True) # TO CHECK IF OK

# def menu():
#     while True:
#         print('\033c', end='')
#         print("+{:-^47}+".format("+"))
#         print("|{:^47}|".format("Menu de opções"))
#         print("+{:-^47}+".format("+"))
#         print("|{:<47}|".format("1 - Executar métodos de procura"))
#         print("|{:<47}|".format("0 - Sair"))
#         print("+{:-^47}+".format("+"))
#         op = input('\nOpção desejada: ')
#         if op in ['1', '0']:
#             print('\033c', end='')
#             return op
#         print('\033c', end='')


# def search_menu():
#     while True:
#         print("+{:-^47}+".format("+"))
#         print("|{:^47}|".format("Métodos de procura"))
#         print("+{:-^47}+".format("+"))
#         print("|{:<47}|".format("1 - Em profundidade primeiro (DFS)"))
#         print("|{:<47}|".format("2 - Custo uniforme (UCS)"))
#         print("|{:<47}|".format("3 - Procura sôfrega (Greedy)"))
#         print("|{:<47}|".format("4 - A*"))
#         print("|{:<47}|".format("0 - Voltar"))
#         print("+{:-^47}+".format("+"))
#         op = input('\nOpção desejada: ')
#         if op in ['1', '2', '3', '4', '0']:
#             print('\033c', end='')
#             return op
#         print('\033c', end='')


# def main():
#     try:
#         while True:
#             option = menu()
#             if option == '1':
#                 option = search_menu()
#                 if option == '0':
#                     continue
#                 source = input('Cidade de origem: ')
#                 source = portugal.get_city(source)
#                 if source == None:
#                     print(
#                         '\nCidade inválida\n\nPressione ENTER para voltar ao menu de opções...')
#                     input()
#                     continue
#                 if option == '1' or option == '2':
#                     destination = input('Cidade de destino: ')
#                     destination = portugal.get_city(destination)
#                     if destination == None:
#                         print(
#                             '\nCidade inválida\n\nPressione ENTER para voltar ao menu de opções...')
#                         input()
#                         continue
#                 else:
#                     destination = source.straight_neighbor.city
#                     print('\nCidade de destino é por omissão \'{}\'\n'.format(destination.name))
#                 if option == '1':
#                     portugal.dfs_get_path(source, destination, True)

#                 elif option == '2':
#                     portugal.ucs_get_path(source, destination, True)

#                 elif option == '3':
#                     portugal.greedy_get_path(source, destination, True)
#                 print('\nPressione ENTER para continuar...')
#                 input()
#             elif option == '0':
#                 break
#             else:
#                 print('Opção inválida')
#     except KeyboardInterrupt:
#         print('Programa interrompido.')


# if __name__ == '__main__':
#     main()
