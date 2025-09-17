import json
import random
import os
from typing import Optional
from utils.checagem_de_texto import Texto

class ChatController:

    def __init__(self, data_dir: Optional[str] = None):
        if data_dir is None:
            base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
            data_dir = os.path.join(base_dir, "data")
        self.data_dir = data_dir
        os.makedirs(self.data_dir, exist_ok=True)

        self.json_path = os.path.join(self.data_dir, "perguntas_e_respostas.json")
        self.txt_path = os.path.join(self.data_dir, "aprendizado.txt")

        # flag usada pela GUI para decidir se deve mostrar o widget
        self.pergunta_desconhecida = None

    @staticmethod
    def normalizar_pergunta(pergunta: str) -> str:
        return pergunta.strip().lower()

    def ler_resposta(self, pergunta: str, estilo: str = "formal") -> Optional[str]:
        # 1 - JSON
        try:
            with open(self.json_path, "r", encoding="utf-8") as f:
                dados = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            dados = {}

        if dados:
            # usa detectar_comando para encontrar a pergunta mais próxima
            perguntas_banco = list(dados.keys())
            pergunta_detectada = Texto.detectar_comando(pergunta, perguntas_banco)
            mapping = {}
            for k, v in dados.items():
                mapping[self.normalizar_pergunta(k)] = v

            pergunta_detectada_normalizada = self.normalizar_pergunta(pergunta_detectada)
            if pergunta_detectada_normalizada in mapping:
                possiveis = mapping[pergunta_detectada_normalizada]
                if isinstance(possiveis, dict) and estilo in possiveis:
                    escolhido = random.choice(possiveis[estilo]) if possiveis[estilo] else None
                    if escolhido:
                        self.pergunta_desconhecida = None
                        return escolhido
                if isinstance(possiveis, list) and possiveis:
                    escolhido = random.choice(possiveis)
                    self.pergunta_desconhecida = None
                    return escolhido

        # 2 - aprendizado.txt
        if os.path.exists(self.txt_path):
            try:
                with open(self.txt_path, "r", encoding="utf-8") as f:
                    perguntas_aprendizado = []
                    linhas = []
                    for linha in f:
                        linha = linha.strip()
                        if not linha:
                            continue
                        try:
                            pergunta_salva, resposta_salva = linha.split("|", 1)
                            perguntas_aprendizado.append(pergunta_salva)
                            linhas.append((pergunta_salva, resposta_salva))
                        except ValueError:
                            continue
                    pergunta_detectada = Texto.detectar_comando(pergunta, perguntas_aprendizado)
                    for pergunta_salva, resposta_salva in linhas:
                        if self.normalizar_pergunta(pergunta_salva) == self.normalizar_pergunta(pergunta_detectada):
                            self.pergunta_desconhecida = None
                            return resposta_salva
            except OSError:
                pass

        self.pergunta_desconhecida = pergunta
        return None
    
    def pergunta_existe(self, pergunta: str) -> bool:
        """Retorna True se a pergunta existe no JSON ou no aprendizado.txt."""
        pergunta_normalizada = self.normalizar_pergunta(pergunta)

        # verifica o JSON
        try:
            with open(self.json_path, "r", encoding="utf-8") as f:
                dados = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            dados = {}

        if dados:
            for k in dados.keys():
                if self.normalizar_pergunta(k) == pergunta_normalizada:
                    return True

        # verifica aprendizado.txt
        if os.path.exists(self.txt_path):
            try:
                with open(self.txt_path, "r", encoding="utf-8") as f:
                    for linha in f:
                        linha = linha.strip()
                        if not linha:
                            continue
                        try:
                            pergunta_salva, _ = linha.split("|", 1)
                        except ValueError:
                            continue
                        if self.normalizar_pergunta(pergunta_salva) == pergunta_normalizada:
                            return True
            except OSError:
                pass

        return False

    def responder(self, pergunta: str) -> str:
        """devolve resposta se souber, caso contrário retorna mensagem padrão."""
        resposta = self.ler_resposta(pergunta)
        if resposta is not None:
            return resposta
        return "Desculpe, ainda não sei responder isso. voçê pode me ensinar usando o campo 'me ensine uma nova resposta'."

    def aprender(self, pergunta: str, resposta: str) -> None:
        """Apende escrevendo no aprendizado.txt (formato: pergunta|resposta)."""
        pergunta_norm = pergunta.strip()
        resposta_norm = resposta.strip()
        if not pergunta_norm or not resposta_norm:
            return
        try:
            with open(self.txt_path, "a", encoding="utf-8") as f:
                f.write(f"{pergunta_norm}|{resposta_norm}\n")
            # após gravar, garante que pergunta_desconhecida seja limpa
            self.pergunta_desconhecida = None
        except OSError:
            #improvavel que aconteça, mas se acontecer, não quero que o bot quebre
            print("Erro ao salvar aprendizado")
