# PROBLEMA DI MONTY HALL

import random
import time

def montyhall(num):
    if not isinstance(num, int):
        raise TypeError("Il numero di porte deve essere un numero intero!")
    if num<3:
        raise ValueError("Il gioco richiede almeno 3 porte!")
    # POSIZIONE DELL'AUTO
    doors = [False] * num # False indica le capre, True indica l'auto
    car = random.randint(0,num-1)
    doors[car] = True
    # Inzio del gioco
    n = int(input(f"Scegli un numero tra 1 e {num}:\n"))
    if not doors[n-1]:
        if num == 3:
            print("Ok, adesso aprirò una porta in cui so che c'è una capra...")
        else:
            print("Ok, adesso aprirò delle porte in cui so che ci sono delle capre...")
        time.sleep(3)
        for i in range(len(doors)):
            if i != (n-1) and not doors[i]:
                print(f"Nella porta {i+1} c'è una capra!")
        print(f"Rimangono chiuse la porta {n} (ossia quella scelta da te) e la porta {car+1}.")
        while True:
            question = int(input("Vuoi cambiare la tua scelta? (digita 0 per NON cambiare, oppure 1 per cambiare)\n"))
            if question==0 or question==1:
                if question==0:
                    print(f"Ok, quindi hai deciso di restare sulla porta {n}, vediamo la soluzione...")
                    time.sleep(3)
                    print(f"Hai perso! Mi dispiace, la macchina era nella porta {car+1}.")
                    return
                if question==1:
                    print(f"Ok, quindi hai deciso di cambiare la porta, scegliendo la {car+1} al posto della {n}, vediamo la soluzione...")
                    time.sleep(3)
                    print(f"Congratulazioni, hai vinto! la macchina era proprio nella porta {car+1}!")
                    return
            else:
                print("Devi scegliere un numero tra 0 e 1")
    if doors[n-1]:
        nocar = random.randint(0,num-1)
        while nocar == n-1: # Il ciclo while serve ad evitare che nocar sia uguale a n
            nocar = random.randint(0,num-1)
        if num == 3:
            print("Ok, adesso aprirò una porta in cui so che c'è una capra...")
        else:
            print("Ok, adesso aprirò delle porte in cui so che ci sono delle capre...")
        time.sleep(3)
        for i in range(len(doors)):
            if i != (n-1) and i != nocar:
                print(f"Nella porta {i+1} c'è una capra!")
        print(f"Rimangono chiuse la porta {car+1} (ossia quella scelta da te) e la porta {nocar+1}.")
        while True:
            question = int(input("Vuoi cambiare la tua scelta? (digita 0 per NON cambiare, oppure 1 per cambiare)\n"))
            if question==0 or question==1:
                if question==0:
                    print(f"Ok, quindi hai deciso di restare sulla porta {car+1}, vediamo la soluzione...")
                    time.sleep(3)
                    print(f"Congratulazioni, hai vinto! la macchina era proprio nella porta {car+1}!")
                    return
                if question==1:
                    print(f"Ok, quindi hai deciso di cambiare la porta, scegliendo la {nocar+1} al posto della {car+1}, vediamo la soluzione...")
                    time.sleep(3)
                    print(f"Hai perso! Mi dispiace, la macchina era nella porta {car+1}.")
                    return
            else:
                print("Devi scegliere un numero tra 0 e 1")


def newgame():
    while True:
        try:
            d = int(input("Vuoi giocare ancora? (0 per NO, 1 per SI)\n"))
            if d == 0:
                print("Grazie per aver giocato!")
                return False
            elif d == 1:
                print("\033[2J\033[H") # serve a cancellare il contenuto del terminale (valido solo su linux/mac e su alcuni playground come online python)
                return True
            else:
                print("Devi scegliere 0 o 1!")
        except ValueError:
            print("Devi inserire un numero!")

while True:
    try:
        n = int(input("PROBLEMA DI MONTY-HALL!\nCi saranno varie porte, in una di queste c'è un'auto e nelle altre delle capre. Tu dovrai trovare l'auto.\nInnanzitutto, con quante porte vuoi giocare? (devono essere minimo 3)\n"))
        montyhall(n)
    except:
        print("C'è stato un errore!")
    if not newgame():
        break