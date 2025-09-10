import json
import random
from src.personalidades import Personalidade as p
from utils.checagem_de_texto import Utilitarios as u

with open('data/perguntas_e_respostas.json', "r", encoding="utf-8") as arquivo:
    base_conhecimento = json.load(arquivo)

print(
    '\nSeja bem vindo (a) à plataforma NutriChat. Você pode escolher uma das seguintes personalidades: '
    '\n( 1 ) N.U.T.R.I Bot (formal)'
    '\n( 2 ) NutriLove (engraçada)'
    '\n( 3 ) Chief (rude)\n'
)

personalidade = p.selecionar_personalidade()

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

    pergunta = u.detectar_comando(pergunta, base_conhecimento)

    if pergunta == 'sair':
        print("Encerando o programa. Até mais!")
        exit()

    elif pergunta == 'trocar personalidade':
        personalidade = p.selecionar_personalidade()

    elif pergunta in base_conhecimento:
        resposta = random.choice(base_conhecimento[pergunta][personalidade])
        print('\n— ',resposta)

    else: 
        print('\n— Desculpe, ainda não sei responder isso.')