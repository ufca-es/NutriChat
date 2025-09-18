from utils.checagem_de_texto import Texto as t

class Personalidade:

    @staticmethod
    def selecionar_personalidade(resposta_usuario: str) -> str|bool:
        """
        Se o texto passado correspnder a uma personalidade, retorna a personalidade(str).
        Senão, retorna Falso(bool).
        """
        #provavelmente, colocar aqui uma opcao para deixar como True no gui, esse deve ser o problema
        opcoes_formal = ('1','formal', 'nutri bot')
        opcoes_engracado = ('2', 'engraçado', 'nutrilove')
        opcoes_rude = ('3', 'rude', 'chief')

        if t.detectar_comando(resposta_usuario, opcoes_formal) in opcoes_formal:
            return 'formal'

        elif t.detectar_comando(resposta_usuario, opcoes_engracado) in opcoes_engracado:
            return 'engraçado'

        elif t.detectar_comando(resposta_usuario, opcoes_rude) in opcoes_rude:
            return 'rude'
                
        else:
            return False