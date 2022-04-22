import mysql.connector

def load(a):
    
    mydb= mysql.connector.connect(host='localhost',user='root',passwd='12345',database='fox')

    mycursor = mydb.cursor()

    mycursor.execute("CREATE TABLE testcase1 (rawdata varchar(1000)) ")
    mycursor.execute("INSERT INTO testcase1 (rawdata) VALUES ({})".format(a))
    mycursor.execute("SELECT * from testcase1")
    for i in mycursor:
        print(i)
def extract():
    mydb= mysql.connector.connect(host='localhost',user='root',passwd='12345',database='fox')

    mycursor = mydb.cursor()

    mycursor.execute("select * from cricketers_data")
    a=''
    for i in mycursor:
        a=a+(str(i))
    # print(a)
    mydb.close()
    load(a)
extract() 

    
    