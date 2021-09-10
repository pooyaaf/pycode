#create dict
students = {}
while True:
    student = input('enter students : ').split()
    if student[0]=='end':break
    students[student[0]]=int(student[1])

#reverse and sort
students = dict(reversed(sorted(students.items(),key=lambda item:item[1])))
#enum
for i,key in enumerate(students):
    print(i+1,key,students[key])
