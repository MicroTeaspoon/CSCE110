for name in [input('Thanks for submitting. What is your name: ') for i in range(4)][::-1] :
    print(f'{name}, your score is: {ord(name[0])}')