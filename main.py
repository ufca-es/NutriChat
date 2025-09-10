import json
import random
from src.personalidades import Personalidade as p
from utils.checagem_de_texto import Texto as t
from src.historico import Historico

class ChatBot:

    def __init__(self):
        self.personalidade = 'formal'
        self.historico = Historico()
        self.comandos = ('sair', 'trocar personalidade')

        with open('data/perguntas_e_respostas.json', "r", encoding="utf-8") as arquivo:
            self.base_conhecimento = json.load(arquivo)
        
    def _processar_comando(self, pergunta: str):

        if pergunta == 'sair':
            print("Encerrando o programa. Até mais!")
            exit()

        elif pergunta == 'trocar personalidade':
            self.personalidade = p.selecionar_personalidade()

    def _gerar_resposta(self, pergunta: str) -> str:
        return random.choice(self.base_conhecimento[pergunta][self.personalidade])
        
    def responder(self, pergunta: str) -> str:
        pergunta = t.detectar_comando(pergunta, self.base_conhecimento)

        if pergunta in self.comandos:
            self._processar_comando(pergunta)
            resposta = f'Personalidade alterada para {self.personalidade}'

        elif pergunta in self.base_conhecimento:
            resposta = self._gerar_resposta(pergunta)
        
        else: 
            resposta = 'Desculpe, ainda não sei responder isso.'
            
        return resposta  

if __name__ == "__main__":

    print(
        '\nSeja bem vindo (a) à plataforma NutriChat. Perguntas disponíveis (por enquanto):'
        '\nO que é uma alimentação saudável'
        '\nQuantos litros de água devo beber por dia'
        '\nQuais alimentos devo evitar\n'

        '\nOutras ações:'
        '\nTrocar personalidade'
        '\nSair'
    )

    chatbot = ChatBot()

    while True:

        pergunta = input('\nDigite sua pergunta:\n')
        resposta = chatbot.responder(pergunta)
        print('\n— ',resposta)
        chatbot.historico.salvar(pergunta, resposta, chatbot.personalidade)    