"""
Primicias:
Pedir o nome e idade
armazenar (str) nome
armazenar (int) numeros
armazenar (float) numeros decimais


"""
#criando Estruturas
print("\n-------------------------")
print("Bem vindo Nerd!")
print("\n-------------------------")

# exibe a mensagem no terminal
nome = str (input ("Qual seu nome meu nobre?"))
idade = int (input ("Quantos anos você tem?"))
altura = float (input ("Quanto tem de altura?"))

# Exibe a mensagem no terminal com a suas respostas 
print(f"Olá {nome}, muito prazer!")
print(f"Você tem {idade} anos e mede {altura} metros.")


#Verificando se é menor de idade
if idade < 18:
    print("Que pena, você é um novato.")
else:
    print("Você tem idade para acessar, bem-vindo!")
