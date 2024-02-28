numero1 = int(input("digite um numero"))
numero2 = int(input("digite um segundo numero"))
 
input("escolha uma das opcoes abaixo")
print("1 - adicao")
print("2 - subtracao")
print("3 - multiplicacao")
print("4 - divisao")
operador = int(input("digite o numero correspondente"))

if operador == 1:
    print("a soma é:" + str(numero1 + numero2))
elif operador == 2:
    print("a soma é:" + str(numero1 - numero2))
elif operador == 3:
    print("a soma é:" + str(numero1 * numero2))
elif operador == 4:
    print("a soma é:" + str(numero1 / numero2))
else:
    print("numero incorreto")
