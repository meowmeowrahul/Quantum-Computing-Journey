import string
try:
    #fname=input("Enter File name:")
    #for this program
    fname="10_3.txt"   
    fhand=open(fname)
except:
    print("Error in opening File:(")
    exit()
lows=dict()
lowlist=[]
for line in fhand:
    line=line.lower()
    line=line.translate(line.maketrans("","",string.punctuation))
    line=line.translate(line.maketrans("","",string.digits))
    line=line.split()
    for words in line:
        for letter in words: 
            lows[letter]=lows.get(letter,0)+1
for key in lows:
    frq,let=lows[key],key
    lowlist.append((frq,let))
lowlist.sort(reverse=True)
for k,v in lowlist:
    print(v,":",k)