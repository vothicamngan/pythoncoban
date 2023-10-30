import math
class Diem:
    x : int = 0
    y : int = 0
    label: str = ""
    def __init__(self,label ,x,y):
        self.label = label
        self.x = x
        self.y = y
    def __str__(self):
        return f"{self.label({self.x},{self.y})}"
    def dich_chuyen(self,dx,dy):
        new_x = self.x + dx
        new_y = self.y + dy
        return new_x, new_y
    def khoang_cach_toi_diem(self,orther):
        delta_x = self.x = orther.x
        delta_y = self.y = orther.y
        return math.sqrt(delta_x**2 + delta_y**2)
d = Diem("C",1,5)
print(d.dich_chuyen(3,6))
print(d.khoang_cach_toi_diem("D",3,6))