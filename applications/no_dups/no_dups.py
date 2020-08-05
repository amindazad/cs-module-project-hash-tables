# def no_dups(str):
#     return "".join(dict.fromkeys(str))

def no_dups(str):
    counts = {}
    words_list = str.split()
    new_str = ''

    for word in words_list:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

        if counts[word] == 1:
            new_str += f'{word} '

    return new_str.rstrip()

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))