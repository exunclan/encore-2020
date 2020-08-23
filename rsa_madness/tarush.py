from Crypto.Util.number import inverse, long_to_bytes

# Some ciphertext (from chall)
# c = 1
c = 328055279212128616898203809983039708787490384650725890748576927208883055381430000756624369636820903704775835777

# Prime numbers (find these from the chall, some program apparently?)
# p = 1
# q = 1
p = 19378812610208711050554891591368513578428260883630885898953907471497427917962675301070084754463193723428901453
q = 29

n = p * q

# Common e value: 65537, but might have to guess for rsa_madness
e = 0x10001

phi = (p - 1) * (q - 1)

d = inverse(e, phi)

m = pow(c, d, n)

print(long_to_bytes(m).decode('utf-8'))
