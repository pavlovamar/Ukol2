import csv
from math import inf
try:
    with open("vstup.csv", encoding = "utf-8", newline = '') as f, \
    open("vystup_7dni.csv", "w", encoding = "utf-8", newline = '') as g, \
    open("vystup_rok.csv", "w", encoding = "utf-8", newline = '') as h:
        reader = csv.reader(f,delimiter=",")
        writer = csv.writer(g)
        writer2 = csv.writer(h)
        if len(list(reader)) == 0:
            print("Soubor je prázdný!")
            quit()
        f.seek(0)
        celkovy_prutok = 0
        cislo_radku = 0
        max_prutok = 0
        min_prutok = inf
        for row in reader:
            cislo_radku += 1                                            
            denni_prutok = row[-1]
            try:
                row[-1]  = float(denni_prutok)
            except:
                radek = cislo_radku
                print("Ve dne " + str(row[-2]) + " byl špatně zadán průtok. Nebyla zadána číselná hodnota průtoku!")
                quit()
            if float(row[-1]) <= 0:
                print("Ve dne " + str(row[-2]) + " byl zadán záporný či nulový průtok!")
            if float(row[-1]) > max_prutok:                             #nejvyšší hodnota průtoku
                max_prutok = float(row[-1])
                max_den = row[-2]
            if float(row[-1]) < min_prutok:                             #nejnižší hodnota průtoku
                min_prutok = float(row[-1])
                min_den = row[-2]
            try:
                celkovy_prutok += float(row[-1])                    
            except ValueError:
                pass
            if cislo_radku%7 == 1:                                      #vypsání každého prvního dne v průměrovaném úseku
                datum = row[-2]
            if cislo_radku%7 == 0:                                      #vypsání průměrného průtoku za sedm dní
                prumerny_prutok = round(celkovy_prutok/7, 4)
                outrow = [row[0], row[1], datum, "   " + str(prumerny_prutok)]
                writer.writerow(outrow)
                prutok = 0
                cislo_radku = 0
            else:                                                       #Vypsání průtoku pokud není průměrovaný za sedm dní
                prumerny_prutok = round(celkovy_prutok/cislo_radku%7, 4)    
        outrow = [row[0], row[1], datum, "   " + str(prumerny_prutok)]
        writer.writerow(outrow)
        print("Nejvyšší hodnota průtoku je " + str(max_prutok) + " a byla naměřena dne " + str(max_den))
        print("Nejnižsí hodnota průtoku je " + str(min_prutok) + " a byla naměřena dne " + str(min_den))

        f.seek(0)
        pocet_dni = 0
        celkovy_prutok = 0
        prumerny_prutok = 0
        soucasny_rok = None
        for row in reader: 
            datum = row[-2].split(".")                                  #Rozdělí datum, abychom pak mohli porovnávat roky mezi sebou
            rok = datum[-1]
            if soucasny_rok == None:
                prvni_den = row[-2]
                soucasny_rok = rok
            elif soucasny_rok != rok:                                   #Vypočítání průměrného průtoku pokud se změní rok
                prumerny_prutok = round(celkovy_prutok/pocet_dni, 4)
                soucasny_rok = rok
                celkovy_prutok = 0
                pocet_dni = 0
                outrow = [row[0], row[1], prvni_den, "   " + str(prumerny_prutok)]
                writer2.writerow(outrow)
                prvni_den = row[-2]
            pocet_dni += 1
            celkovy_prutok += float(row[-1])
        prumerny_prutok = round(celkovy_prutok/pocet_dni, 4)            #Vypočítání a vypsání posledního roku
        outrow = [row[0], row[1], prvni_den, "   " + str(prumerny_prutok)]
        writer2.writerow(outrow)
except FileNotFoundError:
    print("Soubor nebyl nalezen")