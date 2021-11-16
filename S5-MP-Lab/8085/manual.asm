MOV ; move content of the memory location pointed by HL register pair to register r
MVI ; move immediate
SUI ; subtract immediate
INR ; Increment
DCR ; Decrement
INX ; add 1 to the present content of the rp
LXI ; loads 16-bit address into the register pair
LDA ; loads contents in memory to Accumulator
STA ; store accumulator contents to memory
JNC ; jumb if not carry
DAD ; double add
LHLD ; loads HL pair using direct addressing memory loc
SHLD ; store HL pair using direct addressing memory loc
XCHG ; exchanges contents of HL pair DE pair
ANI ; anti digit -> extracts last digit
RLC ; rotate accumulator left without carry
RRC ; rotate accumulator right without carry
ORA ; OR accumalator
CPI ; value in accumulator compare with 10, if eql 0 flag is set
HLT ; Stop
