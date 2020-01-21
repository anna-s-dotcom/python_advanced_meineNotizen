# Erstelle zwei funktionen. Eine, die zu einer Zahl 2 hinzu addiert und eine, die von einer Zahl 2 abzieht.
#
# Erstelle einen shared Value Datentyp mit dem Wert 100.
#
# Erstelle für jede Funktion je 20 Prozesse, die diese Funktion aufrufen.
#
# Gib den Endwert der shared Value Variable aus.
#
# Bonus: Teste Zeit mit Lock und Zeit ohne Lock.
import multiprocessing as mp
import time

def plus2(x):
    x.value += 2

def minus2(x):
    x.value -= 2

if __name__ == '__main__':
    shared_value = mp.Value('i', 100)
    processes = []

    for i in range(20):
        p1 = mp.Process(target = plus2, args=(shared_value, ))
        p2 = mp.Process(target = minus2, args=(shared_value, ))
        processes.append(p1)
        processes.append(p2)
        p1.start()
        p2.start()

    for p in processes:
        p.join()

    print(shared_value.value)
    # print(shared_value.value)
    # print(shared_value.value)
    # print(shared_value.value)
    # time.sleep(0.5)
    # print(shared_value.value)
    # time.sleep(0.5)
    # print(shared_value.value)
