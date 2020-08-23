from pwn import *

p = process('./vuln')

print(p.recvline())
print(p.recvline())
print(p.recvline())

p.close()