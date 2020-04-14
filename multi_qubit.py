from qiskit import QuantumCircuit, execute, Aer

circuit = QuantumCircuit(1)
circuit.x(0)
circuit.z(0)
circuit.h(0)
print(circuit.draw())

backend = Aer.get_backend('unitary_simulator')
unitary = execute(circuit, backend).result().get_unitary()
print(unitary)
