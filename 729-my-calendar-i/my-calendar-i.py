class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        for i,(x,y) in enumerate(self.calendar):
            if (start>=x and start<y) or (end>x and end<y) or (x>=start and x<end) or (y>start and y<end):
                return False
        self.calendar.append([start,end])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)