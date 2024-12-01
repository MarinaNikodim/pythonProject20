import threading
import time


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding= 'utf-8') as f:
        for i in range(word_count):
            time.sleep(0.1)
            line = f'Какое-то слово № {i + 1}\n'
            f.write(line)
            print(f'Завершилась запись в файл {file_name}') #, threading.current_thread().name)


thread1 = threading.Thread(target = write_words, args = (100, 'example8.txt'))
start_time = time.time()
thread1.start()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end_time = time.time()

thread1.join()

print(f'Завершение выполнения потока за: {end_time-start_time:.5f}')

write_words(10, 'example5.txt')
write_words(30, 'example6.txt')
write_words(200, 'example7.txt')
end_time= time.time()

thread1.join()

print(f'Завершение выполнения потока за: {end_time-start_time:.5f}')








