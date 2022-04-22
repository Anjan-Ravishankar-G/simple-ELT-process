def extract():
    #can be used as an extract block

    import mysql.connector

    mydb= mysql.connector.connect(host='localhost',user='root',passwd='12345',database='fox')

    mycursor = mydb.cursor()

    mycursor.execute("select * from cricketers_data")
    a=''
    for i in mycursor:
        a=a+(str(i))
    print(a)
extract()        
    