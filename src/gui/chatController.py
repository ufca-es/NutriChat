import json
import random
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

    def ler_resposta(pergunta: str, estilo: str = "formal") -> str:
        """
        Lê o JSON de perguntas e retorna uma resposta no estilo que foi escolhido.
        """
        caminho_json = str("NutriChat/NutriChat/data/perguntas_e_respostas.json")
        try:
            with open(caminho_json, "r", encoding="utf-8") as carregar_json:
                dados = json.load(carregar_json)

            if pergunta not in dados:
                return f"Desculpe, não conheço a pergunta: '{pergunta}'."

            if estilo not in dados[pergunta]:
                return f"O estilo '{estilo}' não está disponível para essa pergunta."

            return random.choice(dados[pergunta][estilo])

        except FileNotFoundError:
            return f"Erro: arquivo '{caminho_json}' não encontrado."
        except json.JSONDecodeError:
            return "Erro: JSON inválido."
        except Exception as e:
            return f"Ocorreu um erro: {e}"

    if __name__ == "__main__":
        caminho_json = "NutriChat/NutriChat/data/perguntas_e_respostas.json"
        print("=== NutriChat ===")
        print("Digite 'sair' para encerrar.")
        
        while True:
            pergunta = input("\nVocê: ").strip().lower()
            if pergunta == "sair":
                break

            estilo = input("Escolha o estilo (formal, engracado, rude): ").strip().lower()

            resposta = ler_resposta(pergunta, estilo)
            print("Bot:", resposta)
