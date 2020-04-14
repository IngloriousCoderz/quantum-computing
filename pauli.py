from qiskit import QuantumCircuit, execute, Aer

backend = Aer.get_backend('qasm_simulator')
zero_ket = [1, 0]
one_ket = [0, 1]


def pauli(type, initial_state):
    circuit = QuantumCircuit(1)
    circuit.initialize(initial_state, 0)
    if type == 'X':
        circuit.x(0)
    if type == 'Y':
        circuit.y(0)
    if type == 'Z':
        circuit.z(0)
    circuit.measure_all()
    result = execute(circuit, backend).result()
    print(result.get_counts())


for ket in [zero_ket, one_ket]:
    pauli('X', ket)
    pauli('Y', ket)
    pauli('Z', ket)
