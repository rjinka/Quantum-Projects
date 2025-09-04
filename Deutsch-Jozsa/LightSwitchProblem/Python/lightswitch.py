from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import numpy as np

# Define quantum oracle for our 2 input light switch problem

def light_switch_oracle(circuit, n_qubits, func_type, const_output=0):

    if n_qubits < 1 or n_qubits > 3:
        raise ValueError("Number of qubits must be between 1 and 3.")
    
    aux_qubit_idx = n_qubits
    
    if func_type == "constant_off":
        # f(x0, x1) == 0 for all inputs 
        pass

    elif func_type == "constant_on":
        # f(x0, x1) == 1 for all inputs
        circuit.x(aux_qubit_idx)  # Flip all qubits to output 1
        pass

    elif func_type == "balanced_xor":
        # f(x0, x1) is balanced
        circuit.cx(0, aux_qubit_idx)
        circuit.cx(1, aux_qubit_idx)
        pass
    elif func_type == "balanced_custom":
        circuit.cx(0,aux_qubit_idx)
        pass
    else:
        raise ValueError("Invalid function type. Choose from 'constant_off', 'constant_on', or 'balanced_xor'.")
    
# define the Deutsch-Jozsa algorithm

def deutsch_jozsa(n_input_qubits, oracle_func_type, const_val=0):

    qc = QuantumCircuit(n_input_qubits + 1, n_input_qubits)

    # Initialize the ancilla qubit to |1>
    qc.x(n_input_qubits)
    qc.h(n_input_qubits)

    # Apply Hadamard gates to input qubits
    for i in range(n_input_qubits):
        qc.h(i)
        
    qc.barrier()

    # Apply the oracle
    light_switch_oracle(qc, n_input_qubits, oracle_func_type, const_val)
    qc.barrier()

    # Apply Hadamard gates to input qubits again
    for i in range(n_input_qubits+1):
        qc.h(i)

    qc.barrier()

    # Measure the input qubits
    for i in range(n_input_qubits):
        qc.measure(i, i)

    return qc

# Similate the circuit
n_qubits = 2  # Number of input qubits
simulator = Aer.get_backend('qasm_simulator')
shots = 1024

print(f"--- Deutsch-Jozsa for N = {n_qubits} Input Light Switch ---")

# --- Test Case 1: Constant 0 Light Switch (Always OFF) ---pip install qiskit
print("\nTesting: Light Switch is CONSTANT 0 (Always OFF)")
dj_circuit_c0 = deutsch_jozsa(n_qubits, 'constant_off')
print(dj_circuit_c0.draw(output='text'))

job = simulator.run(dj_circuit_c0, shots=shots)
result = job.result()
counts_c0 = result.get_counts(dj_circuit_c0)
print("Measurement Results:", counts_c0)
# Expected: All '00'
if '0' * n_qubits in counts_c0 and len(counts_c0) == 1:
    print(f"Conclusion: CONSTANT (Correct! Measured all '{'0'*n_qubits}')")
else:
    print("Conclusion: UNEXPECTED (Error in constant test)")

# --- Test Case 2: Constant 1 Light Switch (Always ON) ---
print("\nTesting: Light Switch is CONSTANT 1 (Always ON)")
dj_circuit_c1 = deutsch_jozsa(n_qubits, 'constant_on')
print(dj_circuit_c1.draw(output='text'))

job = simulator.run(dj_circuit_c1, shots=shots)
result = job.result()
counts_c1 = result.get_counts(dj_circuit_c1)
print("Measurement Results:", counts_c1)
# Expected: All '11'
if '0' * n_qubits in counts_c1 and len(counts_c1) == 1:
    print(f"Conclusion: CONSTANT (Correct! Measured all '{'1'*n_qubits}')")
else:
    print("Conclusion: UNEXPECTED (Error in constant test)")

# --- Test Case 3: Balanced Light Switch ---
print("\nTesting: Light Switch is BALANCED")
dj_circuit_balanced = deutsch_jozsa(n_qubits, 'balanced_xor')
print(dj_circuit_balanced.draw(output='text'))

job = simulator.run(dj_circuit_balanced, shots=shots)
result = job.result()
counts_balanced = result.get_counts(dj_circuit_balanced)
print("Measurement Results:", counts_balanced)
# Expected: Half '00' and half '11' (for 2 qubits)
expected_counts = {'00': shots//2, '11': shots//2}
if '0' * n_qubits not in counts_balanced:
    print("Conclusion: BALANCED (Correct! Measured half '00' and half '11')")
else:
    print("Conclusion: UNEXPECTED (Error in balanced test)")

# --- Test Case 4: Custom Balanced
print("\nTesting: Light Switch is custom balanced")
dj_circuit_custom_balanced = deutsch_jozsa(n_qubits, 'balanced_custom')
print(dj_circuit_custom_balanced)

job = simulator.run(dj_circuit_custom_balanced, shots=shots)
result = job.result()
custom_balanced = result.get_counts(dj_circuit_custom_balanced)
print("Measurement Results:", custom_balanced)
#Expected: 00 and 10 are 1 and 01 and 11 are 0
if '0' * n_qubits not in custom_balanced:
    print(f"Conclusion: BALANCED (Correct! Never measured '{'0'*n_qubits}')")
else:
    print("Conclusion: UNEXPECTED (Error in custom balanced test)")