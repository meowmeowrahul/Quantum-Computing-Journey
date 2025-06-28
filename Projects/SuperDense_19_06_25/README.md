# 🌀 Superdense Coding

This project demonstrates **Superdense Coding**, a fundamental quantum communication protocol that allows the transfer of two classical bits using one qubit.

---

## 📌 Problem Statement
How to transmit **Classical bits** using **Qubits** 

**Similiar to Quantum Teleportation**

## 🧠 Theory Overview

Superdense Coding uses the following components:
- A sender (Alice) and a receiver (Bob)
- A pair of **entangled qubits** shared between them
- Two **classical bits** to be teleported

Steps:
1. Alice performs **X Gate** or **Z Gate** on her qubit depending on bits.
2. Alice sends qubit to Bob.
3. Bob measures the qubit to reveal classical bits.

The result: The classical bits are now with Bob.

---

## ⚙️ Implementation Details

- Implemented using **Qiskit** (Python)
- Visualized the **quantum circuit** using Qiskit’s circuit drawer
- Simulated results using **Aer simulator** and `plot_histogram`

---

## 📥 Dependencies

- Python 3.3+ miniconda 
- Qiskit (install via `pip install qiskit`)
- Jupyter Notebook
---

## 📚 References
- 'Basics of Quantum Information'[https://learning.quantum.ibm.com/course/basics-of-quantum-information]
---

## 💡 Future Ideas

- Extend to multi-bit transfer
- Add noise simulation using Qiskit’s noise model

---

## 🧑‍💻 Author

Rahul Dubey – [@meowmeowrahul](https://github.com/meowmeowrahul)



