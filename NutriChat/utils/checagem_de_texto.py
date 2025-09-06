import string
from difflib import SequenceMatcher

class Utilitarios:
    
    def similaridade(msg_usuario: str, comando: str) -> float:
        return SequenceMatcher(None, msg_usuario.lower(), comando.lower()).ratio()
    
    def limpar_texto(texto: str) -> str:
        texto = texto.lower().strip()

        # Palavras que não carregam muito significado
        tokens_ignorados = {
            "poderia", "gostaria", "posso", "devo", "deveria"
            "eu", "me", "você", "voce", "vc",
            "quero", "são", "ser", "estar", "ter",
            "as", "os", "de", "do", "dos", "da", "das",
            "um", "uns", "uma", "umas",
            "em", "na", "nas", "no", "nos",
            "que", "para", "pr", "por", "com", "se"
        }
        
        # Remover pontuação
        texto = texto.translate(str.maketrans("", "", string.punctuation))

        palavras = texto.split()
        # Filtra removendo:
        # 1) palavras no conjunto tokens_ignorados
        # 2) palavras de tamanho 1 (len(p) == 1)
        palavras_filtradas = []
        for p in palavras:
            if p not in tokens_ignorados and len(p) > 1:
                palavras_filtradas.append(p)

        return " ".join(palavras_filtradas)
    
    def detectar_comando(msg_usuario, base_conhecimento) -> str:
        for pergunta in base_conhecimento:

            if Utilitarios.similaridade(
                Utilitarios.limpar_texto(msg_usuario), 
                Utilitarios.limpar_texto(pergunta)) > 0.85: # 85% de similariedade

                return pergunta
            
        return msg_usuario