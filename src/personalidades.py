class Personalidade:
        
    def selecionar_personalidade() -> str:
        opcoes_formal = ('1', 'formal', 'n.u.t.r.i. bot')
        opcoes_engraçado = ('2', 'engraçado', 'engracado', 'engraçada', 'engracada', 'nutrilove')
        opcoes_rude = ('3', 'rude', 'chief')

        while True:
            # ----- TRECHO COM INPUT / PRINT -----
            personalidade = input(
                '\nCom qual personagem você deseja conversar? '
                '\n( 1 ) N.U.T.R.I Bot (formal)'
                '\n( 2 ) NutriLove (engraçada)'
                '\n( 3 ) Chief (rude)\n'
            ).strip().lower()

            if personalidade in opcoes_formal:
                return 'formal'

            elif personalidade in opcoes_engraçado:
                return 'engraçado'

            elif personalidade in opcoes_rude:
                return 'rude'
                
            else:
                print('Essa personalidade não está disponível. Tente novamente.')