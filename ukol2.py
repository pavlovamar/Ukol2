# Napište program, který načte historická data o průměrných denních průtocích a spočítá roční a sedmidenní průměry. Program bude neinteraktivní.

import csv

with open("vstup.csv", encoding = "utf-8", newline = '') as f:
    with open("vstup_7dni.csv", "w", encoding = "utf-8") as g:
        reader = csv.reader(f,delimiter=",")
        next(reader)
        writer = csv.writer(g)
        for row in reader:
            datum = row[-2]
            prutok = row[-1]
            outrow = [datum, prutok]
            writer.writerow(outrow)
