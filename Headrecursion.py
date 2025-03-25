def head(n,num):
    if n>num:
        return 
    head(n+1,num)
    print(n)
n=int(input("Enter the number to start counting from:"))
head(1,n)