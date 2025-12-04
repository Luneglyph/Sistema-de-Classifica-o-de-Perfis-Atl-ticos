# model.py
# logica de negocios e processamento de dados

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from bson.objectid import ObjectId
from db import usuarios_collection
from elo_01 import Elo_01
from elo_02 import Elo_02
from elo_03 import Elo_03
from elo_04 import Elo_04

class Model:
    def __init__(self):
        # mapeamento cluster para perfil
        self.mapeamento_perfis = {
            0: "Atlético",
            1: "Força",
            2: "Explosivo",
            3: "Flexível"
        }
        self._treinar_modelo()
        self._montar_cadeia()
    
    def _treinar_modelo(self):
        # carrega os dados do csv
        dados = pd.read_csv('dados_treino.csv')
        
        # separa os dados para o treino
        X = dados[['S. horizontal', 'abdominal', 'flexibilidade', 'arremessoMB', 'IMC']].values
        
        # padroniza os dados
        self.scaler = StandardScaler()
        X_padronizado = self.scaler.fit_transform(X)
        
        # treina kmeans
        self.kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
        self.kmeans.fit(X_padronizado)
        print("kmeans treinado")
    
    def _montar_cadeia(self):
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
        print("usuario cadastrado")
        return resultado
    
    def buscar_todos_usuarios(self):
        usuarios = list(usuarios_collection.find())
        return usuarios
    
    def deletar_usuario(self, usuario_id):
        usuarios_collection.delete_one({"_id": ObjectId(usuario_id)})
        print("usuario deletado")