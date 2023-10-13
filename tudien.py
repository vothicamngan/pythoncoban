tu_dien = [
    {"tieng_viet":"Xin chào", "tieng_anh":"Hello"},
    {"tieng_viet":"Chào", "tieng_anh":"Hi"},
    {"tieng_viet":"Tên", "tieng_anh":"Name"},
    {"tieng_viet":"Ngành", "tieng_anh":"Major"},
]
def dich(word):
    check = False
    for item in tu_dien:
        if word == item['tieng_anh'].lower():
            print(f"{item['tieng_anh']} có nghĩa là {item['tieng_viet']}")
            check = True
            break
    if(check == False):
        print("Không tìm thấy từ điển")


while True:
    nhap_tu = input("Nhập vào từ cần dịch: ").lower().strip()
    if nhap_tu ==1:
        break
    else:
        dich(nhap_tu)
    