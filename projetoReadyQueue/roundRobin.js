const roundRobin = (processes, quantum) => {
    let ms = 0
    while (processes.length > 0) {
        processes.forEach(process => {
            for(let i = 0; i < quantum; i++) {
                if (process.burstTime > 0) {
                    console.log(`Processo: ${process.name}: ${process.burstTime}`)
                    ms++
                    console.log(`Tempo: ${ms}`)
                    process.burstTime--
                }
            }
            if (process.burstTime <= 0) {
                processes.splice(processes.indexOf(process), 1)
            }
        });
    }
}

p1 = { name: "p1", burstTime: 24 }

p2 = { name: "p2", burstTime: 3 }

p3 = { name: "p3", burstTime: 3 }

processes = [p1, p2, p3]

roundRobin(processes, 4)