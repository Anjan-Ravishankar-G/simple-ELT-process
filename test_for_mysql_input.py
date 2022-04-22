import mysql.connector

def load(a):
    
    puncu="!./\{}[]!~@#$%^&*()-_<>"''
    for ele in a:
        if ele in puncu:
            a=a.replace(ele,"")
    b=a.split(',')
    print(b)        
    mydb= mysql.connector.connect(host='localhost',user='root',passwd='12345',database='fox')

    mycursor = mydb.cursor()

    # mycursor.execute("CREATE TABLE testcase1 (rawdata varchar(100)) ")
    for i in b:
        print(i)
        mycursor.execute("INSERT INTO testcase1 (rawdata) VALUES (%s)",(list(i)))

    mycursor.execute("select * from testcase1")
    for i in mycursor:
        print(i)

    mydb.close()    
def extract():
    mydb= mysql.connector.connect(host='localhost',user='root',passwd='12345',database='fox')

    mycursor = mydb.cursor()

    mycursor.execute("select * from testtable")
    a=''
    for i in mycursor:
        a=a+(str(i))
    print(a)
    mydb.close()
    load(a)
extract() 

    
    