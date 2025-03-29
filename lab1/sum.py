from qiskit import QuantumCircuit
import matplotlib.pyplot as plt

def sum(a, b, n = 4):
    ter = 4 * n
    qc = QuantumCircuit(ter, n + 1)

    for i in range(n):
        if (a >> i) & 1:
            qc.x(i)
        if (b >> i) & 1:
            qc.x(i + n)

    carry = list(range(3 * n, 4 * n))
    c = list(range(2 * n, 3 * n))

    for i in range(n):
        if i < (n - 1):
            qc.ccx(i, i + n, carry[i + 1])

        qc.cx(i, c[i])
        qc.cx(i + n, c[i])

        if i > 0:
            qc.ccx(c[i - 1], carry[i], c[i])
            qc.cx(carry[i], c[i])

            qc.ccx(c[i - 1], carry[i], carry[i - 1])

    for i in range(n):
        qc.measure(c[i], i)
    qc.measure(carry[n - 1], n)

    return qc

qc = sum(5, 3)



qc.draw('mpl')
plt.show()
