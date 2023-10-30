import turtle
from datetime import datetime

class AnalogClock:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.bgcolor("black")
        self.screen.title("Đồng hồ Turtle")

        self.clock = turtle.Turtle()
        self.clock.shape("circle")
        self.clock.color("white")
        self.clock.width(3)

        # Thuộc tính giờ, phút, giây
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

        # Gọi hàm để vẽ mặt đồng hồ và các vạch chia
        self.draw_clock_face()
        self.draw_hour_hand(100)
        self.draw_minute_hand(100)
        self.draw_second_hand(100)

    # Hàm để vẽ mặt đồng hồ và các vạch chia
    def draw_clock_face(self):
        self.clock.penup()
        self.clock.goto(0, -200)
        self.clock.pendown()
        self.clock.circle(200)

        # Vẽ vạch chia giờ
        for _ in range(12):
            self.clock.penup()
            self.clock.goto(0, 0)
            self.clock.forward(160)
            self.clock.pendown()
            self.clock.forward(30)
            self.clock.backward(0)
            self.clock.right(30)

    #     # Vẽ vạch chia phút
        for _ in range(60):
            self.clock.penup()
            self.clock.goto(0, 0)
            self.clock.forward(160)
            self.clock.pendown()
            self.clock.forward(20)
            self.clock.backward(10)
            self.clock.right(6)

    # # Hàm để vẽ kim giờ
    def draw_hour_hand(self, length):
        self.clock.penup()
        self.clock.goto(0, 0)
        self.clock.pendown()
        self.clock.setheading(45)
        self.clock.pensize(6)
        self.clock.forward(length)
        self.clock.backward(length)

    # # Hàm để vẽ kim phút
    def draw_minute_hand(self, length):
        self.clock.penup()
        self.clock.goto(0, 0)
        self.clock.pendown()
        self.clock.setheading(90)
        self.clock.pensize(3)
        self.clock.forward(length)
        self.clock.backward(length)

    # # Hàm để vẽ kim giây
    def draw_second_hand(self, length):
        self.clock.penup()
        self.clock.goto(0, 0)
        self.clock.pendown()
        self.clock.color("red")
        self.clock.setheading(90)
        self.clock.pensize(2)
        self.clock.forward(length)
        self.clock.backward(length)

    # Hàm để cập nhật thời gian
    # def update_time(self):
    #     # Lấy thời gian hiện tại
    #     current_time = datetime.now()
    #     self.hours = current_time.hour
    #     self.minutes = current_time.minute
    #     self.seconds = current_time.second

    #     # Xóa hình trước đó để vẽ lại
    #     self.clock.clear()

    #     # Gọi hàm để vẽ mặt đồng hồ và các vạch chia
    #     self.draw_clock_face()

    #     # Vẽ kim giờ
    #     self.draw_hour_hand(50 + self.hours * 10)

    #     # Vẽ kim phút
    #     self.draw_minute_hand(70 + self.minutes * 2)

    #     # Vẽ kim giây
    #     self.draw_second_hand(90 + self.seconds * 2)

    #     self.screen.ontimer(self.update_time, 1000)

    # Hàm để bắt đầu chạy đồng hồ
    def start_clock(self):
        # self.update_time()
        self.screen.mainloop()

# Tạo đối tượng đồng hồ
analog_clock = AnalogClock()

# Bắt đầu chạy đồng hồ
analog_clock.start_clock()