# Viết chương trình cho phép người dùng tìm dữ liệu của
# nhân viên bằng cách nhập id của nhân viên đó (Database
# sẽ được cho sẵn).
employee_db = [
    {"id": "NV001", "name": "Tèo Trần", "gender": True, "salary": 1000},
    {"id": "NV002", "name": "Ly Trần", "gender": False, "salary": 1299},
    {"id": "NV003", "name": "David Lý", "gender": True, "salary": 2199},
    {"id": "NV004", "name": "Leonardo", "gender": True, "salary": 2999},
]

print(employee_db)

# Nhập id cần tìm
# Xuất kết quả tìm kiếm
ma_nhan_vien = input("Nhập vào mã nhân viên cần tìm").lower().strip()
check = False;
for item in employee_db:
    if item['id'].lower() == ma_nhan_vien:
        print(item)
        check = True
        break
if(check == False):
    print("Không tìm thấy nhân viên")

# Đếm số lượng nhân viên là Nam
so_luong_nv_nam = 0
for item in employee_db:
    if item['gender'] == True:
        so_luong_nv_nam +=1
    
print(f"Số lượng nhân viên nam là {so_luong_nv_nam} ")
print(f"Số lượng nhân viên nữ là {len(list(employee_db))-so_luong_nv_nam}")


# Đếm số lượng nhân viên có lương >= 1500
so_luong_nv = 0
for item in employee_db:
    if item['salary']>=1500:
        so_luong_nv +=1
    
print(f"Số lượng nhân viên lương >=1500 là {so_luong_nv} ")
print(f"Số lượng nhân viên lương <1500 là {len(list(employee_db))-so_luong_nv}")
