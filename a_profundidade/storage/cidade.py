class Mapa:
    def __init__(self):
        cidade_aveiro = Cidade("Aveiro", None)
        cidade_aveiro.set_cidade_vizinha([{'cidade': Cidade("Coimbra", None), 'custo': 50}])
        self.cidades = {}

class Cidade:
    n_cidades_vizinhas = 0
    def __init__(self, nome, cidade_vizinha):
        self.nome = nome
        self.cidade_vizinha = cidade_vizinha
    
    def set_cidade_vizinha(self, cidade_vizinha):
        self.cidade_vizinha = cidade_vizinha
        self.n_cidades_vizinhas = len(cidade_vizinha)
    
    def get_cidade_vizinha(self):
        if self.cidade_vizinha is None:
            return None
        print("Cidade: ", self.nome)
        print("Custo: ", self.custo)
        print("Cidades vizinhas: ", self.n_cidades_vizinhas)
        return self.cidade_vizinha.get_cidade_vizinha()


Portugal = Mapa()