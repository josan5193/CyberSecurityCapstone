#In order to work unless openpyxl is already installed on your pc
#You must type 'pip install openpyxl'
#Also make sure the database file is in same file as code
from openpyxl import *

#used to mass enter users into database
#Warning using this function resets database names so be careful use only once
def create_voterdb():
    workbook = Workbook()
    sheet = workbook.active

    usernum = int(input('Enter number of users to load into database: '))
    for x in range(usernum):
        print('Name ',x+1)
        name = input('Enter Name: ')
        sheet["A"+str((x+1))] = name

    workbook.save(filename="Reg_VoterDB.xlsx")


#Reads the name database and returns it to main function
def read_db():
    wb = load_workbook("Reg_VoterDB.xlsx")
    #print(wb.sheetnames)
    sheet = wb['Sheet']
    #print(sheet['A1'].value)
    #print(sheet['A3'].value)
    #print(sheet['A3'].value)
    return wb

#Writes all contents of the modified wb to the database file
def write_db(wb):
    wb.save("Reg_VoterDB.xlsx")


def testmain():
    wb = read_db()
    sheet = wb['Sheet']
    print(sheet['A3'].value)
    sheet['A4'] = 'Test'
    write_db(wb)

    
    
    
    
