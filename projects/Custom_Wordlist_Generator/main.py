def get_information():
    information = []
    information.append(input("Enter victim's First name: "))
    information.append(input("Enter victim's Second name: "))
    information.append(input("Enter victim's Nickname: "))
    information.append(input("Enter Birth Year: "))
    information.append(input("Enter Birth Month: "))

    more = input("Would you like to add more information? [y/N]: ")
    if more.lower() == 'y':
        more_info = input("Enter related keywords separated by commas: ").replace(" ", "")
        info_list = more_info.split(",")
        for element in info_list:
            information.append(element)     
    leet_mode = input("Would you like to enable leet mode? (leet = 1337) [Y/N]: ")
    if leet_mode.lower() == 'y':
        leet_mode = "1"
    elif leet_mode.lower() == 'n':
        leet_mode = "0"
    else:
        print("[-] Incorrect value. Enabling by default...")
        leet_mode = "1"

    file_name = input("Enter the name of the output file: ")
    return information, leet_mode, file_name


def leet_mod(list1):
    list2 = []
    for element in list1:
        list2.append(element.replace('a', '4'))
        list2.append(element.replace('i', '1'))
        list2.append(element.replace('o', '0'))
        list2.append(element.replace('e', '3'))
        list2.append(element.replace('t', '7'))
        list2.append(element.replace('A', '4'))
        list2.append(element.replace('i', '1'))
        list2.append(element.replace('E', '3'))
        list2.append(element.replace('T', '7'))
        list2.append(element.replace('O', '0'))
    list3  = list1 + list2
    return list3    


def make_wordlist(information, file_name,):
    with open(file_name, 'w') as wordlist:
        for element in information:
            wordlist.write(element + '\n')
            wordlist.write(element.lower() + '\n')
            wordlist.write(element.upper() + '\n')
            for element2 in information:
                wordlist.write(element.lower() + element2 + '\n')
                wordlist.write(element.upper() + element2 + '\n')
                wordlist.write(element.upper() + element2.lower() + '\n')
                wordlist.write(element.lower() + element2.lower() + '\n')
                wordlist.write(element.lower() + element2.upper() + '\n')
                wordlist.write(element.upper() + element2.upper() + '\n')


(information, leet_mode, file_name) = get_information()
if leet_mode == "1":
    information = leet_mod(information)
make_wordlist(information, file_name)

print("Wordlist Generated Successfully!")