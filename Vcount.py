word = input("Enter the word")
count=0
for char in word:
    if char in "AEIOaeiou":
        count+=1
print(f"Number of Vowels in the word is:{count}")