items = dict()
total = 0

for i in range(1, 5) :
    inp = input('Enter item : ').split()
    inp[1], inp[2] = float(inp[1]), float(inp[2])
    total += inp[1]*inp[2]

    items[i] = tuple(inp)

print('Data as dictionary :', items)

print(f'''|___|______________|______________|____________|_________|
|No.|     Item     |  Unit Price  |  Quantity  |  Total  |''')

for i in range(1, 5) :
    print(f'|{i}  |{items[i][0]:<14}|{items[i][1]:^14.2f}|{items[i][2]:^12.2f}|{items[i][1]*items[i][2]:>9.2f}|')

print(f'''|___|______________|______________|____________|_________|
|   |              |              |   Total    |{total:>9.2f}|
|___|______________|______________|____________|_________|''')