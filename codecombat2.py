import random
def crea_giocatore(dice_string: str) -> list:
    hp = random.randint(80, 100)
    scudo = random.randint(5, 10)
    return [hp, scudo, dice_string]
def attacca(attaccante: list, difensore: list) -> int:
    dice_string = attaccante[2]
    num_dadi, facce_dado = map(int, dice_string.split('d'))
    lanci = [random.randint(1, facce_dado) for _ in range(num_dadi)]
    valore_attacco = sum(lanci)

    danno = max(valore_attacco - difensore[1], 0)

    return danno, lanci
def ciclo_gioco(player1: list, player2: list) -> str:
    turni = 0

    while player1[0] > 0 and player2[0] > 0:
        turni += 1
        danno1, lanci1 = attacca(player1, player2)
        player2[0] -= danno1

        danno2, lanci2 = attacca(player2, player1)
        player1[0] -= danno2

        print(f"***Turn {turni}***")
        print(f"[Player1] Damage: {danno1} ({sum(lanci1)}-{player2[1]})")
        print(f"[Player2] Health: {player2[0]}")
        print("\t---")
        print(f"[Player2] Damage: {danno2} ({sum(lanci2)}-{player1[1]})")
        print(f"[Player1] Health: {player1[0]}")
        print("\t---")

    if player1[0] > 0:
        return "Player 1", turni
    elif player2[0] > 0:
        return "Player 2", turni
    else:
        return "Draw", turni
def simula_partite(n: int) -> dict:
    vittorie_player1 = 0
    vittorie_player2 = 0
    pareggi = 0
    turni_totali = 0

    for _ in range(n):
        player1 = crea_giocatore("4d6")
        player2 = crea_giocatore("2d12")

        print(f"Player1 starting health: {player1[0]}")
        print(f"Player1 shield: {player1[1]}")
        print(f"Player2 starting health: {player2[0]}")
        print(f"Player2 shield: {player2[1]}")
        print("\n")

        risultato, turni = ciclo_gioco(player1, player2)

        if risultato == "Player 1":
            vittorie_player1 += 1
        elif risultato == "Player 2":
            vittorie_player2 += 1
        else:
            pareggi += 1

        turni_totali += turni

    media_turni = turni_totali / n
    return {
        "Vittorie Player 1": vittorie_player1,
        "Vittorie Player 2": vittorie_player2,
        "Pareggi": pareggi,
        "Media turni": media_turni
    }

def main():
    risultati = simula_partite(10)

    print(f"\nVittorie Player 1: {risultati['Vittorie Player 1']}")
    print(f"Vittorie Player 2: {risultati['Vittorie Player 2']}")
    print(f"Pareggi: {risultati['Pareggi']}")
    print(f"Media dei turni per partita: {risultati['Media turni']}")

main()


