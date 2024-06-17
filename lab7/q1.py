e = input('Enter Expression : ').split()

if e[0] == 'abs' :
    print('abs', e[1], '=', abs(int(e[1])))

if e[0] == ('-') :
    print(e[1], e[0], e[2], '=', int(e[1]) - int(e[2]))

if e[0] == ('+') :
    print(e[1], e[0], e[2], '=', int(e[1]) + int(e[2]))

if e[0] == ('*') :
    print(e[1], e[0], e[2], '=', int(e[1]) * int(e[2]))

if e[0] == ('/') :
    try:
        print(e[1], e[0], e[2], '=', int(int(e[1]) / int(e[2])))
    except :
        print('Division by 0')