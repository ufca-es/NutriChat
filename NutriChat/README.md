# Descrição do projeto

NutriChat

O NutriChat é um chatbot desenvolvido para auxiliar as pessoas na sua tomada de decisões quanto aos seus hábitos alimentares, visando o consumo consciente, a alimentação saudável e a redução do desperdício desses insumos.

O chatbot auxilia o usuário que quer mudar de dieta, seja com fins de perda de peso, aumento de massa magra ou que só deseje melhorar seus hábitos de consumo ao mesmo tempo que preza pela sustentabilidade e pelo bem do planeta. 

O NutriChat fornece respostas a partir das perguntas feitas pelo usuário e oferece dicas práticas e comprovadas de como montar refeições balanceadas.

A plataforma é simples e intuitiva, construída com algoritmos em Python. Utilizando conceitos de classes, funções, vetores, dicionários e outros conceitos importantes.

# Membros e suas funções

Letícia Maria  
Função: Redatora técnica

Atividades desempenhadas: 
Documentação do projeto.
Criação do READ.ME.
Criação das perguntas feitas pelo chat.

José Dhonathan  
Função: Front end

Atividades desempenhadas:
Criação da interface gráfica e integração com o back end

Gabriel
Função: Back end

Atividades desempenhadas:
Implementação das funcionalidades na plataforma.
Implementação da persistência no aprendizado.
Criação de classes, funções e vetores.

# Como executar: 

Para executar o NutriChat é muito simples. Basta clicar na barra de digitação na parte de baixo da interface e digitar uma mensagem de texto e em seguir clicar em enviar. A partir dessa mensagem o chat vai oferecer uma das respostas que estejam cadastradas na sua base de dados em formato .json
Caso a mensagem fornecida pelo usuário seja desconhecida pelo chatbot, será exibida uma resposta de que o ele não sabe responder, uma resposta será solicitada ao usuário e essa resposta ficará gravada na base de dados da plataforma, a partir desse momento.

No NutriChat o usuário tem o direito de escolher com qual personalidade deseja interagir. Temos três opções: a formal, a engraçado e a rude que podem ser trocadas a qualquer momento, ficando a critério do usuário.

Durante a execução o usuário pode fazer perguntas relacionadas a suas necessidades nutricionais, podendo ser relacionadas a desejos de mudanças nos hábitos alimentares, duvidas sobre alimentação saudável e conselhos para evitar o desperdicio dos alimentos.

# Demonstrações

A classe Personalidade representa a função de ser escolhida pelo usuário, uma das três personalidades que o chat dispôe. Dentro dessa classe, há a função selecionar_personalidade que serve para exibir as opções que o usuário pode digitar para o nome de cada personalidade, pois cada uma possui um número, um apelido e o seu adjetivo e fazer a seleção daquela que foi escolhida. 
Dentro da função também foi utilizado loop para que sempre seja possível fazer a troca e as estruturas condicionais que vão identificar qual foi a escolha feita pelo usuário para assim direcioná-lo para ela.

<img width="905" height="566" alt="image" src="https://github.com/user-attachments/assets/fa431f9e-d5e9-49a3-b4d4-abdaf6da9059" />

Nessa outra demonstração temos o loop usado para a identificação do que o usuário deseja que o chatbot exiba. Dentro desse loop, a variável "pergunta" armazena o texto digitado pelo usuário e o compara com informações existentes na base de dados do chat, caso o usuário digite "sair" a conversa será encerrada, caso digite "trocar personalidade" ele poderá escolher a personalidade novamente e caso o que for digitado esteja na base de dados, a resposta será dada. Agora se o que for digite não se relacionar com nenhuma dessas opções, o chat retorna que não sabe responder essa pergunta.

 <img width="733" height="500" alt="image" src="https://github.com/user-attachments/assets/132d6da3-31f8-4c79-8b25-8df88b7c4100" />


Caso as palavras chave da pergunta possuam 85% de similaridade com as que estão no sistema, o chatbot utilizará a resposta mais adequada que ele possui para aquele assunto, caso a pergunta tenha menos de 85% de similaridade o chat responde que não possui aquele conhecimento e solicita uma resposta, depois armazena essa resposta. É justamente para essa função que a classe "Utilitarios" foi usada, ela utiliza as funções para identificar a similaridade das perguntas, limpar o texto para remover palavras muito repetitivas e sinais de pontuação que não alteram o sentido da pergunta.

<img width="993" height="561" alt="image" src="https://github.com/user-attachments/assets/2e684a4a-574e-4606-8502-2d0df2e751bc" />

 
A função "ChatBot" foi criada para processar os comandos já mencionados para que o chat exiba sempre a melhor resposta.

<img width="986" height="590" alt="image" src="https://github.com/user-attachments/assets/8807d96f-83db-486e-a3b8-e491dc6262fc" />




Para mais informações, acesse a nossa documentação do projeto: https://github.com/ufca-es/NutriChat/blob/444317e36009f1064c137b44bd991dbef85b4238/documentacao.md
