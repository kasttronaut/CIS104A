fh = open("mbox-short.txt")

for line in fh:
    words = line.split()
    if len(words) == 0 or words[0] != "From" :
        continue
    print(words[2])