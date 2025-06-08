import sys
sys.path.append('../Chp9')
import dict_9_2
gmail=dict_9_2.main()
lst=list()
for key in gmail:
    count,mail=gmail[key],key
    lst.append((count,mail))
lst.sort(reverse=True)
Most=lst[0]
print(Most[1],Most[0])
