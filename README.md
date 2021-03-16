## # Atividade 01 da matéria de chatbot da pós-graduação em Data Science - Furb.

Este trabalho tem como objetivo realizar a predição de avaliações positivas ou negativas de filmes, utilizando a base de dados imdb.csv, disponibilizada no ava-furb da matéria. Serão utilizadas as bibliotecas NLTK, Regex e BeaultifulSoup para o pre-processameto das avaliações.

Será feita a avaliação dividindo a base em treino e teste na proporção 80/20, balanceado os registros positivos e negativos. Após isto, será calculada a acurácia para os seguintes modelos, com o objtivo de verificar qual irá performar melhor:


A.   Regressão logística da biblioteca sklearn (ótima para classificação binária)
B.   SentimentIntensityAnalyzer da biblioteca NLTK

*O trabalho foi desenvolvido no Google Colab, utilizando a linguagem de programação Python. 

Sugestão para execução:

1. É necessário baixar arquivo "imdb.csv" disponibilizado no repositório da matéria no ava-furb;
2. Estar logado no gmail (caso contrário, somente visualização);
3. Acessar o diretório "AtividadeNLP.ipynb" e clicar em "Open in Colab"; 
4. Após o notebook ser aberto, é necessário realizar o upload do "imdb.csv" dentro da content;
5. Executar as células.

Observação: Pode-se também pegar o arquivo "AtividadeNLP.ipynb" e executa-lo em outro ambiente, como um jupyter notebook local. Porém, se atentar que no ambiente colab, algumas das bibliotecas utilizadas já são disponibilizadas. Caso alguma delas não exista no ambiente local, é necessário baixa-la.
