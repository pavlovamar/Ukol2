# Napište program, který načte historická data o průměrných denních průtocích a spočítá roční a sedmidenní průměry. Program bude neinteraktivní.

import csv

with open("vstup.csv", encoding = "utf-8", newline = '') as f:
    with open("vstup_7dni.csv", "w", encoding = "utf-8") as g:
        reader = csv.reader(f,delimiter=",")
        writer = csv.writer(g)
        sum = 0
        for row in reader:
            try:
                sum += float(row[-1])
            except ValueError:
                pass
            print(sum)
            vysledny_prutok = round(sum, 4)
            datum = row[-2]
            prutok = row[-1]
            outrow = [datum, prutok, vysledny_prutok]
            writer.writerow(outrow)