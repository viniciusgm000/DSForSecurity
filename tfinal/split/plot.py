import csv
import matplotlib.pyplot as plt 

classname = "Class"
classes = ["Malicious", "Benign"]
count = [0, 0] 

def main(filename, delim, label):
    # abre e le o arquivo pelo nome da coluna
    file = open(filename, encoding="utf-8")
    csvreader = csv.DictReader(file, delimiter=delim) 

    # conta o numero de instancias de cada classe
    for row in csvreader:
        if (row[classname] == classes[0]):
            count[0] = count[0] + 1
        if (row[classname] == classes[1]):
            count[1] = count[1] + 1 

    # plota o grafico de barras
    fig = plt.figure(figsize = (10, 5)) 
    plt.bar(list(classes), list(count), color = list(['red', 'blue']), width = 0.5)
    plt.xlabel("Classes") 
    plt.ylabel("Número de amostras") 
    plt.title("Número de amostras por classe no dataset - Divisão " + label + "%")
    plt.savefig(label + ".png")



if __name__ == "__main__":
    main("20.csv", ",", '20')
    main("80.csv", ",", '80')

