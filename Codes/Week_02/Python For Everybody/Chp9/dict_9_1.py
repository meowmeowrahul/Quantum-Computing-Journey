#Program to calculate freuqncy of "Days" in a mbox.txt file
fname=input("Enter File name:") #mbox.txt
fhand=open(fname)
count=0
days=dict()
for line in fhand :
    line=line.strip()
    words=line.split()
    if len(words)==0 or words[0] != "From":continue
    if words[2] not in days:
     days[words[2]] =1
    else: days[words[2]] +=1
print(days)