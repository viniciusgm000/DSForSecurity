# DSForSecurity
Repositório para a disciplina de Ciência de Dados para a Segurança,
Bacharelado em Ciência da Computação - UFPR
Autor: Vinicius Gabriel Machado - Fevereiro~Maio/2022
Professor: André Ricardo Abed Grégio

Resumo do contéudo presente neste repositório (mais detalhes nos respectivos diretórios):

t1 (tarefa 1): Aplicação em Python para a leitura e contagem de dados de um arquivo .pcap, gerado pela aplicação ScaPy.

t2 (tarefa 2): Criação deste repositório e de um arquivo com o link para acesso. Juntamente com ideias de datasets que o aluno achou interessante, que serão utilizados nas próximas atividades.

t3 (tarefa 3): Obtenção e descrição do dataset, incluindo: local de obtenção, referência, contagem de amostras, classes e atributos.

t4 (tarefa 4): Definição de um vetor de características, apresentação da quantidade de amostras por classe por meio de uma figura de um gráfico de barras e apresentação do código utilizado para gerar a figura.

t5 (tarefa 5): Limpeza/Tratamento dos dados, melhor seleção das características - por meio da utilização da ferramenta WEKA - e clusterização dos dados utilizando KMeans com a plotagem sendo feita utilizando PCA.

# Exploração de Dados

Explorando o dataset PDFMalware2022, as seguintes características foram extraídas com base no entendimento sobre elas (algumas não tiveram a diferenciação clara entre si):

pdfsize;
metadata size;
xref Length;
title characters;
images;
text;
header;
obj;
endobj;
stream;
endstream;
xref;
trailer;
startxref;
ObjStm;
JS;
Javascript;
AA;
OpenAction;
Acroform;
JBIG2Decode;
RichMedia;
launch;
XFA;
Colors;
classe;

A última, classe, indica a classificação da amostra em um espaço binário.
Assumindo os valores Malicious (malicioso) e Benign (benigno). O primeiro indica amostras maliciosas que tiveram características parecidas com as benignas na classificação feita na criação do dataset. E a segunda, amostras benignas que tiveram características que as aproximaram de maliciosas.

Segue a distribuição dos dados:

![figure](https://github.com/viniciusgm000/DSForSecurity/blob/main/t4/figure.png)

# Melhor Seleção das Características

A partir da utilização da ferramenta WEKA, o número de características foi reduzido para 7. 

pdfsize: Tamanho do arquivo
metadata size: Tamanho da região de metadata
xref Length: Número de Xrefs
obj: Número de palavras-chave indicando o início de objetos
endobj: Número de palavras-chave indicando o ﬁm de objetos
JS: Número de palavras-chave “/JS”
Javascript: Número de palavras-chave “/JavaScript”

Por meio das opções de classificação e pesquisa do programa, foi-se escolhido as características que mais prevaleceram em diferentes ranqueamentos e que estiveram acima do limiar 0.5 utilizando o método Information Gain:

![figure](https://github.com/viniciusgm000/DSForSecurity/blob/main/t5/weka_selection1.png)

As mesmas também prevaleceram em outros métodos:

![figure](https://github.com/viniciusgm000/DSForSecurity/blob/main/t5/weka_selection2.png)

# Limpeza/Tratamento dos dados

Ao observar os dados, alguns problemas foram detectados, logo, eles tiveram que ser tratados.

Linhas removidas inteiramente:

---> not a number
---> dados inconclusivos, X (1) ou X (2), exemplo 1 (1) em uma coluna de contagem de uma tag
---> resquícios de erros em programas bash
---> dados inconclusivos, -1 em campos de contagem de uma tag, suponho que seja para indicar um erro (não é explicado no artigo do dataset, nem encontrei uma referência para isso no programa extrator que gerou o dataset), então foram descartados

Colunas removidas inteiramente:

---> text: Inicialmente a ideia era indicar se no pdf há texto (uma vez que apresentação não é uma preocupação em situações maliciosas), entretanto não ficou claro a distinção entre os possíveis valores do campo: -1, 0, unclear, no e yes
---> header: Tinha a ideia de indicar a versão do padrão pdf utilizado, entretanto não havia uma padronização em como os dados eram apresentados e muitos não faziam sentido
---> file name: Não há a necessidade de saber o nome do arquivo por hora

Contagem de dados:

Antes (10025 amostras, 5557 maliciosas e 4468 benignas):

![figure](https://github.com/viniciusgm000/DSForSecurity/blob/main/t5/figure_before.png)

Depois (8190 amostras, 3759 maliciosas e 4431 benignas):

![figure](https://github.com/viniciusgm000/DSForSecurity/blob/main/t5/figure_after.png)

# Plotagem

Scatterplot:

![figure](https://github.com/viniciusgm000/DSForSecurity/blob/main/t5/scatterplot.png)

KMeans com PCA:

![figure](https://github.com/viniciusgm000/DSForSecurity/blob/main/t5/pca.png)
