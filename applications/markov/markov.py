import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Split the words into a list 
words_list = words.split()

#Iterate through the words and build a dataset of words following eachother
dataset = {}

for i in range(len(words_list)):
    if words_list[i] not in dataset:
        dataset[words_list[i]] = []

    try:
        dataset[words_list[i]].append(words_list[i+1])
    except IndexError:
        break 

# TODO: construct 5 random sentences

suffix = ('.', '?', '!', '."', '?"', '!"')

def print_random(word):
    print(word, end= " ")

    if word.endswith(suffix):
        print('/n')
        return
    else:
        print_random(random.choice(dataset[word]))

print_random('Alice')
print_random('King')
print_random('Kitty')
print_random('One')
print_random('Queen')

