def square_and_multiply_verbose(g, m, p):
    # ---------- Step 1: Binary expansion of m ----------
    binary_m = bin(m)[2:]
    r = len(binary_m) - 1

    print(f"--- تحلیل عدد توان ({m}) ---")
    print(f"نمایش باینری: {binary_m}")

    # پیدا کردن توان‌های ۲ که m را می‌سازند
    powers_of_2 = []
    for i, bit in enumerate(reversed(binary_m)):
        if bit == '1':
            powers_of_2.append(f"2^{i}")

    print(f"تجزیه توان: {m} = {' + '.join(powers_of_2)}")
    print("-" * 30)

    # ---------- Step 2 & 3 Combined for clarity ----------
    a = g % p
    result = 1

    # پیمایش از راست به چپ (از بیت کم‌ارزش به پرارزش)
    for i in range(r + 1):
        bit = binary_m[-(i + 1)]

        if bit == '1':
            old_result = result
            result = (result * a) % p
            print(f"Step {i}: بیت {i} برابر 1 است -> ضرب در g^(2^{i}) [یعنی {a}]")
            print(f"   حساب شد: ({old_result} * {a}) mod {p} = {result}")
        else:
            print(f"Step {i}: بیت {i} برابر 0 است -> جفت‌سازی انجام نشد.")

        # آماده‌سازی a برای مرحله بعد (مجذور کردن)
        a = (a ** 2) % p

    return result


# تست با مثال شما
g, m, p = 147, 2435, 100
final_answer = square_and_multiply_verbose(g, m, p)
print("-" * 30)
print(f"پاسخ نهایی: {final_answer}")