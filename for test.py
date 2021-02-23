num = int(input("Enter a number: "))
word = input("Enter a word: ")

print("\nHere's each number up to your choice:")
for i in range(1, (num+1)):
    print(i, end=" ")

print("\nHere's each letter in your word:")
for letter in word:
    print(letter)
