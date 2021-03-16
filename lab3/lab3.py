import os
import Students_worker as SW


def cls():
    os.system('cls' if os.name=='nt' else 'clear')

while True: 
    print("\n1.scan directory\n2.open file\n0.exit")
    i=int(input("input operation : "))
    cls()
    if(i==1):
        SW.Scan_directory()
    if(i==2):
        file_name=input("Input file name: ")
        File=open(file_name,"r+")
        Students=SW.Scan_students(File)
        while True:
             print("\n1.print students in file\n2.sort\n3.add student\n0.exit (save)")
             j=int(input("input operation : "))
             cls()
             if(j==1):
                 SW.Print_students_information(Students)
             if(j==2):
                 SW.Sort_by_arithmetic_mean(File,Students)
             if(j==3):
                 Name=input("input student name: ")
                 surName=input("input student surname: ")
                 arefmetic_Mean=input("input student arefmetic mean : ")
                 SW.Write_new_student(File,SW.Create_student(Name,surName,arefmetic_Mean),Students)
             if(j==0):
                 File.close()
                 break
             if(j!=1 and j!=2 and j!=3 and j!=0):
                 print("eror command! ")
    if(i==0):
        break
    if(i!=1 and i!=2 and i!=0):
        print("eror command! ")
