nomes = []

while True:
    nome = input("Digite um nome (ou 'sair' para encerrar): ").strip().capitalize()

    if nome.strip().capitalize() == "Sair":
            break

    nomes.append(nome)

print("\nCadastro concluído!")
print(f"Total de nomes cadastrados: {len(nomes)}")
print("Lista completa:")
print(nomes)