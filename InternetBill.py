#calculate the price for internet browsing.

h = int(input("enter browsing hours 1 to 7 hours:"))
m = int(input("enter browsing minutes :"))
if h == 5 and m == 0:
    print("your bill is 200rs")
elif h == 5 and m > 0:
    bill = 200 + (m*1)
    print("your bill is :", bill ,"rs")    
elif h > 5:
    temp = h - 5
    bill = 200 + (temp*50) + (m*1)
    print("your bill is :", bill ,"rs")
elif h < 5:
    bill = (h*50) + (m*1)
    print("your bill is :", bill ,"rs")
else:
    print("invalid ")

