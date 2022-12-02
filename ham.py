def xuly(a,b):
    if a*a==b or b*b==a:
        tong=s+a+b
    return tong
n=int(input("ban muon nhap bao nhieu cap "))
i=1
s=0
for i in range(1,n+1):
    a = int(input("nhap so a "))
    b = int(input("nhap so b "))
    tong=xuly(a,b)
print("tong la " + str(tong))

