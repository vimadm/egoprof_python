# put your python code here
a=input()
b=a.split(' ')
if b[1]=='plus':
    print(int(b[0])+int(b[2]))
if b[1]=='minus':
    print(int(b[0])-int(b[2]))
if b[1]=='multiply':
    print(int(b[0])*int(b[2]))
if b[1]=='divide':
    print(int(b[0])//int(b[2]))