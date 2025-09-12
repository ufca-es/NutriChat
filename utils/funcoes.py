
# falta associar com a pergunta da quantidade de agua e do imc
class imc:
    def calcular_imc(massa, altura, imc):
        massa = float(input("Qual é o seu peso? "))
        altura = float(input("Digite sua altura: "))
        imc = massa / (altura*altura)

        meu_imc = print("Seu indice de massa corporal é: ")

        if imc < 18.5:
            # para o formal
            print("Você está abaixo do peso.")
            # para o engraçado
            print("Precisa comer mais amiguinho! você está abaixo do peso.")
            # para o rude
            print("Você está abaixo do peso, vê se come mais um pouco para não arriar.")

        elif imc >= 18.5 and imc <= 24.9:
            # para o formal
            print("Seu peso está normal.")
            # para o engraçado
            print("Parabéns! você tem o peso ideal.")
            # para o rude
            print("Você está com o peso normal, não faz mais que a sua obrigaçaõ")
        elif imc > 24.9 and imc <= 29.9:
            # para o formal
            print("Seu imc revela que está com sobrepeso.")
            # para o engraçado
            print(
                "Você está com sobrepeso amiguinho, é bom ter um pouco mais de atenção na sua alimentação")
            # para o rude
            print(
                "Você está com sobrepeso, pare de comer tanto fritura e ultraprocessados.")
        elif imc > 29.9 and imc <= 34.9:
            # para o formal
            print("Seu imc revela que está com obesidade grau 1.")
            # para o engraçado
            print(
                "Você está com obesidade grau 1, precisa ter mais atenção com a dieta, meu amigo.")
            # para o rude
            print("Você está com obesidade grau 1, se eu fosse você me teria cuidado.")
        elif imc > 34.9:
            # para o formal
            print("Seu imc revela que está com obesidade.")
            # para o engraçado
            print("Você está com obesidade grau, escolha alimentos menos caloricos, faça exercicios físicos, vai ser sensacional te ver quebrar uns quilinhos!")
            # para o rude
            print(
                "Você está com obesidade, mude sua alimentação e tira a bunda da cama, movimente-se!")


def litros_de_agua(idade, peso, litros):
    idade = int(input("Digite sua idade: "))
    peso = float(input("Digite seu peso em quilos: "))

    if idade <= 17:
        litros = 0.04 * peso
    elif idade > 17 and idade <= 55:
        litros = 0.035 * peso
    elif idade > 55 and idade <= 65:
        litros = 0.03 * peso
    elif idade > 65:
        litros = 0.025 * peso

    print("A quantidade media de litros de agua que vc deve beber por dia é: ", litros)


def personalidade_mais(self, )
'''Criar um Contador: Adicione um dicionário na sua classe ChatBot para guardar a contagem de cada pergunta. 
As perguntas serão as chaves e o número de vezes que foram feitas serão os valores.
Atualizar o Contador: Toda vez que uma pergunta for feita, você aumenta a contagem dela no dicionário.
Encontrar a Mais Frequente: No final da execução, percorra o dicionário para encontrar a pergunta que tem a maior contagem.
'''
guardar_pergunta = {}

def mostrar_estatisticas(self):
        
        # 3. Encontra e mostra a pergunta mais feita
        if self.contador_perguntas:
            pergunta_mais_feita = max(self.contador_perguntas, key=self.contador_perguntas.get)
            contagem = self.contador_perguntas[pergunta_mais_feita]
            print(f"A pergunta mais feita foi: '{pergunta_mais_feita}' (feita {contagem} vez(es))")
        else:
            print("Nenhuma pergunta válida foi feita.")

def obter_pers_mais_usada(personalidade: str) -> str:

    contar_formal = 0
    contar_engracado = 0
    contar_rude = 0
    cont_personalidade = [contar_formal,contar_engracado, contar_rude, ]

    if Personalidade == "formal":
        contar_formal = contar_formal + 1
        
    elif Personalidade == "engraçada":
        contar_formal = contar_formal + 1 
        
    elif Personalidade == "rude":
        contar_formal = contar_formal + 1

    pe_mais_usada = max(cont_personalidade)

    if pe_mais_usada == contar_formal:
        return "formal"
    elif pe_mais_usada == contar_engracado:
        return "engracado"
    elif pe_mais_usada == contar_rude:
        return "rude"
    
def pergunta_mais_feita(pergunta: str) -> str:

    contarp1 = "o que é uma alimentação saudável", 0
    contarp2 = "quantos litros de água devo beber por dia"= 0
    contarp3 = "quais alimentos devo evitar"= 0
    cont_pergunta = [contarp1,contarp2, contarp3, ]

    if Personalidade == "formal":
        contar_formal = contar_formal + 1
        
    elif Personalidade == "engraçada":
        contar_formal = contar_formal + 1 
        
    elif Personalidade == "rude":
        contar_formal = contar_formal + 1

    pe_mais_usada = max(cont_personalidade)

    if pe_mais_usada == contar_formal:
        return "formal"
    elif pe_mais_usada == contar_engracado:
        return "engracado"
    elif pe_mais_usada == contar_rude:
        return "rude"
    

