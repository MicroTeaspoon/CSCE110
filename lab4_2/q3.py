print(f'''Ascending Order : \
{(nums := sorted([int(input(nth)) for nth in ["1st : ", "2nd : ", "3rd : ", "4th : "]]))}
Descending Order : {nums[::-1]}''')