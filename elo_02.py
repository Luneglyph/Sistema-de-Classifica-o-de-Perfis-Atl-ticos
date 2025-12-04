from elo import Elo

#  previsao de qual cluster o usuario se encaixa
class Elo_02(Elo):
    def __init__(self, modelo_kmeans, scaler):
        super().__init__()
        self.modelo = modelo_kmeans
        self.scaler = scaler
    
    def proc(self, data):
        features = [[
            data['salto_horizontal'],
            data['abdominal'],
            data['flexibilidade'],
            data['arremessoMB'],
            data['imc']
        ]]
        
        features_padronizadas = self.scaler.transform(features)
        cluster = self.modelo.predict(features_padronizadas)[0]
        data['cluster'] = int(cluster)
        return data