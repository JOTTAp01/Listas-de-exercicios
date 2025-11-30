def cadastrar_pessoa(): 
    nome = input("Nome: ")
    idade = input("Idade: ")
    cidade = input("Cidade: ")
    return {"Nome": nome, "Idade": idade, "Cidade": cidade}

cadastros = []

while True:
    print("\nDigite 'sair' no nome para encerrar.")
    nome = input("Nome: ").strip().capitalize()

    if nome.strip().capitalize() == "Sair":
        break

    idade = input("Idade: ")
    cidade = input("Cidade: ")

    pessoa = {"Nome": nome, "Idade": idade, "Cidade": cidade}
    cadastros.append(pessoa)

print("\n=====LISTA DE CADASTROS=====")

indice = 1
for pessoa in cadastros:
    print(f"\nPessoa {indice}:")
    for chave, valor in pessoa.items():
        print(f"{chave}: {valor}")
    indice += 1