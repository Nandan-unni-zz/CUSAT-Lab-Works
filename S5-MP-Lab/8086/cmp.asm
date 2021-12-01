.model small
.stack 100h

.data
    enterMsg1 db 10, 13, "Enter the first string: $"
    enterMsg2 db 10, 13, "Enter the second string: $"
    equalMsg db 10, 13, "The strings are equal $"
    unEqualMsg db 10, 13, "The strings are not equal $"
    str1 db ?
    str2 db ?
    len1 dw 0
    len2 dw 0

.code
    mov ax, @data
    mov ds, ax

    lea dx, enterMsg1
    mov ah, 09h
    int 21h

    lea si, str1
    enterString1:
        mov ah, 01h
        int 21h
        mov [si], al
        inc si
        inc len1
        cmp al, 13
        jne enterString1
    
    sub len1, 1

    lea dx, enterMsg2
    mov ah, 09h
    int 21h

    lea si, str2
    enterString2:
        mov ah, 01h
        int 21h
        mov [si], al
        inc si
        inc len2
        cmp al, 13
        jne enterString2
    
    sub len2, 1

    mov ax, len1
    mov bx, len2
    cmp ax, bx
    jne printUnequalMessage

    lea si, str1
    lea di, str2
    mov cx, len1
    compareStrings:
        mov al, [si]
        mov bl, [di]
        cmp al, bl
        jne printUnequalMessage
        inc si
        inc di
        dec cx
        jnz compareStrings
        lea dx, equalMsg
        mov ah, 09h
        int 21h
        jmp terminate

    printUnequalMessage:
        lea dx, unequalMsg
        mov ah, 09h
        int 21h
    
    terminate:
        mov ah, 04ch
        int 21h


end