frutas = ["maçã", "banana", "uva", "pera", "laranja", "abacaxi", "manga", "maracuja"]

fruta = input("Digite uma fruta: ").strip().lower()

if fruta in frutas:
    print("A fruta está na lista!")
else:
    print("A fruta NÃO está na lista.")