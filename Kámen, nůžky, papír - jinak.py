import random

dalsi_kolo = True

while dalsi_kolo:

    vyber_pc = ["kámen", "nůžky", "papír"]
    pc = random.choice(vyber_pc)
    print(pc)

    vyber_hrace = str(input("Zvol si jestli chceš kámen, nůžky nebo papír.\n")).lower()

    if vyber_hrace == vyber_pc:
        print("Remíza.")
    elif (pc == "kámen" and vyber_hrace == "nůžky") or (pc == "nůžky" and vyber_hrace == "papír") or (pc == "papír" and vyber_hrace == "kámen"):
        print("Vyhrává počítač.")
    else:
        ("Vyhrává hráč.")

    dalsi_kolo = input("Chceš hrát další kolo? Odpověd ano nebo ne.\n").lower()
    if dalsi_kolo != "ano":
        dalsi_kolo = False
        print("Hra ukončena.")
print("Zkouším si git a jeho uložení. ")
print("Další zkouška.")