words = []

for i in range(5):
    word = str(input("Enter Word " + str(i+1)+": "))
    words.append(word)

print("Words ends with 'n' are: ")

nWord = [word for word in words if word.endswith('n')]
print(nWord)