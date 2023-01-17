# 7-11
start1 = ["free", "file", "foe"]
rhymes = [
    ("flop", 'get a mop'),
    ("fope", "turn the rope"),
    ("fa", "get your ma"),
    ("fudge", "call the judge"),
    ("fat", "pet the cat"),
    ("fog", "walk the dog"),
    ("fun", "say we're done")
    ]
start2 = "Someone better"

rhyme1 = rhymes[0][0].capitalize()  # first
for i in start1:
    print(i.capitalize(), end="! ")
print(rhyme1, end="! \n")

rhyme2 = list(rhymes[0])  #second
del(rhyme2[0])
print(start2, ' '.join(rhyme2), '.')




