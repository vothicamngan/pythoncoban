import random
x = random.randint(1,1000)
y = random.randint(1,1000)

if(x%2 ==0 and y%2==0):
    print("BINGO")
elif (x%2 ==1 and y%2==1):
    print("LOSE")
else:
    print("Chúc bạn may mắn lần sau!")