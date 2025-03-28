from qiskit import QuantumCircuit
import matplotlib.pyplot as plt

qc = QuantumCircuit(3)

qc.h(2)      
qc.cx(1, 2)    
qc.cx(0, 2)    
qc.h(2)

qc.measure_all()

qc.draw('mpl')
plt.show()
