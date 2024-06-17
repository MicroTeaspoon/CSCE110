l = list()

for s in ["S1 : ", "S2 : ", "S3 : ", "S4 : "]:
    t = input(s).split()
    l.append(tuple((t[0], float(t[1]))))

print('The list is:')
print(l)