
fhand=input("Enter File name:")
if fhand=="damn u rahul":
    print("Damn u too mr")
    print("Boom program is closed ha ha")
    exit()
try:
    fhand=open(fhand)
        
    count=0
    total=0
    for line in fhand:

        found= line.find("X-DSPAM-Confidence:")
        if found==-1:
            continue
        foundslice=line[found+19:]
        foundnum=float(foundslice.strip())
        count=count+1
        total=total+foundnum
    if count==0:
        print('No match found')        
    else:
        print("Total lines:",count,"Avg:",total/count)
except FileNotFoundError:
    print("No file as:",fhand)
except Exception as e:
    print("Some error has occured:",e)