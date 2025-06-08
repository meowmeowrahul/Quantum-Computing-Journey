def computepay(hours,rate):
    return hours*rate
hours=int(input("Enter hours:"))
rate=int(input("Enter rate:"))
pay=computepay(hours,rate)
if hours>=40:
    print("Pay:",pay*1.5)
else:
    print("Pay:",pay)