# Documentação do Projeto NutriChat

O chatbot NutriChat desenvolvido no projeto da disciplina de Fundamentos de Programação é uma chat para dicas nutricionais, oferecendo dicas de dietas saudáveis e bons hábitos de consumo para incentivar as pessoas a evitar o desperdício e cultivar a sustentabilidade.

# Tópicos explorados na documentação:

1 - Principais funcionalidades
2 - Personalidades do chat
3 - Tecnologias utilizadas
4 - Conceitos utilizados
5 - Classes de projeto e módulos
6 - Como o código está organizado
7 - Diferenciais
8 - Modo de aprendizado
9 - Histórico
10 - Boas práticas
11 - Perguntas com respostas cadastradas no Chat

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
Bibliotecas utilizadas:
- pathlib, tkinter, json, random, time e os.


# Conceitos utilizados:
Interface gráfica de usuário (GUI) Estruturas condicionais para fluxo de atendimento com tomada de decisão. Listas para armazenamento de dados temporários. Dicionários para representar entidades ou mapeamentos. Modularização com funcões e classes.

# Classes de projeto e módulos:

A classe Personalidade representa a função de ser escolhida pelo usuário, uma das três personalidades que o chat dispôe. Dentro dessa classe, há a função selecionar_personalidade que serve para exibir as opções que o usuário pode digitar para o nome de cada personalidade, pois cada uma possui um número, um apelido e o seu adjetivo e fazer a seleção daquela que foi escolhida. 
Dentro da função também foi utilizado loop para que sempre seja possível fazer a troca e as estruturas condicionais que vão identificar qual foi a escolha feita pelo usuário para assim direcioná-lo para ela.

<img width="905" height="566" alt="image" src="https://github.com/user-attachments/assets/fa431f9e-d5e9-49a3-b4d4-abdaf6da9059" />

Nessa outra demonstração temos o loop usado para a identificação do que o usuário deseja que o chatbot exiba. Dentro desse loop, a variável "pergunta" armazena o texto digitado pelo usuário e o compara com informações existentes na base de dados do chat, caso o usuário digite "sair" a conversa será encerrada, caso digite "trocar personalidade" ele poderá escolher a personalidade novamente e caso o que for digitado esteja na base de dados, a resposta será dada. Agora se o que for digite não se relacionar com nenhuma dessas opções, o chat retorna que não sabe responder essa pergunta.

 <img width="733" height="500" alt="image" src="https://github.com/user-attachments/assets/132d6da3-31f8-4c79-8b25-8df88b7c4100" />


Caso as palavras chave da pergunta possuam 85% de similaridade com as que estão no sistema, o chatbot utilizará a resposta mais adequada que ele possui para aquele assunto, caso a pergunta tenha menos de 85% de similaridade o chat responde que não possui aquele conhecimento e solicita uma resposta, depois armazena essa resposta. É justamente para essa função que a classe "Utilitarios" foi usada, ela utiliza as funções para identificar a similaridade das perguntas, limpar o texto para remover palavras muito repetitivas e sinais de pontuação que não alteram o sentido da pergunta.

<img width="993" height="561" alt="image" src="https://github.com/user-attachments/assets/2e684a4a-574e-4606-8502-2d0df2e751bc" />


A função "ChatBot" foi criada para processar os comandos já mencionados para que o chat exiba sempre a melhor resposta.

<img width="986" height="590" alt="image" src="https://github.com/user-attachments/assets/8807d96f-83db-486e-a3b8-e491dc6262fc" />


# ⁠Como o código está organizado

<img width="352" height="290" alt="image" src="https://github.com/user-attachments/assets/10fc3b39-8e33-4e31-8eb0-c7174a907cb2" />

