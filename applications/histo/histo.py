# Your code here

with open("robin.txt") as f:
    words = f.read()

# Characters to ignore
to_ignore = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &' 

histogram = {}

#Splot the words into a list
words_list = words.split()
longest = 0

for word in words_list:
    # Convert the word to lowercase and strip characters
    word = word.lower().strip(to_ignore)

    # Keep track of the longest word 
    if len(word)>longest:
        longest = len(word)

    if word not in histogram:
        #skip if the string is empty 
        if word == "":
            continue
        #Init to empty strig
        histogram[word] = ""
    
    # Increment Hash
    histogram[word] += "#"

histogram_items = list(histogram.items())
histogram_items.sort(key = lambda pair: (-len(pair[1]), pair[0]))

for item in histogram_items:
    print(f"{item[0] :<{longest + 2}}{item[1]}")
