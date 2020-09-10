import sys

sides = [sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]]
allLetters = sides[0] + sides[1] + sides[2] + sides[3]
MAX_WORD_LEN = 12

#make all possible words
words = []

def isValidWord(word, sides):
    prevS = -1
    for char in word:
        if char not in allLetters:
            return False
        else:
            for i in range(0, 4):
                if char in sides[i]:
                    if prevS == i:
                        return False
                    else:
                        prevS = i
            

    return True


with open("words.txt") as f:
    for line in f: 
        line = line.rstrip()
        line = line.lower()
        if len(line) >= 3 and len(line) <= MAX_WORD_LEN:
            if isValidWord(line, sides):
                if line not in words:
                    words.append(line)

words.sort()
#print(words)
pairs = {}

for i in range(0, len(words)):
    for j in range(0, len(words)):
        if i != j:
            if words[i][len(words[i]) - 1] == words[j][0]:
                if set(words[i] + words[j]) >= set(allLetters):
                    if words[i] not in pairs.keys():
                        pairs[words[i]] = [words[j]]
                    else:
                        pairs[words[i]].append(words[j])

for key, val in pairs.items():
    print(key, ":")
    for v in val:
        print("\t", v)