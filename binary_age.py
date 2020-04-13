import math
from qiskit import QuantumCircuit, execute, Aer

backend = Aer.get_backend('qasm_simulator')


def binary_age(age):
    n = math.ceil(math.log2(age))
    qc_output = QuantumCircuit(n, n)
    for j in range(n):
        qc_output.measure(j, j)

    qc_encode = QuantumCircuit(n)
    qc_encode.x(0)
    qc_encode.x(2)
    qc_encode.x(5)

    qc = qc_encode + qc_output
    print(qc.draw())

    result = execute(qc, backend).result()
    print(result.get_counts())


binary_age(37)
