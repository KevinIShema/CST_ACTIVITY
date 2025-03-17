# word =input("Enter a word: ")
# print(len(word))


# words = input("Enter your words: ").replace(" ", "")
# print(len(words))
# print(words)


array = []
x = 0
words = input("Enter five words words: ").split()
if len(words) != 5:
    print("You must enter five words")
else:    
    for word in words:
        array.append(f"{word} => {len(word)}")
print(array)
arr1 = ['a', 'i', 'o', 'e', 'u']
arr2 = ['k', 'j', 'p', 't', 'f']

# Function to replace characters based on arr1 and arr2
def kajipo(text):
    result = []
    for char in text:
        if char in arr1:
            index = arr1.index(char)
            result.append(arr2[index])
        elif char in arr2:
            index = arr2.index(char)
            result.append(arr1[index])
        else:
            result.append(char)
    return ''.join(result)

# Get user input
user_input = input("Enter text: ")

# Replace characters in the user input
result = kajipo(user_input)

print("Updated text:", result)