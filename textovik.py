from collections import defaultdict
text = input()
if (text == ""):
    print("Bruh!")
    exit()
ttl = text.split()
print ("Самое длинное слово: " + str(max(ttl, key=len)))
smth = defaultdict(int)
for sub in ttl:
    for wrd in sub.split():
        smth[wrd] += 1
res = max(smth, key=smth.get)
print("Самое частое: " + str(res))