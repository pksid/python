#OPENING A TEXT FILE AND DISPLAYING THE TOTAL NUMBER OF VOWELS IN FILE

def count_vow_file():
    vowel="aeiouAEIOU"
    count_vow=0
    with open("MYTEXT.txt","r") as file:
        content=file.read()
        for char in content:
            if char in vowel:
                count_vow+=1
        print(f"Number of vowels in file are:{count_vow}")
    file.close()

count_vow_file()