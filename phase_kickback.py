from math import pi, sqrt
from qiskit import QuantumCircuit, execute, Aer

half_turn = 1/sqrt(2)

zero_ket = [1, 0]
one_ket = [0, 1]
plus_ket = [half_turn, half_turn]
minus_ket = [half_turn, -half_turn]


def phase_kickback():
    circuit = QuantumCircuit(2)
    circuit.h(0)
    circuit.x(1)
    circuit.cu1(pi/4, 0, 1)
    print(circuit.draw())

    backend = Aer.get_backend('unitary_simulator')
    result = execute(circuit, backend).result()
    print(result.get_unitary())


phase_kickback()
