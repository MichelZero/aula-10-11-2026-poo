"""

1. Classe `Pessoa` e `Estudante`
Crie uma superclasse `Pessoa` com `__init__(self, nome, idade)`.
Adicione um método `apresentar()` que
imprima "Olá, meu nome é [nome] e tenho [idade] anos."

"""
class Pessoa:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade
  
  def apresentar(self):
    print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")