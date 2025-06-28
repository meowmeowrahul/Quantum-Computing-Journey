# 🌀 Classical Gates to Quantum Gates

This project demonstrates **Quantum OR gate**, a quantum circuit that gives equivalent output to classical OR gate

---

## 📌 Problem Statement
**2 bit**-Exercise: Find a quantum circuit which computes 
∣x1,x2⟩∣0⟩→∣x1,x2⟩∣x1∨x2⟩∣x1​,x2​⟩∣0⟩→∣x1​,x2​⟩∣x1​∨x2​⟩, where ∨∨ denotes the logical OR.

**3-Bits**-Exercise: Find a quantum circuit which performs a clean computation of the classical function s(x1,x2,x3)=x1∨x2∨x3s(x1​,x2​,x3​)=x1​∨x2​∨x3​.
---

## 🧠 Theory Overview

Classical circuit conversion is done by:
- Each classical gate is replaced by **equivalent** ANDs,NOTs or XORs 

Steps:
1. AND gate is made using **Toffoli Gate** 
2. NOT gate using **Pauli X Gate**
3. XOR gate using **Controlled Not Gate**

The result: the output is logical OR which is scalable to n bits by repetition

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
- How the quantum search algorithm works[https://quantum.country/search]
---

## 💡 Future Ideas

- Implementing other logical gates like NAND etc
- Add noise simulation using Qiskit’s noise model

---

## 🧑‍💻 Author

Rahul Dubey – [@meowmeowrahul](https://github.com/meowmeowrahul)



