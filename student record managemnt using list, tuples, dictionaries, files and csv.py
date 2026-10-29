import csv
student=[{"Roll no ":"101","Name":"Anitha","Department":"CSE","Marks":99,
          "Roll no ":"102","Name":"Bala","Department":"CSE","Marks":91,
          "Roll no ":"103","Name":"Chitra","Department":"ESE","Marks":78,}]
course=("Python",4)
print("Coure Tuple:",course)
with open("students.csv","w")as file:
    for stu in student:
        file.write(str(student)+"\n")
with open("student.csv","w",newline=" ")as file:
    fields=["Roll no","Name","Department","Marks"]
    writer=csv.DictWriter(file,fieldnames=fields)
    writer.writeheader()
    for stu in student:
        writer.writerow(stu)
print("Record from CSV file")

with open("students.csv","r")as file:
    reader=csv.DictReader(file)
    for row in reader:
        print(row["Roll no"],row["Name"],row["Department"],row["Marks"])
