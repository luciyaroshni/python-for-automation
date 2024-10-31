inputfile = open("inputFile.txt","r")

passfile = open("PassFile.txt","w")

failfile = open("FailFile.txt","w")

for line in inputfile:
    line_split = line.split()
    if line_split[2] == "P":
        passfile.write(line)
    else:
        failfile.write(line)


inputfile.close()
passfile.close()
failfile.close()
