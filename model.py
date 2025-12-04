import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from bson.objectid import ObjectId
from elo_01 import Elo_01
from elo_02 import Elo_02
from elo_03 import Elo_03
from elo_04 import Elo_04
from db import usuarios_collection

class Model:
    def __init__(self):
        self.mapeamento_perfis = {
            0: "Atletico", 
            1: "Força", 
            2: "Resistente", 
            3: "Flexivel" 
        }
        self.treinar_kmeans()
        self.montar_cadeia()
    
    def treinar_kmeans(self):
        dados = pd.read_csv('dados_treino.csv')
        dados_reais = dados[['S. horizontal', 'abdominal', 'flexibilidade', 'arremessoMB', 'IMC']].values
        self.scaler = StandardScaler()
        dados_padronizados = self.scaler.fit_transform(dados_reais)
        self.kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
        self.kmeans.fit(dados_padronizados)
    
    def montar_cadeia(self):
        elo1 = Elo_01()
        elo2 = Elo_02(self.kmeans, self.scaler)
        elo3 = Elo_03(self.mapeamento_perfis)
        elo4 = Elo_04() 
        elo1.set_next(elo2)
        elo2.set_next(elo3)
        elo3.set_next(elo4)
        self.primeiro_elo = elo1
    
    def cadastrar_usuario(self, dados_usuario):
        resultado = self.primeiro_elo.run(dados_usuario)
        usuarios_collection.insert_one(resultado)  
        return resultado
    
    def buscar_todos_usuarios(self):
        usuarios = list(usuarios_collection.find())
        return usuarios
    
    def deletar_usuario(self, usuario_id):
        usuarios_collection.delete_one({"_id": ObjectId(usuario_id)})
    
    def preparar_dados_radar(self, usuario):
        categorias = ['Salto', 'Abd', 'Flex', 'Arr', 'IMC'] 
        valores = [
            usuario.get('salto_horizontal', 0),
            usuario.get('abdominal', 0),
            usuario.get('flexibilidade', 0),
            usuario.get('arremessoMB', 0),
            usuario.get('imc', 0)
        ]
        valores = valores + valores[:1]
        num_vars = len(categorias)
        angles = []
        num_vars = len(categorias)
        
        for n in range(num_vars):
            angulo = (n / float(num_vars)) * 2 * 3.14159
            angles.append(angulo)

        angles += angles[:1]
        return categorias, valores, angles