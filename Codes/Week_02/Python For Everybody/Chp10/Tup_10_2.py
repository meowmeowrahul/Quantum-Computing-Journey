#To calculate hours appered in mbox.txt
'''
try:
    fhand=open("../Chp9/mbox.txt")
except:
    print("Error in opening File:(")
hours=dict()
for line in fhand:
    line=line.strip()
    words=line.split()
    if len(words)==0 or words[0]!="From":continue
    hour=words[5]
    hour=hour[:hour.find(":")]
    if hour not in hours:
        hours[int(hour)]=1
    else:
        hours[int(hour)] +=1
lst=list(hours.items())
print(lst)'''
try:
    fhand = open("../Chp9/mbox.txt")
except:
    print("Error in opening File :(")
    exit()

hours = dict()
for line in fhand:
    line = line.strip()
    words = line.split()
    if len(words) == 0 or words[0] != "From":
        continue
    time = words[5]
    hour = time.split(":")[0]
    hours[hour] = hours.get(hour, 0) + 1

# Convert to list of tuples and sort by hour
lst = sorted(hours.items())
for k, v in lst:
    print(k, v)
