# Documentação do Projeto NutriChat

O chatbot NutriChat desenvolvido no projeto da disciplina de Fundamentos de Programação é uma chat para dicas nutricionais, oferecendo dicas de dietas saudáveis e bons hábitos de consumo para incentivar as pessoas a evitar o desperdício e cultivar a sustentabilidade.

# Principais funcionalidades
O usuário pode fazer perguntas a respeito de como deve elaborar a sua dieta, conforme as suas necessidades. O chat responderá essas perguntas oferecendo ideias de refeições balanceadas. O chat pode agir de três maneiras diferentes a depender da personalidade escolhida pelo usuário: formal, alegre ou rude.
Ao inicializar o programa o usuário seleciona essa personalidade:

# Personalidades do chat
N.U.T.R.I BOT: É a versão mais formal do chat, ele responde de maneira mais simples e com comportamento similar ao das inteligências artificiais.
NutriLove: É a versão alegre, tem um jeito engraçado e um pouco mais informal de responder. Seu comportamento é baseado na ideia de um nutricionista amigável e brincalhão.
NutriChief ou só Chief: É a versão rude do chat, ele responde maneira direta, é mais imperativo e gosta de dar lições no lugar de dicas. 


# Tecnologias utilizadas
Python - linguagem simples e com testagem rápida para Machine Learning.

# Conceitos utilizados:
Interface gráfica de usuário (GUI) Estruturas condicionais para fluxo de atendimento com tomada de decisão. Listas para armazenamento de dados temporários. Dicionários para representar entidades ou mapeamentos. Modularização com funcões e classes.

# Tema do chatbot: 
Educação alimentar, saúde e bem-estar.

# Classes de domínio e módulos do projeto:

A classe Personalidade representa a função de ser escolhida pelo usuário, uma das três personalidades que o chat dispôe. Dentro dessa classe, há a função selecionar_personalidade que serve para exibir as opções que o usuário pode digitar para o nome de cada personalidade, pois cada uma possui um número, um apelido e o seu adjetivo e fazer a seleção daquela que foi escolhida. 
Dentro da função também foi utilizado loop para que sempre seja possível fazer a troca e as estruturas condicionais que vão identificar qual foi a escolha feita pelo usuário para assim direcioná-lo para ela.

<img width="905" height="566" alt="image" src="https://github.com/user-attachments/assets/fa431f9e-d5e9-49a3-b4d4-abdaf6da9059" />

Nessa outra demonstração temos o loop usado para a identificação do que o usuário deseja que o chatbot exiba. Dentro desse loop, a variável "pergunta" armazena o texto digitado pelo usuário e o compara com informações existentes na base de dados do chat, caso o usuário digite "sair" a conversa será encerrada, caso digite "trocar personalidade" ele poderá escolher a personalidade novamente e caso o que for digitado esteja na base de dados, a resposta será dada. Agora se o que for digite não se relacionar com nenhuma dessas opções, o chat retorna que não sabe responder essa pergunta.

 <img width="733" height="500" alt="image" src="https://github.com/user-attachments/assets/132d6da3-31f8-4c79-8b25-8df88b7c4100" />


Caso as palavras chave da pergunta possuam 85% de similaridade com as que estão no sistema, o chatbot utilizará a resposta mais adequada que ele possui para aquele assunto, caso a pergunta tenha menos de 85% de similaridade o chat responde que não possui aquele conhecimento e solicita uma resposta, depois armazena essa resposta. É justamente para essa função que a classe "Utilitarios" foi usada, ela utiliza as funções para identificar a similaridade das perguntas, limpar o texto para remover palavras muito repetitivas e sinais de pontuação que não alteram o sentido da pergunta.

<img width="993" height="561" alt="image" src="https://github.com/user-attachments/assets/2e684a4a-574e-4606-8502-2d0df2e751bc" />

 
A função "ChatBot" foi criada para processar os comandos já mencionados para que o chat exiba sempre a melhor resposta.

<img width="986" height="590" alt="image" src="https://github.com/user-attachments/assets/8807d96f-83db-486e-a3b8-e491dc6262fc" />


 

# Respostas aleatórias para a mesma pergunta.

# Persistência de aprendizado

# Apresentação do histórico anterior ao iniciar

# Histórico de conversas da sessão em arquivo .txt.

#	Coleta de estatísticas:

# Exibição de sugestões de perguntas frequentes:

# Arquivo de perguntas/respostas 
Para acessar o arquivo  com as perguntas e respostas do chatbot, acesse: https://github.com/ufca-es/NutriChat/blob/309ff59a119742e92d23d316cd1d0f808af3b2a0/NutriChat/data/perguntas_e_respostas.json

# Rascunho do fluxo básico de conversa



- Como o projeto comtribui com a sociedade 
