from Encrypter import Encrypter
from os import system

# key

if __name__ == "__main__":

    i = input("key, path: ").split(' ')
    path = "KEY"

    if len(i) == 2:
        path = i[1]

    e = Encrypter(i[0], path)
    print()
    while True:
        command = input("command :")


        if command.startswith("ex"):
            r1 = int(command.split(" ")[1])
            r2 = int(command.split(" ")[2])

            i = 5 + len(command.split(" ")[1]) + len(command.split(" ")[2])

            print()
            en = e.encrypt(command[i:], r1, r2)
            print(en[0])
            print(en[1], en[2])
            print()

        elif command.startswith("e"):
            print()
            en = e.encrypt(command[2:])
            print(en[0])
            print(en[1], en[2])
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


        elif command == "clear":
            system("clear")

        else:
            print("command not found")
