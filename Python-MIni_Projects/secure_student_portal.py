student = {}        

while True:
    # Main-Menu
    print("\n\t\t\t ===== STUDENT PORTAL =====")
    print("1. Register Student")
    print("2. View Profile")
    print("3. Add Skills")
    print("4. View Skills")
    print("5. Login Verification")
    print("6. Exit")

    # Options mapped to numbered inputs
    option_1 = "1"
    option_2 = "2"
    option_3 = "3"
    option_4 = "4"
    option_5 = "5"
    option_6 = "6"

    option = input("\nEnter your choice (1-6): ")

    # 1. Register Student
    if option == option_1:
        print("\n\t\t\t Register yourself")
        name = input("Enter Your Name: ")
        age = int(input("Enter Your Age: "))
        roll_number = input("Enter Your Roll Number: ")
        course = input("Enter Your Course: ")
        college = input("Enter Your College: ")
        password = input("Enter Your Password: ")

        student = {
            "name_key": name,
            "age_key": age,
            "roll_number_key": roll_number,
            "course_key": course,
            "college_key": college,
            "password_key": password,
            "skills_key": ()
        }
        print("\n\t\t\tYou have registered successfully!")

    # 2. View Profile
    elif option == option_2:
        if not student:
            print("\nNo student registered yet. Please register first!")
            continue

        print("\n\t\t\t View your Profile")
        name_p_v = input("Enter Your Name: ")
        roll_number_p_v = input("Enter Your Roll Number: ")

        if name_p_v == student['name_key'] and roll_number_p_v == student["roll_number_key"]:
            print(f"\nName\t: {student['name_key']}")
            print(f"Age\t: {student['age_key']}")
            print(f"Roll No\t: {student['roll_number_key']}")
            print(f"Course\t: {student['course_key']}")
            print(f"College\t: {student['college_key']}")
        else:
            print("\nInvalid Name or Roll Number!")

    # 3. Add Skills
    elif option == option_3:
        if not student:
            print("\nNo student registered yet. Please register first!")
            continue

        skill_1 = input("Enter your First Skill: ")
        skill_2 = input("Enter your Second Skill: ")
        skill_3 = input("Enter your Third Skill: ")
        skill_4 = input("Enter your Fourth Skill: ")

        # Save tuple directly into student dictionary
        student["skills_key"] = (skill_1, skill_2, skill_3, skill_4)
        print("\nSkills added successfully!")

    # 4. View Skills
    elif option == option_4:
        if not student or not student.get("skills_key"):
            print("\nNo skills added yet!")
        else:
            skills = student["skills_key"]
            print(f"\nTotal Skills: {len(skills)}")
            for skill_v_s in skills:
                print(f" - {skill_v_s}")

    # 5. Login Verification
    elif option == option_5:
        if not student:
            print("\nNo student registered yet. Please register first!")
            continue

        print("\n\t\t\t Login for Student Portal")
        Age = int(input("Enter Your Age: "))
        Password = input("Enter Your Password: ")

        # Check age restriction first
        if Age <= 16:
            print("\nYour Age is 16 or less. Not Eligible!")
        elif Age == student["age_key"] and Password == student["password_key"]:
            print("\nAccess Granted !!!!")
            print("Student Privilege Mode Enabled")
        else:
            print("\nWrong password or age mismatch.\nAccess Denied")

    # 6. Exit
    elif option == option_6:
        print("\nExiting Student Portal. Goodbye!")
        break

    else:
        print("\nInvalid choice! Please enter a number from 1 to 6.")

  