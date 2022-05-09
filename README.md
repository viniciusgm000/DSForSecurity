# DSForSecurity
Repositório para a disciplina de Ciência de Dados para a Segurança

Bacharelado em Ciência da Computação - UFPR

Autor: Vinicius Gabriel Machado - Fevereiro~Maio/2022

Professor Doutor André Ricardo Abed Grégio

### Resumo do contéudo presente neste repositório:

t1 (tarefa 1): Aplicação em Python para a leitura e contagem de dados de um arquivo .pcap, gerado pela aplicação ScaPy.

t2 (tarefa 2): Criação deste repositório e de um arquivo com o link para acesso. Juntamente com ideias de datasets que o aluno achou interessante, que serão utilizados nas próximas atividades.

t3 (tarefa 3): Obtenção e descrição do dataset, incluindo: local de obtenção, referência, contagem de amostras, classes e atributos.

t4 (tarefa 4): Definição de um vetor de características, apresentação da quantidade de amostras por classe por meio de uma figura de um gráfico de barras e apresentação do código utilizado para gerar a figura.

t5 (tarefa 5): Limpeza/Tratamento dos dados, melhor seleção das características - por meio da utilização da ferramenta WEKA - e clusterização dos dados utilizando KMeans com a plotagem sendo feita utilizando PCA.

t6 (tarefa 6): Classificação dos dados utilizando KNN e Random Forest.

tfinal (tarefa final): A partir da remoção de 20% dos dados do dataset, com os 80% restantes foi realizado um grid search com diferentes classificadores, parâmetros e visando uma meta para o reajuste de limiar. Com os melhores parâmetros encontrados, os classificadores foram treinados, salvos, medidos o tempo de treinamento, geradas curvas P/R e matrizes de confusão para k-fold com k = 5 e comparados com os resultados do artigo original.

# Referências

**LINK #1** - Artigo sobre o dataset: https://www.scitepress.org/PublicationsDetail.aspx?ID=VibgIHYeOxw=&t=1

**LINK #2** - Visão geral do dataset e link para fazer o download: https://www.unb.ca/cic/datasets/pdfmal-2022.html

**LINK #3** - WEKA: https://www.cs.waikato.ac.nz/ml/weka/

**LINK #4** - Bibliotecas Python: https://numpy.org, https://matplotlib.org, https://scikit-learn.org/stable/ e https://pandas.pydata.org

# O Dataset

O dataset PDFMalware2022 é resultante de um estudo por parte dos autores (Issakhani, M. et al. 2022), sobre diferentes modelos propostos para a detecção de agentes maliciosos em arquivos PDF e dos datasets utilizados nestes experimentos, e da proposta de um modelo baseado em empilhamento de classificadores por parte deles.

Segundo os autores, muitos dos artigos criados utilizam o dataset de PDFs do Contagio e que tal dataset possui diversos problemas (demonstrados no artigo). Citando alguns dos problemas: Alto número de duplicatas (aproximadamente 44% do dataset), baixo coeficiente de variação tanto em amostras maliciosas quanto benignas (com coeficiente menor que 1) e baixa distribuição (possível classificar o dataset com apenas 2 características obtendo uma precisão de 80%).

Desta forma, surgiu a ideia de criar um dataset que corrija esses erros. A partir da combinação dos datasets do Contagio e do VirusTotal, e da extração de 28 características do PDF, foram removidas as duplicatas. O que segundo os autores, resultou em um maior coeficiente de variação e em um equilíbrio de 49% nas duas características que antes podiam ser facilmente separadas por um classificador linear.

Utilizando K-means, os autores separaram apenas as amostras evasivas para o dataset. Ou seja, as benignas que tiveram características semelhantes as de maliciosas e as maliciosas semelhantes as benignas.

Por fim, foi proposto um modelo de classificação baseado no empilhamento de classificadores, utilizando MLP, Linear SVM e Random Forest como base learners e Logistic Regression como meta learner.

Utilizando esse modelo, os autores realizaram a classificação que é apresentada no dataset. Tendo acurácia, precisão, recall e f1-score maiores que 98% no dataset.

