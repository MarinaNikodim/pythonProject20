import threading
import time
from multiprocessing import Pool


def read_info(name): #где name - название файла
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())


threads = []
file_names = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов
# start_time = time.time()
# for file_name in file_names:
#
#     thread = threading.Thread(target=read_info, args=(file_name, ))
#     threads.append(thread)
#     thread.start()
#
#     thread.join()
# end_time = time.time()
# print(f'{end_time - start_time}')

# Многопроцессный
if __name__ == '__main__':
    start_time2 = time.time()
    with Pool() as pool:
        pool.map(read_info, file_names)
    end_time2 = time.time()

    print(f'{end_time2 - start_time2}')






