print("=== Prime Numbers Between 1 to 100 ===")
print("Prime numbers between 1-100 are ",end="")
for i in range(2,101):
    count=0
    for j in range(1,i//2):
        if i%j==0:
            count+=1
    if count>1:
        pass
    else:
        print(i,end=" ")
