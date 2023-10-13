class ProductManager:
    def __init__(self):
        self.products = []

    def display_products(self):
        print("Danh sách sản phẩm:")
        for product in self.products:
            print(product)

    def add_product(self, product_name):
        self.products.append(product_name)
        print(f"Sản phẩm '{product_name}' đã được thêm vào danh sách.")

    def edit_product(self, old_name, new_name):
        if old_name in self.products:
            index = self.products.index(old_name)
            self.products[index] = new_name
            print(f"Sản phẩm '{old_name}' đã được sửa thành '{new_name}'.")
        else:
            print(f"Sản phẩm '{old_name}' không tồn tại trong danh sách.")

    def delete_product(self, product_name):
        if product_name in self.products:
            self.products.remove(product_name)
            print(f"Sản phẩm '{product_name}' đã được xoá khỏi danh sách.")
        else:
            print(f"Sản phẩm '{product_name}' không tồn tại trong danh sách.")


# Tạo đối tượng quản lý sản phẩm
product_manager = ProductManager()

# Menu chức năng
while True:
    print("\nChọn chức năng:")
    print("1. Hiển thị danh sách sản phẩm")
    print("2. Thêm sản phẩm mới")
    print("3. Sửa tên sản phẩm")
    print("4. Xoá sản phẩm")
    print("0. Thoát")

    choice = input("Nhập lựa chọn: ")

    if choice == "1":
        product_manager.display_products()
    elif choice == "2":
        product_name = input("Nhập tên sản phẩm mới: ")
        product_manager.add_product(product_name)
    elif choice == "3":
        old_name = input("Nhập tên sản phẩm cần sửa: ")
        new_name = input("Nhập tên mới: ")
        product_manager.edit_product(old_name, new_name)
    elif choice == "4":
        product_name = input("Nhập tên sản phẩm cần xoá: ")
        product_manager.delete_product(product_name)
    elif choice == "0":
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")