print(" ===== Enter Your Details   ===== ") 


#This segment stores student's Basic data 

Basic_Data=[]
b1=input("Enter your Name:")
Basic_Data.append(b1)
b2=input("Enter your Age:")
Basic_Data.append(b2)
b3=input("Enter your Course:")
Basic_Data.append(b3)
b4=input("Enter your College Name:")
Basic_Data.append(b4)
 

# This segment store student's Skills

Skills=[]
s1=input("Enter your  Skill 1:")
Skills.append(s1)
s2=input("Enter your Skill 2:")
Skills.append(s2)
s3=input("Enter your Co Skill 3:")
Skills.append(s3)
s4=input("Enter your Col Skill 4:")
Skills.append(s4)



# This segment store student's valuable Data

v1=input("Enter your  Course Name:")
v2=input("Enter your  Semester:")
v3=input("Enter your Roll No:")

Valuable_Data=(v1,v2,v3)


print("\n\n\n\n\n   ===== STUDENT PROFILE =====")

print("\nName:", Basic_Data[0])
print("Age:", Basic_Data[1])
print("Course:", Basic_Data[2])
print("College:", Basic_Data[3])

print("\nSkills:")
print("Skill 1:", Skills[0])
print("Skill 2:", Skills[1])
print("Skill 3:", Skills[2])
print("Skill 4:", Skills[3])

print("\nValuable Data:")
print("Course Name:", Valuable_Data[0])
print("Semester:", Valuable_Data[1])
print("Roll No:", Valuable_Data[2])
