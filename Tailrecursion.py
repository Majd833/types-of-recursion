def tail(n,num):
    if n>num:
        return
    print(n)
    tail(n+1,num)
n=int(input("Enter the number to start counting;"))
tail(1,n)