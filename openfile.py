# OPENING A TEXT FILE IN READ MODE

with open("MYTEXT.txt", "r") as file:
    
    #content=file.read() #read the all content of file
    #print(content) #printing the content of file

    #content1=file.read(20)   #reading 8 characters/bytes from file
    #print(content1)

    #line1=file.readline() #Reading first line from file
    #print(line1)

    #line2=file.readline()   #Reading second line from file
    #print(line2)

    #line3=file.readline()   #Reading third line from file
    #print(line3)

    lines=file.readlines()  #Reading all line of  the file as list
    print(lines)

    file.close()    #closing the file