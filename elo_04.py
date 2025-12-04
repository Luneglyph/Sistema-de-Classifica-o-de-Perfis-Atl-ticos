# elo_04.py
# gera recomendacao de modalidade

from elo import Elo

class Elo_04(Elo):
    def __init__(self):
        super().__init__()
        self.recomendacoes = {
            "Força": "Musculação",
            "Explosivo": "CrossFit",
            "Flexível": "Pilates",
            "Atlético": "Atletismo"
        }
    
    def proc(self, data):
        perfil = data['perfil']
        recomendacao = self.recomendacoes.get(perfil, "Atividade Geral")
        
        data['recomendacao'] = recomendacao
        
        return data