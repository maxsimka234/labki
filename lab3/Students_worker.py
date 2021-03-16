import collections
import files
import os
Student=collections.namedtuple('Student',['name', 'surname', 'arithmetic_mean'])
def Get_mean(Student):
    i=0
    Arithmetic_mean_tmp=list(Student.arithmetic_mean)
    while i < len(Arithmetic_mean_tmp):
        if Arithmetic_mean_tmp[i]==',':
            Arithmetic_mean_tmp[i]='.'
            break
        i+=1
    Arithmetic_mean=''.join(Arithmetic_mean_tmp)        
    return float(str(Arithmetic_mean))

def Clear_file(pfile):
    pfile.seek(0)
    pfile.truncate()
    return

def Scan_students(File):   
    Students=[]
    for line in File.readlines():
        if line!="\n" and " ":
            student_info=line.split()
            Students.append(Student(student_info[0],student_info[1],student_info[2]))
        
    return Students

def Print_students_information(Students):
    n=0
    for i in Students:
        print(n,". ", i.name," ",i.surname," ",i.arithmetic_mean)
        n+=1
    return
    
def Write_new_student(File,Student,Students=None):
    if(Students!=None):
        Students.append(Student)
    File.writelines("\n"+Student.name+" "+Student.surname+" "+Student.arithmetic_mean)
    return

def Create_student(Name,Surname,Arithmetic_mean='0'):
    return Student(Name,Surname,Arithmetic_mean)

def Sort_by_arithmetic_mean(File,Students):
    Clear_file(File)
    Sorted_students=sorted(Students,key=Get_mean)
    Sorted_students.reverse()
    Students[:]=Sorted_students
    for student in Sorted_students:
        Write_new_student(File,student)    
    return
def Scan_directory():
    for filename in  os.listdir():
        print(filename)
        