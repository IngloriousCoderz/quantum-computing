from qiskit import *
# from qiskit.visualization import plot_histogram

# used in Jupyter notebooks
# %config InlineBackend.figure_format = 'svg'


def main():
    qc = create_circuit()
    draw_circuit(qc)
    run_circuit(qc)


def create_circuit():
    circuit = QuantumCircuit(2)
    circuit.h(0)
    circuit.cx(0, 1)
    circuit.measure_all()
    return circuit


def draw_circuit(circuit):
    print(circuit.draw())


def run_circuit(circuit):
    emulator = Aer.get_backend('qasm_simulator')
    job = execute(circuit, emulator, shots=10, memory=True)
    result = job.result()
    counts = result.get_counts()
    print(counts)
    shots = result.get_memory()
    print(shots)


main()


def explicit_circuit():
    circuit = QuantumCircuit()
    qubits = QuantumRegister(2, 'qreg')
    circuit.add_register(qubits)
    bits = ClassicalRegister(2, 'creg')
    circuit.add_register(bits)

    circuit.h(qubits[0])
    circuit.cx(qubits[0], qubits[1])
    # circuit.measure(qubits[0], bits[0])
    # circuit.measure(qubits[1], bits[1])
    circuit.measure(qubits, bits)
    print(circuit.draw())

    # print(Aer.backends())

    # emulator = Aer.get_backend('statevector_simulator')
    # job = execute(circuit, emulator)
    # ket = job.result().get_statevector()
    # for amplitude in ket:
    #     print(amplitude)

    emulator = Aer.get_backend('qasm_simulator')
    job = execute(circuit, emulator, shots=10, memory=True)
    result = job.result()
    counts = result.get_counts()
    print(counts)
    shots = result.get_memory()
    print(shots)
    # plot_histogram(counts)

    # Initialize with arbitrary values
    # new_circuit = QuantumCircuit(qubits)
    # new_circuit.initialize(ket, qubits)
    # new_circuit.h(qubits[0])
    # new_circuit.cx(qubits[0], qubits[1])
    # print(new_circuit.draw())
