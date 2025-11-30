dados = {}

dados["Nome"] = input("Digite o nome: ")
dados["Idade"] = int(input("Digite a idade: "))
dados["Curso"] = input("Digite o curso: ")

print("\n--- DADOS CADASTRADOS ---")
for chave, valor in dados.items():
    print(f"{chave}: {valor}")