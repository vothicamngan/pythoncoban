chieu_cao = float(input("Nhâp vào chiều cao:"))
can_nang = float(input("Nhập vào cân nặng:"))
if(chieu_cao <=0 and can_nang<=0):
    print("Số nhập vào không hợp lệ")
else:
    bmi = can_nang /(chieu_cao ** 2)
    print(f"BMI là: {bmi}")
    if bmi<16:
        print("Gầy cấp độ III")
    elif bmi<17:
        print("Gầy cấp độ II")
    elif bmi<18.5:
        print("Gầy cấp độ I")
    elif bmi<25:
        print("Bình thường")
    elif bmi<30:
        print("Thừa cân")
    elif bmi<35:
        print("Béo phì cấp độ I")
    elif bmi<40:
        print("Béo phì cấp độ II")
    elif bmi>40:
        print("Béo phì cấp độ III")
    else:
        print("Ngoài đo lường")