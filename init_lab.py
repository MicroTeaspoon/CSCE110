import os

def get_type(folder_types) :
    
    print('What type of folder would you like to create?')
    
    for n, type in enumerate(folder_types) :
        print(f'({n + 1}) {type}')
    
    while True :
        i = input('\n> ')
        if i.isdigit() :
            if 0 < int(i) <= len(folder_types) :
                return folder_types[int(i) - 1]


def main(folder_types) :
    
    # get all elements of current directory
    elements = os.listdir('.')

    type = get_type(folder_types)
    
    existing_folders = list()
    
    for element in elements:
        if element.startswith(type) \
        and '.' not in element       \
        and element[len(type):].isdigit()    :
            existing_folders.append(int(element[len(type):]))
            
    folder_to_create = type + str(max(existing_folders) + 1)

    path = os.path.join('.', folder_to_create)

    os.mkdir(path)
    
    for q in ['q1.py', 'q2.py', 'q3.py', 'q4.py', 'q5.py'] :
        with open(os.path.join(path, q), 'w') as f :
            f.write("""\
# author: noahr
#

def main() :
    pass

if __name__ == '__main__' :
    main()
""")

if __name__ == '__main__' :
    folder_types = ['lab', 'hw']
    main(folder_types)