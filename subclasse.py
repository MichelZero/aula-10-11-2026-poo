# autor: Michel
# data: 10/11/2026

# importar a classe base ou superclasse
from superclasse import Superclasse
from superclasse import Animal

# criar a nova classe Subclasse
class Subclasse(Superclasse):
  # atributos
  # métodos
  pass


# criando a classe Cachorro
class Cachorro(Animal):
  def __init__(self, nome, raca):
    super().__init__(nome)
    self.raca = raca
    
  def latir(self):
    print(f"{self.nome} ({self.raca}) latir: Au Au!")