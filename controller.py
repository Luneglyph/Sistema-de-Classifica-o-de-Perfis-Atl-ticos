from model import Model

class Controller:
    def __init__(self, view):
        self.model = Model()
        self.view = view
    
    def cadastrar_usuario(self, dados_usuario):
        resultado = self.model.cadastrar_usuario(dados_usuario)
        return resultado
    
    def listar_usuarios(self):
        usuarios = self.model.buscar_todos_usuarios()
        return usuarios
    
    def deletar_usuario(self, usuario_id):
        self.model.deletar_usuario(usuario_id)
    
    def get_mapeamento_perfis(self):
        return self.model.mapeamento_perfis