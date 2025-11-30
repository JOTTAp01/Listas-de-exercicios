produtos = {
    "arroz": 5.50,
    "feijão": 7.20,
    "macarrão": 4.00
}

produto = input("Digite o nome do produto: ").strip().lower()

if produto in produtos:
    print(f"O preço de {produto} é R$ {produtos[produto]:.2f}")
else:
    print("Produto não cadastrado.")