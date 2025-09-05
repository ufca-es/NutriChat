import json
import random

with open('data/perguntas_e_respostas.json', "r", encoding="utf-8") as arquivo:
    base_conhecimento = json.load(arquivo)

def selecionar_personalidade():
        opcoes_formal = ('1', 'formal')
        opcoes_engraçado = ('2', 'engraçada')
        opcoes_rude = ('3', 'rude',)

        while True:
            personalidade = input('Com qual personagem você deseja conversar? ').strip().lower()

            if personalidade in opcoes_formal:
                return 'formal'

            elif personalidade in opcoes_engraçado:
                return 'engracada'

            elif personalidade in opcoes_rude:
                return 'rude'
                

            else:
                print('Essa personalidade não está disponível. Tente novamente.')

print(
    '\nSeja bem vindo (a) à plataforma NutriChat. Você pode escolher uma das seguintes personalidades: '
    '\n( 1 ) formal'
    '\n( 2 ) engraçada'
    '\n( 3 ) rude\n'
)

personalidade = selecionar_personalidade()

print(
    '\nPerguntas disponíveis (por enquanto):'
    '\nO que é uma alimentação saudável'
    '\nQuantos litros de água devo beber por dia'
    '\nQuais alimentos devo evitar\n'

    '\nOutras ações:'
    '\nTrocar personalidade'
    '\nSair'
)

while True:
    
    pergunta = input('\nDigite sua Pergunta\n').strip().lower()

    if pergunta == 'sair':
        exit()

    elif pergunta == 'trocar personalidade':
        personalidade = selecionar_personalidade()

    elif pergunta in base_conhecimento:
        resposta = random.choice(base_conhecimento[pergunta][personalidade])
        print('\n—',resposta)

    else: 
        print('\n—Desculpe, ainda não sei responder isso.')