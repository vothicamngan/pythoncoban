myfile = open("buoi21\workinghouse.txt" , encoding="utf8")
lines = myfile.readlines()
print(lines)
myfile.close
for line in lines:
    # print(line)
    data = line.split( )
    # print(data)
    hours = data[2:]
    # print(hours)
    tonggio = 0
    sum_hours = sum(list(map(lambda item: float(item), data[2:])))
    print(data[0], data[1],sum_hours)
    # for i in data[2:]:
    #     tonggio += float(i)
    # print(f"Tổng giờ làm viên của nhân viên {data[1]} là {tonggio}")