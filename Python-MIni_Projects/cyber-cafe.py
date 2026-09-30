import random

print("\t\t ====== CYBER CAFE ======")

menu = [
    "New session",
    "View all Sessions",
    "Search Sessions",
    "Exit"
]

for num, options in enumerate(menu, start=1):
    print(f"{num}. {options}")

print("\n")

while True:
    try:
        Sec_option = int(input("Enter your choice: "))

    except ValueError:
        print("Invalid! Enter a number.")
        continue

    if Sec_option == 1:
        print("\t\t\nNew session")

        while True:
            try:
                Hex_code = "#" + "".join(
                    random.choices("0123456789ABCDEF", k=7)
                )

                name = input("Enter your name: ")
                com_no = int(input("Your computer No: "))
                hours = int(input("No of hours you want: "))

                bill = hours * 40

                print(f"Your bill is INR {bill}")
                print(f"Your Session ID is {Hex_code}")
                print("\n")

                with open("data.txt", "a") as file:
                    file.write(
                        f"Session id {Hex_code}\n"
                        f"Name: {name}\n"
                        f"Computer No: {com_no}\n"
                        f"Hours: {hours}\n"
                        f"Bill: {bill}\n\n"
                    )

                break

            except ValueError:
                print("Invalid! Input try again...")
                continue

    elif Sec_option == 2:
        print("\n====== ALL SESSIONS ======\n")

        with open("data.txt", "r") as file:
            lines = file.readlines()

        if lines:
            for line in lines:
                print(line, end="")
        else:
            print("No sessions found.")

    elif Sec_option == 3:
        search = input("Enter your session id: ")
        found = False

        with open("data.txt", "r") as file:
            sessions = file.read().split("\n\n")

        for session in sessions:
            if f"Session id {search}" in session:
                print("\n====== SESSION FOUND ======")
                print(session)
                found = True
                break

        if not found:
            print("Session ID not found.")

    elif Sec_option == 4:
        print("Exiting Cyber Cafe...")
        break

    else:
        print("Invalid choice. Enter 1-4.")


    

