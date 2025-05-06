import os

def write_file():
    
    filepath="12345.txt"

    if os.path.exists((filepath)):
        print(f"the file '{filepath}' exists")
        with open(filepath,"w") as file:
            content="hello\n"
            content2="hello"
            file.write(content)
            file.write(content2)
            file.close()
    else:
        print(f"the file '{filepath}'does not exists")
        print(f"Creating '{filepath}'")
        with open(filepath,"w") as file:
            content="hello\n"
            content2="hello"
            file.write(content)
            file.write(content2)
            file.close()
        
    with open(filepath,"r") as file1:
        con=file1.read()
        print(con)

write_file()
