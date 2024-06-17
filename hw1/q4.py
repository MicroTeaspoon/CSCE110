print(f'''
At {(r := float(input("Enter interest rate (in percentage) = ")))}\
% interest rate, you will need to pay $\
{round(15000*(1 + r/100)**(y := float(input("Enter loan period = "))), 2)}\
 in {y} years''')