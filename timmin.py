def tim_so_nho_nhat(arr):
    num_min = arr[0]
    for item in arr:
        if item < num_min:
            num_min = item
    print(f"Số nhỏ nhất là: {num_min}")
arr = [5,4,2,10,6]
tim_so_nho_nhat(arr)