
class Bbox:
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self._get_w_h()

    def __str__(self): #Он представляет класс в виде строки
        return f"(x0={self.x0}; y0={self.y0}), (x1={self.x1}, y1={self.y1})"

    def __repr__(self): #представляет класс в виде строки в обектах
        return f"(({self.x0}; {self.y0}), ({self.x1}, {self.y1}))"

    def __add__(self, other):
        return Bbox(min(self.x0, other.x0),
                    min(self.y0, other.y0),
                    max(self.x1, other.x1),
                    max(self.y1, other.y1))


    def _get_w_h(self): #внутренний метод, Не для Пользователя
        self.w = self.x1 - self.x0
        self.h = self.y1 - self.y0

    def get_area(self):
        return self.w * self.h


# bbox_1 = Bbox(0,0,2,3)
# print(bbox_1.w, bbox_1.h)
#
# area = bbox_1.get_area()
# print(area)
bbox_1 = Bbox(0,0,2,3)
bbox_2 = Bbox (1,2,3,4)
print(str(bbox_1))
bbox_list = [bbox_1, bbox_2]
bbox_3 = bbox_1+bbox_2
print(bbox_3)
print(bbox_list)