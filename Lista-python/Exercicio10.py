def saudar(nome):
    print(f"Olá, {nome}! Seja bem-vindo(a)!")

for i in range(3):
    nome = input(f"Digite o {i+1}º nome: ")
    saudar(nome)