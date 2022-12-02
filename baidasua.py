f=1
S=0
def xuly(a,b):
    if a*a==b or b*b==a:
       s=a+b
    else:
        s=0
    return s
while f==1:
    a=int(input("nhap so a "))
    b=int(input("nhap so b "))
    s=xuly(a,b)
    S=S+s
    f=int(input("neu muon nhap tiep thi nhan 1. neu muon ket thuc thi nhap 0 "))
print(S)