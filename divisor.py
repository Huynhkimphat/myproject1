x=int(input())
y=int((x/2)+1)
for i in range(1,y):
    if x%i==0:
        print(i,end=" ")