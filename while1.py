check = str
check1 = str
while True:
    command = input("> " ).lower()
    if command == check:
        print("The car has already started")
        continue
    elif command == check1:
        print("The car has already stopped")
        continue
    if command == "start":
        print("The car started")
        check = command
        check1 = ""
    elif command == "stop":
        print("The car stopped")
        check1 = command
        check = ""
    elif command == "help":
        print('''
start - to start the car
stop - to stop the car
quit - to quit the program  
        ''')
    elif command == "quit":
        print("Quitting...")
        break
    else:
        print("Invalid command!")

