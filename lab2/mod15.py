from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from qiskit.circuit.library import QFT
import numpy as np
from math import gcd
import matplotlib.pyplot as plt

N = 15

while True:
    try:
        a = int(input(f"input: "))
        if gcd(a, N) != 1:
            print(f"{a} and {N} aren't coprime. try again")
        else:
            print(f"can find order of {a} mod {N}")
            break
    except ValueError:
        print("error. need int. try again")

n = 4

qc = QuantumCircuit(2 * n, n)

qc.h(range(n))

for q in range(n):
    exponent = 2 ** q
    angle = 2 * np.pi * (a ** exponent / N)
    qc.cp(angle, q, q + n)

qc.append(QFT(n, inverse=True), range(n))

qc.measure(range(n), range(n))

qc.draw("mpl", scale=1.5)
plt.show()

simulator = AerSimulator()
compiled_circuit = transpile(qc, simulator)
job = simulator.run(compiled_circuit, shots=1024)
result = job.result()
counts = result.get_counts()

plot_histogram(counts)
plt.show()

#measured_value = max(counts, key=counts.get)
#s = int(measured_value, 2)
