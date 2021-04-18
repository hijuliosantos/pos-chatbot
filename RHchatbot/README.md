Este projeto consiste em um chatbot feito em rasa para um sistema de RH, onde, os colaboradores podem realizar perguntas de questões empresariais para o bot, como: qual o saldo de férias, beneficios da empresa, seu salário, seu saldo do vale, entre outras... Para utilizar este projeto:

Projeto foi desenvolvido com o Python 3.8 e utilizando as seguintes bibliotecas:
> rasa
> flask
> flask-cors

Verifique requirements.txt

Para executar este projeto é necessário subir 3 servidores (abrir terminais, selecionar o enviroment do python e navegar até a pasta deste projeto):

1º Subir o modelo do python através do seguinte comando:
> rasa run --cors "*" --enable-api
> Ele irá rodar em "http://localhost:5005"

2º Subir o servidor de ações do rasa:
> rasa run actions
> Ele irá rodar em "http://localhost:5055"

3º Subir o webservice desenvlvido com flask:
> python webservice.py
> Ele irá rodar em "http://localhost:5000"

Com os 3 servidores onlines, abrir o arquivo "website/index.html" no navegador.

É necessário realizar o login hipotético no sistema, selecionando um usuário. Após a seleção do usuário, o chatbot é instanciado para interação.

Importante:
* O chatbot armazena as conversas no arquivo "rasadb.db" através do "tracke_store" do arquivo endpoints.yml.
* O chatbot possui um FallbackClassifier padrão com threshold de 0.7.
* O arquivo "ChatbotRH_graficos.ipynb" apresenta 3 gráficos com os dados de "rasadb.db"
* O arquivo "Fluxograma intecoes.pdf" apresenta um fluxograma com 3 interações entre o usuário e o chatbot.
* O arquivo "Exemplo utilizacao.PNG" apresenta uma demonstração do chatbot rodando.