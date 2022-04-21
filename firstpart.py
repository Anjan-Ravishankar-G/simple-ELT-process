from collections import Counter
def extract():
    if count==0:
        d=input('\n Enter the directory with 2 front slash to open the file that you want for first part ,ex:<C://Users//ADMIN//anjan-python//fileproject//documents//1.txt>)')
        f=open(d,'r')
        content=f.read()
        f.close()
        transformation(content)
    elif count==1:
        d=input('\n Enter the directory with 2 front slash to open the file that you want for second part ,ex:<C://Users//ADMIN//anjan-python//fileproject//documents//1.txt>)')
        f=open(d,'r')
        content=f.read()
        f.close()
        transformation1(content)    
    
def transformation(content):
    c=content.upper()
    # print(c)
    writer(c)

def transformation1(content):
    c2=content.lower()
    # print(c2)
    puncu="!.,/\{}[]!~@#$%^&*()-_<>"
    for ele in c2:
        if ele in puncu:
            c2=c2.replace(ele,"")
    c=list(c2.split())
    c1=Counter(c)
    key=list(c1.keys())
    value=list(c1.values())
    d=[]
    for i in range(0, len(key)):
        str1=key[i]+'->'+str(value[i])
        d.append(str1)
    writer(d)    
    
def writer(c):
    d1=input('\n Enter directory where you want to write the file with file name as txt, ex:<C://Users//ADMIN//anjan-python//fileproject//writtendoc//xyz.txt> ')
    f=open(d1,'w')
    if count==0:
        f.write(c)
        f.close()
        print('\n First part to write into a file is done')
    elif count==1:    
        sentence=''
        for i in range(0,len(c)):
            sentence=c[i]+'\n'
            f.write(sentence)   
        f.close()
        print('second part to write into a file is done')
    
print('\nTHE FIRST PART TO WRITE INFORMATION IN ALL CAPS TO ANOTHER FILE')
count=0
extract()
print('\n THE SECOND PART TO COUNT UNIQUE WORDS AND WRITE THE CONTENTS TO ANOTHER FILE')
count=1
extract()


