InputFile = open("inputFile.txt","r")
for line in InputFile:
    line_split = line.split()
    if line_split[2] == "P":
        print(line)
InputFile.close()
