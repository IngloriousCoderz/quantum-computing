from qiskit import QuantumCircuit, execute, Aer, IBMQ
# from qiskit.visualization import plot_histogram

# used in Jupyter notebooks
# %config InlineBackend.figure_format = 'svg'


def bell_state(type='qasm'):
    qc = create_circuit(type)
    draw_circuit(qc)
    run_circuit(qc, type)


def create_circuit(type='qasm'):
    circuit = QuantumCircuit(2)
    circuit.h(0)
    # circuit.x(1)
    circuit.cx(0, 1)

    if type != 'unitary':
        circuit.measure_all()

    return circuit


def draw_circuit(circuit):
    print(circuit.draw())


def get_backend(type='qasm'):
    if type == 'quantum':
        IBMQ.load_account()
        provider = IBMQ.get_provider(hub='ibm-q')
        # for backend in provider.backends():
        #     print(backend.status())
        return provider.get_backend('ibmq_london')
    elif type == 'unitary':
        return Aer.get_backend('unitary_simulator')
    else:
        return Aer.get_backend('qasm_simulator')


def run_circuit(circuit, type='qasm'):
    backend = get_backend(type)
    if type == 'unitary':
        job = execute(circuit, backend)
    else:
        job = execute(circuit, backend, shots=10, memory=True)

    result = job.result()

    if type == 'unitary':
        print(result.get_unitary())
    else:
        print(result.get_counts())
        print(result.get_memory())


bell_state(type='qasm')


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
    # backend = Aer.get_backend('statevector_simulator')
    # job = execute(circuit, backend)
    # ket = job.result().get_statevector()
    # for amplitude in ket:
    #     print(amplitude)

    backend = Aer.get_backend('qasm_simulator')
    job = execute(circuit, backend, shots=10, memory=True)
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
