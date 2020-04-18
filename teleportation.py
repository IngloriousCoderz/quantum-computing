from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, Aer
from qiskit.extensions import Initialize
from math import sin, cos, pi

alice = 0
common = 1
bob = 2


def teleportation(psi):
    qr = QuantumRegister(3)
    crz = ClassicalRegister(1)
    crx = ClassicalRegister(1)
    qc = QuantumCircuit(qr, crz, crx)
    init_gate = Initialize(psi)
    qc.append(init_gate, [alice])
    qc.barrier()

    create_bell_pair(qc, common, bob)
    qc.barrier()
    create_alice(qc, alice, common)
    qc.barrier()
    measure_and_send(qc, alice, common)
    qc.barrier()
    create_bob(qc, bob, crz, crx)
    print(qc.draw())

    result = execute(qc, Aer.get_backend('statevector_simulator')).result()
    print(result.get_statevector())

    reverse_init_gate = init_gate.gates_to_uncompute()
    qc.append(reverse_init_gate, [bob])
    print(qc.draw())

    cr_result = ClassicalRegister(1)
    qc.add_register(cr_result)
    qc.measure(bob, 2)
    print(qc.draw())

    result = execute(qc, Aer.get_backend('qasm_simulator')).result()
    print(result.get_counts())


def create_bell_pair(circuit, control, target):
    circuit.h(control)
    circuit.cx(control, target)


def create_alice(circuit, control, target):
    circuit.cx(control, target)
    circuit.h(control)


def measure_and_send(circuit, control, target):
    circuit.measure(control, 0)
    circuit.measure(target, 1)


def create_bob(circuit, qubit, crz, crx):
    circuit.z(qubit).c_if(crz, 1)
    circuit.x(qubit).c_if(crx, 1)


psi = [cos(pi/4), sin(pi/4)]
teleportation(psi)
