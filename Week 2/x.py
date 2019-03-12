import io

def main()
    string = input('Input string: ')
    str_length = len(string)

    counter = 0 
    while counter < str_length:
        strings = []
        curr_string = ''
        if string[counter] != ' ':
            curr_string += string[counter]
        else:
            strings.append(curr_string)
            curr_string = ''
        counter += 1
    strings.append(curr_string)

    index = len(strings)
    while index >0:
        print(strings[index])
        index -= 1

if __name__ == '__main__':
    main()