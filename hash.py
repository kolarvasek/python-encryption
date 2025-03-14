def personal_hash(s):
    output = ''
    for chars in s:
        if chars == 'a':
            output += 'y'
        elif chars == 'e':
            output += 'x'
        elif chars == 'i':
            output += 'w'
        elif chars == 'o':
            output += 'v'
        elif chars == 'u':
            output += 'u'
        elif chars == 'b':
            output += '9'
        elif chars == 'c':
            output += '5'
        elif chars == 'd':
            output += 'q'
        elif chars == 'f':
            output += '4'
        elif chars == 'g':
            output += 'z'
        elif chars == 'h':
            output += 'z'
        elif chars == 'j':
            output += 'z'
        elif chars == 'k':
            output += 'z'
        elif chars == 'l':
            output += 'z'
        elif chars == 'm':
            output += 'z'
        elif chars == 'n':
            output += 'z'
        elif chars == 'p':
            output += '1'
        elif chars == 'q':
            output += '1'
        elif chars == 'r':
            output += '1'
        elif chars == 's':
            output += '1'
        elif chars == 't':
            output += '1'
        elif chars == 'v':
            output += '1'
        elif chars == 'w':
            output += '1'
        elif chars == 'x':
            output += '1'
        elif chars == 'y':
            output += '1'
        elif chars == 'z':
            output += '1'
        elif chars == '1':
            output += 'o'
        elif chars == '2':
            output += 'o'
        elif chars == '3':
            output += 'o'
        elif chars == '4':
            output += 'o'
        elif chars == '5':
            output += 'o'
        elif chars == '6':
            output += 'o'
        elif chars == '7':
            output += 'o'
        elif chars == '8':
            output += 'o'
        elif chars == '9':
            output += 'o'
        elif chars == '0':
            output += '0'
        else:
            output += '0'
    
    print(output)
    return output

personal_hash('vasek@kolar.com')