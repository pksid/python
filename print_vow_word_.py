#PYTHON FUNCTION TO READ CONTENT OF FILE "Report.txt" AND PRINTING WORDS WHICH STARTS AND ENDS WITH VOWELS

def print_vow_word():
    vowel='aeiouAEIOU'
    with open("Report.txt","r") as file:   
        content=file.read()
        words=content.split()
        for word in words:
            if word[0] in vowel and word[-1] in vowel:
                print(word, end=" ")
        file.close()
    
print_vow_word() #calling the function