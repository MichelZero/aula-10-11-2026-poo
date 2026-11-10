# autor: Michel
# data: 10/11/2026

# importando as classes
from subclasse import Subclasse
from subclasse import Cachorro
#from superclasse import Animal
'''
Crie uma instância de `Estudante` e
chame `apresentar()` e `estudar()`.
'''
from estudante import Estudante

# criando os objetos
lista1 = list()
s1 = Subclasse()
# criando um animal e um cachorro
#a1 = Animal("teste_nome")
c1 = Cachorro("caramelo", "vira-lata")

# teste de uso
#a1.som()
c1.som()
c1.latir()

# criando estudante
e1 = Estudante("Davi", 13, "fundamental II")

e1.apresentar()
e1.estudar()