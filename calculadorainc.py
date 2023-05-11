#desenvolva uma calculadora de IMC, o programa deve pedir o peso e a altura
#ao usuario, calcular o IMC e retornar para o usuário o IMC
#menor que 18,5 - abaixo do peso
#entre 18,5 e 24,9 - peso normal
#entre 25 e 29,9 - acima do peso
#igual ou acima de 30 - obesidade
def calcular_IMC(peso,altura):
    IMC = peso / (altura * altura)
    return IMC
def classificacao(numero):
    if int(numero) < 18.5:
        return "abaixo do peso"
    elif numero < 25:
        return "peso normal"
    elif numero < 30:
        return "sobrepeso"
    elif int(numero) >= 30:
        return "obesidade"

peso = float(input("insira seu peso: "))
altura = float(input("insira sua altura: "))
print(calcular_IMC(peso,altura))
imc = calcular_IMC(peso,altura)
print(classificacao(imc))