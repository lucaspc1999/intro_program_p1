print("Programa para calular suas notas e verificar se foi aprovado ou não")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = float(nota1+nota2)/2

if media>=6:
    print("Sua média foi de: ",media)
    print("Aluno Aprovado")

else:
    print("Sua média foi de: ",media)
    print("Aluno Reprovado")
