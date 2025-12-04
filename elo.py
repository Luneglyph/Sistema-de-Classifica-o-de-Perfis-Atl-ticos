from abc import ABC, abstractmethod

class Elo(ABC):
    def __init__(self):
        self.next = None
    
    def set_next(self, next):
        # define o proximo elo da cadeia
        self.next = next
    
    @abstractmethod
    def proc(self, data):
        # metodo abstrato que cada elo deve implementar
        pass
    
    def run(self, data):
        # executa o processamento deste elo
        data = self.proc(data)
        
        # se houver proximo elo, passa os dados para ele
        if self.next is not None:
            return self.next.run(data)
        else:
            # se for o ultimo elo, retorna o resultado final
            return data