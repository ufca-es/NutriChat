import os
import json
import random

class Bot:
    def __init__(self):
        self.caminho_json = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            "data", "perguntas_e_respostas.json"
        )

    def gerar_resposta(self, pergunta, estilo="formal"):
        """
        Gera resposta do bot baseada no arquivo perguntas_e_respostas.json.
        """
        try:
            with open(self.caminho_json, "r", encoding="utf-8") as carregar_json:
                dados = json.load(carregar_json)

            pergunta = pergunta.strip().lower()
            if pergunta not in dados:
                return f"Desculpe, não conheço a pergunta: '{pergunta}'."

            if estilo not in dados[pergunta]:
                return f"O estilo '{estilo}' não está disponível para essa pergunta."

            return random.choice(dados[pergunta][estilo])

        except FileNotFoundError:
            return f"Erro: arquivo '{self.caminho_json}' não encontrado."
        except json.JSONDecodeError:
            return "Erro: JSON inválido."
        except Exception as e:
            return f"Ocorreu um erro: {e}"