estMax = int(input("Digite a quantidade padrão para estoque máximo do item: "))
estMin = int(input("Digite a quantidade padrão para estoque mínimo do item: "))
estq = int(input("Digite o quantido do estoque atual do item: "))

estIdeal= int((estMax+estMin)/2)

if estq>=estIdeal:
    print("Levando em consideração o estoque ideal sendo de: ",estIdeal,"unds")
    print("Não se faz necessário efetuar a compra do item")

else:
    print("Levando em consideração o estoque ideal sendo de: ",estIdeal,"unds")
    print("É necessário efetuar a compra do item")