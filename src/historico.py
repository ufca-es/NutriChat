import json
from datetime import datetime
from collections import Counter
from utils.checagem_de_texto import Texto as t
import os

class Historico:
    def __init__(self, arquivo="data/historico.txt"):
        self.arquivo = arquivo

        # carrega base de conhecimento com segurança
        try:
            with open('data/perguntas_e_respostas.json', "r", encoding="utf-8") as arq:
                self.base_conhecimento = json.load(arq)
        except (FileNotFoundError, json.JSONDecodeError):
            self.base_conhecimento = {}

        # carrega aprendizado (linhas) com segurança
        try:
            with open('data/aprendizado.txt', "r", encoding="utf-8") as arq:
                self.base_aprendizado = arq.readlines()
        except FileNotFoundError:
            self.base_aprendizado = []

        # listas usadas para estatísticas — serão resetadas em gerar_estatisticas
        self.perguntas = []
        self.personalidades = []
        self.estatisticas = {}

    def iniciar(self):
        """
        Escreve uma linha no hitórico para indicar o início de uma interação.
        """
        with open(self.arquivo, "a", encoding="utf-8") as arq:
            arq.write("\n<<< inicio da seção >>>\n<<<=================>>>\n")
            
    def salvar(self, pergunta: str, resposta: str, personalidade: str):
        """
        Salva uma interação no histórico.
        """
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")  # Formato: dia/mês/ano hora:minuto:segundo

        with open(self.arquivo, "a", encoding="utf-8") as arq:
            arq.write(f"\n[{data_hora}] Usuário: {pergunta}\n[{data_hora}] Bot[{personalidade}]: {resposta}\n")

    def ler_ultimos(self, limite=5):
        """
        Lê e retorna as últimas interações.
        """
        try:
            with open(self.arquivo, "r", encoding="utf-8") as arq:
                linhas = arq.readlines()
                return linhas[-(limite * 3):]  # 3 linhas por interação
        except FileNotFoundError:
            return []
        
    def registro_vazio(self):
        """
        Checa se há algo escrito no histórico.
        """
        try:
            with open(self.arquivo, "r", encoding="utf-8") as arq:
                conteudo = arq.read().strip()
                return conteudo == "" 
        except FileNotFoundError:
            return True
        
    def ler_todo_conteudo(self):
        """Lê todo o histórico e retorna como lista de linhas."""
        try:
            with open(self.arquivo, "r", encoding="utf-8") as arq:
                return arq.readlines()
        except FileNotFoundError:
            return []

    def ultima_sessao(self):
        """
        Retorna a última sessão completa do histórico como lista de linhas.
        Uma sessão começa na linha '<<< inicio da interacao >>>'
        e vai até o final do arquivo.
        """
        try:
            with open(self.arquivo, "r", encoding="utf-8") as arq:
                linhas = arq.readlines()

        # Procura a última ocorrência do marcador de início
            for i in range(len(linhas) - 1, -1, -1):
                if "<<<=================>>>" in linhas[i]:
                    return linhas[i:]  # retorna do marcador até o fim

            return linhas  # se não achar marcador, retorna tudo

        except FileNotFoundError:
            return []
        
    def perguntas_frequentes(self):
        perguntas_feitas = []

        # Lê todas as linhas do histórico
        try:
            with open(self.arquivo, "r", encoding="utf-8") as arq:
                for linha in arq:
                    if "Usuário:" in linha:
                        pergunta = linha.split("Usuário:")[1].strip()
                        pergunta = t.detectar_comando(pergunta, self.base_conhecimento)
                        pergunta = t.detectar_comando(pergunta, self.base_aprendizado)
                        perguntas_feitas.append(pergunta)
        except FileNotFoundError:
            return []

        # Pega as 3 mais comuns (se houver menos, retorna só as disponíveis)
        perguntas_mais_frequentes = [p for p, _ in Counter(perguntas_feitas).most_common(3)]

        return perguntas_mais_frequentes


        
    def gerar_estatisticas(self):
        """
        Gera estatísticas do histórico:
        - pergunta mais frequente
        - número de interações
        - personalidade mais usada

        Reinicia as listas para evitar acumulo em chamadas repetidas.
        """
        # reinicia contadores locais para cada execução
        self.perguntas = []
        self.personalidades = []

        for linha in self.ultima_sessao():
            if "Usuário:" in linha:
                pergunta = linha.split("Usuário:")[1].strip()
                # tenta normalizar/combinar com conhecimento/aprendizado
                try:
                    pergunta = t.detectar_comando(pergunta, self.base_conhecimento)
                except Exception:
                    pass
                try:
                    pergunta = t.detectar_comando(pergunta, self.base_aprendizado)
                except Exception:
                    pass
                self.perguntas.append(pergunta)

            elif "Bot[" in linha:
                personalidade = linha.split("Bot[")[1].split("]")[0]
                self.personalidades.append(personalidade)

        # trata listas vazias para evitar IndexError
        if self.perguntas:
            pergunta_mais_frequente = Counter(self.perguntas).most_common(1)[0]
        else:
            pergunta_mais_frequente = ("", 0)

        if self.personalidades:
            personalidade_mais_usada = Counter(self.personalidades).most_common(1)[0]
        else:
            personalidade_mais_usada = ("N/A", 0)

        self.estatisticas = {
            "pergunta_mais_frequente": pergunta_mais_frequente,
            "contagem_interacoes": len(self.perguntas),
            "personalidade_mais_usada": personalidade_mais_usada
        }

    def gerar_relatorio(self):
         # sobe de /src para a raiz
         
        self.gerar_estatisticas() 
         
        base_dir = os.path.dirname(os.path.dirname(__file__))
        caminho_relatorio = os.path.join(base_dir, "data", "relatorio.txt")

        #troquei "a"(append) para "w" (write) para reiniciar
        #o relatório a cada vez que o user precisa gerar relatório
        with open(caminho_relatorio, "w", encoding="utf-8") as arq:
            for linha in self.ultima_sessao():
                arq.write(linha)

            arq.write("----Estatísticas----\n")
            arq.write(f"Pergunta Mais Frequente: {self.estatisticas['pergunta_mais_frequente']}\n")
            arq.write(f"Contagem de Interações: {self.estatisticas['contagem_interacoes']}\n")
            arq.write(f"Personalidade Mais usada: {self.estatisticas['personalidade_mais_usada']}\n")

        return caminho_relatorio 
    
    def reiniciar_relatorio(self):
        with open("data/relatorio.txt", "w", encoding="utf-8") as arq:
            arq.write('')
    