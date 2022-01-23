.model small
.stack 100h
.data 
    msg1 db 10,13,"Enter value of n:$",10,13
    msg2 db 10,13,"Enter value of r:$",10,13
    msg3 db 10,13,"The ncr is:$"
    nf db ?
    rf db ?
    nmr db ?
    nrf db ?

.code
start:mov ax,@data
    mov ds,ax

    lea dx,msg1
    mov ah,09h
    int 21h
    mov ah,01h
    int 21h
    sub al,30h
    mov bl,al

    lea dx,msg2
    mov ah,09h
    int 21h
    mov ah,01h
    int 21h
    sub al,30h
    mov cl,al

    mov al,bl
    sub al,cl
    mov nmr,al
    mov bh,01h
    mov ch,01h
    mov dh,01h
fact:
    mul bh,bl
    aam
    dec bl
    jnz fact
    add bh,30h
    mov nf,bh

fact1:
    mul ch,cl
    aam
    dec cl
    jnz fact1
    add ch,30h
    mov rf,ch

fact2:
    mul dh,nmr 
    aam
    dec nmr 
    jnz fact2
    add dh,30h
    mov nrf,dh

    mov al,rf
    mul al,nrf
    aam
    mov cl,al
    mov al,nf
    div al,cl

    lea dx,msg3
    mov ah,09h
    int 21h

    mov dl,al
    add dl,30h
    mov ah,02h
    int 21h
end start   