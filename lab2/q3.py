print(f'''
{(s := int(input('Enter number of seconds: ')))} seconds = \
{s//3600} hours, \
{(s%3600)//60} minutes and \
{s%60} seconds''')