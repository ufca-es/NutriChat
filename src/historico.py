from datetime import datetime

class Historico:
    def __init__(self, arquivo="data/historico.txt"):
        self.arquivo = arquivo

    def salvar(self, pergunta: str, resposta: str, personalidade: str):

        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")  # Formato: dia/mês/ano hora:minuto:segundo

        with open(self.arquivo, "a", encoding="utf-8") as arq:
            arq.write(f"\n[{data_hora}] Usuário: {pergunta}\n[{data_hora}] Bot[{personalidade}]: {resposta}\n")

    def ler_ultimos(self, limite=5):
        try:
            with open(self.arquivo, "r", encoding="utf-8") as arq:
                linhas = arq.readlines()
                return linhas[-(limite * 3):]  # 3 linhas por interação
        except FileNotFoundError:
            return []
        
    def historico_vazio(self):
        try:
            with open(self.arquivo, "r", encoding="utf-8") as arq:
                conteudo = arq.read().strip()
                return conteudo == "" 
        except FileNotFoundError:
            return True
