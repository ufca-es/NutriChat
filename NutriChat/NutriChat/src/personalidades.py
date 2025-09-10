class Personalidade:
        
    def selecionar_personalidade() -> str:
        opcoes_formal = ('1', 'formal', 'n.u.t.r.i. bot')
        opcoes_engraçado = ('2', 'engraçado', 'nutrilove')
        opcoes_rude = ('3', 'rude', 'chief')

        while True:
            personalidade = input('Com qual personagem você deseja conversar? ').strip().lower()

            if personalidade in opcoes_formal:
                return 'formal'

            elif personalidade in opcoes_engraçado:
                return 'engracado'

            elif personalidade in opcoes_rude:
                return 'rude'
                

            else:
                print('Essa personalidade não está disponível. Tente novamente.')