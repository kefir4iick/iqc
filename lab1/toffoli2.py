from qiskit import QuantumCircuit
import matplotlib.pyplot as plt

qc = QuantumCircuit(3)

qc.ccx(0, 1, 2)

qc.measure_all()

qc.draw('mpl')
plt.show()
