import threading
from time import sleep, time
from datetime import timedelta

def wite_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8'  ) as f:
        for i in range(1, word_count + 1):
            f.write(f"Какое-то слово № {i}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

start_time = time()
wite_words(10, "example1.txt")
wite_words(30, "example2.txt")
wite_words(200, "example3.txt")
wite_words(100, "example4.txt")
end_time = time()
print(f"Работа функций: {timedelta(seconds=end_time - start_time)}")

start_time = time()

threads = [
    threading.Thread(target=wite_words, args=(10, "example5.txt")),
    threading.Thread(target=wite_words, args=(30, "example6.txt")),
    threading.Thread(target=wite_words, args=(200, "example7.txt")),
    threading.Thread(target=wite_words, args=(100, "example8.txt")),
]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

end_time = time()
print(f"Работа потоков: {timedelta(seconds=end_time - start_time)}")
