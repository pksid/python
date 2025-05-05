#PYTHON FUNCTION TO READ CONTENT OF FILE "Elections.txt AND PRINTING THE LINES WHICH CONTAINS "Python" word

def print_lines():
    word='vote'
    with open("Elections.txt","r") as file:
        content=file.readlines()
        for line in content:
            words=line.split()
            if word in words:
                print(line)
        file.close()

print_lines() #calling functions