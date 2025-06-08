#Program to find domain names and frequwncy
import dict_9_2
gmail=dict_9_2.main()
domain=dict()
for key in gmail:
    stringmail=str(key)
    domainname=stringmail[stringmail.find("@")+1:]
    #print(domainname)
    if domainname not in domain:
        domain[domainname]=1
    else:
        domain[domainname]  +=1
print(domain)