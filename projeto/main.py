# Description: Main file for the project
from map import Map
from colorama import Fore
from custom_exeptions import CityNotFound, PathNotFound, OriginAndDestinyAreTheSame
from config import Config

# This function prints the menu and returns the option chosen
def menu():
    while True:
        print('\033c', end='') if not Config.DEBUG else None # Clears the screen if DEBUG is True
        print("+{:-^47}+".format("+")) # Prints the top of the menu
        print("|{:^47}|".format("MENU DE OPÇÕES")) # Prints the title of the menu
        print("+{:-^47}+".format("+")) # Prints the line under the title
        print("|{:<47}|".format("1 - Mostrar todas as cidades e seus vizinhos")) # Prints the first option
        print("|{:<47}|".format("2 - Procurar caminho entre duas cidades")) # Prints the second option
        print("|{:<47}|".format("0 - Sair")) # Prints the third option
        print("+{:-^47}+".format("+")) # Prints the bottom of the menu
        op = input('Digite a opção desejada: ') # Gets the option chosen
        if op in ['1', '2', '0']: # If the option is valid
            print('\033c', end='') if not Config.DEBUG else None # Clears the screen if DEBUG is True
            return op # Returns the option chosen
        print('\033c', end='') if not Config.DEBUG else None # Clears the screen if DEBUG is True

# This function prints the search menu and returns the option chosen
def search_menu():
    while True:
        print("+{:-^47}+".format("+")) # Prints the top of the menu
        print("|{:^47}|".format("ALGORITMOS DE PESQUISA")) # Prints the title of the menu
        print("+{:-^47}+".format("+")) # Prints the line under the title
        print("|{:<47}|".format("1 - Procura em profundidade")) # Prints the first option
        print("|{:<47}|".format("2 - Procura custo uniforme [LEGACY]")) # Prints the second option
        print("|{:<47}|".format("3 - Procura custo uniforme [OPTIMIZED]")) # Prints the third option
        print("|{:<47}|".format("4 - Procura sôfrega")) # Prints the fourth option
        print("|{:<47}|".format("5 - Procura A*")) # Prints the fifth option
        print("|{:<47}|".format("0 - Voltar")) # Prints the sixth option
        print("+{:-^47}+".format("+")) # Prints the bottom of the menu
        op = input('Digite a opção desejada: ') # Gets the option chosen
        if op in ['1', '2', '3', '4', '5', '0']: # If the option is valid
            print('\033c', end='') if not Config.DEBUG else None # Clears the screen if DEBUG is True
            algorithm_name = '' # Creates a variable to store the name of the algorithm
            if op == '1': # If the option is 1 (Depth-first search)
                algorithm_name = 'Procura em profundidade' # Sets the name of the algorithm to 'Depth-first search'
            elif op == '2': # If the option is 2 (Uniform cost search [LEGACY])
                algorithm_name = 'Procura custo uniforme [LEGACY]' # Sets the name of the algorithm to 'Uniform cost search [LEGACY]'
            elif op == '3': # If the option is 3 (Uniform cost search [OPTIMIZED])
                algorithm_name = 'Procura custo uniforme [OPTIMIZED]' # Sets the name of the algorithm to 'Uniform cost search [OPTIMIZED]'
            elif op == '4': # If the option is 4 (Greedy search)
                algorithm_name = 'Procura sôfrega' # Sets the name of the algorithm to 'Greedy search'
            elif op == '5': # If the option is 5 (A* search)
                algorithm_name = 'Procura A*' # Sets the name of the algorithm to 'A* search'
            return (op, algorithm_name) # Returns the option chosen and the name of the algorithm
        print('\033c', end='') if not Config.DEBUG else None # Clears the screen if DEBUG is True

# This function waits for the user to press ENTER
def press_enter():
    input(f'\n{Fore.BLACK}Pressione ENTER para continuar...{Fore.RESET}') # Waits for the user to press ENTER
    print('\033c', end='') # Clears the screen

# This function is the main function of the program
try: # Tries to run the program
    portugal = Map() # Creates a new Map object (Portugal)
    while True: # Infinite loop
        option = menu() # Gets the option chosen
        if option == '1': # If the option is 1 (Show all cities and their neighbors)
            portugal.print_all_cities() # Prints all cities and their neighbors
            press_enter() if not Config.DEBUG else None # Waits for the user to press ENTER
        elif option == '2': # If the option is 2 (Search for a path between two cities)
            try: # Tries to find a path between two cities
                option, algorithm_name = search_menu() # Gets the option chosen
                if option == '0': # If the option is 0 (Go back)
                    continue # Goes back to the beginning of the loop (menu)
                city = input('Digite o nome da cidade de origem: ') # Gets the origin city
                if option == '4' or option == '5': # If the option is 4 (Greedy search) or 5 (A* search)
                    print(f'{Fore.YELLOW}Aviso: Esta procura irá apenas ter como destino: Faro{Fore.RESET}') # Prints a warning message
                    destiny = 'Faro' # Sets the destiny city to Faro
                else: # If the option is not 4 or 5
                    destiny = input('Digite o nome da cidade de destino: ') # Gets the destiny city
                path = portugal.find_path(city, destiny, option) # Finds the path between the origin and destiny cities using the chosen algorithm
                portugal.print_path(path, algorithm_name) # Prints the path
            except CityNotFound as e: # If the origin or destiny city is not found
                print(f'\n{Fore.YELLOW}Aviso: {e}{Fore.RESET}') # Prints a warning message
            except PathNotFound as e: # If there is no path between the origin and destiny cities
                print(f'\n{Fore.YELLOW}Aviso: {e}{Fore.RESET}') # Prints a warning message
            except OriginAndDestinyAreTheSame as e: # If the origin and destiny cities are the same
                print(f'\n{Fore.YELLOW}Aviso: {e}{Fore.RESET}') # Prints a warning message
            finally: # Runs no matter what
                press_enter() if not Config.DEBUG else None # Waits for the user to press ENTER
        elif option == '0': # If the option is 0 (Exit)
            break # Exits the infinite loop
except KeyboardInterrupt: # If the user presses CTRL+C
    print('\033c', end='') if not Config.DEBUG else None # Clears the screen if DEBUG is True
    print(f'\n{Fore.YELLOW}Aviso: Programa interrompido!{Fore.RESET}') # Prints a warning message