O código foi organizado na estrutura da imagem acima, sendo a pasta data, o lugar onde estão salvos os dados de perguntas, respostas, aprendizado e histórico.
A pasta Source, armazena as classes de projeto do Chat e uma subpasta GUI, onde estão os arquivos da interface gráfica que será exibida para o usuário
Na pasta Utils, há algumas funções uteis que são a checagem do texto para filtra-lo por palavras chave, e removendo aquelas palavras que devem ser ignoradas, por não alterar o sentido do texto.
Fora dessas pastas tem os arquivos de documentação e README que explicam como o Chat funciona e como foi desenvolvido.
No arquivo main temos as funcionalidades principais conversando para a execução do chat, de maneira que todas os demais arquivos consigam se relacionar.

# ⁠Apresentação de diferenciais do código.

Metodologia usada para mudar de personalidade
A lógica para mudar a personalidade do chatbot está no arquivo personalidades.py. A ideia é manter essa funcionalidade separada do código principal do bot, usando a orientação a objetos a partir das nossas classes de projeto.
Dentro de personalidades.py: A classe Personalidade contém um método chamado selecionar_personalidade. O @staticmethod foi usado para chamar a classe Personalidade.selecionar_personalidade() sem precisar criar uma instancia.

 <img width="701" height="102" alt="image" src="https://github.com/user-attachments/assets/28b304a7-e724-4088-8ada-6a6fa0fe481d" />

O método recebe a resposta do usuário e tem uma lista de palavras-chave para detectar a personalidade, que são: opcoes_formal, opcoes_engracado e opcoes_rude. 

 <img width="536" height="85" alt="image" src="https://github.com/user-attachments/assets/1af41323-656d-40db-8e70-6dbc366be240" />

A função detectar_comando do arquivo checagem_de_texto.py é usada para verificar se a resposta do usuário é similar a alguma dessas opções.

<img width="722" height="67" alt="image" src="https://github.com/user-attachments/assets/1d13222d-f34e-4bd5-8e8f-6cf4c21a16ae" />

Aqui temos um exemplo das estruturas condicionais sendo utilizadas para que a personalidade seja detectada corretamente.

<img width="722" height="131" alt="image" src="https://github.com/user-attachments/assets/0417889c-e376-4a66-9dba-d26f73f35637" />

Como exibido na imagem acima. No arquivo chatbot.py, o método responder verifica se o usuário solicitou uma mudança de personalidade. Se sim, ele chama a função Personalidade.selecionar_personalidade com a resposta do usuário. Se a função retornar um nome de personalidade, o atributo self.personalidade do chatbot é atualizado com o novo valor, e a conversa continua com o novo "humor". 

Atualização da Base de Perguntas e Respostas
A lógica para que novas perguntas sejam salvas está nos arquivos chatbot.py e aprendizado.py. Quando a pergunta do usuário ao ser buscada no arquivo perguntas_e_respostas.json não é encontrada, ele entra em modo de aprendizado.

<img width="838" height="113" alt="image" src="https://github.com/user-attachments/assets/ca075aba-43e1-428b-87ae-a9ae6d2eabf5" />

# O modo de Aprendizado

O bot identifica que a pergunta é desconhecida e armazena-a na variável self.pergunta_desconhecida. 
Então pergunta ao usuário: "Desculpe, ainda não sei a responder isso. Quer cadastrar uma resposta?". A variável self.aguardando_aprendizado é definida como True.
Se o usuário responder que sim, a variável self.solicitado_aprendizado é ativada. O chatbot então pede para que seja digitada a resposta.
Quando a nova resposta é digitada, o método salvar do objeto aprendizado é chamado:

<img width="610" height="188" alt="image" src="https://github.com/user-attachments/assets/801cc9b5-a041-49c2-a5f4-45ba22037f56" />

E o arquivo aprendizado.txt recebe as novas informações no formato pergunta|resposta
A função carregar() da mesma classe lê esse arquivo e armazena todas as perguntas e respostas em um dicionário, que é usado pelo chatbot para procurar as respostas cadastradas pelo usuário para quando forem solicitadas por perguntas com pelo menos 85% de semelhança no futuro.

