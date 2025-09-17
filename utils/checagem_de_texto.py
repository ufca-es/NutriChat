import string
from difflib import SequenceMatcher
from utils.tokens import Tokens

class Texto:
        
    @staticmethod
    def similaridade(msg_usuario: str, comando: str) -> float:
        """
        Checa a similariedade entre duas Strings e retorna um número
        entre 0 e 1. quanto mais similar, mais próximo de 1.
        """
        return SequenceMatcher(None, msg_usuario.lower(), comando.lower()).ratio()

    @staticmethod
    def limpar_texto(texto: str) -> str:
        """
        Retorna um texto com sem pontuação e com mais palavras núcleo.
        """
        texto = texto.lower().strip()
        # Remover pontuação
        texto = texto.translate(str.maketrans("", "", string.punctuation))

        palavras = texto.split()
        # Filtra removendo:
        # 1) palavras no conjunto tokens_ignorados
        # 2) palavras de tamanho 1 (len(p) == 1)
        palavras_filtradas = []
        for p in palavras:
            if p not in Tokens.ignorados and len(p) > 1:
                palavras_filtradas.append(p)

        return " ".join(palavras_filtradas)
    
    @staticmethod
    def detectar_comando(txt_usuario: str, base_dados) -> str:
        """
        Recebe uma String e um conjunto de Strings. Se a String passada for
        similar sufiente, a função retorna uma correspondete do conjuto.
        Senão, retorna a própria String recebida.
        """
        for pergunta in base_dados:

            if Texto.limpar_texto(txt_usuario) == '':
                return txt_usuario

            elif Texto.similaridade(
                Texto.limpar_texto(txt_usuario), 
                Texto.limpar_texto(pergunta)
            ) > 0.85: # 85% de similariedade

                return pergunta
            
        return txt_usuario