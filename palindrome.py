import time 
print("=== Checking pallindrome ===")
n=input("Enter a number : ")
check=n==n[::-1]
if check:
    print(n,"is a pallindrome string.")
else:
    print(n,"is not a pallindrome string.")
print()
time.sleep(5)
print("Script executed upto end.")
