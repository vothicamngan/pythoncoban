start = int(input("Nhập vào số nguyên thứ nhất :"))
end = int(input("Nhập vào số nguyên thứ hai :"))
i=1
while i in range(start,end +1):
    if(i%3 ==0 and i%5==0):
        print('FizzBuzz')
    elif(i%3 == 0):
        print('Fizz')
    elif (i%5 == 0):
        print('Buzz')
    else: 
        print(i)
    i +=1