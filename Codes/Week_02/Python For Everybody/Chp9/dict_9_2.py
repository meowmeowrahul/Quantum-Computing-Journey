#Program to calculate freuqncy of ""Gmail" in a mbox.txt file 
def main():
    fname=input("Enter File name:") #mbox.txt
    try:
        fhand=open(fname)
    except:
        print("Some error has occured pls try again:(")
        exit()
    count=0
    gmail=dict()
    for line in fhand :
        line=line.strip()
        words=line.split()
        if len(words)==0 or words[0] != "From":continue
        if words[1] not in gmail:
         gmail[words[1]] =1
        else: gmail[words[1]] +=1
    return gmail
if __name__=='__main__':
    gmail=main()
    print(gmail)
    
    