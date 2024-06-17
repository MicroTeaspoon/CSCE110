n = int(input("Enter decimal number : "))

if n < 343 :
    d1 = n//49

    d2 = n%49//7

    d3 = n%7


    print(f'{n} in base 7 is : {d1}{d2}{d3}')
else :
    print("Number out of range")