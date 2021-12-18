import os

if __name__ == "__main__":
    os.system("clear")
    print(
        "Welcome to Family Tree Maker!\n" +
        "You want to... \n" +
        "1. Create a new one\n" +
        "2. Generate a new one from existed json file\n"
    )
    command = input("Your command: ")
