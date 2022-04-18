import time

class Process:
    def __init__(self, name, burstTime):
        self.name = name
        self.burstTime = burstTime

def roundRobin(processes, quantum):
    ms = 0
    while len(processes) > 0:
        for process in processes:
            for i in range(quantum):
                if process.burstTime > 0:
                    print("Processo: " + process.name + " - BurstTime: " + str(process.burstTime))
                    ms += 1
                    time.sleep(1)
                    print("Tempo: " + str(ms))
                    process.burstTime -= 1
            if process.burstTime <= 0:
                processes.remove(process)

p1 = Process("p1", 24)
p2 = Process("p2", 3)
p3 = Process("p3", 3)

processes = [p1, p2, p3]
roundRobin(processes, 4)



