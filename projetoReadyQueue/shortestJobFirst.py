import time

class Process:
    def __init__(self, name, burstTime):
        self.name = name
        self.burstTime = burstTime

def ordenar(processes):
    ordenated_processes = sorted(processes, key=lambda x: x.burstTime)
    return (ordenated_processes)

def sjf(processes):
    ordenated_processes = ordenar(processes)
    ms = 0
    while len(ordenated_processes) > 0:
        for process in ordenated_processes:
            while process.burstTime > 0:
                print("Processo: " + process.name + " - BurstTime: " + str(process.burstTime))
                ms += 1
                time.sleep(1)
                print("Tempo: " + str(ms))
                process.burstTime -= 1
            if process.burstTime <= 0:
                ordenated_processes.remove(process)

p1 = Process("p1", 6)
p2 = Process("p2", 8)
p3 = Process("p3", 7)
p4 = Process("p4", 3)

processes = [p1, p2, p3, p4]
sjf(processes)