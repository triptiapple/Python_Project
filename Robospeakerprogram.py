import os

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1 Created by Tripti")
    while True:
        x = input("Enter what you want me to speak: ")
        if x == "q":
            os.system("Say 'bye bye'")
            break
        command = f"Say {x}"
        os.system(command)
