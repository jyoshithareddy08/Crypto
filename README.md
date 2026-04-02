# August Cipher with Hash Function

## Overview

This project implements the **August Cipher** (a Caesar Cipher with shift = 1) along with a **custom hash function**.

It demonstrates:

* Encryption of plaintext
* Decryption back to original text
* Hash generation for data integrity

---

## Theory

### 1. August Cipher

The August Cipher is a substitution cipher where:

* Encryption: Each alphabet is shifted **forward by 1**
* Decryption: Each alphabet is shifted **backward by 1** 

#### Example:

* a → b
* z → a 

---

### 2. Hash Function

A **hash function** converts input text into a fixed-size value.

We use a **custom polynomial rolling hash**:

```
hash_value = (hash_value * 31 + ord(char)) % 100000
```

#### Why this approach?

* Efficient and fast
* Uses prime multiplier (31) to reduce collisions


---

## How to Run

### Step 1: Clone Repository

```bash
git clone <your-repo-link>
cd <repo-folder>
```

### Step 2: Run Program

```bash
python august_cipher.py
```

### Step 3: Provide Input

Enter any text when prompted.

---

## Code Components

* `encrypt(text)` → Performs encryption
* `decrypt(text)` → Performs decryption
* `simple_hash(text)` → Generates hash value
* Main program → Executes full flow

---

## Worked Examples

### Example 1

<img width="368" height="276" alt="image" src="https://github.com/user-attachments/assets/fa74d13c-4a67-41dd-a462-6538af97ec0f" />

### Example 2

<img width="387" height="251" alt="image" src="https://github.com/user-attachments/assets/226902ca-6abb-4d60-8ca9-b2b42686b0c5" />

---

## Test Script (Round Trip)

The program verifies correctness using:

```
Plaintext → Encrypt → Hash → Decrypt → Original
```

✔ Ensures:

* Encryption works correctly
* Decryption restores original text
* Hash remains consistent

---

## ⏱️ Time Complexity

* Encryption: O(n)
* Decryption: O(n)
* Hashing: O(n)

Where **n = length of input**

---


## Author

**Jyoshitha Reddy**
(23011102060)
