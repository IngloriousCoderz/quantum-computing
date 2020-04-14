from qiskit import QuantumCircuit, execute, Aer

backend = Aer.get_backend('qasm_simulator')
zero_ket = [1, 0]
one_ket = [0, 1]


def half_adder():
    circuit = QuantumCircuit(4, name='half adder')
    circuit.append(xor_gate(), [0, 1, 2])
    circuit.append(and_gate(), [0, 1, 3])
    return circuit.to_instruction()


def xor_gate():
    circuit = QuantumCircuit(3, name='XOR')
    circuit.cx(0, 2)
    circuit.cx(1, 2)
    return circuit.to_instruction()


def and_gate():
    circuit = QuantumCircuit(3, name='AND')
    circuit.ccx(0, 1, 2)
    return circuit.to_instruction()


circuit = QuantumCircuit(4, 2)
circuit.initialize(one_ket, 0)  # same as circuit.x(0)
circuit.initialize(one_ket, 1)  # same as circuit.x(1)
circuit.append(half_adder(), [0, 1, 2, 3])
circuit.measure(2, 0)
circuit.measure(3, 1)
print(circuit.draw())
result = execute(circuit, backend).result()
print(result.get_counts())
