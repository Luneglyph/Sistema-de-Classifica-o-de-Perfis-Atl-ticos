from elo import Elo

# associa o numero do cluster ao nome do perfil
class Elo_03(Elo):
    def __init__(self, mapeamento_perfis):
        super().__init__()
        self.mapeamento = mapeamento_perfis
    
    def proc(self, data):
        cluster = data['cluster']
        perfil = self.mapeamento.get(cluster, "não definido") 
        data['perfil'] = perfil
        
        return data