import random

print("Witaj w naszej grze!\n")
print("choose game mode:"
      "\nto easy(0)"
      "\nrandom(1)"
      "\nnormal(2)")
game_mode = int(input("\ngameMode:"))
if (game_mode == 0):
    while True:
        print("1. Papier\n")
        print("2. Kamien\n")
        print("3. Nozyce\n")
        wybor = input("Wybierz swoja opcje (lub 'stop' jesle chcesz zakonczyc):")
        if(wybor == 'stop'):
            print('Koniec rozgrywki')
            break
        if int(wybor) == 1:
            print("Ooops, ja wybralem nozyce, przegrywasz :))\n")
        if int(wybor) == 2:
            print("Ooops, ja wybralem papier, przegrywasz :))\n")
        if int(wybor) == 3:
            print("Ooops, ja wybralem kamien, przegrywasz :))\n")

if (game_mode == 1):
    while True:
        print("1. Papier\n")
        print("2. Kamien\n")
        print("3. Nozyce\n")
        wybor = input("Wybierz swoja opcje (lub 'stop' jesle chcesz zakonczyc):")
        if(wybor == 'stop'):
            print('Koniec rozgrywki')
            break
        comp_choose = random.randint(1, 3)
        if (int(wybor) == comp_choose):
            print(f"remis-wybrales:{wybor},wybralem{comp_choose}")
        if ((int(wybor) == 1 and comp_choose == 2) or (int(wybor) == 2 and comp_choose == 3) or (
                int(wybor) == 3 and comp_choose == 1)):
            print(f"wygrales-wybrales:{wybor},wybralem{comp_choose}")
        if ((int(wybor) == 2 and comp_choose == 1) or (int(wybor) == 3 and comp_choose == 2) or (
                int(wybor) == 1 and comp_choose == 3)):
            print(f"przegrales-wybrales:{wybor},wybralem{comp_choose}")
if (game_mode == 2):
    None
