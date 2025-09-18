from src.chatbot import ChatBot
from src.historico import Historico
from src.gui.iniciarChatGrafico import Root

if __name__ == "__main__":

    app = Root()
    app.mainloop()

    historico = Historico()
    chatbot = ChatBot()

    if not historico.registro_vazio():
        ultimas_interacoes = historico.ler_ultimos(5)
        print('\n<<< Histórico Anterior de Conversas >>>')
        for linha in ultimas_interacoes:
            print(linha, end="")
        print('-------------------------------------------------')

    print(
        '\nSeja bem vindo (a) à plataforma NutriChat.'

        '\nOutras ações:'
        '\nTrocar personalidade'
        '\nSair'
    )
    print('Perguntas frequntes:')
    for i in historico.perguntas_frequentes():
       print('- ', i)

    historico.iniciar()
    historico.reiniciar_relatorio()

    while True:

        pergunta = input('\n<Digite algo: >\n')
        resposta = chatbot.responder(pergunta)
        print('\n— ',resposta)

        historico.salvar(pergunta, resposta, chatbot.personalidade)

        if chatbot.solicitado_sair:

            historico.gerar_estatisticas()
            historico.gerar_relatorio()

            print(
                "----Estatísticas----\n",
                f"Pergunta Mais Frequente: {historico.estatisticas["pergunta_mais_frequente"]}\n",
                f"Contagem de Interações: {historico.estatisticas["contagem_interacoes"]}\n",
                f"Personalidade Mais usada: {historico.estatisticas["personalidade_mais_usada"]}\n"
            )
            exit()   