fname = input("Enter file name: ")
fh = open(fname)

words = list()

for line in fh:
    for word in line.split():
        if word in words:
            continue
        else:
            words.append(word)
words.sort()
print(words)
