print("Estimativa de variação do PIB, em percentual, entre 2013 e 2020!\n")
import csv
    
with open("Assessment_PIBs - modelo 1.csv", encoding="utf-8") as menu:
        lista = csv.reader(menu, delimiter=',')
        for l , horizontal in enumerate(lista):
                if l > 0:
                    dados = horizontal
                    variacao = (float(dados[8]) / float(dados[1]) - 1) * 100
                    print(f"{horizontal[0]} tem a variação de {variacao:.2f}% do PIB entre 2013 e 2020.")

pais = input("Digite um nome de uma País: ")
ano = int(input("Digite um ano entre 2013 e 2020: "))

import csv

dados = 0
if ano <= 2012 or ano >= 2021:
        print("Este ano não é valido.")
else:
    with open("Assessment_PIBs - modelo 1.csv", encoding="utf-8") as menu:
        lista = csv.reader(menu, delimiter=",")
        for l,horizontal in enumerate(lista):
            if l == 0:
                for l,quantia in enumerate(horizontal):
                    if l > 0:
                        if int(quantia) == ano:
                            determinado_ano = l
            if pais == horizontal[0]:
                dados = list(horizontal)
        if dados == 0:
            print("Este País não é valido")
        else:
            print(f"O PIB do(a) {dados[0]} no ano de {ano} era de:${dados[determinado_ano]} trilhões")