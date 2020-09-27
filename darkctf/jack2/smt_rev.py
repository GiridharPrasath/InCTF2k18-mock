from z3 import *

s = Solver()

htest = [0xcb9f59b7, 0x5b90f617, 0x20e59633, 0x102fd1da]

def SHR(v, n):
    return (v >> n) & (1 << (32-n))

def SHL(v, n):
    return (v << n) & (1 >> (32-n))

h1 = t1 = BitVec('h1', 32)
h2 = t2 = BitVec('h2', 32)
h3 = t3 = BitVec('h3', 32)
h4 = t4 = BitVec('h4', 32)

def funct(h):
    for i in range(2):
        uVar1 = h;
        iVar2 = SHR(h,3);
        h = uVar1 ^ h * 0x20 + iVar2;
        uVar1 = h;
        iVar2 = SHL(h,5);
        h = uVar1 ^ h * 0x80 + iVar2;
        h = h + (h >> 1 & 0xff);
    return h

h1 = funct(h1)
h2 = funct(h2)
h3 = funct(h3)
h4 = funct(h4)

s.add(h1 == htest[0])
s.add(h2 == htest[1])
s.add(h3 == htest[2])
s.add(h4 == htest[3])

print s.check()
s1  = str(hex(s.model()[t1].as_long()))[2:].decode("hex")[::-1]
s2  = str(hex(s.model()[t2].as_long()))[2:].decode("hex")[::-1]
s3  = str(hex(s.model()[t3].as_long()))[2:].decode("hex")[::-1]
s4  = str(hex(s.model()[t4].as_long()))[2:].decode("hex")[::-1]

print s1+s2+s3+s4
