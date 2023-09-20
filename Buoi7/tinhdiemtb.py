diem = float(input("Nhập vào điểm của bạn:"))
if(diem>=0 and diem <=10):
    if(diem>=8.5):
        print(f"{diem} - Điểm A")
    elif(diem>=7.8):
        print(f"{diem} - Điểm B+")
    elif(diem>=7):
        print(f"{diem} - Điểm B")
    elif(diem>=5):
        print(f"{diem} - Điểm C")
    else:
        print(f"{diem} - Điểm D")
else:
    print("Điểm không hợp lệ")