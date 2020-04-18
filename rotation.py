from qiskit import QuantumCircuit, execute, Aer


def rotation():
    circuit = QuantumCircuit(1)
    circuit.h(0)
    circuit.t(0)
    circuit.h(0)
    circuit.t(0)
    # circuit.measure_all()
    print(circuit.draw())

    result = execute(circuit, Aer.get_backend('unitary_simulator')).result()
    print(result.get_unitary())


rotation()
