import json
import random

#resolvido o problema do caminho do json
#tinha de importar o caminho de todas as pastas até ele
#no caso, tinhamos 2 pastas nutri chat, vou remover uma depois

caminho_json = str("NutriChat/NutriChat/data/perguntas_e_respostas.json")


def ler_resposta(pergunta: str, estilo: str = "formal") -> str:
    """
    Lê o JSON de perguntas e retorna uma resposta no estilo que foi escolhido.
    """
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
    #path do caminho resolvido
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
