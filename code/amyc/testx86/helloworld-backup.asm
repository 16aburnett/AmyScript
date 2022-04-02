; ========================================================================

        global    _start

        section   .text
        extern printf

; ========================================================================
; Built-in library

; Exits the program with the given exit code 
; void exit(int exit_code)
; - exit_code : [rbp + 16]
; - uses external exit function from libc
exit__int: 
        push    rbp 
        mov     rbp, rsp 
        
        mov     rdi, qword [rbp + 16]
        call exit                          ; invoke operating system to exit

        pop     rbp 
        ret

; ========================================================================

; Prints an int to the screen
; Utilizes printf "%d"
; void print (int valueToPrint);
; valueToPrint : [rbp + 16]
print__int:
        push rbp 
        mov rbp, rsp

        mov rsi, qword [rbp + 16]
        mov rdi, __data__print__int__format
        mov eax, 0
        call printf 

        pop rbp
        ret 

        section .data
__data__print__int__format: db "%d", 0
        section .text

; Prints an int to the screen
; void print (int intToPrint);
; - intToPrint : [rbp + 16] (8-bytes)
; Usage:
;        push rdx
;        call print__int
;        pop
manual_print__int:
        push rbp
        mov rbp, rsp  
        sub rsp, 4                       ; num        [rbp -  4] [int 4-bytes]
        sub rsp, 4                       ; isNegative [rbp -  8] [int 4-bytes]
        sub rsp, 4                       ; digit      [rbp - 12] [int 4-bytes]
        sub rsp, 4                       ; char       [rbp - 16] [int 4-bytes]
        sub rsp, 4                       ; numDigits  [rbp - 20] [int 4-bytes]

        ; initialize local vars
        mov edx, dword [rbp + 16]
        mov dword [rbp - 4], edx
        mov dword [rbp - 8], 0
        mov dword [rbp - 12], 0
        mov dword [rbp - 16], 0
        mov dword [rbp - 20], 0

        ; account for negative numbers
        ; if num < 0:
        ;   isNegative = 1
        ;   num = -num
        cmp dword [rbp - 4], 0
        jge positive0
        mov dword [rbp - 8], 1
        neg dword [rbp - 4]
positive0: nop

        ; while num > 9:
while0:
        cmp dword [rbp - 4], 9 
        jle endwhile0 
        ;   digit = num % 10
        ;   num = num / 10
        mov edi, 10
        mov eax, dword [rbp - 4]
        cdq
        idiv edi
        mov dword [rbp - 12], edx  ; digit = num % 10
        mov dword [rbp - 4], eax   ; num = num / 10

        ;   char = digit + '0'
        mov eax, dword [rbp - 12]
        add eax, '0'
        ;   push char
        push rax
        ;   numDigits++ 
        inc dword [rbp - 20]
        ; repeat
        jmp while0
endwhile0: 

        ;   char = num + '0'
        mov eax, dword [rbp - 4]
        add eax, '0'
        ;   push char
        push rax
        ;   numDigits++ 
        inc dword [rbp - 20]
        
        ; if isNegative == 1:
        cmp dword [rbp - 8], 1
        jne positive1
        ;   push '-'
        push '-'
        ;   numDigits++
        inc dword [rbp - 20]

positive1: nop
        
        ; while numDigits > 0:
while1:
        cmp dword [rbp - 20], 0
        jle endwhile1
        ;   pop char
        pop rdx
        ;   printchar char
        push rdx   ; arg0
        call print__char 
        pop rdx    ; arg0
        ;   numDigits--
        dec dword [rbp - 20]
        ;   repeat 
        jmp while1
endwhile1:

        mov rsp, rbp                     ; pop local vars 
        pop rbp
        ret

; ========================================================================

; Prints a char to the screen
; Utilizes printf "%c"
; void print (char valueToPrint);
; valueToPrint : [rbp + 16]
print__char:
        push rbp 
        mov rbp, rsp

        mov rsi, qword [rbp + 16]
        mov rdi, __data__print__char__format
        mov eax, 0
        call printf 

        pop rbp
        ret 

        section .data
__data__print__char__format: db "%c", 0
        section .text

; void print(char c)
; c : [rbp + 16] (8-bytes)
manual_print__char:
        push rbp
        mov rbp, rsp  
        sub rsp, 1  ; make space for char
        mov dl, byte [rbp + 16]
        mov byte [rbp - 4], dl

        mov       rax, 1                 ; system call for write
        mov       rdi, 1                 ; file handle 1 is stdout
        mov       rsi, rbp               ; address of string to output
        sub       rsi, 4
        mov       rdx, 1                 ; number of bytes
        syscall                          ; invoke operating system to do the write

        mov rsp, rbp                     ; pop local vars 
        pop rbp
        ret

; ========================================================================

; Prints a float to the screen
; Utilizes printf "%f"
; void print (float valueToPrint);
; valueToPrint : [rbp + 16]
; Usage:
;       push qword [myfloat]
;       call print__float
;       pop rdx 
;       ...
; section   .data
; myfloat: dq 3.1415926535
print__float:
        push rbp 
        mov rbp, rsp

        movq xmm0, qword [rbp + 16]
        mov rdi, __data__print__float__format
        mov eax, 1
        call printf 

        pop rbp
        ret 

        section .data
__data__print__float__format: db "%f", 0
        section .text

; ========================================================================

_start: 
        push rbp 
        mov rbp, rsp
        sub rsp, 16

        ; print hello world
        ; mov       rax, 1                 ; system call for write
        ; mov       rdi, 1                 ; file handle 1 is stdout
        ; mov       rsi, message           ; address of string to output
        ; mov       rdx, 14                ; number of bytes
        ; syscall                          ; invoke operating system to do the write
        mov rsi, message
        mov rdi, format
        mov rax, 0
        call printf

        ; print -7
        push -7  ; arg0 
        call print__int
        pop  rdx ; arg0
        
        ; print newline 
        push 10  ; arg0 - newline
        call print__char
        pop  rdx ; arg0

        mov rsi, -7
        mov rdi, format2
        mov rax, 0
        call printf

        push qword [myfloat]
        call print__float
        pop rdx 

        ; print newline 
        push 10  ; arg0 - newline
        call print__char
        pop  rdx ; arg0

        ; end of program - exit
        push 0
        call exit__int

; ========================================================================

        section   .data

message: db "Hello, World!", 0
format:  db "%s", 10, 0
format2: db "%d", 10, 0

myfloat: dq 3.1415926535
