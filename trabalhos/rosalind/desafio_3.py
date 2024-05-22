with open("rosalind_ini3.txt", "r") as data:
    challenge3 = data.read().split()

def ss(txtfile):
    line1 = txtfile[0]
    a = int(txtfile[1])
    b = int(txtfile[2]) + 1
    c = int(txtfile[3])
    d = int(txtfile[4]) + 1
    strslice1 = line1[a:b]
    strslice2 = line1[c:d]
    return strslice1 + ' ' + strslice2

print(ss(challenge3))