# Exploração de Dados

Explorando o dataset, as seguintes características foram extraídas com base no entendimento sobre elas (em **LINK #2**). Algumas não tiveram a diferenciação entre si clara, logo, não foram utilizadas.

- pdfsize
- metadata size
- xref Length
- title characters
- images
- text
- header
- obj
- endobj
- stream
- endstream
- xref
- trailer
- startxref
- ObjStm
- JS
- Javascript
- AA
- OpenAction
- Acroform
- JBIG2Decode
- RichMedia
- launch
- XFA
- Colors
- Class (classe)

A última, classe, indica a classificação da amostra em um espaço binário.
Assumindo os valores Malicious (malicioso) e Benign (benigno). O primeiro indica amostras maliciosas que tiveram características parecidas com as benignas na classificação feita na criação do dataset. E a segunda, amostras benignas que tiveram características que as aproximaram de maliciosas.

## Distribuição dos Dados:

![figure](https://github.com/viniciusgm000/DSForSecurity/blob/main/t4/figure.png)

# Melhor Seleção das Características

A partir da utilização da ferramenta WEKA (em **LINK #3**), o número de características foi reduzido para 7. 

- pdfsize: Tamanho do arquivo;
- metadata size: Tamanho da região de metadata;
- xref Length: Número de Xrefs;
- obj: Número de palavras-chave indicando o início de objetos;
- endobj: Número de palavras-chave indicando o ﬁm de objetos;
- JS: Número de palavras-chave “/JS”;
- Javascript: Número de palavras-chave “/JavaScript”;

Por meio das opções de classificação e pesquisa do programa, foi-se escolhido as características que mais prevaleceram em diferentes ranqueamentos e que estiveram acima do limiar 0.5 utilizando o método Information Gain:

![figure](https://github.com/viniciusgm000/DSForSecurity/blob/main/t5/weka_selection1.png)

As mesmas também prevaleceram em outros métodos:

![figure](https://github.com/viniciusgm000/DSForSecurity/blob/main/t5/weka_selection2.png)

# Limpeza/Tratamento dos dados

Ao observar os dados, alguns problemas foram detectados, logo, eles tiveram que ser tratados.

Linhas removidas inteiramente:

- not a number
- dados inconclusivos, X (1) ou X (2), exemplo 1 (1) em uma coluna de contagem de uma tag
- resquícios de erros em programas bash
- dados inconclusivos, -1 em campos de contagem de uma tag, suponho que seja para indicar um erro (não é explicado no artigo do dataset, nem encontrei uma referência para isso no programa extrator que gerou o dataset), então foram descartados

Colunas removidas inteiramente:

- text: Inicialmente a ideia era indicar se no pdf há texto (uma vez que apresentação não é uma preocupação em situações maliciosas), entretanto não ficou claro a distinção entre os possíveis valores do campo: -1, 0, unclear, no e yes

- header: Tinha a ideia de indicar a versão do padrão pdf utilizado, entretanto não havia uma padronização em como os dados eram apresentados e muitos não faziam sentido

- file name: Não há a necessidade de saber o nome do arquivo por hora

## Contagem de dados:

Antes (10025 amostras, 5557 maliciosas e 4468 benignas):

![figure](https://github.com/viniciusgm000/DSForSecurity/blob/main/t5/figure_before.png)

Depois (8190 amostras, 3759 maliciosas e 4431 benignas):

![figure](https://github.com/viniciusgm000/DSForSecurity/blob/main/t5/figure_after.png)

## Plotagem

Scatterplot (vermelho = benign, azul = malicious):

![figure](https://github.com/viniciusgm000/DSForSecurity/blob/main/t5/scatterplot.png)

## Clusterização

KMeans com PCA - Centróides:

![figure](https://github.com/viniciusgm000/DSForSecurity/blob/main/t5/centroids_clustering_pca.png)

KMeans com PCA - Clusters predição:

![figure](https://github.com/viniciusgm000/DSForSecurity/blob/main/t5/clustering_pca_fl.png)

KMeans com PCA - Clusters originais:

![figure](https://github.com/viniciusgm000/DSForSecurity/blob/main/t5/clustering_pca_ol.png)

## Classificação

KNN:

![figure](https://github.com/viniciusgm000/DSForSecurity/blob/main/t6/knn_results.png)

![figure](https://github.com/viniciusgm000/DSForSecurity/blob/main/t6/knn.png)

Random Forest:

![figure](https://github.com/viniciusgm000/DSForSecurity/blob/main/t6/random_forest_results.png)

![figure](https://github.com/viniciusgm000/DSForSecurity/blob/main/t6/randomforest.png)

# Tarefa Final

Como instruído pelo professor, os dados foram separados em um grupo de 80% (que seram utilizados nos próximos passos) e um de 20% (para demonstração prática em aula)

Inicialmente foi realizado um grid search para procurar os melhores parâmetros (dentre alguns definidos pelo professor) para os classificadores: KNN, MLP, SVM e Random Forest. 

A solução que se visa atingir é a de detecção em tempo real, por parte de uma ferramenta como um antivírus. Dito isso, utilizou-se precision_score como meta para o ajuste de limiar, visando diminuir o número de falsos positivos. Uma vez que para esse tipo de ferramenta, julgou-se fundamental que o usuário não seja incomodado com alertas falsos positivos.

- Classe positiva: Malicious - 1
- Classe negativa: Benign - 0

## Ambiente de execução

Sistema Operacional: Ubuntu 20.04

Processador: Ryzen 5 3600 4.2 GHz - 32 MB cache L3

RAM: 16 GB 3000 MHz

Disco: HDD 7200 rpm/SSD 550 MB/s (escrita e leitura)

## Grid Search:

![figure](https://github.com/viniciusgm000/DSForSecurity/blob/main/tfinal/grid_search/results.png)

Para cada classificador, com seus melhores parâmetros, foram treinados dois modelos, um com divisão de dados 80/20 e outro 50/50. Esses foram salvos e tiveram os seus tempos de treinamento medidos.

## Tempos de treinamento:

![figure](https://github.com/viniciusgm000/DSForSecurity/blob/main/tfinal/training_models/training_time.png)

Por fim, para realizar uma validação cruzada, foram geradas curvas Precision/Recall e matrizes de confusão para K-fold com k = 5.

## Curvas Precision/Recall

KNeighborsClassifier:

![figure](https://github.com/viniciusgm000/DSForSecurity/blob/main/tfinal/training_models/pr_figures/KNeighborsClassifier.png)

MLPClassifier:

![figure](https://github.com/viniciusgm000/DSForSecurity/blob/main/tfinal/training_models/pr_figures/MLPClassifier.png)

RandomForestClassifier:

![figure](https://github.com/viniciusgm000/DSForSecurity/blob/main/tfinal/training_models/pr_figures/RandomForestClassifier.png)

SVC:

![figure](https://github.com/viniciusgm000/DSForSecurity/blob/main/tfinal/training_models/pr_figures/SVC.png)

## Matrizes de Confusão

Para visualizar todas as 5 de cada classificador, consulte o [diretório](https://github.com/viniciusgm000/DSForSecurity/tree/main/tfinal/training_models/cm_figures) de matrizes de confusão.

KNeighborsClassifier:

![figure](https://github.com/viniciusgm000/DSForSecurity/blob/main/tfinal/training_models/cm_figures/KNeighborsClassifier-1.png)

MLPClassifier:

![figure](https://github.com/viniciusgm000/DSForSecurity/blob/main/tfinal/training_models/cm_figures/MLPClassifier-1.png)

RandomForestClassifier:

![figure](https://github.com/viniciusgm000/DSForSecurity/blob/main/tfinal/training_models/cm_figures/RandomForestClassifier-1.png)

SVC:

![figure](https://github.com/viniciusgm000/DSForSecurity/blob/main/tfinal/training_models/cm_figures/SVC-1.png)

