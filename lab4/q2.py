# author: noahr
#

def main() :
    names = list()
    
    for i in range(4) :
        names.append(input('Thanks for submitting. What is your name: '))
        
    for name in names[::-1] :
        print(f'{name}, your score is: {ord(name[0])}')

if __name__ == '__main__' :
    main()
