def sap_xep_so_nguyen (n1, n2, n3):
    temp= 0
    if(n1<n2 and n1<n3):
        if(n2<n3):
            temp = n1
            n1 = n2
            n2 = n3
        else:
            temp = n1
            n1 = n3
    if(n2<n1 and n2<n3):
        if(n1<n3):
            temp =n2
            n2 = n3
        else:
            temp = n2
            n2= n1
    if(n3<n1 and n3<n2):
        if n1<n2:
            temp = n3
        else:
            temp = n3
            n1 = n2
            n2 = n1
    print(temp , n1, n2)

try:
    n1 = int(input("Nhập vào số nguyên thứ nhất:"))
    n2 = int(input("Nhập vào số nguyên thứ hai:"))
    n3 = int(input("Nhập vào số nguyên thứ ba:"))
    sap_xep_so_nguyen(n1,n2,n3)
except:
    print("Nhập vào số nguyên")