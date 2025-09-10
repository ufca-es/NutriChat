class Aprendizado:
    def __init__(self, arquivo="data/aprendizado.txt"):
        self.arquivo = arquivo
        self.conhecimentos = {
            # "pergunta1": ["r1", "r2", ...],
            # "pergunta2": ["r1", "r2", ...]
        }

    def salvar(self, pergunta: str, resposta: str):

        pergunta = pergunta.replace("|", " ")
        resposta = resposta.replace("|", " ")

        with open(self.arquivo, "a", encoding="utf-8") as arq:
            arq.write(f"{pergunta}|{resposta}\n")

    def carregar(self):
        try:
            with open(self.arquivo, "r", encoding="utf-8") as arq:
                for linha in arq:
                    pergunta, resposta = linha.strip().split("|", 1)

                    if pergunta not in self.conhecimentos:
                        self.conhecimentos[pergunta] = []

                    self.conhecimentos[pergunta].append(resposta)

        except FileNotFoundError:
            pass

        return self.conhecimentos