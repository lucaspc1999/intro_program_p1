numConta =  int(input("Digite o número da conta sem dígito:"))
saldo =  float(input("Digite o saldo: "))
deb =  float(input("Digite o débito: "))
cred = float(input("Digite o crédito disponivel: "))

saldoFinal = saldo-deb+cred

if saldoFinal > 0:
    print()
    print("        SALDO POSITIVO          ")
    print("----------- EXTRATO ------------")
    print()
    print("Conta número           ",numConta)
    print("Saldo:                    ",saldo)
    print("Débito:                    -",deb)
    print("Crédito disponível:       +",cred)
    print("--------------------------------")
    print("SALDO TOTAL:            ",saldoFinal)


    
elif saldoFinal < 0:
    print()
    print("        SALDO NEGATIVO          ")
    print("----------- EXTRATO ------------")
    print()
    print("Conta número           ",numConta)
    print("Saldo:                    ",saldo)
    print("Débito:                    -",deb)
    print("Crédito disponível:       +",cred)
    print("--------------------------------")
    print("SALDO TOTAL:            ",saldoFinal)
    

else:
    print()
    print("         SALDO ZERADO          ")
    print("----------- EXTRATO ------------")
    print()
    print("Conta número           ",numConta)
    print("Saldo:                    ",saldo)
    print("Débito:                    -",deb)
    print("Crédito disponível:       +",cred)
    print("--------------------------------")
    print("SALDO TOTAL:            ",saldoFinal)