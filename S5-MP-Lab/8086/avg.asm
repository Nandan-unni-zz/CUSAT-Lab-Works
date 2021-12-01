.model small
.stack 100h

.data
    count db 13, 10, "Enter the no of number: $"
    numbers db 13, 10, "Enter the numbers: $"
    numberInput db 13, 10, "Enter the number: $"
    result db 13, 10, "The average of the numbers is $"
    sum db ?
    avg db ?

.code
    mov ax, @data
    mov ds, ax

    ; printing input statement
    lea dx, count
    mov ah, 09h
    int 21h
    
    ; input no of numbers
    mov ah, 01h
    int 21h
    sub al, 30h

    ; initializing flags
    mov bl, al
    mov cl, 00
    mov al, 00
    mov sum, al


    lea dx, numbers

    mov ah, 09h
    int 21h
    inputNumbers:
        lea dx, numberInput

        mov ah, 09h
        int 21h
        
        mov ah, 01h
        int 21h
        ; converting to int
        sub al, 30h
        ; adding input num to total
        add al, sum
        mov sum, al
        ; incrementing count
        add cl, 01
        ; comparing if all numbers are taken
        cmp bl, cl
        jne inputNumbers
    
    findAvg:
        ; print output msg
        lea dx, result
        mov ah, 09h
        int 21h

        mov ax, 00 ; nthinnooo veendi

        mov al, sum
        div bl

        add ax, 3030H ; nthinnooo veendi
        mov dx, ax ; nthinnooo veendi
        
        mov ah, 02h
        int 21h

    terminate:
        mov ah, 04ch
        int 21h
end
