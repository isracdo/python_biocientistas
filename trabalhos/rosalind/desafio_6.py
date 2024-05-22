with open("rosalind_ini6.txt", "r") as data:
    challenge6 = data.read().split()

dictionary = {}

for word in challenge6:
    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary[word] = 1

for key, value in dictionary.items():
    print (key, value)
