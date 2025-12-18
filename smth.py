from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def bell_phi_plus():
    qc = QuantumCircuit(2,2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure([0, 1], [0, 1])
    return qc

def bell_phi_minus():
    qc = QuantumCircuit(2,2)
    qc.h(0)
    qc.cx(0, 1)
    qc.z(1) 
    qc.measure([0, 1], [0, 1])
    return qc

def bell_psi_plus():
    qc = QuantumCircuit(2,2)
    qc.h(0)      
    qc.cx(0, 1)  
    qc.x(0)
    qc.measure([0, 1], [0, 1])
    return qc

def bell_psi_minus():
    qc = QuantumCircuit(2,2)
    qc.h(0)
    qc.cx(0, 1)
    qc.x(0)
    qc.z(1) 
    qc.measure([0, 1], [0, 1])
    return qc

# def teleport_phi_plus():
#     qc = QuantumCircuit(3,3)
#     # qc.x(0)
#     # qc.measure([0,1], [0,1])
#     qc.h(1)
#     qc.cx(1,2)
#     qc.cx(0,1)
#     qc.h(0)
#     qc.cx(1,2)
#     qc.cz(0,2)
#     qc.measure([2], [2])
#     return qc

def teleport_phi_plus():
    qc = QuantumCircuit(3,3)
    qc.x(0)
    qc.h(1)
    qc.cx(1,2)
    qc.cx(0,1)
    qc.h(0)
    qc.cx(1,2)
    qc.cz(0,2)
    qc.measure([0, 1, 2], [0, 1, 2])

    return qc

def zip_psi_plus():
    qc = QuantumCircuit(4,2)
    # qc.x(0)
    # qc.x(1)
    qc.h(2)
    qc.cx(2,3)
    qc.x(2)
    qc.x(1)
    # qc.cx(1,2)
    qc.cx(1,2)
    qc.cz(0,2)
    qc.cx(2,3)
    qc.h(2)
    qc.measure([2,3],[0,1])
    return qc

def grover_2_with_dop():
    qc = QuantumCircuit(3,2)
    qc.h(0)
    qc.h(1)
    qc.x(2)
    qc.h(2)
    qc.ccx(0,1,2)
    qc.h(0)
    qc.h(1)
    qc.x(0)
    qc.x(1)
    qc.ccx(0, 1, 2)
    qc.x(0)
    qc.x(1)
    qc.h(0)
    qc.h(1)
    qc.measure([0,1],[0,1])
    return qc

def grover_2():
    qc = QuantumCircuit(2,2)
    qc.h(0)
    qc.h(1)
    # TODO оракул который превращает нужное значение системы(00,01...) в значение со знаком -
    qc.cz(0,1) # это для значения 11
    #конец оракула

    # инверсия по среднемуф
    qc.h(0)
    qc.h(1)
    qc.z(0)
    qc.z(1)
    qc.cz(0,1)
    qc.h(0)
    qc.h(1)


bell_circuits = {
    # "|Φ⁺⟩": bell_phi_plus(),
    # "|Φ⁻⟩": bell_phi_minus(),
    # "|Ψ⁺⟩": bell_psi_plus(),
    # "|Ψ⁻⟩": bell_psi_minus(),
    # "teleport_|Φ⁺": teleport_phi_plus(),
    #"zip_|Ψ⁺": zip_psi_plus(),
    "grover_2": grover_2_with_dop()
}


simulator = AerSimulator()

results = {}
shots = 1024

for name, qc in bell_circuits.items():
    job = simulator.run(qc, shots=shots)
    result = job.result()
    counts = result.get_counts()
    print(f"{name}: {counts}")
    print(f"\nСхема для {name}:\n")
    
    print(qc.draw())
