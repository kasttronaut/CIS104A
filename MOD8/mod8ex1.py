def chop(i):
    del i[0]
    del i[-1]

def middle(i):
    new = i[1:]
    del new[-1]
    return new

rhyme = ["knick","knack", "patty", "whack"]
rhyme2 = ["give", "a", "dog", "a", "bone"]

print(rhyme)
print(chop(rhyme))

print(rhyme2)
print(middle(rhyme2))