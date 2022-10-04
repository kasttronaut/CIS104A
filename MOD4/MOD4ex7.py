score = input("Enter Score: ")
try:
    s = float(score)
except: 
    print("Bad score")



def computegrade(s):
    if s >= 0.9:
        print("A.")
    elif s >= 0.8:
        print("B")
    elif s >= 0.7:
        print("C")
    elif s >= .6:
        print("D")
    else:
         print("F")
    
computegrade(s)