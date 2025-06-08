fhand=open("mbox.txt")
senders=[]    
for line in fhand:
    if not line.startswith("From"): continue
    else:
        line=line.split()
        senders.append(line[1])

deli="\n "
new=deli.join(senders)   
print(new)  
        