def computegrade(score):
    if not(score<0 or score>1): 
        if score >= 0.9:
            return "A"
        elif score >=0.8:
            return "B"
        elif score >=0.7:
            return "C"    
        elif score >=0.6:
            return "D"    
        elif score >0.6:
            return "F"                   
    else:
        return "Bad Score"  
def chop(t):
    del t[0]
    del t[len(t)-1]
def middle(t):
    t1=t[1:]
    print(t1)
    del t1[len(t1)-1]
    return t1
numlist=list()
numlist=input("enter elem seperated by spaces").split()
#chop(numlist)
#print("Chop",numlist)
newlist=middle(numlist)
print(numlist)
print(newlist)

