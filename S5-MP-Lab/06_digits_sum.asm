; A S Nandanunni
; Reg No: 20219023
; CS - A
; Sum of digits of a 8 Bit Number

LDA 2000h
MOV B,A
ANI 0Fh 
MOV C,A
MOV A,B
RLC
RLC
RLC
RLC
ANI 0Fh
ADD C
STA 2001h
HLT
