def find_acronym():
    look_up = input("What software acronym wold you like to up?\n")

    found = False
    try:
        with open('acronyms.txt') as file:
                for line in file:
                    if look_up in line:
                        print(line)
                        found = True
                        break
    except FileNotFoundError as e:
        print('File not found')
        return
    
    if not found:
        print('The acronyms doas no exist')

def add_acronym():
    acronym = input('what acronym they wnnt to add?\n')
    definition = input('What is the definition?\n')
    with open('acronyms.txt','a') as file:
        file.write(acronym + ' - ' + definition + '\n')
def main():
    # ask the user whether they want to find or add an acronym
    choice = input('Do you want to find(F os add(A) an acronym?)')
    if choice == 'F':
        find_acronym()
    elif choice == 'A':
        add_acronym()
main()