# put your python code here
x,y=input().split()
x=int(x)
y=int(y)
for i in range(x,y+1):
    if i%15==0:
        print('FizzBuzz')
    elif i%3==0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    else:
        print(i)