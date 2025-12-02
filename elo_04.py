# elo_04.py
# gera a recomendacao de modalidade esportiva para o usuário com base em qual cluster ele foi jogado

from elo import Elo

class Elo_04(Elo):
    def __init__(self):
        super().__init__()
        # mapeia perfil e modalidade recomendada
        self.recomendacoes = {
            "Força": "Musculação",
            "Explosivo": "CrossFit",
            "Flexível": "Pilates",
            "Atlético": "Atletismo"
        }
    
    def proc(self, data):
        # pega o perfil e mapeia para a recomendacao
        perfil = data['perfil']
        recomendacao = self.recomendacoes.get(perfil, "Atividade Geral")
        
        # adiciona a recomendacao nos dados
        data['recomendacao'] = recomendacao
        
        return data