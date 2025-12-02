# controller.py
# camada de controle que conecta a view com o model

from model import Model

class Controller:
    def __init__(self, view):
        # cria o model
        self.model = Model()
        # armazena referencia da view
        self.view = view
    
    def cadastrar_usuario(self, dados_usuario):
        # processa o cadastro no model
        resultado = self.model.cadastrar_usuario(dados_usuario)
        return resultado
    
    def listar_usuarios(self):
        # busca usuarios do model
        usuarios = self.model.buscar_todos_usuarios()
        return usuarios
    
    def deletar_usuario(self, usuario_id):
        # deleta usuario
        self.model.deletar_usuario(usuario_id)
    
    def get_dados_para_grafico(self):
        # pega dados para o grafico
        return self.model.get_dados_treino_para_grafico()
    
    def get_mapeamento_perfis(self):
        # retorna mapeamento de perfis
        return self.model.mapeamento_perfis