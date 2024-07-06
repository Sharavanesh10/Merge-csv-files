import csv
import sys
def getdata():
    f=open("D:\sara\project\csv_file_excel.csv","a",newline='')
    w=csv.writer(f)
    print("FUNCTION FOR WRITE A CSV FILE TO EXCEL")
    n=int(input("Enter the number of records:"))
    for i in range(n):
        r=int(input("Enter the serial Number:"))
        name=input("Enter the Name of the Student:")
        batch=int(input("Enter the batch number:"))
        dept=input("Enter the department:")
        l=[r,name,batch,dept]
        w.writerow(l)
    f.close()
def displaydata():
    print("FUNCTION FOR READ A CSV FILE FROM EXCEL")
    f=open("D:\sara\project\csv_file_excel.csv","r")
    s=csv.reader(f)
    for i in s:
        print(i)
    f.close()
print("\n***********MENU*************")
while True:
    print("This is Menu for \n1.Get_data\n2.Display_data")
    ch=int(input("Enter the choice:"))
    if ch==1:
        getdata()
    elif ch==2:
        displaydata()
    else:
        print("!!!!Enter the correct choice!!!!")
        print("******THANK YOU******")
sys.exit()
