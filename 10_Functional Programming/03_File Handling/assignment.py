file_path = "C:\\Users\\easleter000\\POC_Sem2_Assignments\\10_Functional Programming\\03_File Handling\\myFile.txt"

try:
    stream = open(file_path)
    print(stream.read())
except:
    pass


