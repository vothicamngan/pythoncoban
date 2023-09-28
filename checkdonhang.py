so_tien = float(input("Nhập vào số $: "))
print(f"Số tiền đơn hàng: {so_tien}")
if so_tien >=0:
    if so_tien >= 150:
        so_tien = so_tien - 50
    elif so_tien >= 100:
        so_tien = so_tien -25
    elif so_tien >= 75:
        so_tien = so_tien - 10
    print(f"Số tiên sau khi khuyến mãi {so_tien}")
else:
    print("Không có đơn hàng5")


