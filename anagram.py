import time
print("=== Anagram of a String ===")
string=input("Enter a string : ")
string1=input("Enter another string to check whether anagram or not : ")
condition=True
for character in string1:
    if character not in string:
        condition =False
for character in string:
    if character not in string1:
        condition =False
if len(string1)==len(string) and condition:
    print(f"{string} and {string1} are anagrams.")
else:
    print(f"{string} and {string1} are not anagrams.")
print()
time.sleep(5)
print("Script executed upto end.")