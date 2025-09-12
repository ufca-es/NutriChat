import json
import random
from src.personalidades import Personalidade as p
from utils.checagem_de_texto import Texto as t
from src.aprendizado import Aprendizado
from src.historico import Historico

class ChatBot:

    def __init__(self):
        self.personalidade = 'formal'
        self.pergunta_desconhecida = False
        self.historico = Historico()
        self.aprendizado = Aprendizado()
        self.conhecimentos_aprendidos = self.aprendizado.carregar()
        self.comandos = ('sair', 'trocar personalidade')

        with open('data/perguntas_e_respostas.json', "r", encoding="utf-8") as arquivo:
            self.base_conhecimento = json.load(arquivo)
        
    def _processar_comando(self, pergunta: str):

        if pergunta == 'sair':
            # ----- TRECHO COM INPUT / PRINT -----
            print("Encerrando o programa. Até mais!")
            exit()

        elif pergunta == 'trocar personalidade':
            # ----- TRECHO COM INPUT / PRINT -----
            self.personalidade = p.selecionar_personalidade()

    def _gerar_resposta(self, pergunta: str) -> str:
        return random.choice(self.base_conhecimento[pergunta][self.personalidade])
    
    def _gerar_resposta_aprendida(self, pergunta: str) -> str:
        self.conhecimentos_aprendidos = self.aprendizado.carregar()
        return random.choice(self.conhecimentos_aprendidos[pergunta])
    
    def aprender(self, pergunta: str):
        # ----- TRECHO COM INPUT / PRINT -----
        sugerir_resposta = input('Gostaria de sugerir uma resposta? (digite "sim" para fazer a sugestão)')

        if sugerir_resposta == 'sim':
            resposta = input(
                '\nComo devo responder a pergunta?:'
                f'\n{pergunta}\n'
            )

            self.aprendizado.salvar(pergunta, resposta)
            
    def responder(self, pergunta: str) -> str:
        pergunta = t.detectar_comando(pergunta, self.base_conhecimento)

        if pergunta in self.comandos:
            self._processar_comando(pergunta)
            resposta = f'Personalidade alterada para {self.personalidade}' # ---- ALTERAR ----

        elif pergunta in self.base_conhecimento:
            resposta = self._gerar_resposta(pergunta)

        elif pergunta in self.conhecimentos_aprendidos:
            resposta = self._gerar_resposta_aprendida(pergunta)

        else: 
            resposta = 'Desculpe, ainda não sei responder isso.'
            self.pergunta_desconhecida = True
            
        return resposta  

if __name__ == "__main__":

    h = Historico()

    # ----- TRECHO COM INPUT / PRINT -----
    if not h.historico_vazio():
        ultimas_interacoes = h.ler_ultimos(5)
        print('Histórico anterior de coversas\n')
        for linha in ultimas_interacoes:
            print(linha, end="")

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

        # ----- TRECHO COM INPUT / PRINT -----
        pergunta = input('\nDigite sua pergunta:\n')
        resposta = chatbot.responder(pergunta)
        print('\n— ',resposta)

        if chatbot.pergunta_desconhecida:
            chatbot.aprender(pergunta)
            chatbot.conhecimentos_aprendidos = chatbot.aprendizado.carregar()



        chatbot.historico.salvar(pergunta, resposta, chatbot.personalidade)    
        