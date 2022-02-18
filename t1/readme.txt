Resumo da tarefa:

Criar um programa em python que leia um arquivo .pcap gerado pela aplicação ScaPy e que realize as seguintes atividades:
(Citando a solicitação do professor)

Conte quantos pacotes foram capturados no Total;
Conte quantos pacotes possuem protocolo de camada de Rede "IP"
Conte quantos pacotes possuem protocolo de camada de Transporte "TCP"
Conte quantos pacotes possuem protocolo de camada de Transporte "UDP"
Separe as sessões "TCP" e "UDP" em dicionários de listas (chave == sessão, valor recebe lista de payloads daquela sessão em formato legível)
Imprima a quantidade de sessões TCP e UDP, bem como a quantidade de pacotes não-associados ao protocolo de rede IP.


Entrada:

Um arquivo de nome "trace.pcap" no mesmo diretório do arquivo python "conta_sessoes.py".

Para gerar o arquivo foi realizada as seguintes operações ao executar o ScaPy em um terminal:

data = sniff(timeout=60)

// 60 segundos consumindo conteúdo de vídeo e acessando páginas das disciplinas do curso

wrpcap("trace.pcap", data)


Execução:

python3 conta_sessoes.py


Exemplo de Saída:

O arquivo "trace.pcap" possui:
15434 pacotes no total
15428 pacotes IP
8603 pacotes TCP
6821 pacotes UDP
96 sessoes TCP
79 sessoes UDP
6 pacotes nao-IP