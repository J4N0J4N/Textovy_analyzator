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
which are about 300 feet thick.''',
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

#podmienka na vyhodnotenie, či je užívateľ registrovaný alebo nie
if zaregistrovani.get(username) == password: 
    print(
        "-" * 40 + "\n" + "Welcome to the app, " 
        + username + "\n" + "We have 3 texts to be analyzed." + 
        "\n" + "-" * 40
        )

    #nová premenná, do ktorej sa uloží vstup od užívateľa
    cislo_textu = input("Enter a number btw. 1 and 3 to select: ")

    #vnorená podmienka, ktorá vyhodnocuje, či je vstup číslo
    if cislo_textu.isnumeric() is True:
        
        #ak je vstup číslo, vyhodnocuje sa či je v intervale <1,3>
        if int(cislo_textu) in range(1, 4):
            print("zadal si dobre")

        else:
            print("Your number is out of range")
    
    else:
        print("The input must be a number")
else:
    print("unregistered user, terminating the program..")


