# Caesar Cipher Multi-Case Brute-Forcer

A robust Python 3 command-line utility designed to automate keyspace exploration for classical substitution ciphers. This script systematically loops through all 25 possible rotation keys to break Caesar-encrypted strings while cleanly preserving message structure and text formatting.

---

## Key Features

* **Interactive CLI Input:** Prompts the user dynamically at runtime for the ciphertext.
* **Full Case Preservation:** Separately processes uppercase (`ASCII 65-90`) and lowercase (`ASCII 97-122`) letters using safe modular arithmetic offsets.
* **Format-Safe Invariant Handling:** Skips numbers, spaces, punctuation, and special symbols entirely, passing them directly to the output string without modification.
* **Optimized Search Space:** Iterates exactly from shift 1 to 25, automatically filtering out the redundant Shift 0 (identity shift).

---

## How It Works

When a message is encrypted with a Caesar cipher, letters are shifted forward by adding a key value. To decrypt the message, this script reverses that process by **subtracting** the shift value to roll the characters backward to their original positions.

The core mathematical formula used for each character is:

$$new\_number = (alphabet\_code - shift) \pmod{26}$$

By pairing subtraction with Python's modulo operator (`% 26`), the script cleanly handles negative boundaries. For instance, shifting the letter `A` (index 0) backward by 1 automatically wraps it around to `Z` (index 25) without throwing out-of-bounds errors.

---

## Getting Started

### Prerequisites
* Python 3.x installed on your local environment.

### Usage

1. Open your terminal and navigate to your project directory:
   ```bash
   cd caesar-cipher-bruteforce
