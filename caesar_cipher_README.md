# 🔐 Caesar Cipher Tool

A professional Python cryptography tool that encodes and decodes messages using the Caesar cipher — with brute force decryption, frequency analysis, challenge mode, and a history lesson built in.

---

## 📌 Features

- ✅ **Encode messages** with any shift key (1–25)
- ✅ **Decode messages** with a known key
- ✅ **Brute force** — try all 25 shifts automatically
- ✅ **Frequency analysis** — crack cipher using letter patterns
- ✅ **Auto-detection** — highlights likely correct decryptions
- ✅ **Challenge mode** — test your cracking skills
- ✅ **Shift detail table** — see how each letter was shifted
- ✅ **History lesson** — learn the origins of the Caesar cipher

---

## 🖥️ Demo

```
MAIN MENU
────────────────────────────
  [1] 🔒 Encode a message
  [2] 🔓 Decode a message
  [3] 💥 Brute force cipher
  [4] 📊 Frequency analysis
  [5] 🎯 Challenge mode
  [6] 📜 History of Caesar cipher
  [7] ❌ Exit

Enter message to encode: Hello World
Enter shift key (1-25): 3

Original  : Hello World
Shift Key : 3
Encoded   : Khoor Zruog
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- No external libraries needed

### Installation

```bash
git clone https://github.com/feliue/caesar-cipher-tool.git
cd caesar-cipher-tool
python caesar_cipher.py
```

---

## 🔬 How It Works

Each letter is shifted by a fixed number of positions in the alphabet:

```
Shift 3:  A→D  B→E  C→F ... X→A  Y→B  Z→C
Message:  H  E  L  L  O
Encoded:  K  H  O  O  R
```

Only letters are shifted — spaces, numbers, and symbols stay the same.

---

## 💥 Cracking Methods

### Brute Force
Tries all 25 possible shift keys and displays results. The tool automatically highlights likely English text.

### Frequency Analysis
In English, the letter **E** appears most frequently (~13%). By finding the most common letter in the ciphertext, we can estimate the shift key.

---

## 📁 Project Structure

```
caesar-cipher-tool/
│
├── caesar_cipher.py    # Main tool
└── README.md           # Documentation
```

---

## 📚 What I Learned

- Classical cryptography concepts
- Caesar cipher encoding/decoding logic
- Brute force attack techniques
- Frequency analysis for breaking ciphers
- Why modern encryption is stronger than Caesar cipher
- Python string manipulation and ASCII/ord/chr functions

---

## ⚠️ Note

This tool is for **educational purposes** — learning how classical cryptography works and why it's no longer secure. Modern systems use AES-256 encryption which has 2²⁵⁶ possible keys.

---

## 📜 License

MIT License — free to use and modify.

---

## 👤 Author

**Abdulhakeem Umar Toyin**
Cybersecurity Student
GitHub: [@feliue](https://github.com/feliue)
Email: abdulhakeemumar616@gmail.com
