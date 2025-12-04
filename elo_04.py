from elo import Elo

# adiciona recomendação baseada no perfil
class Elo_04(Elo):
    def __init__(self):
        super().__init__()
        self.recomendacoes = {
            "Força": "Powerlift, Musculaçao",
            "Resistente": "Escalada, Maratonas, Ciclismo",
            "Flexivel": "Pilates, Ginástica, Yoga",
            "Atletico": "Corrida, Salto, Nataçao"
        }
    
    def proc(self, data):
        perfil = data['perfil']
        recomendacao = self.recomendacoes.get(perfil, "Atividade geral")
        data['recomendacao'] = recomendacao
        return data