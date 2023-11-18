import random

print("Witaj w naszej grze!\n")
game_mode = 0
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
        wybor = int(input("Wybierz swoja opcje:"))
        if wybor == 1:
            print("Ooops, ja wybralem nozyce, przegrywasz :))\n")
        if wybor == 2:
            print("Ooops, ja wybralem papier, przegrywasz :))\n")
        if wybor == 3:
            print("Ooops, ja wybralem kamien, przegrywasz :))\n")

if (game_mode == 1):
    None
if (game_mode == 2):
    None
