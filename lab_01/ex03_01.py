def tinh_tong_so_chan(lst):
    tong = 0
    for i in lst:
        if i % 2 == 0:
            tong += i
    return tong

input_list = input("Nhập một dãy số, cách nhau bởi dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))

tong_chan = tinh_tong_so_chan(numbers)
print(f"Tổng các số chẵn trong dãy: {tong_chan}")