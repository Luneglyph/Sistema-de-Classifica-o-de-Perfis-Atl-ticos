from elo import Elo

class Elo_03(Elo):
    # mapeia cluster para perfil
    def __init__(self, mapeamento_perfis):
        super().__init__()
        # recebe o dicionario que mapeia a relação cluster e perfil
        self.mapeamento = mapeamento_perfis
    
    def proc(self, data):
        # pega o numero do cluster e mapeia para o nome do perfil
        cluster = data['cluster']
        perfil = self.mapeamento.get(cluster, "Desconhecido")
        
        # adiciona o perfil nos dados
        data['perfil'] = perfil
        
        return data