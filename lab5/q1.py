print(f'''List = {(l := input("Enter a comma separated list:\n").split(','))}
List without duplicate = {sorted(list(set(l)))}''')