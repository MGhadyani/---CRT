import itertools

public_key = [400, 7, 14, 28, 70, 326, 59, 107]
ciphertext = [375, 108, 128, 49, 347, 583, 583, 108]

# brute-force possible mod p
for p in range(max(public_key)+1, 2000):
    for n in range(2, p):

        try:
            n_inv = pow(n, -1, p)
        except:
            continue

        d = [(n_inv * ei) % p for ei in public_key]

        # check super increasing
        if all(d[i] > sum(d[:i]) for i in range(1, len(d))):
            print("Private key found!")
            print("p =", p)
            print("n =", n)
            print("S' =", d)

            message = ""
            for c in ciphertext:
                y = (n_inv * c) % p
                m = [0]*8
                for i in range(7, -1, -1):
                    if y >= d[i]:
                        m[i] = 1
                        y -= d[i]
                message += "".join(map(str, m))

            print("Recovered message:", message)
            exit()
