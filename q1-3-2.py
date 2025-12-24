# ---------- Key Generation ----------
d = [2, 5, 11]          # private super increasing set
p = 31
n = 7

# public key
e = [(n * di) % p for di in d]

# modular inverse of n mod p
n_inv = pow(n, -1, p)

# ---------- Encryption ----------
message = "101011011"
blocks = [message[i:i+3] for i in range(0, len(message), 3)]

cipher = []
for block in blocks:
    c = sum(int(block[i]) * e[i] for i in range(3))
    cipher.append(c)

print("Public key:", e)
print("Ciphertext:", cipher)

# ---------- Decryption ----------
decrypted = ""

for c in cipher:
    c_prime = (n_inv * c) % p
    y = c_prime
    m = [0, 0, 0]

    for i in range(2, -1, -1):
        if y >= d[i]:
            m[i] = 1
            y -= d[i]

    decrypted += "".join(map(str, m))

print("Decrypted message:", decrypted)
