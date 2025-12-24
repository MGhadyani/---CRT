# ===============================
# Chinese Remainder Theorem (CRT)
# مطابق الگوریتم ارائه‌شده در متن
# ===============================

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y


def mod_inverse(a, m):
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError("Inverse does not exist")
    return x % m


def chinese_remainder_theorem(a, n_list):
    """
    حل دستگاه هم‌نهشتی‌ها با الگوریتم سازنده CRT
    """

    # Step 1: n = n1 * n2 * ... * nk
    n = 1
    for ni in n_list:
        n *= ni

    # Step 2–4: محاسبه Σ ai * mi * yi
    x = 0
    for i in range(len(n_list)):
        ni = n_list[i]
        ai = a[i]

        mi = n // ni                 # m_i = n / n_i
        yi = mod_inverse(mi, ni)    # y_i = m_i^{-1} mod n_i

        x += ai * mi * yi

    # Step 5: جواب نهایی mod n
    return x % n


# ===============================
# تست با مثال کتاب
# ===============================
a = [5, 3, 10]          # a1, a2, a3
n_list = [7, 11, 13]    # n1, n2, n3

result = chinese_remainder_theorem(a, n_list)
print("x =", result)
