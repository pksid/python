def c_words():
    count_upper = 0
    count_lower = 0
    with open("Report.txt", "r") as file:
        content = file.read()
        print(content)
        for char in content:
            if ord(char) > 65 and ord(char) < 91:
                print(char)
                count_upper += 1
            elif ord(char) > 97 and ord(char) < 123:
                print(char)
                count_lower += 1
                
        file.close()
    print(f"Number of uppercase characters{count_upper}")
    print(f"Number of lowercase characters{count_lower}")
    
c_words()


