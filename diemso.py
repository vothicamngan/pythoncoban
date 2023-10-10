def count_chars(txt):
    result = 0
    for char in txt:
        result += 1
    return result
string = input("Nhâp vào chuỗi ký tự: ")
print(f"Chuỗi ký tự dài: ", count_chars(string))