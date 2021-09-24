; A S Nandanunni
; Reg No: 20219023
; CS - A
; Hexadecimal to BCD

LXI H, 0000h
MOV C, M
loop: STA 0002h
XRA A
LDA 0002h
ADI 01h
DAA
DCR C
JNZ loop
STA 0010h
HLT
