import random as r
n = r.randint(0,9)
m = int(input("Nhâp Vào số M: "))
print(f"{n} - {m}")
if  m ==n:
    print("Đúng")
else:
    print("Sai")
