# 🌀 Classical Gates to Quantum Gates

This project demonstrates **Grover's Search Algoritm'**, a quantum circuit that gives equivalent output to classical OR gate

---

## 📌 Problem Statement
Classical algorithms require O(N)O(N) time to search an unsorted database of NN items, which is inefficient for large datasets.
This project explores Grover's Algorithm to achieve faster search in O(N^0.5) time using quantum computing.
## 🧠 Theory Overview

Grover's circuit repetively flips a vector about solution and equivalent state so to modify it in 
such a way output is matched case with **high probability** 

Steps:
1. Starting at ket0 apply **hadmard gate** to each qubit
2. Repeat the following Grover iteration a number of times equal to: **pi*(root(N)/4)**
3. Measure to obtain the search solution s with probability at least **1−1/N**.
4. Use the search black box to check whether the measurement outcome is truly a solution to the search problem. If it is, we’re done; if not, rerun the algorithm.

The result: The result is solution to problem with high probability
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

- Add noise simulation using Qiskit’s noise model

---

## 🧑‍💻 Author

Rahul Dubey – [@meowmeowrahul](https://github.com/meowmeowrahul)



