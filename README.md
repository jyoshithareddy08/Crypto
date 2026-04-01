# August Cipher with Hash Function
---

##  Features

* Encryption using August Cipher (shift = +1)
* Decryption using reverse shift (shift = -1)
* Custom hash function (no external libraries used)
* Simple and beginner-friendly implementation

---

## How It Works

### 1. Encryption

Each alphabet character is shifted forward by 1:

* `a → b`
* `z → a`

### 2. Decryption

Each character is shifted backward by 1:

* `b → a`
* `a → z`

### 3. Hash Function

A custom hash is generated using:

* ASCII values of characters
* Multiplication and modulus operation
* hash_value = (hash_value * 31 + ord(char)) % 100000

---


Input:

```
hello
```

Output:

```
Encrypted Text : ifmmp
Decrypted Text : hello
Hash Value     : 99123
```


---


## Author

Jyoshitha Reddy
23011102060

---
