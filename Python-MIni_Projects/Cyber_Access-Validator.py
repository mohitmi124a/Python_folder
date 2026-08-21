name = input("Enter your Name: ")
age = int(input("Enter your Age: "))
role = input("Enter your Role: ")
password = input("Enter your Password: ")

pass_code = "python123"

role_1 = "Admin"
role_2 = "Student"

# Access check
if password == pass_code and age >= 16:
    print("Access Granted")
    print("Welcome", name)

    # Role check
    if role == role_1:
        print("Administrator Mode Enabled")
    elif role == role_2:
        print("Student Privilege Mode Enabled")
    else:
        print("Invalid Trespassing")

else:
    print("Either your password is incorrect or your age is below consent.") 

        







