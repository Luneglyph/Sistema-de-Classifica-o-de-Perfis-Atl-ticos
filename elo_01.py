# elo_01.py
# calcula o imc do usuario baseado em peso e altura

from elo import Elo

class Elo_01(Elo):
    def proc(self, data):
        # recebe peso em kg e altura em cm
        peso = data['peso']
        altura = data['altura']
        
        # calcula imc = peso / (altura em metros)^2
        altura_metros = altura / 100
        imc = peso / (altura_metros ** 2)
        
        # arredonda para 2 casas decimais
        data['imc'] = round(imc, 2)
        
        # retorna os dados atualizados
        return data