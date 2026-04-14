"""
1
10
101
1010
10101  
101010

"""

N=int(input("N="))
for i in range(1,N+1):
    for j in range(1,i+1):
        if (i+j)%2==0:
         print("1",end="")
        elif (i+j)%2==1:
            print("0",end="")
    print()

