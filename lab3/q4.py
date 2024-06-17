st = int(input('Enter start time (24-hr): '))
dur = int(input('Enter duration (minutes): '))


st = [st//100, st%100]
dur = [dur//60, dur%60]

t = (st[0]+dur[0]+(st[1]+dur[1])//60)*100%2400+(st[1]+dur[1])%60

print(f'''
Event end time: {t:04d}''')