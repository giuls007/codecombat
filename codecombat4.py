import random
def crea_personaggio(classe):
    if classe == "guerriero":
        vita = random.randint(100, 120)
        energia = random.randint(8, 10)
        difesa = random.randint(4, 8)
        attacco = sum(random.randint(1, 6) for _ in range(2))  # 2d6
        abilita = random.randint(1, 6)  # 1d6
    elif classe == "mago":
        vita = random.randint(70, 90)
        energia = random.randint(14, 18)
        difesa = random.randint(3, 5)
        attacco = random.randint(1, 20)  # 1d20
        abilita = random.randint(1, 8)  # 1d8
    elif classe == "ladro":
        vita = random.randint(80, 100)
        energia = random.randint(10, 12)
        difesa = random.randint(3, 5)
        attacco = sum(random.randint(1, 4) for _ in range(3))  # 3d4
        abilita = random.randint(1, 4)  # 1d4
    elif classe == "chierico":
        vita = random.randint(80, 100)
        energia = random.randint(10, 12)
        difesa = random.randint(4, 6)
        attacco = random.randint(1, 12)  # 1d12
        abilita = random.randint(1, 6)  # 1d6

    return {
        "classe": classe,
        "vita": vita,
        "energia": energia,
        "difesa": difesa,
        "attacco": attacco,
        "abilita": abilita
    }
def crea_party():
    classi = ["guerriero", "mago", "ladro", "chierico"]
    return [crea_personaggio(classe) for classe in classi]
def abilita_speciale(personaggio):
    if personaggio["classe"] == "guerriero":
        if personaggio["abilita"] >= 5:
            return "Berserk", random.choice([True, False])
    elif personaggio["classe"] == "mago":
        if personaggio["abilita"] >= 5:
            return "Concentrazione assoluta", random.randint(1, 4)
    elif personaggio["classe"] == "ladro":
        if personaggio["abilita"] in [7, 8]:
            return "Pugnali acidi", True
    elif personaggio["classe"] == "chierico":
        if personaggio["abilita"] >= 5:
            return "Favore degli dei", random.randint(5, 20)

    return None, 0
def attacco(personaggio1, personaggio2):
    if personaggio1["energia"] >= 2:
        danno = personaggio1["attacco"] - personaggio2["difesa"]
        danno = max(danno, 0)
        personaggio2["vita"] -= danno
        personaggio1["energia"] -= 2
        print(
            f"{personaggio1['classe']} attacca {personaggio2['classe']}! Danno: {danno}. Vita rimanente di {personaggio2['classe']}: {personaggio2['vita']}")
    else:
        personaggio1["energia"] = 12
        print(f"{personaggio1['classe']} riposa per recuperare energia.")
def partita_fine(partita1, partita2):
    if all(p["vita"] <= 0 for p in partita1):
        print("Partita 2 vince!")
        return True
    if all(p["vita"] <= 0 for p in partita2):
        print("Partita 1 vince!")
        return True
    return False
def combattimento(partita1, partita2, max_turni=50):
    turno = 1
    while turno <= max_turni:
        print(f"\n--- Turno {turno} ---")

        for i in range(4):
            personaggio1 = partita1[i]
            personaggio2 = partita2[i]

            print(f"\n{personaggio1['classe']} del Partita 1 attacca {personaggio2['classe']} del Partita 2")
            attacco(personaggio1, personaggio2)

            abilita_nome, abilita_valore = abilita_speciale(personaggio1)
            if abilita_nome:
                print(f"Abilità speciale attivata: {abilita_nome} con valore {abilita_valore}")
                if abilita_nome == "Berserk":
                    if abilita_valore:
                        print(f"{personaggio1['classe']} attacca di nuovo!")
                        attacco(personaggio1, personaggio2)
                    else:
                        print(f"{personaggio1['classe']} perde il 20% della vita.")
                        personaggio1["vita"] -= personaggio1["vita"] // 5
                elif abilita_nome == "Concentrazione assoluta":
                    personaggio1["attacco"] += abilita_valore
                    print(
                        f"{personaggio1['classe']} aumenta il suo attacco di {abilita_valore}. Nuovo attacco: {personaggio1['attacco']}")
                elif abilita_nome == "Pugnali acidi":
                    for p in partita2:
                        p["difesa"] -= p["difesa"] // 4
                    print(f"{personaggio1['classe']} riduce la difesa degli avversari.")
                elif abilita_nome == "Favore degli dei":
                    debole = min(partita1, key=lambda p: p["vita"])
                    debole["vita"] += abilita_valore
                    print(f"{personaggio1['classe']} cura {debole['classe']} di {abilita_valore} punti vita.")

            if partita_fine(partita1, partita2):
                return

            personaggio1, personaggio2 = personaggio2, personaggio1

            print(f"\n{personaggio2['classe']} del Partita 2 attacca {personaggio1['classe']} del Partita 1")
            attacco(personaggio2, personaggio1)

            abilita_nome, abilita_valore = abilita_speciale(personaggio2)
            if abilita_nome:
                print(f"Abilità speciale attivata: {abilita_nome} con valore {abilita_valore}")
                if abilita_nome == "Berserk":
                    if abilita_valore:
                        print(f"{personaggio2['classe']} attacca di nuovo!")
                        attacco(personaggio2, personaggio1)
                    else:
                        print(f"{personaggio2['classe']} perde il 20% della vita.")
                        personaggio2["vita"] -= personaggio2["vita"] // 5
                elif abilita_nome == "Concentrazione assoluta":
                    personaggio2["attacco"] += abilita_valore
                    print(
                        f"{personaggio2['classe']} aumenta il suo attacco di {abilita_valore}. Nuovo attacco: {personaggio2['attacco']}")
                elif abilita_nome == "Pugnali acidi":
                    for p in partita1:
                        p["difesa"] -= p["difesa"] // 4
                    print(f"{personaggio2['classe']} riduce la difesa degli avversari.")
                elif abilita_nome == "Favore degli dei":
                    debole = min(partita2, key=lambda p: p["vita"])
                    debole["vita"] += abilita_valore
                    print(f"{personaggio2['classe']} cura {debole['classe']} di {abilita_valore} punti vita.")

            if partita_fine(partita1, partita2):
                return

        turno += 1
    vita_partita1 = sum(p["vita"] for p in partita1)
    vita_partita2 = sum(p["vita"] for p in partita2)

    if vita_partita1 > vita_partita2:
        print("Partita 1 vince!")
    elif vita_partita2 > vita_partita1:
        print("Partita 2 vince!")
    else:
        print("Pareggio!")

partita1 = crea_party()
partita2 = crea_party()

combattimento(partita1, partita2)








