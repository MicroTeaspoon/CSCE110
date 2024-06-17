# author: noahr
#

def main() :
    nums = list()
    
    for nth in ['1st : ', '2nd : ', '3rd : ', '4th : '] :
        nums.append(int(input(nth)))
        
    print(f'Ascending Order : {sorted(nums)}')
    print(f'Descending Order : {sorted(nums)[::-1]}')

if __name__ == '__main__' :
    main()
