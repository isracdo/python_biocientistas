with open("rosalind_ini5.txt", "r") as data:
    for index, line in enumerate(data):
        if index % 2 != 0:
            print(line.strip())
