import random

class Personalidade:
    def __init__(self, nome, respostas):
        """
        nome: string com o nome da personalidade (ex: 'formal', 'engraçada')
        respostas: dicionário {pergunta: [lista de respostas possíveis]}
        """
        self.nome = nome
        self.respostas = respostas
    
    def responder(self, pergunta):
        pergunta = pergunta.lower()
        if pergunta in self.respostas:
            return random.choice(self.respostas[pergunta])
        else:
            return "Ainda não sei responder isso."
        
    def selecionar_personalidade():
        opcoes_formal = ('1', 'formal', 'n.u.t.r.i. bot')
        opcoes_engraçado = ('2', 'engraçado')
        opcoes_rude = ('3', 'rude',)

        while True:
            personalidade = input('Com qual personagem você deseja conversar? ').strip().lower()

            if personalidade in opcoes_formal:
                return 'formal'

            elif personalidade in opcoes_engraçado:
                return 'engraçado'

            elif personalidade in opcoes_rude:
                return 'rude'
                

            else:
                print('Essa personalidade não está disponível. Tente novamente.')