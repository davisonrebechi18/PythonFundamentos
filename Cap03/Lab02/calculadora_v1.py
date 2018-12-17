# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")
print("\n")
print("Digite o número da operação solicitada: ")
print("\n")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("\n")
operacao = int(input ("Digite sua opção (1,2,3,4):"))

def soma(arg1, arg2):
    result = arg1 + arg2
    return result

def subtracao(arg1, arg2):
    result = arg1 - arg2
    return result

def multiplicacao(arg1, arg2):
    result = arg1 * arg2
    return result

def divisao(arg1, arg2):
    result = arg1 // arg2
    return result

if operacao == 1:
    x = int(input("Digite o primeiro número: "))
    y = int(input("Digite o segundo número: "))
    print(x, '+', y, '=', soma(x,y))
       
elif operacao == 2:
    x = int(input("Digite o primeiro número: "))
    y = int(input("Digite o segundo número: "))
    print(x, '-', y, '=', subtracao(x,y))
    
elif operacao == 3:
    x = int(input("Digite o primeiro número: "))
    y = int(input("Digite o segundo número: "))
    print(x, '*', y, '=', multiplicacao(x,y))

elif operacao == 4:
    x = int(input("Digite o primeiro número: "))
    y = int(input("Digite o segundo número: "))
    print(x, '/', y, '=', divisao(x,y))
  
else:
    print("Opção inválida!")

    

    





