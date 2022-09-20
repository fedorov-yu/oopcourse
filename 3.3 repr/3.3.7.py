import time
class Clock:
    def __init__(self, hours, minutes, seconds):
        if all(type(i) == int and i >= 0 for i in (hours, minutes, seconds)):
            self.hours = hours
            self.minutes = minutes
            self.seconds = seconds

    def get_time(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds


class DeltaClock:
    def __init__(self, clock1, clock2):
        self.clock1 = clock1
        self.clock2 = clock2

    def __str__(self):
        times = self.clock1.get_time() - self.clock2.get_time()
        if times < 0:
            return "00: 00: 00"
        hours = times // 3600
        minutes = times % 3600 // 60
        seconds = times % 3600 % 60
        # return ": ".join([f'0{i}' if i < 10 else f"{i}" for i in (hours, minutes, seconds)])
        return time.strftime("%H: %M: %S", time.gmtime(times))

    def __len__(self):
        return self.clock1.get_time() - self.clock2.get_time()


dt = DeltaClock(Clock(2, 45, 00), Clock(1, 15, 00))
print(dt) # 01: 30: 00
len_dt = len(dt) # 5400