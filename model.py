# model.py
# camada de logica de negocios do sistema
# responsavel por treinar o kmeans e processar os dados dos usuarios

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from db import usuarios_collection
from elo_01 import Elo_01
from elo_02 import Elo_02
from elo_03 import Elo_03
from elo_04 import Elo_04

class Model:
    def __init__(self):
        # mapeamento de clusters para perfis baseado na analise dos centroides
        self.mapeamento_perfis = {
            0: "Atlético",
            1: "Força",
            2: "Explosivo",
            3: "Flexível"
        }
        
        # treina o modelo no inicio
        self._treinar_modelo()
        
        # monta a cadeia de responsabilidade
        self._montar_cadeia()
    
    def _treinar_modelo(self):
        # carrega os dados do csv
        dados = pd.read_csv('dados_treino.csv')
        
        # separa as features
        X = dados[['S. horizontal', 'abdominal', 'flexibilidade', 'arremessoMB', 'IMC']].values
        
        # padroniza os dados para que todas as features tenham a mesma escala
        # isso evita que caracteristicas que variam mais deixem o clustering muito tendencioso
        self.scaler = StandardScaler()
        X_padronizado = self.scaler.fit_transform(X)
        
        # treina o kmeans com 4 clusters
        self.kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
        self.kmeans.fit(X_padronizado)
        
        print("kmeans treinado!")
    
    def _montar_cadeia(self):
        # cria os elos da cadeia de responsabilidade
        elo1 = Elo_01()  # calcula imc
        elo2 = Elo_02(self.kmeans, self.scaler)  # prediz cluster
        elo3 = Elo_03(self.mapeamento_perfis)  # classifica perfil
        elo4 = Elo_04()  # gera recomendacao
        
        # encadeia os elos
        elo1.set_next(elo2)
        elo2.set_next(elo3)
        elo3.set_next(elo4)
        
        # guarda o primeiro elo para iniciar a cadeia
        self.primeiro_elo = elo1
    
    def cadastrar_usuario(self, dados_usuario):
        # recebe os dados do usuario e processa pela cadeia
        # dados_usuario deve ser um dicionario com:
        # nome, salto_horizontal, abdominal, flexibilidade, arremessoMB, peso, altura
        
        # inicia a cadeia de responsabilidade
        resultado = self.primeiro_elo.run(dados_usuario)
        
        # salva no banco de dados
        usuarios_collection.insert_one(resultado)
        
        print("usuario cadastrado com sucesso!")
        
        return resultado
    
    def buscar_todos_usuarios(self):
        # busca todos os usuarios do banco
        usuarios = list(usuarios_collection.find())
        return usuarios
    
    def deletar_usuario(self, usuario_id):
        # deleta um usuario do banco pelo id
        from bson.objectid import ObjectId
        usuarios_collection.delete_one({"_id": ObjectId(usuario_id)})
        print("usuario deletado!")
    
    def get_dados_treino_para_grafico(self):
        # retorna os dados de treino e seus clusters para plotar no grafico
        dados = pd.read_csv('dados_treino.csv')
        X = dados[['S. horizontal', 'abdominal', 'flexibilidade', 'arremessoMB', 'IMC']].values
        X_padronizado = self.scaler.transform(X)
        clusters = self.kmeans.predict(X_padronizado)
        
        return X, clusters