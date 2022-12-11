with open ('/Users/joseyalbrecht/Desktop/cs61a/inputday5.txt') as hash:
    hashhash = hash.read()

def tally():
    place = 0
    for x in hashhash:
        mysegment = hashhash[place:place+14]
        if not duplicates(mysegment):
            return place
        place = place + 1

def duplicates(string1): 
    if string1 is '':
        return False
    first1 = string1[0]
    rest = string1[1:]
    if first1 in rest:
        return True
    return duplicates(rest)

print(tally()+14)