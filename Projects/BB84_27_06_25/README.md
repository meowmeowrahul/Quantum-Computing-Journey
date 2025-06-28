# 🌀 Classical Gates to Quantum Gates

This project demonstrates **BB84 Protocol**, a quantum circuit that demonstrates quantum encryption of data.

---

## 📌 Problem Statement

Secure key exchange over classical channels is vulnerable to eavesdropping and computational attacks.
This project implements the BB84 quantum key distribution protocol to enable provably secure communication using quantum principles.


## 🧠 Theory Overview

BB84 works on principle of **No cloning theorom** of quantum physics and that quantum states are very **fragile**.Any intrusion is detected easily

Steps:
1. Alice(sender) and Bob(reveiver) shares a entangled qubit beforehand.
2. Alice chooses a **random bais** and encodes her bits accordingly.
3. Bob also chooses a **random basis** and measures the bit accordingly
4. After they both match their basis and bits of unmatched bits are discarded.
5. If a eavesdropper was present then that will introduce a error ~25% in step 3 and they will know data is compromised.

The result: The result is data is shared securely
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
- Youtube
---

## 💡 Future Ideas

- Add noise simulation using Qiskit’s noise model

---

## 🧑‍💻 Author

Rahul Dubey – [@meowmeowrahul](https://github.com/meowmeowrahul)



