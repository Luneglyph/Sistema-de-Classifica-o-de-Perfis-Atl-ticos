# elo_02.py
# usa o modelo do kmeans prra prever o cluster do usuario

from elo import Elo

class Elo_02(Elo):
    def __init__(self, modelo_kmeans, scaler):
        super().__init__()
        # recebe o modelo kmeans ja treinado e o scaler
        self.modelo = modelo_kmeans
        self.scaler = scaler
    
    def proc(self, data):
        # prepara os dados na ordem correta pro modelo
        # ordem: salto_horizontal, abdominal, flexibilidade, arremessoMB, imc
        features = [[
            data['salto_horizontal'],
            data['abdominal'],
            data['flexibilidade'],
            data['arremessoMB'],
            data['imc']
        ]]
        
        # padroniza os dados usando o scaler do treino do kmeans
        features_padronizadas = self.scaler.transform(features)
        
        # predict do cluster
        cluster = self.modelo.predict(features_padronizadas)[0]
        
        # adiciona o cluster nos dados
        data['cluster'] = int(cluster)
        
        return data