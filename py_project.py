def display():
    file = open("C:\yunus\students.txt","r")
    for line in file:
        students = line.strip().split(',')
        print(*students, sep='\t')
    file.close()

def insert(stdid,name,cgpa,date,gender):
    file = open("C:\yunus\students.txt","a")
    txt = f"{stdid},{name},{cgpa},{date},{gender}"
    file.write(txt)
    file.write('\n')

    file.close()

def modify(stdid,field,new_value):
    file = open("C:\yunus\students.txt","r+")
    new_f = file.readlines()
    file.seek(0)
    for line in new_f:
        if(str(stdid) in line):
            details = line.strip().split(',')
            details[2] = str(new_value)
            file.write(",".join(details)+"\n")
        else:
            file.write(line)
    file.truncate()


def delete(stdid):
    file = open("C:\yunus\students.txt","r+")
    new_f = file.readlines()
    file.seek(0)
    for line in new_f:
        if str(stdid) not in line:
            file.write(line)
    file.truncate()

def stats():
    file=open("C:\yunus\students.txt", "r")
    students=[]
    for student in file.readlines():

        students.append(student.strip().split(","))
    file.close()

    file=open("C:\yunus\stats.txt", "w")


    avg_cgpa=0
    total=0
    male=0
    female=0

    for student in students:
        if student[4]=="M":
            male=male+1
        if student[4]=="F":
            female=female+1
        avg_cgpa=avg_cgpa+float(student[2])
        total=total+1

    avg_cgpa=avg_cgpa/total

    file.write(f"Number of male students: {male}\n")
    file.write(f"Number of female students: {female}\n")
    file.write("Average of cgpa: {:.2f}\n".format(avg_cgpa))
    file.write(f"Number of Total Students: {total}\n")
    file.close()






print("Students List:")
display()
modify(9821,'cgpa',3.12)
insert(3579,'Bruce Willis',2.1,'12-08-1981','M')
delete(1235)
print("\n\nNew Students List:")
display()
stats()
