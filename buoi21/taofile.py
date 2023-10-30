ten_file = input("nhập vào tên file:").strip()
if ten_file !="":
    noi_dung = input("Nhập nội dung:")
    with open(ten_file , "w", encoding="utf8") as myfile:
        myfile.write(noi_dung)