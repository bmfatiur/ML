file=open("/home/frozen/Desktop/schedule","r")
file_out=open("Python/files/learn schedule.txt","a")

for line in file:
    tokens=line.split(" ")
    print(tokens)
    file_out.write("number of words: "+str(len(tokens))+"\t"+line)
file.close()
file_out.close()