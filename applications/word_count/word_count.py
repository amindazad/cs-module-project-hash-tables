def word_count(str):
    counts = dict()
    to_ignore = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'
    lowercase = str.lower()
    words = lowercase.split()

    for word in words:
        word = word.strip(to_ignore)
        # If there are no valid chars, skip to the next word
        if word == '': continue
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))