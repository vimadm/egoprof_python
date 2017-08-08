def fun(n):
    if n == 1:
        return 1
    elif n%2==0 and n>1:
        n=int(n/2)
        print(int(n))
        return fun(n)
    elif n%2==1 and n>1:
        n=int(n*3+1)
        print(int(n))
        return fun(n)
n = int(input(""))
fun(n)
