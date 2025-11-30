soma = 0

for i in range(5):
    numero = float(input(f"Digite o {i+1}º número: "))
    soma += numero

media = soma / 5

print("\n=====Resultado=====")
print(f"Soma total: {soma}".replace(".",","))
print(f"Média: {media}".replace(".",","))