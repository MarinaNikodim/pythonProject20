import threading
import random
import time


class Bank:
    def __init__(self, balance):
        super().__init__()
        self.balance = int(balance)
        self.lock = threading.Lock()

    def deposit(self):
        self.lock.acquire()
        for i in range(100):
            random_transaction = random.randint(50, 500)
            self.balance += random_transaction
            print(f'Пополнение: {random_transaction}. Баланс: {self.balance}.')
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            random_transaction = random.randint(50, 500)
            print(f'Запрос на снятие: {random_transaction}.')
            if random_transaction <= self.balance:
                self.balance -= random_transaction

                print(f' "Снятие: {random_transaction}. Баланс: {self.balance}".')
            else:
                print("Запрос отклонён, недостаточно средств")
        self.lock.release()


bk = Bank(10)
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args =(bk,))
th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')















