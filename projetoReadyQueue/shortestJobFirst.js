function sjf(processes) {
    let sortedProcess = processes.sort((a, b) => {
        return a.burstTime - b.burstTime
    })
    sortedProcess.forEach(process => {
        while (process.burstTime > 0) {
            showSJF(process)
            process.burstTime--
        }
    })
}

p1 = { name: "p1", burstTime: 6 }

p2 = { name: "p2", burstTime: 8 }

p3 = { name: "p3", burstTime: 7 }

p4 = { name: "p4", burstTime: 3 }

processes = [p1, p2, p3, p4]

function showSJF(process) {
    let elem = document.getElementById("teste");
    let elem2 = document.createElement("div")
    elem2.innerHTML = `Processo: ${process.name}: ${process.burstTime}`
    elem.appendChild(elem2)
}

document.querySelector("button").onclick = () => sjf(processes)
