from elo import Elo

class Elo_02(Elo):
    # prediz o cluster usando kmeans
    def __init__(self, modelo_kmeans, scaler):
        super().__init__()
        self.modelo = modelo_kmeans
        self.scaler = scaler
    
    def proc(self, data):
        # prepara os dados
        features = [[
            data['salto_horizontal'],
            data['abdominal'],
            data['flexibilidade'],
            data['arremessoMB'],
            data['imc']
        ]]
        
        # padroniza os dados
        features_padronizadas = self.scaler.transform(features)
        
        # prediz o cluster
        cluster = self.modelo.predict(features_padronizadas)[0]
        
        data['cluster'] = int(cluster)
        
        return data