<img width="665" height="260" alt="image" src="https://github.com/user-attachments/assets/e89c9a6d-acec-4f05-ae25-91fff1817c59" />

 # Histórico 

A classe Historico presente no arquivo historico.py serve para registrar as perguntas e respostas das interações que o usuário teve com o chat. Ela utiliza a mesma lógica das classe de aprendizado ao registrar as mensagens em um arquivo txt, só que age de maneira diferente ao registrar todas as mensagens e não só as desconhecidas. Exemplo:

<img width="822" height="225" alt="image" src="https://github.com/user-attachments/assets/319d6473-dd3f-4526-a5f6-c153fcc95a72" />

# Boas práticas aplicadas ao código

No nosso projeto, utilizamos boas práticas tanto na organização dos códigos quanto no planejamento. 
O uso de comentários antes de cada função importante, variáveis autodescritivas, padrões para nomenclatura de classes e organização dos arquivos em pastas. Como é possível observar neste exemplo: 

<img width="741" height="350" alt="image" src="https://github.com/user-attachments/assets/ecd9906c-a17c-4fcc-b544-fdab22bd5b08" />

Utilizamos a orientação a objetos para que o código não ficasse confuso com muitas classes diferentes no mesmo arquivo podendo ser utilizadas para funções diversas. Tornando muito verboso e difícil de organizar. Dessa forma, apresentamos nossas classes da seguinte maneira. 

# Perguntas com respostas cadastradas no Chat

1. o que é uma alimentação saudável?
2. quantos litros de água devo beber por dia?
3. quais alimentos devo evitar?
4. quantas refeições por dia são recomendadas?
5. o que é uma dieta equilibrada?
6. por que é importante variar os alimentos consumidos?
7. comer muito rápido pode prejudicar a digestão?
8. quantas porções de frutas é recomendado consumir diariamente?
9. por que devo incluir verduras e legumes em todas as refeições?
10. qual a diferença entre comer frutas inteiras e tomar sucos?
11. quais frutas são ricas em vitamina C?
12. o que pode acontecer se eu não consumir vegetais regularmente?
13. quais são as principais fontes de proteína?
14. o que são proteínas e qual a sua função no corpo?
15. qual a diferença entre proteína animal e vegetal?
16. pessoas vegetarianas conseguem consumir proteína suficiente?
17. por que o cálcio é essencial para a saúde?
18. leite desnatado é mais saudável que o integral?
19. quais são os principais tipos de carboidratos?
20. por que os carboidratos são importantes para o corpo?
21. qual a diferença entre carboidratos simples e complexos?
22. carboidrato engorda?
23. quais alimentos são boas fontes de carboidrato saudável?
24. quais são os tipos de gorduras?
25. por que precisamos de gorduras boas?
26. qual a diferença entre gorduras boas e ruins?
27. quais alimentos são fontes de gorduras saudáveis?
28. o que acontece se eu consumir muita gordura ruim?
29. o que é metabolismo basal?
30. quais são os distúrbios alimentares?
31. o que são micronutrientes?
32. qual a importância das vitaminas?
33. qual a importância dos minerais?
34. quais alimentos são ricos em vitaminas e minerais?
35. por que a água é importante para o corpo?
36. sucos podem substituir a água?
37. como saber se estou desidratado?
38. o que são alimentos ultraprocessados?
39. por que devemos evitar alimentos ultraprocessados?
40. posso comer fast food de vez em quando?
41. quais os riscos de comer muito açúcar?
42. quais os riscos de comer muito sal?
43. o que é desperdício de alimentos?
44. quais são as principais causas do desperdício de alimentos?
45. qual a importância de reduzir o desperdício de alimentos?
46. o que são macronutrientes?
47. o que são proteínas?
48. o que são carboidratos?
49. o que são gorduras?
