fname = input("Enter file name:")
try :
    if fname == 'absolute':
        print("Only a sith deals in those, you clown.")
        quit()
    else :
        fhand = open(fname)
except :
    if fname == 'absolute':
        quit()
    else :
        print("File cannot be opened:", fname)
        exit()

count = 0

for line in fname:
    if line.startswith('Subject:') :
        count = count + 1 

print("There were", count, "subject lines in", fname)
    