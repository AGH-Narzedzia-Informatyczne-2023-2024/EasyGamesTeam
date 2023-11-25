import random

print("Witaj w naszej grze!\n")
print("choose game mode:"
      "\nto easy(0)"
      "\nrandom(1)"
      "\nnormal(2)")
game_mode = int(input("\ngameMode:"))
if (game_mode == 0):
    while True:
        while True:
            try:
                print("1. Papier\n")
                print("2. Kamien\n")
                print("3. Nozyce\n")
                print(4. Wyjscie)
                wybor = input("Wybierz swoja opcje:")
                if wybor == 4:
                    break
                wybor = int(wybor)
                break
            except ValueError:
                print('\nNieprawidlowy wybor, sproboj jeszcze raz!\n')
                pass
        if wybor == 4:
            print('Koniec rozgrywki')
            break
        if wybor == 1:
            print("\nOoops, ja wybralem nozyce, przegrywasz :))\n")
        elif wybor == 2:
            print("\nOoops, ja wybralem papier, przegrywasz :))\n")
        elif wybor == 3:
            print("\nOoops, ja wybralem kamien, przegrywasz :))\n")
        else:
            print('\nNieprawidlowy wybor, sproboj jeszcze raz!\n')

if (game_mode == 1):
    while True:
        while True:
            try:
                print("1. Papier\n")
                print("2. Kamien\n")
                print("3. Nozyce\n")
                print(4. Wyjscie)
                wybor = input("Wybierz swoja opcje (lub 'stop' jesle chcesz zakonczyc):")
                if wybor == 4:
                    break
                wybor = int(wybor)
                break
            except ValueError:
                print('\nNieprawidlowy wybor, sproboj jeszcze raz!\n')
                pass
        if wybor == 4:
            print('Koniec rozgrywki')
            break
        wybor = int(wybor)
        comp_choose = random.randint(1, 3)
        if (wybor == comp_choose):
            print(f"\nRemis! Wybrales: {wybor}, wybralem: {comp_choose}.\n")
        elif ((wybor == 1 and comp_choose == 2) or (wybor == 2 and comp_choose == 3) or (
                wybor == 3 and comp_choose == 1)):
            print(f"\nWygrales! Wybrales: {wybor}, wybralem: {comp_choose}.\n")
        elif ((wybor == 2 and comp_choose == 1) or (wybor == 3 and comp_choose == 2) or (
                wybor == 1 and comp_choose == 3)):
            print(f"\nPrzegrales! Wybrales: {wybor}, wybralem: {comp_choose}.\n")
        else:
            print('\nNieprawidlowy wybor, sproboj jeszcze raz!\n')
if (game_mode == 2):
    None
