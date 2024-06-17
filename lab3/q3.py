print(f'''
Date in ISO 8601 format: \
{(d := input("Enter date in US format: "))[-4:]+"-"+d[:5]}''')