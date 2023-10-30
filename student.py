class Student:
    students = []
    
    def __init__(self, ma_sv, hoten_sv,ngaysinh_sv, quequan_sv,chuyen_nganh,lop ):
        self.ma_sv = ma_sv
        self.hoten_sv = hoten_sv
        self.ngaysinh_sv = ngaysinh_sv
        self.quequan_sv = quequan_sv
        self.chuyen_nganh = chuyen_nganh
        self.lop = lop
        Student.students.append(self)
    @classmethod
    def add_sv (cls,ma_sv, hoten_sv,ngaysinh_sv, quequan_sv,chuyen_nganh,lop):
        new_student = cls(ma_sv, hoten_sv,ngaysinh_sv, quequan_sv,chuyen_nganh,lop)
        print(f"Student {hoten_sv} added successfully.")
    @classmethod
    def edit_sv(cls, ma_sv, new_hoten_sv,new_ngaysinh_sv, new_quequan_sv,new_chuyen_nganh,new_lop):
        flash = False
        for item in cls.students:
            if ma_sv == item.ma_sv:
                cls.hoten_sv = new_hoten_sv
                cls.ngaysinh_sv = new_ngaysinh_sv
                cls.quequan_sv = new_quequan_sv
                cls.chuyen_nganh = new_chuyen_nganh
                cls.lop = new_lop
                flash = True
                break
        if flash == False:
            print(f"Not found {ma_sv}")
    @classmethod
    def delete_sv(self,ma_sv ):
        print
        for item in self.students:
            print(item)
            if ma_sv == item.ma_sv:
                self.students.remove(item)
                print(f"Deleted {ma_sv}")
                break
            else:
                print(f"Not found {ma_sv}")
    @classmethod
    def find_sv(self, ma_sv):
        flash = False
        for item in self.students:
            if ma_sv == item.ma_sv:
                print(f"Infor student {item.ma_sv}")
                flash = True
                break
        if flash ==False:
            print(f"{ma_sv} is not found")
        
    
Student.add_sv('ST01', 'c', '20/11/2000' , 'CT' , 'IT' , '1')
Student.add_sv('ST02', 'd', '20/11/2000','CT','IT','2')
Student.add_sv('ST03', 'a', '20/11/2000','CT','IT','2')
Student.edit_sv('ST02', 'b', '20/11/2000','CT','IT','3')
print("Current Students:")
for student in Student.students:
    print(f"ID: {student.ma_sv}, Ten: {student.hoten_sv}")

        



    