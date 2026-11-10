# autor: Michel
# data: 10/11/2026

# Superclasse ou classe base
# class Superclasse(object): Exemplo de uso da superclasse do python.
class Superclasse:
  # atributos
  # métodos
  pass

# Exemplo: `Animal`
class Animal:
  def __init__(self, nome):
    self.nome = nome
    
  def som(self):
    print(f"{self.nome} faz um som genérico.")