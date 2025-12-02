# elo_03.py
# mapeia o numero do cluster para o nome do perfil atletico

from elo import Elo

class Elo_03(Elo):
    def __init__(self, mapeamento_perfis):
        super().__init__()
        # recebe o dicionario que mapeia a relação cluster e perfil
        # exemplo: {0: "Força", 1: "Explosivo", 2: "Flexível", 3: "Atlético"} (Mudar depois de testar o treino)
        self.mapeamento = mapeamento_perfis
    
    def proc(self, data):
        # pega o numero do cluster e mapeia para o nome do perfil
        cluster = data['cluster']
        perfil = self.mapeamento.get(cluster, "Desconhecido")
        
        # adiciona o perfil nos dados
        data['perfil'] = perfil
        
        return data