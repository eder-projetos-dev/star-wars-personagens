import csv

""" Lê o arquivo csv, transforma e retorna uma lista """

def ler_csv(arquivo):
    with open(arquivo,"r") as arquivo:
        arquivo_csv = csv.reader(arquivo, delimiter=",")
        return list(arquivo_csv)

personagens = ler_csv("star_wars_character_dataset.csv")

for persona in personagens:
    print("name: " + persona[0])
    print("height: " + persona[1])
    #print(persona[2])
    print("hair_color: " + persona[3])
    print("skin_color: " + persona[4])
    print("eye_color: " + persona[5])
    #print(persona[6])
    #print(persona[7])
    print("gender: " + persona[8])
    print("homeworld: " + persona[9])
    print("species: " + persona[10])
    print("films: " + persona[11])
    print("------------------")
    #print(persona[12])
    #print(persona[13])
