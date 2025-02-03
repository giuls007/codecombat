import random

nomi = ["Drakar", "Lirael", "Thalas", "Eldorin", "Lyndra", "Kaelith", "Sylas", "Faelan", "Mirabelle", "Zephyr",
        "Isolde", "Thorn", "Elysia", "Varian", "Aeris", "Nerys", "Gwynn", "Eldira", "Soren", "Lirion"]
cognomi = ["Stoneforge", "Moonshadow", "Starwhisper", "Thunderbeard", "Fireheart", "Ravenwing", "Icebane",
           "Stormrider", "Swiftfoot", "Dragonflame", "Shadowcloak", "Ironhammer", "Frostbeard", "Silverleaf",
           "Goldenshield", "Windrider", "Hawkseye", "Deepstone", "Steelheart", "Oakenshield"]

def genera_nome():
    nome = random.choice(nomi)
    cognome = random.choice(cognomi)
    return nome + " " + cognome
def lancia_dadi(tipo_giocatore):
    tiri_dadi = []
    if tipo_giocatore == "giocatore1":
        num_dadi = 6
        facce = 6
    elif tipo_giocatore == "giocatore2":
        num_dadi = 4
        facce = 12

    for _ in range(num_dadi):
        tiri_dadi.append(random.randint(1, facce))

    tiri_dadi.sort()

    piu_basso = tiri_dadi.pop(0)
    piu_alto = tiri_dadi.pop(-1)

    return tiri_dadi, piu_basso, piu_alto
def calcola_danno(nome_giocatore, salute_giocatore, scudo, tiri_dadi, piu_basso, piu_alto):
    print(f"[{nome_giocatore}] dadi: {tiri_dadi}")
    print(f"Il dado più basso ({piu_basso}) e il più alto ({piu_alto}) sono stati rimossi.")

    danno = sum(tiri_dadi) - scudo
    print(f"[{nome_giocatore}] Danno: {danno} ({sum(tiri_dadi)}-{scudo})")

    if danno > 0:
        salute_giocatore -= danno
    else:
        print(f"[{nome_giocatore}] Danno: 0 ({sum(tiri_dadi)}-{scudo}). L'attacco è stato evitato.")

    return salute_giocatore
def game_loop():
    giocatore1_nome = genera_nome()
    giocatore2_nome = genera_nome()

    giocatore1_salute = 98
    giocatore2_salute = 82
    giocatore1_scudo = 6
    giocatore2_scudo = 9

    print(f"{giocatore1_nome} salute iniziale: {giocatore1_salute}")
    print(f"{giocatore1_nome} scudo: {giocatore1_scudo}")
    print(f"{giocatore2_nome} salute iniziale: {giocatore2_salute}")
    print(f"{giocatore2_nome} scudo: {giocatore2_scudo}")

    turni = 0

    while giocatore1_salute > 0 and giocatore2_salute > 0:
        turni += 1

        giocatore1_tiri, giocatore1_basso, giocatore1_alto = lancia_dadi("giocatore1")
        giocatore1_salute = calcola_danno(giocatore1_nome, giocatore1_salute, giocatore2_scudo, giocatore1_tiri, giocatore1_basso, giocatore1_alto)

        giocatore2_tiri, giocatore2_basso, giocatore2_alto = lancia_dadi("giocatore2")
        giocatore2_salute = calcola_danno(giocatore2_nome, giocatore2_salute, giocatore1_scudo, giocatore2_tiri, giocatore2_basso, giocatore2_alto)

        print(f"[{giocatore1_nome}] Salute: {giocatore1_salute}")
        print(f"[{giocatore2_nome}] Salute: {giocatore2_salute}")

    if giocatore1_salute <= 0 and giocatore2_salute <= 0:
        print("È un pareggio!")
    elif giocatore1_salute <= 0:
        print(f"{giocatore2_nome} vince!")
    else:
        print(f"{giocatore1_nome} vince!")

    print(f"Turni giocati: {turni}")

game_loop()

