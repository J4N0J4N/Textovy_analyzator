"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Ján Jankovič
email: jankovic.jan4@gmail.com
discord: jano_15654 
"""

#premenná so zadaným textom
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick. ''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

#vytvorenie slovníka s registrovanými užívateľmi
zaregistrovani = {
    "bob" : "123",
    "ann" : "pass123",
    "mike" : "password123",
    "liz" : "pass123"
}

#zadanie mena a hesla užívateľom a uloženie do premenných 
username = input("username:")
password = input("password:")

ciara = "-" * 40

#podmienka na vyhodnotenie, či je užívateľ registrovaný alebo nie
if zaregistrovani.get(username) == password: 
    print(
        ciara, "Welcome to the app, " + username, 
        "We have 3 texts to be analyzed.", ciara, sep="\n"
        )

    #nová premenná, do ktorej sa uloží vstup od užívateľa
    cislo_textu = input("Enter a number btw. 1 and 3 to select: ")

    #vnorená podmienka, ktorá vyhodnocuje, či je vstup číslo
    if cislo_textu.isnumeric() is True:
        
        #ak je vstup číslo, vyhodnocuje sa či je v intervale <1,3>
        if int(cislo_textu) in range(1, 4):

            #rozsplituje string na vybranom indexe listu 
            TEXTS_split = TEXTS[int(cislo_textu)-1].split()

            #vráti počet slov vo vybranom stringu
            pocet_slov = len(TEXTS_split)

            #premenná, do ktorej sa pripočítava hodnota, pokiaľ
            #nájde výskyt veľkého písmena na začiatku slova
            capital = 0

            #premenná, do ktorej sa pripočítava hodnota, pokiaľ
            #nájde výskyt slova zloženého z veľkých písmen
            upper = 0

            #premenná, do ktorej sa pripočítava hodnota, pokiaľ
            #nájde výskyt slova zloženého z malých písmen
            lower = 0
            
            #premenná, do ktorej sa pripočítava hodnota, pokiaľ
            #nájde výskyt stringu s číselnou hodnotou
            number = 0

            #list, do ktorého sa pridávajú čísla nájdené v texte
            soucet = []

            #list, do ktorého sa pridáva četnost jednotlivých slov v texte
            cetnost_list = []


            for slovo in TEXTS_split:

                if slovo[0].isupper():
                    capital += 1
                
                if slovo.isupper() and slovo.isalpha():
                    upper += 1

                if slovo.islower(): #skontrolovať ešte správnosť tejto podmienky(podľa výpisu v zadaní sedí) and slovo.isalpha():
                    lower += 1

                if slovo.isnumeric():
                    number += 1
                    soucet.append(int(slovo)) #popisat podmienku

                #očistí slova od znakov, ktoré sa by sa inak započítavali do četnosti
                #následne pridá jednotlivé hodnoty do listu cetnost_list
                ciste_slovo = slovo.replace(".", "").replace(",", "").replace("-", "") 
                cetnost = len(ciste_slovo)   
                cetnost_list.append(cetnost)    

                #šírka stĺpca "occurences" sa prispôsobuje podLa najväčšej hodnoty v liste četnosti 
                #pripočítavajú sa 2 miesta kvôli tomu aby nebol stĺpec nalepený na "NR."
                max_vyskyt = max(cetnost_list.count(x) for x in range(1, 12))
                medzera = max_vyskyt + 2

            #vyprintuje počty podľa zadania
            print(
                ciara, 
                "There are " + str(pocet_slov) + " words in the selected text.",
                "There are " + str(capital) + " titlecase words.",
                "There are " + str(upper) + " uppercase words.",
                "There are " + str(lower) + " lowercase words.",
                "There are " + str(number) + " numeric strings.",
                "The sum of all the numbers " + str(sum(soucet)),
                sep="\n"
                )

            #vyprintovanie tabuľky
            print(ciara, "LEN|" + "OCCURENCES".center(medzera) + "|NR.", ciara, sep="\n")
            print(
                "1|".rjust(4) + ((cetnost_list.count(1)) * "*").ljust(medzera) + "|" + str(cetnost_list.count(1)),
                "2|".rjust(4) + ((cetnost_list.count(2)) * "*").ljust(medzera) + "|" + str(cetnost_list.count(2)), 
                "3|".rjust(4) + ((cetnost_list.count(3)) * "*").ljust(medzera) + "|" + str(cetnost_list.count(3)),
                "4|".rjust(4) + ((cetnost_list.count(4)) * "*").ljust(medzera) + "|" + str(cetnost_list.count(4)), 
                "5|".rjust(4) + ((cetnost_list.count(5)) * "*").ljust(medzera) + "|" + str(cetnost_list.count(5)),
                "6|".rjust(4) + ((cetnost_list.count(6)) * "*").ljust(medzera) + "|" + str(cetnost_list.count(6)), 
                "7|".rjust(4) + ((cetnost_list.count(7)) * "*").ljust(medzera) + "|" + str(cetnost_list.count(7)),
                "8|".rjust(4) + ((cetnost_list.count(8)) * "*").ljust(medzera) + "|" + str(cetnost_list.count(8)), 
                "9|".rjust(4) + ((cetnost_list.count(9)) * "*").ljust(medzera) + "|" + str(cetnost_list.count(9)),
                "10|".rjust(4) + ((cetnost_list.count(10)) * "*").ljust(medzera) + "|" + str(cetnost_list.count(10)), 
                "11|".rjust(4) + ((cetnost_list.count(11)) * "*").ljust(medzera) + "|" + str(cetnost_list.count(11)),
                sep="\n"
               )  

        else:
            print("Your number is out of range")
    
    else:
        print("The input must be a number")
else:
    print("unregistered user, terminating the program..")


