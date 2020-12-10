# Bit Manipulation: Bit operations on integers (ints only)

a = 10  #1010
b = 4   #0100

# BITWISE OPERATORS

# & -> Bitwise AND
res = a & b
print(res) # 0000 = 0

# | -> Bitwise OR
res = a | b
print(res) # 1110 = 14 = 8+4+2+0

# ~ -> Bitwise NOT -> one's compliment -> negative and flip first bit
res = ~a
print(res) # 1010 -> -(1011) = -11
res = ~b
print(res) # 0100 -> -(0101) = -5

# ^ -> Bitwise XOR -> return 1 if bits are NOT the same, else return 0 if they ARE the same
res = a^b
print(res) # 1010 ^ 0100 -> 1110 = 14

# BITWISE SHIFTS

a = 10  #1010
b = 4   #0100

# >> -> Bitwise RIGHT SHIFT - shifts all 1 bits RIGHT by n spaces. Doesn't loop back. 
print(a>>1) # 1010 -> 0101 = 5
print(b>>1) # 0100 -> 0010 = 2

# << -> Bitwise LEFT SHIFT - same as right but goes left
print(b<<1) # 0100 -> 1000 = 8