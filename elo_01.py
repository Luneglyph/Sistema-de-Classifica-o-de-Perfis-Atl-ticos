from elo import Elo

# calculo do imc
class Elo_01(Elo):
    def proc(self, data):
        peso = data['peso']
        altura = data['altura']
        altura_metros = altura / 100
        imc = peso / (altura_metros ** 2)
        
        data['imc'] = round(imc, 2)
        
        return data