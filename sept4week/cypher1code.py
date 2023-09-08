#talk code
#with open("talk.txt") as f:
    #f is the variable name for talk.txt within the program
    #f is an object
   # pen=f.read() 
    #pen is the variable name for the contents of talk.txt
    #.read is a method
   # print(pen)
   # pen = pen.splitlines()
    # this line is now spliting up the words into different lines ( into different arrays )
   # print(pen[1])
   # for i in pen:
       # print(i)
    # this is a for loop that is printing out each line of the text file
 
 #cipher code
#with open("cypher1.txt") as c:
    #num1=c.read()
    #num1=num1.split()
    #print(num1)

#enumerate
#for i, row in enumerate(paper)

#- read the cypher information from cypher1.txt
#- read the encoded text from talk.txt
#- decipher the specified words based on line and word numbers from cypher1.txt
#- print the decoded text
#- use the following function to decipher a specific word based on line and word numbers
#- use the first number as the line number
#- use the second number as the word value


# gets the cypher1.txt
with open("sept4week/cypher1.txt") as a:
    cypherl = a.read().splitlines()

# gets the talk.txt
with open("sept4week/talk.txt") as b:
    textlines = b.read().splitlines()

# a list to dump the words into
worddump = []

for line_info in cypherl:
    line_parts = line_info.split()

    # checks if the line has two parts and then set it equal to line for the first value and word for the second value
    if len(line_parts) == 2:
        line_number = int(line_parts[0])
        word_number = int(line_parts[1])

        if 0 <= line_number < len(textlines):
            #pulls line as a string
            line = textlines[line_number]

            # Split the line into words and check the word_number 
            words = line.split()
            if 0 <= word_number < len(words):
                word = words[word_number]
                worddump.append(word)

print(" ".join(worddump))

    #answer somewhere in this room