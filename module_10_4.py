import threading
import time
import random
from queue import Queue


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None # Изначально стол свободен


class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        waiting_time = random.randint(3, 10) # ожидание случайным образом от 3 до 10 секунд
        time.sleep(waiting_time)


class Cafe:
    def __init__(self, queue, *tables):
        self.tables = tables # Столы для гостей
        self.queue = Queue() # Очередь из гостей

    def guest_arrival(self, *guests): # процесс прибытия гостей
        for guest in guests:
            free_table = next((table for table in self.tables if table.guest is None), None)
            if free_table:
                free_table.guest = guest
                guest.start()
                print(f'{free_table.guest.name} сел(-а) за стол номер {free_table.number}')
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди"')

    def discuss_guests(self): # имитирует процесс обслуживания гостей.
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest and not table.guest.is_alive(): # (поток завершил работу - метод is_alive)
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)\nСтол номер {table.number} свободен')
                    table.guest = None
                    if not self.queue.empty() and table.guest is None:
                        next_guest = self.queue.get()
                        table.guest = next_guest
                        next_guest.start()
                        print(f'{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')



# Создание столов
tables = [Table(number) for number in range(0, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()

for guest in guests:
    guest.join()

