#Program to calculate freuqncy of ""Gmail" in a mbox.txt file and to person with most&least msg sent/recieved
fname=input("Enter File name:") #mbox.txt
try:
    fhand=open(fname)
except:
    print("Some error as occured:(")
count=0
gmail=dict()
for line in fhand :
    line=line.strip()
    words=line.split()
    if len(words)==0 or words[0] != "From":continue
    if words[1] not in gmail:
     gmail[words[1]] =1
    else: gmail[words[1]] +=1
most=None
most_gmail=None
least_gmail=None
least=None
for key in gmail:
    if most is None or gmail[key]>most:
        most=gmail[key]
        most_gmail=key
    if least is None or gmail[key]<least:
        least=gmail[key]
        least_gmail=key
print("Most:",most_gmail,most)  
print("least:",least_gmail,least)