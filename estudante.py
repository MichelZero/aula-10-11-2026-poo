"""
Crie uma subclasse `Estudante` que 
herde de `Pessoa`. Seu `__init__` 
deve aceitar `nome`, `idade` e `curso`.
Use `super().__init__` para os 
atributos de `Pessoa`. Adicione 
um método `estudar()` que 
imprima "Estou estudando [curso]."

"""
from pessoa import Pessoa

class Estudante(Pessoa):
  def __init__(self, nome, idade, curso):
    super().__init__(nome, idade)
    self.curso = curso
    
  def estudar(self):
    print(f"Estou estudando {self.curso}.")