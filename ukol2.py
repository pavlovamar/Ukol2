import csv
from math import inf
with open("vstup.csv", encoding = "utf-8", newline = '') as f:
    with open("vystup_7dni.csv", "w", encoding = "utf-8") as g:
        reader = csv.reader(f,delimiter=",")
        writer = csv.writer(g)
        prutok = 0
        cislo_radku = 0
        max_prutok = 0
        min_prutok = inf
        for row in reader:
            cislo_radku += 1                                    #očíslování řádků
            if float(row[-1]) > max_prutok:                     #nejvyšší hodnota průtoku
                max_prutok = float(row[-1])
                max_den = row[-2]
            if float(row[-1]) < min_prutok:                     #nejnižší hodnota průtoku
                min_prutok = float(row[-1])
                min_den = row[-2]
            try:
                prutok += float(row[-1])                        #celkový průtok
            except ValueError:
                pass
            if cislo_radku%7 == 1:                              #vypsání každého prvního dne v průměrovaném úseku
                outrow = [row[0], row[1], row[2]]
                writer.writerow(outrow)
            if cislo_radku%7 == 0:                              #vypsání průměrného průtoku za sedm dní
                prumerny_prutok = round(prutok/7, 4)
                outrow = [prumerny_prutok]
                writer.writerow(outrow)
                sum = 0
                cislo_radku = 0
        print("Nejvyšší hodnota průtoku je " + str(max_prutok) + " a byla naměřena dne " + str(max_den))
        print("Nejnižsí hodnota průtoku je " + str(min_prutok) + " a byla naměřena dne " + str(min_den))

