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

for i in rhymes:
    for j in start1:
        print(j.capitalize(), end="! ")
    print(i[0].capitalize(), end="! \n")
    rhyme2 = list(i)  #second
    print(start2, rhyme2[1], '.\n \n')