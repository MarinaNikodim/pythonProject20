import threading
from time import sleep
import time


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding= 'utf-8') as f:
        for i in range(word_count):
            sleep(0.1)
            line = f'Какое-то слово № {i + 1}\n'
            f.write(line)
        print(f'Завершилась запись в файл {file_name}, поток: {threading.current_thread().name}')


start_time = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end_time = time.time()

print(f'Завершение выполнения потока за: {end_time-start_time:.5f}')


def run_thread(word_count, file_name):
    thread = threading.Thread(target=write_words, args=(word_count, file_name))
    return thread


threads = [
    run_thread(10, 'example5.txt'),
    run_thread(30, 'example6.txt'),
    run_thread(200, 'example7.txt'),
    run_thread(100, 'example8.txt')]

start_time_thr = time.time()
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

end_time_thr = time.time()

print(f'Завершение выполнения потока за: {end_time_thr-start_time_thr:.5f}')

