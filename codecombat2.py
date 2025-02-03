import random
def simula_battaglia():
    salute_giocatore1 = random.randint(80, 100)
    scudo_giocatore1 = random.randint(5, 10)
    attacco_giocatore1 = [random.randint(1, 6) for _ in range(4)]

    salute_giocatore2 = random.randint(80, 100)
    scudo_giocatore2 = random.randint(5, 10)
    attacco_giocatore2 = [random.randint(1, 12) for _ in range(2)]

    turni = 0
    while salute_giocatore1 > 0 and salute_giocatore2 > 0:
        turni += 1

        valore_attacco1 = sum(attacco_giocatore1)
        danno_giocatore1 = max(valore_attacco1 - scudo_giocatore2, 0)
        salute_giocatore2 -= danno_giocatore1

        valore_attacco2 = sum(attacco_giocatore2)
        danno_giocatore2 = max(valore_attacco2 - scudo_giocatore1, 0)
        salute_giocatore1 -= danno_giocatore2

        print(f"Turno {turni}: Salute Giocatore1 = {salute_giocatore1}, Salute Giocatore2 = {salute_giocatore2}")
        if salute_giocatore1 <= 0 or salute_giocatore2 <= 0:
            print(f"Giocatore1: {salute_giocatore1}, Giocatore2: {salute_giocatore2}")

    if salute_giocatore1 > 0 and salute_giocatore2 <= 0:
        return "Giocatore1", turni
    elif salute_giocatore2 > 0 and salute_giocatore1 <= 0:
        return "Giocatore2", turni
    else:
        return "Pareggio", turni

numero_partite = 10
turni_totali = 0
vittorie_giocatore1 = 0
vittorie_giocatore2 = 0
pareggi = 0

for _ in range(numero_partite):
    vincitore, turni = simula_battaglia()
    if vincitore == "Giocatore1":
        vittorie_giocatore1 += 1
    elif vincitore == "Giocatore2":
        vittorie_giocatore2 += 1
    else:
        pareggi += 1
    turni_totali += turni

print(f"\nVittorie Giocatore1: {vittorie_giocatore1}")
print(f"Vittorie Giocatore2: {vittorie_giocatore2}")
print(f"Pareggi: {pareggi}")
print(f"Numero medio di turni per partita: {turni_totali / numero_partite:.2f}")