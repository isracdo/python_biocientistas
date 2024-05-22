with open("rosalind_ini4.txt", "r") as data:
    challenge4 = data.read().split()

def sumodd(txtfile):
    a = int(txtfile[0])
    b = int(txtfile[1]) + 1
    list = [x if x % 2 != 0 else 0 for x in range(a, b)]
    return sum(list)

print(sumodd(challenge4))
