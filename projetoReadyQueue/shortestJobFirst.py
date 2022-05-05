import time

class Process:
    def __init__(self, name, burstTime):
        self.name = name
        self.burstTime = burstTime

def sort(processes):
    sorted_processes = sorted(processes, key=lambda x: x.burstTime)
    return (sorted_processes)

def sjf(processes):
    sorted_processes = sort(processes)
    ms = 0
    for process in sorted_processes:
        while process.burstTime > 0:
            print("Processo: " + process.name + " - BurstTime: " + str(process.burstTime))
            ms += 1
            time.sleep(1)
            print("Tempo: " + str(ms))
            process.burstTime -= 1
                
p1 = Process("p1", 6)
p2 = Process("p2", 8)
p3 = Process("p3", 7)
p4 = Process("p4", 3)

processes = [p1, p2, p3, p4]
sjf(processes)