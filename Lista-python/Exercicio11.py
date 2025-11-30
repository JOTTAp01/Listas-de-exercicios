def calcular_media(lista_notas):
    return sum(lista_notas) / len(lista_notas)

# Programa principal
notas = []

for i in range(4):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)

media = calcular_media(notas)

print(f"\nA média das notas é: {media:.2f}".replace(".",","))