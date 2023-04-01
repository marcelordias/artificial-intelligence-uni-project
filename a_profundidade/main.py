from map import Map

def menu():
    print("+{:-^47}+".format("+"))
    print("|{:^47}|".format("MENU DE OPÇÕES"))
    print("+{:-^47}+".format("+"))
    print("|{:<47}|".format("1 - Mostrar todas as cidades e seus vizinhos"))
    print("|{:<47}|".format("2 - Procurar caminho entre duas cidades"))
    print("|{:<47}|".format("0 - Sair"))
    print("+{:-^47}+".format("+"))
    return input('Digite a opção desejada: ')
def search_menu():
    print("+{:-^47}+".format("+"))
    print("|{:^47}|".format("MENU DE BUSCA"))
    print("+{:-^47}+".format("+"))
    print("|{:<47}|".format("1 - Busca em profundidade"))
    print("|{:<47}|".format("2 - Busca custo uniforme"))
    print("|{:<47}|".format("0 - Voltar"))
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
                while True:
                    city = input('Digite o nome da cidade de origem: ')
                    destiny = input('Digite o nome da cidade de destino: ')
                    option = search_menu()
                    if option == '1':
                        path = portugal.find_path(city, destiny)
                        portugal.print_path(path)
                        break
                    elif option == '2':
                        path = portugal.find_path(city, destiny, True)
                        portugal.print_path(path)
                        break
                    elif option == '0':
                        break
                    else:
                        print('Opção inválida')
            elif option == '0':
                break
            else:
                print('Opção inválida')
    except KeyboardInterrupt:
        print('Programa interrompido.')

if __name__ == '__main__':
    main()