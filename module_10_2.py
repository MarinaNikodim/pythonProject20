import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = str(name)
        self.power = int(power)
        self.enemies = 100
        self.days = 0
        self.lock = threading.Lock()

    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.enemies > 0:
            time.sleep(1)
            with self.lock:
                self.enemies -= self.power
                self.days += 1
                print(f'{self.name} сражается {self.days} дней..., осталось {self.enemies} воинов.')
            if self.enemies < 0 or self.enemies == 0:
                print(f'{self.name} одержал победу спустя {self.days} дней(дня)!')



first_knight = Knight('Sir Lancelot', 10)

second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
print('Все воины закончились!')
