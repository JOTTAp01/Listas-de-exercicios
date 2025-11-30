numeros = (3, 7, 2, 7, 9, 4, 7, 1)

num = int(input("Digite um número: "))

if num in numeros:
    print("O número está na tupla!")
    indice = numeros.index(num)
    print(f"Ele aparece pela primeira vez na posição: {indice}")
else:
    print("O número não está na tupla.")