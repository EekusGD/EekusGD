#Register page
#PYDROID

import time
while True:
    print("Please, write your name.")
    name = input()
    if name == "" or name == " ":
        print("Name can't be blank.")
    else:
        print("Hello, " + name + ", Nice to meet you!")
        time.sleep(1)
        print("Now write your username.")
        username = input()
        if username == "" or username == " ":
            print("Username, like name, can't be blank.")
            print("")
            print("Because of you, we start again!:(")
        else:
            time.sleep(1)
            print("Good! now write your password.")
            password = input()
            if password == "" or password == " ":
                print("Come on, it's so easy to hack you with this password! Try thinking about something more!")
                print("")
                print("Because of you, we start again!:(")
                print("")
            else:
                print("")
                print("Good! Here's your information:")
                print("")
                print("Name: " + name)
                print("Username: @" + username)
                print("Password: " + password)
                break