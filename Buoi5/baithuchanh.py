# Bài 1
diem_toan = float(input("Nhập vào điểm toán"))
diem_ly = float(input("Nhập vào điểm lý"))
diem_hoa = float(input("Nhập vào điểm hóa"))
diem_trung_binh = (diem_toan + diem_ly + diem_hoa) / 3
print(diem_trung_binh)
print('Giỏi',diem_trung_binh >= 8)
print('Khá',6 <= diem_trung_binh < 8)
print('Trung bình', diem_trung_binh < 6)
# Bài 2
participation_percent = float(input('Nhập vào tỉ lệ tham gia lớp (0-1)'))
courser_complete_percent = float(input('Nhập vào tỉ lệ hoàn thành learn (0-1))'))
final_exam_mark = float(input('Nhập vào điểm thi cuối khóa VD: 0.75'))
print(participation_percent > 0.75 and courser_complete_percent > 0.8 and final_exam_mark >= 7.5)
# Bài 3
van_toc_mot_gio = float(input("nhập vào vận tốc 10 giờ"))
van_toc_mot_phut = van_toc_mot_gio/60
quang_duong_di_duoc_trong_1_gio_12_phut = van_toc_mot_phut*(60+12)
print('a, Vận tốc đi được trong một phút', str(van_toc_mot_phut))
print('b, Quảng đường đi được một giờ 12 phut', str(quang_duong_di_duoc_trong_1_gio_12_phut))
# Bài 4
length = 16
width = 10
current_area = length * width
new_area = (length + 4) * width
result = (new_area - current_area) / current_area * 100
print("% tăng chu vi:", str(result))
# Bài 5
v_xe_may = float(input("Nhập vào vận tốc xe máy"))
v_xe_dap = float(input("Nhập vào vận tốc xe đạp"))
khoang_cach = float(input("Nhập vào khoảng cách của 2 xe"))

hieu_van_toc = v_xe_may - v_xe_dap
thoi_gian = khoang_cach / hieu_van_toc

print("Thời gian 2 xem gặp nhau:", str(thoi_gian))
