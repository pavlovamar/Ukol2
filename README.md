Uživatelská dokumentace

Program načte historická data o průměrných denních průtocích. Následně z nich vypočítá sedmidenní a roční průměrné průtoky, které poté zapíše do nově vzniklých souborů. Program je neinteraktivní a nejde do něj tedy nic zadávat. 

Vstupní soubor se musí jmenovat vstup.csv, přičemž byl měl mít 4 sloupce oddělené čárkami (,). V prvním je uvedeno databázové číslo vodního toku a ve druhém je označení typu dat. Třetí z nich obsahuje datum ve formátu DD.MM.RRRR a čtvrtý obsahuje průměrný denní průtok, který pokud je desetinným číslem musí být zapsán desetinnou tečkou. 

Prvním výstupním souborem je vstup_7dni.csv, který má opět 4 sloupce. První dva jsou stejné jako ve vstupním souboru. Ve třetím je uvedené datum prvního dne časového úseku, který se průměruje a ve čtvtém je průměrný průtok za daný časový úsek. Druhý výstupní soubor se jmenuje vystup_rok.csv. Má také čtyři sloupce, kde první dva jsou stejné jako ty ve vstupním souboru. Třetí uvádí první den v roce, pro který byl průtok naměřen. Čtvrtý sloupec obsahuje průměrný roční průtok. 

Pokud je zadaný soubor prázdný, vypíše se chybová hláška "Soubor je prázdný!" <br>

Pokud některý ze zadaných průtoků nebyl číslo, vypíše se chybová hláška "Ve dne ... byl špatně zadán průtok! Nebyla zadána číselná hodnota průtoku!" Místo znaku ... program vypíše, ve který den byl zadaný nesprávný průtok<br>

Pokud měl některý ze zadaných průtoků zápornou či nulovou hodnotu, vypíše se chybová hláška "Ve dne ... byl zadán záporný či nulový průtok!" Místo znaku ... program vypíše, ve který den byl zadaný nesprávný průtok

Program vypíše do konzole den, kdy byl průtok nejvyšší a nejnižší a jeho hodnotu. 
<br>
<br>
<br>

Vývojářská dokumentace

Program zkontroluje zda vstupní soubor existuje a jestli není prázdný. Za pomoci csv.reader dochází k procházení souboru v cyklu, přičemz zkontroluje, zda jsou průměrné denní průtoky zadány číselnými hodnotami a jestli nebyly zadány záporné či nulové hodnoty průtoků. Dochází k počítání celkového průtoku, přičemž se do výstupního souboru vypíše vždy datum prvního dne časového úseku (7 dní) a následně průměrný průtok za tento úsek. Po vypočítání průměrného průtoku dojde k vynulování celkového průtoku a počtu řádků. Pokud vstupní soubor není násobkem 7, vypíše se do výstupního souboru na konci průměr za zbývající dny. Dále se do konzole vypíše den a hodnota nejvyššího a nejnižšího průměrného denního průtoku. 

Poté začne program číst vstupní soubor od začátku. Při vypočítávání průměrných průtoků pro celé roky dojde nejdříve k rozdělení datua, aby se následně daly porovnávat roky mezi sebou. Do proměnné prvni_den se ukláá první den jednotlivých roků. Pokud se rok aktuálního řádku nerovná roku, který byl uložen na začátku do proměnné prvni_den, vypíše se průměrný průtok předchozího roku. Zároveň dojde k vynulování počtu dní, celkového průtoku a změně prvního dne časového úseku. Nakonec se do výstupního souboru vypíše poslední zbývající rok. 

