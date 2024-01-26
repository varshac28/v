def nQueens(k,n):
    for i in range(1,n+1):
        if(place(k,i)):
            x[k]=i
            if(k==n):
                print("The Positions are : ")
                for j in range(1,n+1):
                    for l in range(1,n+1):
                        if x[j]==l:
                            print("Q",end=" ")
                        else:
                            print("-",end=" ")
                    print()
            else:
                nQueens(k+1,n)
def place(k,i):
    for j in range(1,k):
        if x[j]==i or abs(x[j]-i)==abs(j-k):
            return False
    return True
n=int(input("Enter the no of Queens: "))
x=list()
if n==2 or n==3:
    print("Not Possible")
else:
    x=[0]*(n+1)
    nQueens(1,n)
