# 🌀 Quantum Teleportation

This project demonstrates **Quantum Teleportation**, a fundamental quantum communication protocol that allows the transfer of a quantum state from one qubit to another — without physically sending the qubit itself.

---

## 📌 Problem Statement

How can we transmit an unknown quantum state from one location to another **without directly measuring or copying it**?

Classical methods can't solve this due to the **no-cloning theorem** in quantum mechanics. Quantum teleportation solves this using **entanglement** and **classical communication**.

---

## 🧠 Theory Overview

Quantum Teleportation uses the following components:
- A sender (Alice) and a receiver (Bob)
- A pair of **entangled qubits** shared between them
- One **unknown quantum state** to be teleported

Steps:
1. Alice entangles her qubit with Bob's.
2. Alice performs a **Bell measurement** on her qubit and the unknown state.
3. She sends the result (2 classical bits) to Bob.
4. Bob uses that classical info to **recover the original quantum state** on his qubit.

The result: the original state is recreated on Bob’s qubit!

---

## ⚙️ Implementation Details

- Implemented using **Qiskit** (Python)
- Visualized the **quantum circuit** using Qiskit’s circuit drawer
- Simulated results using **Aer simulator** and `plot_histogram`

---

## 📥 Dependencies

- Python 3.8+
- Qiskit (install via `pip install qiskit`)
- Jupyter Notebook
---

## 📚 References
- 'Basics of Quantum Information'[https://learning.quantum.ibm.com/course/basics-of-quantum-information]
---

## 💡 Future Ideas

- Extend to multi-qubit teleportation
- Add noise simulation using Qiskit’s noise model

---

## 🧑‍💻 Author

Rahul Dubey – [@meowmeowrahul](https://github.com/meowmeowrahul)



