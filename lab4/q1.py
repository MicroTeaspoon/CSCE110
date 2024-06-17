# author: noahr
#

def main() :
    names = list()
    
    for i in range(5) :
        names.append(input('Welcome to our Coffee Shop. What is your name : '))
        
    for name in names :
        print(f'Here is your coffee {name}. Have a nice day.')

if __name__ == '__main__' :
    main()
