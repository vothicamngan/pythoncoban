my_list = []
def add_list(name, cost, date):
    new_list = [name, cost, date]
    my_list.append(new_list)
def xoa_du_lieu(name):
    for item in my_list:
        if(item[0] ==name):
            my_list.remove(item)
            print(f"Đã xóa {item}")

while True:
    new_list = []
    choice = int(input("Nhập 1 để thêm, nhập 2 để số, nhập 3 để thoát khỏi chương trình: "))
    if choice == 1:
        name = input("Nhập vào nội dung chi tiêu: ")
        cost = int(input("Nhập vào số tiên thu: "))
        date = input("Nhập vào ngày chi tiêu: ")
        new_list = [name, cost, date]
        my_list.append(new_list)
        print(my_list)
    if choice ==2:
        name = input("Nhập vào nội dung chi tiêu: ")
        xoa_du_lieu(name)
        print(my_list)
    
    if choice ==3:
        print(my_list)
        break
