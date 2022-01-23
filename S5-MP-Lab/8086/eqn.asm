.model small
.stack 100h

.data 
    msga db 10, 13, "Enter a: $"
    msgb db 10, 13, "Enter b: $"
    msgc db 10, 13, "Enter c: $"
    msgd db 10, 13, "Enter d: $"
    vala db ?
    valb db ?
    valc db ?
    vald db ?
    outMsg1 db 10, 13, "The value of ((a+b)(c+d)/(a+c)) is $"
    outMsg2 db " and reminder is $"

.code 
    mov ax, @data
    mov ds, ax

    ; input a
    lea dx, msga
    mov ah, 09h
    int 21h
    mov ah, 01h
    int 21h
    sub al, 30h
    mov vala, al

    ; input b
    lea dx, msgb
    mov ah, 09h
    int 21h
    mov ah, 01h
    int 21h
    sub al, 30h
    mov valb, al

    ; input c
    lea dx, msgc
    mov ah, 09h
    int 21h
    mov ah, 01h
    int 21h
    sub al, 30h
    mov valc, al

    ; input d
    lea dx, msgd
    mov ah, 09h
    int 21h
    mov ah, 01h
    int 21h
    sub al, 30h
    mov vald, al

    ; (a+b) in bl
    mov al, vala
    mov bl, valb
    add al, bl
    mov bl, al

    ; (c+d) in al
    mov al, vald
    mov cl, valc
    add al, cl

    ; (a+b)(c+d) in bl
    mul bl
    mov bl, al

    ; (a+c) in cl
    mov al, vala
    mov cl, valc
    add al, cl
    mov cl, al

    ; final result in bl, reminder in cl
    mov al, bl
    div cl
    mov bl, al
    mov cl, ah

    mov ax, 00
    mov dx, 00

    ; print output : I
    lea dx, outMsg1
    mov ah, 09h
    int 21h

    mov al, bl
    add al, 30h
    mov dl, al
    mov ah, 02h
    int 21h

    ; print output : II
    lea dx, outMsg2
    mov ah, 09h
    int 21h

    mov al, cl
    add al, 30h
    mov dl, al
    mov ah, 02h
    int 21h

    mov ah, 04ch
    int 21h

end
