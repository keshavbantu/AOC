
with open("day1.txt", "r") as file: 
    old_line=file.read().split("\n")

    line=[]
    for j in range(0,len(old_line)-2):
        total=int(old_line[j])+int(old_line[j+1])+int(old_line[j+2])
        line.append(total)
    
    counter=0
    for i in range(0,len(line)-1):
        if i==0:
            if line[1]>line[0]:
                counter+=1
            else:
                counter=0
        else:
            if line[i+1]>line[i]:
                counter+=1
    print(counter)
