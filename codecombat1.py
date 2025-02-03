import random
def inizializza_gioco():
    punti_vita = 30
    torni = 0
    lista_danni = []
    return punti_vita, torni, lista_danni
def turno(punti_vita):
    danno = random.randint(1, 6)
    punti_vita -= danno
    return danno, max(punti_vita, 0)
def stampa_rapporto_turno(danno, punti_vita):
    print(f"Danno subito: {danno}.")
    print(f"Punti vita rimanenti: {punti_vita}")
def stampa_rapporto_finale(torni, lista_danni):
    print("Il personaggio è stato sconfitto.")
    print(f"Sono stati giocati {torni} turni.")
    print("Danni subiti in ogni turno:", lista_danni)

punti_vita, torni, lista_danni = inizializza_gioco()
print(f"Punti vita iniziali: {punti_vita}")

while punti_vita > 0:
    danno, punti_vita = turno(punti_vita)
    lista_danni.append(danno)
    torni += 1
    stampa_rapporto_turno(danno, punti_vita)

stampa_rapporto_finale(torni, lista_danni)