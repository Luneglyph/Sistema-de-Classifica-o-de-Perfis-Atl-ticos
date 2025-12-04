from elo import Elo

# transforma o numero do cluster em nome do perfil
class Elo_03(Elo):
    def __init__(self, mapeamento_perfis):
        super().__init__()
        # recebe o dicionario que mapeia a relação cluster e perfil
        self.mapeamento = mapeamento_perfis
    
    def proc(self, data):
        cluster = data['cluster']
        perfil = self.mapeamento.get(cluster, "desconhecido") 
        data['perfil'] = perfil
        
        return data