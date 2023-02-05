import csv

""" Lê o arquivo csv, converte, e retorna uma lista """

def ler_csv():
    arquivo = "star_wars_character_dataset.csv"    
    with open(arquivo,"r") as arquivo:
        arquivo_csv = csv.reader(arquivo, delimiter=",")
        lista = list(arquivo_csv)        
        return lista

def proximo(atual, ultimo):
    if atual + 1 <= ultimo:
        return atual + 1
    else:
        atual = 1
        return atual

def anterior(atual):
    if (atual - 1) > 1:
        atual = atual -1
        return atual
    else:
        return 87



