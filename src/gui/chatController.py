
from src.main import ChatBot

class ChatController:
    """
    Controlador do chatBot
    """
    def __init__(self):
        self.chatbot = ChatBot()

    def responder(self, pergunta: str) -> str:
        """
        Processa uma pergunta e retorna a resposta para exibir na gui. \n
        :param: pergunta: a pergunta que o user vai digitar
        """
        resposta = self.chatbot.responder(pergunta)

        # salva no histórico
        self.chatbot.historico.salvar(
            pergunta, resposta, self.chatbot.personalidade
        )

        # Se a pergunta é desconhecida, o ChatBot devolve
        # "Desculpe, ainda não sei responder isso."
        return resposta

    def trocar_personalidade(self, nova_personalidade: str):
        self.chatbot.personalidade = nova_personalidade

    def precisa_aprender(self) -> bool:
        
        return self.chatbot.pergunta_desconhecida

    def aprender(self, pergunta: str, resposta: str):
        """
        Ensina uma nova resposta ao bot (chamado pela GUI).\n
        :param: pergunta: oque o user vai digitar para o bot salvar\n
        :param: resposta: oque o bot vai salvar em /data/aprendizado
        """
        self.chatbot.aprendizado.salvar(pergunta, resposta)
        self.chatbot.conhecimentos_aprendidos = self.chatbot.aprendizado.carregar()
        self.chatbot.pergunta_desconhecida = False
