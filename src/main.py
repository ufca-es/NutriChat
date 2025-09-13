import json
import random
from src.personalidades import Personalidade as p
from src.aprendizado import Aprendizado
from src.historico import Historico
from utils.checagem_de_texto import Texto as t
from utils.tokens import Tokens

class ChatBot:

    def __init__(self):
        self.personalidade = 'formal'
        self.pergunta_desconhecida = None
        self.aguardando_aprendizado = False
        self.solicitado_aprendizado = False
        self.solicitado_trocar_personalidade = False
        self.solicitado_sair = False
        self.aprendizado = Aprendizado()
        self.conhecimentos_aprendidos = self.aprendizado.carregar()
        self.comandos = ('sair', 'trocar personalidade')

        with open('data/perguntas_e_respostas.json', "r", encoding="utf-8") as arquivo:
            self.base_conhecimento = json.load(arquivo)
        
    def _gerar_resposta(self, pergunta: str) -> str:
        return random.choice(self.base_conhecimento[pergunta][self.personalidade])
    
    def _gerar_resposta_aprendida(self, pergunta: str) -> str:
        self.conhecimentos_aprendidos = self.aprendizado.carregar()
        return random.choice(self.conhecimentos_aprendidos[pergunta])
            
    def responder(self, pergunta: str) -> str:
        """
        Recebe uma String e processa uma resposta ou executa um comando baseada nela.
        """

        # Fluxo onde o usuário cadastra uma resposta nova
        if t.detectar_comando(pergunta, Tokens.afirmativos) in Tokens.afirmativos and self.aguardando_aprendizado:
            self.solicitado_aprendizado = True
            return f'Como devo responder a pergunta?\n{self.pergunta_desconhecida}'
        
        elif t.detectar_comando(pergunta, Tokens.negativos) in Tokens.negativos and self.aguardando_aprendizado:
            self.aguardando_aprendizado = False
            return 'Entendido, posso tentar aprender depois.'
        
        elif self.solicitado_aprendizado:
            self.solicitado_aprendizado = False
            self.aprendizado.salvar(self.pergunta_desconhecida, pergunta)
            self.pergunta_desconhecida = None
            return 'Conhecimento aprendido!'
        
        self.aguardando_aprendizado = False

        # Fluxo de execução de comandos
        if pergunta == 'sair':
            self.solicitado_sair = True
            return "Encerrando o programa. Até mais!"
        
        if pergunta == 'trocar personalidade' and not self.solicitado_trocar_personalidade:
            self.solicitado_trocar_personalidade = True
            return (
                'Qual personagem deseja conversar?: 1. N.U.T.R.I Bot(formal), 2. NutriLove(engraçada) ou Chief(rude)\n'
            )
            
        elif self.solicitado_trocar_personalidade:
            # Retorna se a troca de personalidade é possivel (bool)
            if p.selecionar_personalidade(pergunta) == False:
                return 'Essa personalidade não está disponível. Tente novamente.'
            # Muda a personalidade (str)
            else:
                self.solicitado_trocar_personalidade = False
                self.personalidade = p.selecionar_personalidade(pergunta)
                return f'Personalidade alterada para {self.personalidade}'
                
        # Fluxo padrão
        pergunta = t.detectar_comando(pergunta, self.conhecimentos_aprendidos)
        pergunta = t.detectar_comando(pergunta, self.base_conhecimento)

        if pergunta in self.comandos:
            self._processar_comando(pergunta)
            return f'Personalidade alterada para {self.personalidade}' # ---- ALTERAR ----

        if pergunta in self.base_conhecimento:
            return self._gerar_resposta(pergunta)

        elif pergunta in self.conhecimentos_aprendidos:
            resposta = self._gerar_resposta_aprendida(pergunta)
            resposta += '\nGostaria de cadastrar um nova resposta?'
            self.aguardando_aprendizado = True
            self.pergunta_desconhecida = pergunta
            return resposta

        else: 
            self.aguardando_aprendizado = True
            self.pergunta_desconhecida = pergunta
            return 'Desculpe, ainda não sei a responder isso.\nQuer cadastrar uma resposta?'
        

    def get_base_conhecimento():
        return

if __name__ == "__main__":

    historico = Historico()
    chatbot = ChatBot()

    # ----- TRECHO COM INPUT / PRINT -----
    if not historico.historico_vazio():
        ultimas_interacoes = historico.ler_ultimos(5)
        print('\n<<< Histórico Anterior de Conversas >>>')
        for linha in ultimas_interacoes:
            print(linha, end="")
        print('-------------------------------------------------')

    print(
        '\nSeja bem vindo (a) à plataforma NutriChat. Perguntas disponíveis (por enquanto):'
        '\nO que é uma alimentação saudável'
        '\nQuantos litros de água devo beber por dia'
        '\nQuais alimentos devo evitar\n'

        '\nOutras ações:'
        '\nTrocar personalidade'
        '\nSair'
    )

    historico.iniciar()

    while True:

        # ----- TRECHO COM INPUT / PRINT -----
        pergunta = input('\nDigite sua pergunta:\n')
        resposta = chatbot.responder(pergunta)
        print('\n— ',resposta)

        historico.salvar(pergunta, resposta, chatbot.personalidade)

        if chatbot.solicitado_sair:

            historico.gerar_estatisticas()
            historico.gerar_relatorio()

            print(
                "----Estatísticas----\n",
                f"Pergunta Mais Frequente: {historico.estatisticas["pergunta_mais_frequente"]}\n",
                f"Contagem de Interações: {historico.estatisticas["contagem_interacoes"]}\n",
                f"Personalidade Mais usada: {historico.estatisticas["personalidade_mais_usada"]}\n"
            )
            exit()   