#!/usr/bin/python 
# -*- encoding: iso-8859-1 -*-

import sys
import csv
import numpy as np 
import matplotlib.pyplot as plt 

classname = "Class"
classes = ["Malicious", "Benign"]
count = [0, 0] 

def main(filename, delim):
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
    plt.title("Número de amostras por classe no dataset")
    plt.savefig("figure.png")



if __name__ == "__main__":
    if (len(sys.argv) != 3):
        print("Error - Correct usage:")
        print(str(sys.argv[0]), " <FILE> <DELIMITER>")
        sys.exit()

    main(str(sys.argv[1]), str(sys.argv[2]))

