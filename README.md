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

**Plaintext:**

```
hello
```

**Key:**

```
Shift = +1
```

**Ciphertext:**

```
ifmmp
```

**Decrypted Text:**

```
hello
```

**Hash Output:**

```
99114
```

---

### Example 2

**Plaintext:**

```
ABC xyz
```

**Key:**

```
Shift = +1
```

**Ciphertext:**

```
BCD yza
```

**Decrypted Text:**

```
ABC xyz
```

**Hash Output:**

```
80285
```

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
