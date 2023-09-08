#element 1 is the line number
#element 2 is the word number
# element 3 is the character number

#answer: the next turing could be
# gets the cypher1.txt
with open("sept4week/cypher2.txt") as a:
    cypherl = a.read().splitlines()

# gets the talk.txt
with open("sept4week/talk.txt") as b:
    textlines = b.read().splitlines()

# a list to dump the words into
worddump = []

for line_info in cypherl:
    line_parts = line_info.split()

    # checks if the line has two parts and then set it equal to line for the first value and word for the second value
    if len(line_parts) == 3:
        line_number = int(line_parts[0])
        word_number = int(line_parts[1])
        character_number = int(line_parts[2])


        if 0 <= line_number < len(textlines):
            #pulls line as a string
            line = textlines[line_number].strip()

            # Split the line into words and check the word_number 
            words = line.strip().split()
            if 0 <= word_number < len(words):
                word = words[word_number][character_number :]
                worddump.append(word)

print(" ".join(worddump))