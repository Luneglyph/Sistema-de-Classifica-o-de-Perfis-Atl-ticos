from elo import Elo

class Elo_01(Elo):
    # calcula o imc do usuario
    def proc(self, data):
        peso = data['peso']
        altura = data['altura']
        
        # calcula imc
        altura_metros = altura / 100
        imc = peso / (altura_metros ** 2)
        
        data['imc'] = round(imc, 2)
        
        return data