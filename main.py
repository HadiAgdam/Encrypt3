from Encrypter import Encrypter
from os import system
from pyperclip import copy
from threading import Timer
from random import randint


def clearClipBoard():
    copy("")




if __name__ == "__main__":

    i = input("key, key_file_path: ").split(' ')
    path = "KEY"

    if len(i) == 2:
        path = i[1]

    keys = input("keys :")
    if keys == '':
        keys = f"{randint(1, 100)} {randint(1, 100)}"
        print(f"{keys.split(' ')[0]} {keys.split(' ')[1]}")
    e = Encrypter(i[0], path, keys.split(' '))
    print()
    while True:
        command = input("command :")


        # if command.startswith("ex"):
        #     r1 = int(command.split(" ")[1])
        #     r2 = int(command.split(" ")[2])

        #     i = 5 + len(command.split(" ")[1]) + len(command.split(" ")[2])

        #     print()
        #     en = e.encrypt(command[i:], r1, r2)
        #     print(en[0])
        #     print(en[1], en[2])
        #     print()

        if command.startswith("e"):
            print()
            en = e.encrypt(command[2:])
            print(en)
            print()
        
        elif command.startswith("cp"):
            timer = Timer(10, clearClipBoard, ())
            print()
            en = e.encrypt(command[3:])
            copy(en)
            timer.start()
            print(en)

            print()

        elif command.startswith("d"):
            print()
            x = e.decrypt(command[2:])
            print("Encrypt1 :")
            print(x[0])

            print()

            print("Encrypt2 :")
            print(x[1])

            print()


            print("Encrypt3 :")
            print(x[2])

            print()

            print("Encrypt4 :")
            print(x[3])

            print()

        elif command == "clear":
            system("clear")

        else:
            print("command not found")
