import os

often_long = {}
longest_eng = {}

alpha = 'abcdefghijklmnopqrstuvwxyz'
alphaUp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

with open(os.path.join(input("Enter filename:\n")), encoding="utf8") as user_file:
    for line in user_file:
        for word in line.split():
            if len(word) > 3:
                if word in often_long:
                    often_long[word] += 1
                else:
                    often_long[word] = 1
            if word[0] in alpha or word[0] in alphaUp:
                if word not in longest_eng:
                    longest_eng[word] = len(word)

print((sorted(often_long, key=often_long.get, reverse=True)[0]))
print((sorted(longest_eng, key=longest_eng.get, reverse=True)[0]))
