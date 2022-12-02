# Napište program, který načte historická data o průměrných denních průtocích a spočítá roční a sedmidenní průměry. Program bude neinteraktivní.

import csv

with open("vstup.csv", encoding = "utf-8", newline = '') as f:
    with open("vstup_7dni.csv", "w", encoding = "utf-8") as g:
        reader = csv.reader(f,delimiter=",")
        for row in reader:
            print(row)
