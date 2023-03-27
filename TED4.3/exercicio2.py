quant = int(input("Digite a quantidade de maças: "))

if quant < 12:
    total= quant*1.3
    print("O valor total foi de: R$",total)
else:
    total= quant*1
    print("O valor total foi de: R$",total)