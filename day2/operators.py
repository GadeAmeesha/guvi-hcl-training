a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a % b)   # 1  (remainder)
print(a // b)  # 3  (floor division)
print(a ** b)  # 1000 (10 power 3)


x = 5     # simple assign
x += 3    # x = x + 3 → 8
x -= 2    # x = x - 2 → 6
x *= 2    # x = x * 2 → 12
x /= 4    # x = x / 4 → 3.0
x %= 2    # x = x % 2 → 1.0


a = 10
b = 5

print(a == b)   # False
print(a != b)   # True
print(a > b)    # True
print(a < b)    # False
print(a >= 10)  # True
print(a <= 5)   # False


x = 10
print(x > 5 and x < 15)   # True (both true)
print(x > 5 or x < 5)     # True (one is true)
print(not(x > 5))         # False (negation)


fruits = ["apple", "banana", "mango"]

print("apple" in fruits)       # True
print("orange" in fruits)      # False
print("grape" not in fruits)   # True


a = 5     # 0101
b = 3     # 0011

print(a & b)   # 1  (0001)
print(a | b)   # 7  (0111)
print(a ^ b)   # 6  (0110)
print(~a)      # -6 (invert)
print(a << 1)  # 10 (left shift)
print(a >> 1)  # 2  (right shift)
