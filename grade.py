mark1 =float(input("Enter the mark for subject 1: "))
mark2 =float(input("Enter the mark for subject 2: "))
mark3 =float(input("Enter the mark for subject 3: "))
mark4 =float(input("Enter the mark for subject 4: "))
mark5 =float(input("Enter the mark for subject 5: "))
average = (mark1 + mark2 + mark3 + mark4 + mark5) / 5
print("The average mark is: " + str(average)) 
if average >= 90:
    print("Grade: A")
elif average >= 80:
    print("Grade: B")
elif average >= 70:
    print("Grade: C")
elif average >= 60:
    print("Grade: D")
else:
    print("Grade: F")
    