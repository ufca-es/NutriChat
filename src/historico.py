import json
from datetime import datetime
from collections import Counter
from utils.checagem_de_texto import Texto as t

class Historico:
    def __init__(self, arquivo="data/historico.txt"):
        self.arquivo = arquivo

        with open('data/perguntas_e_respostas.json', "r", encoding="utf-8") as arq:
            self.base_conhecimento = json.load(arq)

        with open('data/aprendizado.txt', "r", encoding="utf-8") as arq:
            self.base_aprendizado = arq.readlines()

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
        
    def historico_vazio(self):
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
        
    #def perguntas_frequentes():
        
    def gerar_estatisticas(self):
        """"
        Gera estatísticas do histórico:
        - pergunta mais frequente
        - número de interações
        - personalidade mais usada
        """

        for linha in self.ultima_sessao():
            
            if "Usuário:" in linha:
                pergunta = linha.split("Usuário:")[1].strip()
                pergunta = t.detectar_comando(pergunta, self.base_conhecimento)
                pergunta = t.detectar_comando(pergunta, self.base_aprendizado)
                self.perguntas.append(pergunta)

            elif "Bot[" in linha:
                personalidade = linha.split("Bot[")[1].split("]")[0]
                self.personalidades.append(personalidade)

            pergunta_mais_frequente = Counter(self.perguntas).most_common(1)[0]
            personalidade_mais_usada = Counter(self.personalidades).most_common(1)[0]

        self.estatisticas = {
            "pergunta_mais_frequente": pergunta_mais_frequente,
            "contagem_interacoes": len(self.perguntas),
            "personalidade_mais_usada": personalidade_mais_usada
        }

    def gerar_relatorio(self):
        with open("data/relatorio.txt", "a", encoding="utf-8") as arq:

            for linha in self.ultima_sessao():
                arq.write(linha)

            arq.write("----Estatísticas----")
            arq.write("Pergunta Mais Frequente: ", self.estatisticas["pergunta_mais_frequente"])
            arq.write("Contagem de Interações: ", self.estatisticas["contagem_interacoes"])
            arq.write("Personalidade Mais usada: ", self.estatisticas["personalidade_mais_usada"])


    