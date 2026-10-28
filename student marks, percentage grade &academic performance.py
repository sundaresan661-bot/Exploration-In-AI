# student marks, percentage and grade
name=input("Enter student name: ")
n=int(input("Enter number of subjects: "))
total=0
for i in range(1,n+1):
    marks=float(input(f"Enter marks for subject {i}: "))
    total+=marks
percentage=total/n
if percentage>=90:
    grade='A+'
    performance='outstanding'
elif percentage>=80:
    grade='A'
    performance='excellent'
elif percentage>=70:
    grade='B'
    performance='very good'
elif percentage>=60:
    grade='C'
    performance='good'
elif percentage>=50:
    grade='D'
    performance='average'
else:
    grade='F'
    performance='needs improvement'
print("\n---Academic Performance---")
print("student name:",name)
print("total marks:",total)
print("percentage:",round(percentage,2),"%")
print("grade:",grade)
print("performance:",performance)
