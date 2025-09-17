# src/gui/chatController.py
from src.chatbot import ChatBot

class ChatController:
    def __init__(self):
        self.chatbot = ChatBot()

    def responder(self, pergunta: str) -> str:
        """
        Processa uma pergunta e retorna a resposta para exibir na GUI.
        """
        resposta = self.chatbot.responder(pergunta)

        # salva no histórico
        self.chatbot.historico.salvar(
            pergunta, resposta, self.chatbot.personalidade
        )

        # Se a pergunta é desconhecida, o ChatBot já devolve
        # "Desculpe, ainda não sei responder isso."
        # Então basta repassar esse texto para a GUI
        return resposta

    def trocar_personalidade(self, nova_personalidade: str):
        self.chatbot.personalidade = nova_personalidade

    def precisa_aprender(self) -> bool:
        return self.chatbot.pergunta_desconhecida

    def aprender(self, pergunta: str, resposta: str):
        """
        Ensina uma nova resposta ao bot (chamado pela GUI).
        """
        self.chatbot.aprendizado.salvar(pergunta, resposta)
        self.chatbot.conhecimentos_aprendidos = self.chatbot.aprendizado.carregar()
        self.chatbot.pergunta_desconhecida = False
