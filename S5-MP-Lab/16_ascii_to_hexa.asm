; A S Nandanunni
; Reg No: 20219023
; CS - A
; ASCII to hexadecimal

LDA 0000h
SUI 30h
CPI 0Ah
JC SKIP
SUI 07h
SKIP: STA 0010h
HLT
