words = []

for i in range(5):
    word = str(input("Enter Word " + str(i+1)+": "))
    words.append(word)

print("Words starts with 'b' are: ")
for word in words:
    if word.startswith('b'):
        print(word)
    