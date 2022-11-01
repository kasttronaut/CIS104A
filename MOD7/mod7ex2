fname = input("Enter file name: ")
fh = open(fname)
count = 0
tot=0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    ipos = line.find(':')
    flt = float(line[ipos+1: ])
    tot= tot+flt
    count = count +1
    
print('Average spam confidence:', tot/count)
