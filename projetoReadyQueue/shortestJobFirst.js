const sjf = (processes) => {
    let sortedProcess = processes.sort((a, b) => {
        return a.burstTime - b.burstTime
    })
    const tela = document.querySelector('tela')
    sortedProcess.forEach(process => {
        while (process.burstTime > 0) {
            tela.appendChild(process.elemento)
            process.burstTime--
        }
    })
}

p1 = { name: "p1", burstTime: 6 }

p2 = { name: "p2", burstTime: 8 }

p3 = { name: "p3", burstTime: 7 }

p4 = { name: "p4", burstTime: 3 }

processes = [p1, p2, p3, p4]

sjf(processes)