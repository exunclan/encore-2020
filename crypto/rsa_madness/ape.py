from pwn import *
from Crypto.Util.number import inverse
context.log_level = 'critical'

e = 65537


r = process('rsa.py')
r.recvuntil('\n')

c = int(r.recvuntil('\n').strip().split("- ")[1])

r.recvuntil('Exit\n')
r.sendline('2')
print(r.recvuntil('\n'))

r.close()

print(c)