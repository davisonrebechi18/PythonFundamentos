# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")

print("\n\nSelecione o número da operação desejada: ")

print("\n1 - Adição: ")
print("2 - Subtração: ")
print("3 - Multiplicação: ")
print("4 - Divisão: ")

numoperacao = int(input("\nDigite sua opção 1/2/3/4 : "))

num1 = int(input("\nDigite o primeiro número:"))
num2 = int(input("\nDigite o segundo número:"))

if numoperacao == 1: # Operação soma
	# Função soma da calculadora
	def soma(num1, num2):
		adicao = num1 + num2
		#print("\n", str(num1) + " +", str(num2) + " =", adicao)
		print("\n%s + %s = " % (num1, num2), adicao)
	# Exibe o resultado da soma calculdora	
	soma(num1,num2)
	
elif numoperacao == 2: # Operação subtração
	#Função subtração da calculadora
	def subtracao(num1, num2):
		subt = num1 - num2
		print("\n%s - %s = " % (num1, num2), subt)
	# Exibe o resultado da subtração calculadora
	subtracao(num1, num2)

elif numoperacao == 3: # Operação multiplicação
	# Função multiplicação da calculadora
	def multiplicacao(num1,num2):
		multiplica = num1 * num2
		print("\n%s * %s = " % (num1, num2), multiplica)
	# Exibe o resultado da multiplicação calculadora
	multiplicacao(num1,num2)

elif numoperacao == 4: # Operação divisão
	# Função divisão da calculadora
	def divisao(num1,num2):
		divide = int(num1 / num2)
		print("\n%s / %s = " %(num1,num2), divide)
	# Exibe o resultado da divisão calculadora
	divisao(num1,num2)
else:
	print("\nOperação não existe!!! ")


	
