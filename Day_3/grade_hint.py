mark1:float =float(input("Enter the mark for subject 1: "))
mark2:float =float(input("Enter the mark for subject 2: "))
mark3:float =float(input("Enter the mark for subject 3: "))
mark4:float =float(input("Enter the mark for subject 4: "))
mark5:float =float(input("Enter the mark for subject 5: "))

def average_cal(m1: float,m2: float,m3:float,m4:float,m5:float) -> float:
    return (m1 + m2 + m3 + m4 + m5) / 5

average=average_cal(mark1,mark2,mark3,mark4,mark5)

print(f"The average mark is: {average}") 
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