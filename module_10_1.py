import threading
import time


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding= 'utf-8') as f:
        for i in range(word_count):
            time.sleep(0.1)
            line = f'Какое-то слово № {i + 1}\n'
            f.write(line)
            print(f'Завершилась запись в файл {file_name}, поток: {threading.current_thread().name}')


def first_block():
    write_words(10, 'example1.txt')
    write_words(30, 'example2.txt')
    write_words(200, 'example3.txt')
    write_words(100, 'example4.txt')


def second_block():
    write_words(10, 'example5.txt')
    write_words(30, 'example6.txt')
    write_words(200, 'example7.txt')
    write_words(100, 'example8.txt')


thread1 = threading.Thread(target = first_block)
thread2 = threading.Thread(target = second_block)
start_time = time.time()
thread1.start()
thread2.start()

thread1.join()
thread2.join()

end_time = time.time()

print(f'Завершение выполнения потока за: {end_time-start_time:.5f}')
