with open("rosalind_ini2.txt", "r") as data:
    challenge2 = data.read().split()

def sqhyp(values):
    a = int(values[0])
    b = int(values[1])
    return a**2 + b**2

print(sqhyp(challenge2))
