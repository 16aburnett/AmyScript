; ### x86-64 generated from AmyScript Compiler ###########################
; ========================================================================

; ========================================================================
; ### LIBRARY CODE #######################################################
; ========================================================================

; AmyScript Built-in library
; Author: Amy Burnett
; ========================================================================

        global _start
        section   .text
        extern printf, exit, getline, stdin
        extern free, malloc
        extern atoi, atof

; ========================================================================

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

; Frees memory of the given pointer
; void free()
; - exit_code : [rbp + 16]
; - uses external exit function from libc
; free__void__: 
;         push    rbp 
;         mov     rbp, rsp 
        


;         pop     rbp 
;         ret

; ========================================================================
; Prints a given string to the screen
; void print (char[] stringToPrint);
; stringToPrint : [rbp + 16]
print__char__1:
        push rbp
        mov rbp, rsp

        mov     rsi, qword [rbp + 16]
        mov     rdi, __data__print__char__1__format
        mov     eax, 0
        call    printf 

        pop rbp
        ret

section .data
__data__print__char__1__format: db "%s", 0
section .text

; print__char__1:
;     // grab string
;     stackget __str 0
;     sizeof __size __str
;     // print each char
;     // init
;     assign __i 0
; __print__char__1__loop:
;     // cond
;     cmp __i __size
;     jge __print__char__1__endloop
;     // Body
;     print __str[__i]
;     // update
;     add __i __i 1
;     // repeat
;     jump __print__char__1__loop
; __print__char__1__endloop:
;     return 0

; ========================================================================

; Prints an int to the screen
; Utilizes printf "%d"
; void print (int valueToPrint);
; valueToPrint : [rbp + 16]
print__int:
        push    rbp 
        mov     rbp, rsp

        mov     rsi, qword [rbp + 16]
        mov     rdi, __data__print__int__format
        mov     eax, 0
        call    printf 

        pop     rbp
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
        push    rbp
        mov     rbp, rsp  
        sub     rsp, 4                   ; num        [rbp -  4] [int 4-bytes]
        sub     rsp, 4                   ; isNegative [rbp -  8] [int 4-bytes]
        sub     rsp, 4                   ; digit      [rbp - 12] [int 4-bytes]
        sub     rsp, 4                   ; char       [rbp - 16] [int 4-bytes]
        sub     rsp, 4                   ; numDigits  [rbp - 20] [int 4-bytes]

        ; initialize local vars
        mov     edx, dword [rbp + 16]
        mov     dword [rbp - 4], edx
        mov     dword [rbp - 8], 0
        mov     dword [rbp - 12], 0
        mov     dword [rbp - 16], 0
        mov     dword [rbp - 20], 0

        ; account for negative numbers
        ; if num < 0:
        ;   isNegative = 1
        ;   num = -num
        cmp     dword [rbp - 4], 0
        jge     positive0
        mov     dword [rbp - 8], 1
        neg     dword [rbp - 4]
positive0: nop

        ; while num > 9:
while0:
        cmp     dword [rbp - 4], 9 
        jle     endwhile0 
        ;   digit = num % 10
        ;   num = num / 10
        mov     edi, 10
        mov     eax, dword [rbp - 4]
        cdq     
        idiv    edi
        mov     dword [rbp - 12], edx  ; digit = num % 10
        mov     dword [rbp - 4], eax   ; num = num / 10

        ;   char = digit + '0'
        mov     eax, dword [rbp - 12]
        add     eax, '0'
        ;   push char
        push    rax
        ;   numDigits++ 
        inc     dword [rbp - 20]
        ; repeat
        jmp     while0
endwhile0: 

        ;   char = num + '0'
        mov     eax, dword [rbp - 4]
        add     eax, '0'
        ;   push char
        push    rax
        ;   numDigits++ 
        inc     dword [rbp - 20]
        
        ; if isNegative == 1:
        cmp     dword [rbp - 8], 1
        jne     positive1
        ;   push '-'
        push    '-'
        ;   numDigits++
        inc     dword [rbp - 20]

positive1: 
        nop
        
        ; while numDigits > 0:
while1:
        cmp     dword [rbp - 20], 0
        jle     endwhile1
        ;   pop char
        pop     rdx
        ;   printchar char
        push    rdx   ; arg0
        call    print__char 
        pop     rdx    ; arg0
        ;   numDigits--
        dec     dword [rbp - 20]
        ;   repeat 
        jmp     while1
endwhile1:

        mov     rsp, rbp                 ; pop local vars 
        pop     rbp
        ret

; ========================================================================

; Prints a char to the screen
; Utilizes printf "%c"
; void print (char valueToPrint);
; valueToPrint : [rbp + 16]
print__char:
        push    rbp 
        mov     rbp, rsp

        mov     rsi, qword [rbp + 16]
        mov     rdi, __data__print__char__format
        mov     eax, 0
        call    printf 

        pop     rbp
        ret 

section .data
__data__print__char__format: db "%c", 0
section .text

; void print(char c)
; c : [rbp + 16] (8-bytes)
manual_print__char:
        push    rbp
        mov     rbp, rsp  
        sub     rsp, 1                   ; make space for char
        mov     dl, byte [rbp + 16]
        mov     byte [rbp - 4], dl

        mov     rax, 1                   ; system call for write
        mov     rdi, 1                   ; file handle 1 is stdout
        mov     rsi, rbp                 ; address of string to output
        sub     rsi, 4
        mov     rdx, 1                   ; number of bytes
        syscall                          ; invoke operating system to do the write

        mov     rsp, rbp                 ; pop local vars 
        pop     rbp
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
        push    rbp 
        mov     rbp, rsp

        movq    xmm0, qword [rbp + 16]
        mov     rdi, __data__print__float__format
        mov     eax, 1
        call    printf 

        pop     rbp
        ret 

section .data
__data__print__float__format: db "%f", 0
section .text

; //========================================================================
; // Prints a given string to the screen with a newline at the end
; // void println (char[] stringToPrint);
; stringToPrint : [rbp + 16]
println__char__1:
        push rbp
        mov rbp, rsp

        mov     rsi, qword [rbp + 16]
        mov     rdi, __data__println__char__1__format
        mov     eax, 0
        call    printf 

        pop rbp
        ret

section .data
__data__println__char__1__format: db "%s", 10, 0
section .text

; println__char__1:
;     // grab string
;     stackget __str 0
;     sizeof __size __str
;     // print each char
;     // init
;     assign __i 0
; __println__char__1__loop:
;     // cond
;     cmp __i __size
;     jge __println__char__1__endloop
;     // Body
;     print __str[__i]
;     // update
;     add __i __i 1
;     // repeat
;     jump __println__char__1__loop
; __println__char__1__endloop:
;     println
;     return 0

; ========================================================================

; Prints an int to the screen with a newline
; Utilizes printf "%d"
; void println (int valueToPrint);
; valueToPrint : [rbp + 16]
println__int:
        push    rbp 
        mov     rbp, rsp

        mov     rsi, qword [rbp + 16]
        mov     rdi, __data__println__int__format
        mov     eax, 0
        call    printf 

        pop     rbp
        ret 

section .data
__data__println__int__format: db "%d", 10, 0
section .text

; ========================================================================
; // Prints a float to the screen with a newline
; // void println (float floatToPrint);
println__float:
        push    rbp 
        mov     rbp, rsp

        movq    xmm0, qword [rbp + 16]
        mov     rdi, __data__println__float__format
        mov     eax, 1
        call    printf 

        pop     rbp
        ret 

section .data
; g uses the shortest representation
; of f and e (scientific)
__data__println__float__format: db "%g", 10, 0
section .text

; //========================================================================
; // Prints a char to the screen with a newline
; // void println (char charToPrint);
println__char:
        push    rbp 
        mov     rbp, rsp

        mov     rsi, qword [rbp + 16]
        mov     rdi, __data__println__char__format
        mov     eax, 0
        call    printf 

        pop     rbp
        ret 

section .data
__data__println__char__format: db "%c", 10, 0
section .text

; //========================================================================
; // Prints an enum's integer value with a newline
; // void println (Enum e);
; println__Enum:
;     stackget __e 0
;     println __e
;     return 0

; //========================================================================
; // Prints a newline to the console
; // void println ();
println:
        push    rbp 
        mov     rbp, rsp

        mov     rdi, __data__println__format
        mov     eax, 0
        call    printf 

        pop     rbp
        ret 

section .data
__data__println__format: db 10, 0
section .text

; //========================================================================
; // grabs input from the console 
; this waits for a line if there isnt one
; // char[] input ();
input:
        ; function setup
        push    rbp
        mov     rbp, rsp
        sub     rsp, 16
        ; function body 
        mov     qword [rbp-8], 0    ; char* buffer = nullptr;
        mov     qword [rbp-16], 0   ; size_t buflen = 0;
        ; getline (&buffer, &buflen, stdin);
        mov     rdx, qword [stdin]  ; stdin
        lea     rcx, [rbp-16]
        lea     rax, [rbp-8]
        mov     rsi, rcx
        mov     rdi, rax
        call    getline
        ; return pointer to the line
        mov     rax, qword [rbp-8]

        add     rsp, 16
        pop     rbp
        ret 

; //========================================================================
; // returns default float value
; // float float ();
; float:
;     return 0.0

; //========================================================================
; // converts int to float
; // float intToFloat (int);
; intToFloat__int:
;     stackget val 0
;     itof res val
;     return res

; //========================================================================
; // parses a float from a given char[]
; // float stringToFloat (char[]);
; str : [rbp + 16]
stringToFloat__char__1:
        ; function setup
        push    rbp
        mov     rbp, rsp

        mov     rdi, qword [rbp+16]
        call    atof
        ; value stored in xmm0
        
        pop rbp
        ret

; //========================================================================
; // returns default int value
; // int int ();
; int:
;     return 0

; //========================================================================
; // returns default char value
; // char char ();
; char:
;     return '0'

; //========================================================================
; // converts float to int
; // int floatToInt (float);
; floatToInt__float:
;     stackget val 0
;     ftoi res val
;     return res

; //========================================================================
; // parses an int from a given char[]
; // int stringToInt (char[] str);
; str : [rbp + 16]
stringToInt__char__1:
        ; function setup
        push    rbp
        mov     rbp, rsp

        mov     rdi, qword [rbp+16]
        call    atoi
        ; value stored in rax

        pop rbp
        ret

; //========================================================================
; // parses an int from a given char
; // int charToInt (char);
; charToInt__char:
;     stackget val 0
;     ctoi res val
;     return res

; //========================================================================
; // converts int to string
; // char[] string (int);
; string__int:
;     stackget val 0
;     string res val
;     return res

; //========================================================================
; // converts float to string
; // char[] string (float);
; string__float:
;     stackget val 0
;     string res val
;     return res

; //========================================================================

; // returns default value for array and object (null)
; // null null ();
; null:
;     return __null

; ========================================================================

section .data
__builtin__neg: dq -1.0
section .text; ========================================================================
; ### COMPILED CODE ######################################################
; ========================================================================

_start:
main:
        ; Main Header:
        push rbp
        mov rbp, rsp
        sub rsp, 160
        ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
        ; x [rbp - 8]
        ; y [rbp - 16]
        ; c0 [rbp - 24]
        ; c1 [rbp - 32]
        ; c2 [rbp - 40]
        ; c3 [rbp - 48]
        ; string0 [rbp - 56]
        ; string1 [rbp - 64]
        ; x [rbp - 72]
        ; y [rbp - 80]
        ; z [rbp - 88]
        ; i [rbp - 96]
        ; i [rbp - 104]
        ; j [rbp - 112]
        ; x [rbp - 120]
        ; x [rbp - 128]
        ; y [rbp - 136]
        ; line [rbp - 144]
        ; x [rbp - 152]
        ; y [rbp - 160]

        ; Body
;------------------------------------------------------------------------
        ; Code Block
           ; Assignment - '='
              ; RHS
                 ; Mod - int, int
                    ; LHS
                       ; Multiplication - int, int
                          ; LHS
                             ; Addition - int, int
                                ; LHS
                                   ; Addition - int, int
                                      ; LHS
                                         ; Int Literal
                                            push -17
                                      ; RHS
                                         ; Multiplication - int, int
                                            ; LHS
                                               ; Int Literal
                                                  push 42
                                            ; RHS
                                               ; Addition - int, int
                                                  ; LHS
                                                     ; Int Literal
                                                        push 2
                                                  ; RHS
                                                     ; Int Literal
                                                        push 2
                                                  pop rdx ; rhs
                                                  pop rax ; lhs
                                                  add rax, rdx
                                                  push rax
                                            pop rdx
                                            pop rax
                                            imul rax, rdx
                                            push rax
                                      pop rdx ; rhs
                                      pop rax ; lhs
                                      add rax, rdx
                                      push rax
                                ; RHS
                                   ; Int Literal
                                      push 1
                                pop rdx ; rhs
                                pop rax ; lhs
                                add rax, rdx
                                push rax
                          ; RHS
                             ; Int Literal
                                push -1
                          pop rdx
                          pop rax
                          imul rax, rdx
                          push rax
                    ; RHS
                       ; Int Literal
                          push 3
                    pop rdx
                    pop rax
                    mov esi, edx
                    mov edx, 0
                    cdq
                    idiv esi
                    mov rax, rdx
                    push rax
              ; LHS
                 ; Variable Declaration - x
                    mov rax, qword [rbp - 8]  ; __main__block__0__x
              pop rdx ; __rhs
              mov qword [rbp - 8], rdx
              push rdx
           ; Statement results can be ignored
           pop rdx
           ; Assignment - '='
              ; RHS
                 ; Multiplication - int, int
                    ; LHS
                       ; Identifier - x
                          push qword [rbp - 8]
                    ; RHS
                       ; Int Literal
                          push 23
                    pop rdx
                    pop rax
                    imul rax, rdx
                    push rax
              ; LHS
                 ; Variable Declaration - y
                    mov rax, qword [rbp - 16]  ; __main__block__0__y
              pop rdx ; __rhs
              mov qword [rbp - 16], rdx
              push rdx
           ; Statement results can be ignored
           pop rdx
           ; Function Call - println(int) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Division - int, int
                       ; LHS
                          ; Identifier - y
                             push qword [rbp - 16]
                       ; RHS
                          ; Identifier - x
                             push qword [rbp - 8]
                       pop rdx
                       pop rax
                       mov esi, edx
                       mov edx, 0
                       cdq
                       idiv esi
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call println(int)
              call println__int
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
;------------------------------------------------------------------------
;------------------------------------------------------------------------
        ; Code Block
           ; Assignment - '='
              ; RHS
                 ; Char Literal
                    push 65 ; \101
              ; LHS
                 ; Variable Declaration - c0
                    mov rax, qword [rbp - 24]  ; __main__block__1__c0
              pop rdx ; __rhs
              mov qword [rbp - 24], rdx
              push rdx
           ; Statement results can be ignored
           pop rdx
           ; Assignment - '='
              ; RHS
                 ; Char Literal
                    push 'm'
              ; LHS
                 ; Variable Declaration - c1
                    mov rax, qword [rbp - 32]  ; __main__block__1__c1
              pop rdx ; __rhs
              mov qword [rbp - 32], rdx
              push rdx
           ; Statement results can be ignored
           pop rdx
           ; Assignment - '='
              ; RHS
                 ; Char Literal
                    push 'y'
              ; LHS
                 ; Variable Declaration - c2
                    mov rax, qword [rbp - 40]  ; __main__block__1__c2
              pop rdx ; __rhs
              mov qword [rbp - 40], rdx
              push rdx
           ; Statement results can be ignored
           pop rdx
           ; Assignment - '='
              ; RHS
                 ; Char Literal
                    push 10 ; \n
              ; LHS
                 ; Variable Declaration - c3
                    mov rax, qword [rbp - 48]  ; __main__block__1__c3
              pop rdx ; __rhs
              mov qword [rbp - 48], rdx
              push rdx
           ; Statement results can be ignored
           pop rdx
           ; Function Call - print(char) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Identifier - c0
                       push qword [rbp - 24]
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(char)
              call print__char
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - print(char) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Identifier - c1
                       push qword [rbp - 32]
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(char)
              call print__char
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - print(char) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Identifier - c2
                       push qword [rbp - 40]
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(char)
              call print__char
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - print(char) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Identifier - c3
                       push qword [rbp - 48]
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(char)
              call print__char
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
;------------------------------------------------------------------------
;------------------------------------------------------------------------
        ; Code Block
           ; Assignment - '='
              ; RHS
                 ; String Literal
                    ; "\110ello, "
                    mov rax, .str0
                    push rax
              ; LHS
                 ; Variable Declaration - string0
                    mov rax, qword [rbp - 56]  ; __main__block__2__string0
              pop rdx ; __rhs
              mov qword [rbp - 56], rdx
              push rdx
           ; Statement results can be ignored
           pop rdx
           ; Assignment - '='
              ; RHS
                 ; String Literal
                    ; "World!"
                    mov rax, .str1
                    push rax
              ; LHS
                 ; Variable Declaration - string1
                    mov rax, qword [rbp - 64]  ; __main__block__2__string1
              pop rdx ; __rhs
              mov qword [rbp - 64], rdx
              push rdx
           ; Statement results can be ignored
           pop rdx
           ; Function Call - print(char[]) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Identifier - string0
                       push qword [rbp - 56]
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(char[])
              call print__char__1
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - print(char[]) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Identifier - string1
                       push qword [rbp - 64]
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(char[])
              call print__char__1
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - print(char[]) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; String Literal
                       ; "\n"
                       mov rax, .str2
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(char[])
              call print__char__1
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
;------------------------------------------------------------------------
;------------------------------------------------------------------------
        ; Code Block
           ; Assignment - '='
              ; RHS
                 ; Int Literal
                    push 1
              ; LHS
                 ; Variable Declaration - x
                    mov rax, qword [rbp - 72]  ; __main__block__3__x
              pop rdx ; __rhs
              mov qword [rbp - 72], rdx
              push rdx
           ; Statement results can be ignored
           pop rdx
           ; Assignment - '='
              ; RHS
                 ; Bitwise Negation - int
                    ; RHS
                       ; Identifier - x
                          push qword [rbp - 72]
                    pop rdx
                    not rdx
                    mov rax, rdx
                    push rax
              ; LHS
                 ; Variable Declaration - y
                    mov rax, qword [rbp - 80]  ; __main__block__3__y
              pop rdx ; __rhs
              mov qword [rbp - 80], rdx
              push rdx
           ; Statement results can be ignored
           pop rdx
           ; Assignment - '='
              ; RHS
                 ; AND
                    ; Eval LHS
                       ; AND
                          ; Eval LHS
                             ; AND
                                ; Eval LHS
                                   ; Addition - int, int
                                      ; LHS
                                         ; Identifier - x
                                            push qword [rbp - 72]
                                      ; RHS
                                         ; Identifier - y
                                            push qword [rbp - 80]
                                      pop rdx ; rhs
                                      pop rax ; lhs
                                      add rax, rdx
                                      push rax
                                ; Check if we need to short-circuit
                                   pop rax ; __lhs
                                   test rax, rax
                                   je .AND_SHORT_CIRCUIT4
                                ; Eval RHS
                                   ; Pre-Increment - int
                                      ; RHS
                                         ; Identifier - y
                                            push qword [rbp - 80]
                                      pop rdx
                                      add qword [rbp - 80], 1
                                      mov rax, qword [rbp - 80]
                                      push rax
                                ; Check RHS
                                   pop rax ; __rhs
                                   test rax, rax
                                   je .AND_SHORT_CIRCUIT4
                                ; Success state
                                mov rax, 1 ; result = True
                                jmp .AND_END4
.AND_SHORT_CIRCUIT4:
                                mov rax, 0 ; result = False
.AND_END4:
                                movzx eax, al
                                push rax ; result
                          ; Check if we need to short-circuit
                             pop rax ; __lhs
                             test rax, rax
                             je .AND_SHORT_CIRCUIT5
                          ; Eval RHS
                             ; Pre-Decrement - int
                                ; RHS
                                   ; Identifier - x
                                      push qword [rbp - 72]
                                pop rdx
                                sub qword [rbp - 72], 1
                                mov rax, qword [rbp - 72]
                                push rax
                          ; Check RHS
                             pop rax ; __rhs
                             test rax, rax
                             je .AND_SHORT_CIRCUIT5
                          ; Success state
                          mov rax, 1 ; result = True
                          jmp .AND_END5
.AND_SHORT_CIRCUIT5:
                          mov rax, 0 ; result = False
.AND_END5:
                          movzx eax, al
                          push rax ; result
                    ; Check if we need to short-circuit
                       pop rax ; __lhs
                       test rax, rax
                       je .AND_SHORT_CIRCUIT6
                    ; Eval RHS
                       ; Negate - int
                          ; RHS
                             ; Post-Increment
                                mov rax, qword [rbp - 72]
                                add qword [rbp - 72], 1
                                push rax
                          pop rdx
                          cmp rdx, 0
                          sete al
                          movzx eax, al
                          push rax
                    ; Check RHS
                       pop rax ; __rhs
                       test rax, rax
                       je .AND_SHORT_CIRCUIT6
                    ; Success state
                    mov rax, 1 ; result = True
                    jmp .AND_END6
.AND_SHORT_CIRCUIT6:
                    mov rax, 0 ; result = False
.AND_END6:
                    movzx eax, al
                    push rax ; result
              ; LHS
                 ; Variable Declaration - z
                    mov rax, qword [rbp - 88]  ; __main__block__3__z
              pop rdx ; __rhs
              mov qword [rbp - 88], rdx
              push rdx
           ; Statement results can be ignored
           pop rdx
           ; Function Call - print(int) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Identifier - x
                       push qword [rbp - 72]
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(int)
              call print__int
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - print(char) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Char Literal
                       push ' '
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(char)
              call print__char
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - print(int) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Identifier - y
                       push qword [rbp - 80]
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(int)
              call print__int
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - print(char) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Char Literal
                       push ' '
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(char)
              call print__char
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - println(int) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Identifier - z
                       push qword [rbp - 88]
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call println(int)
              call println__int
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
   ;---------------------------------------------------------------------
           ; If-Statement
              ; Condition
                 ; Equal
                    ; LHS
                       ; Identifier - x
                          push qword [rbp - 72]
                    ; RHS
                       ; Int Literal
                          push 1
                    pop rdx ; rhs
                    pop rax ; lhs
                    cmp rax, rdx
                    sete al
                    movzx eax, al
                    push rax
                 pop rdx ; __cond
                 cmp rdx, 0 ; ensure condition is true
                 je .__elif__7x0 ; jump to first elif
              ; Body
         ;---------------------------------------------------------------
                 ; Code Block
                    ; Function Call - println(char) -> void
                       ; Make space for 1 arg(s)
                       sub rsp, 8
                       ; Arguments
                          ; Eval arg0
                             ; Char Literal
                                push 'A'
                          ; Move arg0's result to reverse order position on stack
                          pop rax
                          mov qword [rsp + 0], rax
                       ; Call println(char)
                       call println__char
                       ; Remove args
                       add rsp, 8
                       ; Push return value
                       push rax
                    ; Statement results can be ignored
                    pop rdx
         ;---------------------------------------------------------------
              jmp .__endif__7 ; jump to end of condition chain
      ;------------------------------------------------------------------
              ; Elif-Statement
.__elif__7x0:
                 ; Condition
                 ; Not Equal
                    ; LHS
                       ; Identifier - y
                          push qword [rbp - 80]
                    ; RHS
                       ; Int Literal
                          push -1
                    pop rdx ; rhs
                    pop rax ; lhs
                    cmp rax, rdx
                    setne al
                    movzx eax, al
                    push rax
                 pop rdx ; __cond
                 cmp rdx, 0 ; ensure condition is true
                 je .__else__7
                 ; Body
                 ; Function Call - println(char) -> void
                    ; Make space for 1 arg(s)
                    sub rsp, 8
                    ; Arguments
                       ; Eval arg0
                          ; Char Literal
                             push 'B'
                       ; Move arg0's result to reverse order position on stack
                       pop rax
                       mov qword [rsp + 0], rax
                    ; Call println(char)
                    call println__char
                    ; Remove args
                    add rsp, 8
                    ; Push return value
                    push rax
                 ; Statement results can be ignored
                 pop rdx
                 jmp .__endif__7
      ;------------------------------------------------------------------
      ;------------------------------------------------------------------
              ; Else-Statement
.__else__7:
              ; Function Call - println(char) -> void
                 ; Make space for 1 arg(s)
                 sub rsp, 8
                 ; Arguments
                    ; Eval arg0
                       ; Char Literal
                          push 'C'
                    ; Move arg0's result to reverse order position on stack
                    pop rax
                    mov qword [rsp + 0], rax
                 ; Call println(char)
                 call println__char
                 ; Remove args
                 add rsp, 8
                 ; Push return value
                 push rax
              ; Statement results can be ignored
              pop rdx
      ;------------------------------------------------------------------
              ; End of if
.__endif__7:
   ;---------------------------------------------------------------------
           ; Function Call - print(char[]) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; String Literal
                       ; "x: "
                       mov rax, .str3
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(char[])
              call print__char__1
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - println(int) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Identifier - x
                       push qword [rbp - 72]
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call println(int)
              call println__int
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - print(char[]) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; String Literal
                       ; " x <  0 -> "
                       mov rax, .str4
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(char[])
              call print__char__1
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - println(int) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Less Than
                       ; LHS
                          ; Identifier - x
                             push qword [rbp - 72]
                       ; RHS
                          ; Int Literal
                             push 0
                       pop rdx ; rhs
                       pop rax ; lhs
                       cmp rax, rdx
                       setl al
                       movzx eax, al
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call println(int)
              call println__int
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - print(char[]) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; String Literal
                       ; " x <= 0 -> "
                       mov rax, .str5
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(char[])
              call print__char__1
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - println(int) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Less Than or Equal to
                       ; LHS
                          ; Identifier - x
                             push qword [rbp - 72]
                       ; RHS
                          ; Int Literal
                             push 0
                       pop rdx ; rhs
                       pop rax ; lhs
                       cmp rax, rdx
                       setle al
                       movzx eax, al
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call println(int)
              call println__int
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - print(char[]) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; String Literal
                       ; " x == 0 -> "
                       mov rax, .str6
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(char[])
              call print__char__1
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - println(int) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Equal
                       ; LHS
                          ; Identifier - x
                             push qword [rbp - 72]
                       ; RHS
                          ; Int Literal
                             push 0
                       pop rdx ; rhs
                       pop rax ; lhs
                       cmp rax, rdx
                       sete al
                       movzx eax, al
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call println(int)
              call println__int
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - print(char[]) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; String Literal
                       ; " x >= 0 -> "
                       mov rax, .str7
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(char[])
              call print__char__1
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - println(int) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Greater Than or Equal to
                       ; LHS
                          ; Identifier - x
                             push qword [rbp - 72]
                       ; RHS
                          ; Int Literal
                             push 0
                       pop rdx ; rhs
                       pop rax ; lhs
                       cmp rax, rdx
                       setge al
                       movzx eax, al
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call println(int)
              call println__int
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - print(char[]) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; String Literal
                       ; " x >  0 -> "
                       mov rax, .str8
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(char[])
              call print__char__1
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - println(int) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Greater Than
                       ; LHS
                          ; Identifier - x
                             push qword [rbp - 72]
                       ; RHS
                          ; Int Literal
                             push 0
                       pop rdx ; rhs
                       pop rax ; lhs
                       cmp rax, rdx
                       setg al
                       movzx eax, al
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call println(int)
              call println__int
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
   ;---------------------------------------------------------------------
           ; If-Statement
              ; Condition
                 ; Less Than
                    ; LHS
                       ; Identifier - y
                          push qword [rbp - 80]
                    ; RHS
                       ; Int Literal
                          push 0
                    pop rdx ; rhs
                    pop rax ; lhs
                    cmp rax, rdx
                    setl al
                    movzx eax, al
                    push rax
                 pop rdx ; __cond
                 cmp rdx, 0 ; ensure condition is true
                 je .__elif__9x0 ; jump to first elif
              ; Body
                 ; Function Call - println(char[]) -> void
                    ; Make space for 1 arg(s)
                    sub rsp, 8
                    ; Arguments
                       ; Eval arg0
                          ; String Literal
                             ; "y < 0"
                             mov rax, .str9
                             push rax
                       ; Move arg0's result to reverse order position on stack
                       pop rax
                       mov qword [rsp + 0], rax
                    ; Call println(char[])
                    call println__char__1
                    ; Remove args
                    add rsp, 8
                    ; Push return value
                    push rax
                 ; Statement results can be ignored
                 pop rdx
              jmp .__endif__9 ; jump to end of condition chain
      ;------------------------------------------------------------------
              ; Elif-Statement
.__elif__9x0:
                 ; Condition
                 ; Equal
                    ; LHS
                       ; Identifier - y
                          push qword [rbp - 80]
                    ; RHS
                       ; Int Literal
                          push 0
                    pop rdx ; rhs
                    pop rax ; lhs
                    cmp rax, rdx
                    sete al
                    movzx eax, al
                    push rax
                 pop rdx ; __cond
                 cmp rdx, 0 ; ensure condition is true
                 je .__elif__9x1
                 ; Body
                 ; Function Call - println(char[]) -> void
                    ; Make space for 1 arg(s)
                    sub rsp, 8
                    ; Arguments
                       ; Eval arg0
                          ; String Literal
                             ; "y == 0"
                             mov rax, .str10
                             push rax
                       ; Move arg0's result to reverse order position on stack
                       pop rax
                       mov qword [rsp + 0], rax
                    ; Call println(char[])
                    call println__char__1
                    ; Remove args
                    add rsp, 8
                    ; Push return value
                    push rax
                 ; Statement results can be ignored
                 pop rdx
                 jmp .__endif__9
      ;------------------------------------------------------------------
      ;------------------------------------------------------------------
              ; Elif-Statement
.__elif__9x1:
                 ; Condition
                 ; Greater Than
                    ; LHS
                       ; Identifier - y
                          push qword [rbp - 80]
                    ; RHS
                       ; Int Literal
                          push 0
                    pop rdx ; rhs
                    pop rax ; lhs
                    cmp rax, rdx
                    setg al
                    movzx eax, al
                    push rax
                 pop rdx ; __cond
                 cmp rdx, 0 ; ensure condition is true
                 je .__endif__9
                 ; Body
                 ; Function Call - println(char[]) -> void
                    ; Make space for 1 arg(s)
                    sub rsp, 8
                    ; Arguments
                       ; Eval arg0
                          ; String Literal
                             ; "y > 0"
                             mov rax, .str11
                             push rax
                       ; Move arg0's result to reverse order position on stack
                       pop rax
                       mov qword [rsp + 0], rax
                    ; Call println(char[])
                    call println__char__1
                    ; Remove args
                    add rsp, 8
                    ; Push return value
                    push rax
                 ; Statement results can be ignored
                 pop rdx
                 jmp .__endif__9
      ;------------------------------------------------------------------
              ; End of if
.__endif__9:
   ;---------------------------------------------------------------------
   ;---------------------------------------------------------------------
           ; If-Statement
              ; Condition
                 ; Less Than or Equal to
                    ; LHS
                       ; Identifier - z
                          push qword [rbp - 88]
                    ; RHS
                       ; Int Literal
                          push 0
                    pop rdx ; rhs
                    pop rax ; lhs
                    cmp rax, rdx
                    setle al
                    movzx eax, al
                    push rax
                 pop rdx ; __cond
                 cmp rdx, 0 ; ensure condition is true
                 je .__elif__10x0 ; jump to first elif
              ; Body
         ;---------------------------------------------------------------
                 ; If-Statement
                    ; Condition
                       ; Less Than
                          ; LHS
                             ; Identifier - z
                                push qword [rbp - 88]
                          ; RHS
                             ; Int Literal
                                push 0
                          pop rdx ; rhs
                          pop rax ; lhs
                          cmp rax, rdx
                          setl al
                          movzx eax, al
                          push rax
                       pop rdx ; __cond
                       cmp rdx, 0 ; ensure condition is true
                       je .__else__11 ; jump to else
                    ; Body
                       ; Function Call - println(char[]) -> void
                          ; Make space for 1 arg(s)
                          sub rsp, 8
                          ; Arguments
                             ; Eval arg0
                                ; String Literal
                                   ; "z < 0"
                                   mov rax, .str12
                                   push rax
                             ; Move arg0's result to reverse order position on stack
                             pop rax
                             mov qword [rsp + 0], rax
                          ; Call println(char[])
                          call println__char__1
                          ; Remove args
                          add rsp, 8
                          ; Push return value
                          push rax
                       ; Statement results can be ignored
                       pop rdx
                    jmp .__endif__11 ; jump to end of condition chain
            ;------------------------------------------------------------
                    ; Else-Statement
.__else__11:
                    ; Function Call - println(char[]) -> void
                       ; Make space for 1 arg(s)
                       sub rsp, 8
                       ; Arguments
                          ; Eval arg0
                             ; String Literal
                                ; "z == 0"
                                mov rax, .str13
                                push rax
                          ; Move arg0's result to reverse order position on stack
                          pop rax
                          mov qword [rsp + 0], rax
                       ; Call println(char[])
                       call println__char__1
                       ; Remove args
                       add rsp, 8
                       ; Push return value
                       push rax
                    ; Statement results can be ignored
                    pop rdx
            ;------------------------------------------------------------
                    ; End of if
.__endif__11:
         ;---------------------------------------------------------------
              jmp .__endif__10 ; jump to end of condition chain
      ;------------------------------------------------------------------
              ; Elif-Statement
.__elif__10x0:
                 ; Condition
                 ; Greater Than
                    ; LHS
                       ; Identifier - z
                          push qword [rbp - 88]
                    ; RHS
                       ; Int Literal
                          push 0
                    pop rdx ; rhs
                    pop rax ; lhs
                    cmp rax, rdx
                    setg al
                    movzx eax, al
                    push rax
                 pop rdx ; __cond
                 cmp rdx, 0 ; ensure condition is true
                 je .__endif__10
                 ; Body
                 ; Function Call - println(char[]) -> void
                    ; Make space for 1 arg(s)
                    sub rsp, 8
                    ; Arguments
                       ; Eval arg0
                          ; String Literal
                             ; "z > 0"
                             mov rax, .str14
                             push rax
                       ; Move arg0's result to reverse order position on stack
                       pop rax
                       mov qword [rsp + 0], rax
                    ; Call println(char[])
                    call println__char__1
                    ; Remove args
                    add rsp, 8
                    ; Push return value
                    push rax
                 ; Statement results can be ignored
                 pop rdx
                 jmp .__endif__10
      ;------------------------------------------------------------------
              ; End of if
.__endif__10:
   ;---------------------------------------------------------------------
;------------------------------------------------------------------------
;------------------------------------------------------------------------
        ; Code Block
   ;---------------------------------------------------------------------
           ; For-Loop
           ; Init
              ; Assignment - '='
                 ; RHS
                    ; Int Literal
                       push 0
                 ; LHS
                    ; Variable Declaration - i
                       mov rax, qword [rbp - 96]  ; __main__block__12__for__13__i
                 pop rdx ; __rhs
                 mov qword [rbp - 96], rdx
                 push rdx
           jmp .__forcond__13
.__for__13:
              ; Update
                 ; Pre-Increment - int
                    ; RHS
                       ; Identifier - i
                          push qword [rbp - 96]
                    pop rdx
                    add qword [rbp - 96], 1
                    mov rax, qword [rbp - 96]
                    push rax
.__forcond__13:
              ; Condition
                 ; Less Than
                    ; LHS
                       ; Identifier - i
                          push qword [rbp - 96]
                    ; RHS
                       ; Int Literal
                          push 10
                    pop rdx ; rhs
                    pop rax ; lhs
                    cmp rax, rdx
                    setl al
                    movzx eax, al
                    push rax
                 pop rax ; __cond
                 cmp rax, 0 ; __cond
                 je .__endfor__13
              ; Body
         ;---------------------------------------------------------------
                 ; Code Block
                    ; Function Call - print(int) -> void
                       ; Make space for 1 arg(s)
                       sub rsp, 8
                       ; Arguments
                          ; Eval arg0
                             ; Identifier - i
                                push qword [rbp - 96]
                          ; Move arg0's result to reverse order position on stack
                          pop rax
                          mov qword [rsp + 0], rax
                       ; Call print(int)
                       call print__int
                       ; Remove args
                       add rsp, 8
                       ; Push return value
                       push rax
                    ; Statement results can be ignored
                    pop rdx
                    ; Function Call - print(char) -> void
                       ; Make space for 1 arg(s)
                       sub rsp, 8
                       ; Arguments
                          ; Eval arg0
                             ; Char Literal
                                push ' '
                          ; Move arg0's result to reverse order position on stack
                          pop rax
                          mov qword [rsp + 0], rax
                       ; Call print(char)
                       call print__char
                       ; Remove args
                       add rsp, 8
                       ; Push return value
                       push rax
                    ; Statement results can be ignored
                    pop rdx
         ;---------------------------------------------------------------
              ; Repeat
jmp .__for__13
              ; End of For
.__endfor__13:
   ;---------------------------------------------------------------------
           ; Function Call - println() -> void
              ; Make space for 0 arg(s)
              sub rsp, 0
              ; Arguments
              ; Call println()
              call println
              ; Remove args
              add rsp, 0
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
   ;---------------------------------------------------------------------
           ; For-Loop
           ; Init
              ; Assignment - '='
                 ; RHS
                    ; Int Literal
                       push 10
                 ; LHS
                    ; Variable Declaration - i
                       mov rax, qword [rbp - 104]  ; __main__block__12__for__15__i
                 pop rdx ; __rhs
                 mov qword [rbp - 104], rdx
                 push rdx
           jmp .__forcond__15
.__for__15:
              ; Update
                 ; Pre-Decrement - int
                    ; RHS
                       ; Identifier - i
                          push qword [rbp - 104]
                    pop rdx
                    sub qword [rbp - 104], 1
                    mov rax, qword [rbp - 104]
                    push rax
.__forcond__15:
              ; Condition
                 ; Greater Than
                    ; LHS
                       ; Identifier - i
                          push qword [rbp - 104]
                    ; RHS
                       ; Int Literal
                          push -5
                    pop rdx ; rhs
                    pop rax ; lhs
                    cmp rax, rdx
                    setg al
                    movzx eax, al
                    push rax
                 pop rax ; __cond
                 cmp rax, 0 ; __cond
                 je .__endfor__15
              ; Body
         ;---------------------------------------------------------------
                 ; Code Block
                    ; Function Call - print(int) -> void
                       ; Make space for 1 arg(s)
                       sub rsp, 8
                       ; Arguments
                          ; Eval arg0
                             ; Identifier - i
                                push qword [rbp - 104]
                          ; Move arg0's result to reverse order position on stack
                          pop rax
                          mov qword [rsp + 0], rax
                       ; Call print(int)
                       call print__int
                       ; Remove args
                       add rsp, 8
                       ; Push return value
                       push rax
                    ; Statement results can be ignored
                    pop rdx
                    ; Function Call - print(char) -> void
                       ; Make space for 1 arg(s)
                       sub rsp, 8
                       ; Arguments
                          ; Eval arg0
                             ; Char Literal
                                push ' '
                          ; Move arg0's result to reverse order position on stack
                          pop rax
                          mov qword [rsp + 0], rax
                       ; Call print(char)
                       call print__char
                       ; Remove args
                       add rsp, 8
                       ; Push return value
                       push rax
                    ; Statement results can be ignored
                    pop rdx
            ;------------------------------------------------------------
                    ; If-Statement
                       ; Condition
                          ; Less Than or Equal to
                             ; LHS
                                ; Identifier - i
                                   push qword [rbp - 104]
                             ; RHS
                                ; Int Literal
                                   push 0
                             pop rdx ; rhs
                             pop rax ; lhs
                             cmp rax, rdx
                             setle al
                             movzx eax, al
                             push rax
                          pop rdx ; __cond
                          cmp rdx, 0 ; ensure condition is true
                          je .__endif__17 ; jump to end
                       ; Body
                          ; Break out of __for__15
                          jmp .__endfor__15
                       jmp .__endif__17 ; jump to end of condition chain
                       ; End of if
.__endif__17:
            ;------------------------------------------------------------
         ;---------------------------------------------------------------
              ; Repeat
jmp .__for__15
              ; End of For
.__endfor__15:
   ;---------------------------------------------------------------------
           ; Function Call - println() -> void
              ; Make space for 0 arg(s)
              sub rsp, 0
              ; Arguments
              ; Call println()
              call println
              ; Remove args
              add rsp, 0
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Assignment - '='
              ; RHS
                 ; Int Literal
                    push 1
              ; LHS
                 ; Variable Declaration - j
                    mov rax, qword [rbp - 112]  ; __main__block__12__j
              pop rdx ; __rhs
              mov qword [rbp - 112], rdx
              push rdx
           ; Statement results can be ignored
           pop rdx
   ;---------------------------------------------------------------------
           ; While-Loop
.__while__18:
              ; Condition
                 ; Less Than
                    ; LHS
                       ; Identifier - j
                          push qword [rbp - 112]
                    ; RHS
                       ; Int Literal
                          push 100
                    pop rdx ; rhs
                    pop rax ; lhs
                    cmp rax, rdx
                    setl al
                    movzx eax, al
                    push rax
                 pop rax ; __cond
                 cmp rax, 0 ; __cond
                 je .__endwhile__18
              ; Body
         ;---------------------------------------------------------------
                 ; Code Block
                    ; Function Call - print(int) -> void
                       ; Make space for 1 arg(s)
                       sub rsp, 8
                       ; Arguments
                          ; Eval arg0
                             ; Multiplication - int, int
                                ; LHS
                                   ; Identifier - j
                                      push qword [rbp - 112]
                                ; RHS
                                   ; Identifier - j
                                      push qword [rbp - 112]
                                pop rdx
                                pop rax
                                imul rax, rdx
                                push rax
                          ; Move arg0's result to reverse order position on stack
                          pop rax
                          mov qword [rsp + 0], rax
                       ; Call print(int)
                       call print__int
                       ; Remove args
                       add rsp, 8
                       ; Push return value
                       push rax
                    ; Statement results can be ignored
                    pop rdx
                    ; Function Call - print(char) -> void
                       ; Make space for 1 arg(s)
                       sub rsp, 8
                       ; Arguments
                          ; Eval arg0
                             ; Char Literal
                                push ' '
                          ; Move arg0's result to reverse order position on stack
                          pop rax
                          mov qword [rsp + 0], rax
                       ; Call print(char)
                       call print__char
                       ; Remove args
                       add rsp, 8
                       ; Push return value
                       push rax
                    ; Statement results can be ignored
                    pop rdx
                    ; Pre-Increment - int
                       ; RHS
                          ; Identifier - j
                             push qword [rbp - 112]
                       pop rdx
                       add qword [rbp - 112], 1
                       mov rax, qword [rbp - 112]
                       push rax
                    ; Statement results can be ignored
                    pop rdx
            ;------------------------------------------------------------
                    ; If-Statement
                       ; Condition
                          ; Less Than
                             ; LHS
                                ; Identifier - j
                                   push qword [rbp - 112]
                             ; RHS
                                ; Int Literal
                                   push 10
                             pop rdx ; rhs
                             pop rax ; lhs
                             cmp rax, rdx
                             setl al
                             movzx eax, al
                             push rax
                          pop rdx ; __cond
                          cmp rdx, 0 ; ensure condition is true
                          je .__else__20 ; jump to else
                       ; Body
                          ; Continue in __while__18
                          jmp .__while__18
                       jmp .__endif__20 ; jump to end of condition chain
               ;---------------------------------------------------------
                       ; Else-Statement
.__else__20:
                       ; Break out of __while__18
                       jmp .__endwhile__18
               ;---------------------------------------------------------
                       ; End of if
.__endif__20:
            ;------------------------------------------------------------
                    ; Pre-Decrement - int
                       ; RHS
                          ; Identifier - j
                             push qword [rbp - 112]
                       pop rdx
                       sub qword [rbp - 112], 1
                       mov rax, qword [rbp - 112]
                       push rax
                    ; Statement results can be ignored
                    pop rdx
         ;---------------------------------------------------------------
              jmp .__while__18
              ; End of While
.__endwhile__18:
   ;---------------------------------------------------------------------
           ; Function Call - println() -> void
              ; Make space for 0 arg(s)
              sub rsp, 0
              ; Arguments
              ; Call println()
              call println
              ; Remove args
              add rsp, 0
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
;------------------------------------------------------------------------
;------------------------------------------------------------------------
        ; Code Block
   ; =====================================================================
           ; Function Declaration - mul2(int) -> int
           ; Skip over function declaration
           jmp .__end____main__block__21____mul2__int
.__main__block__21____mul2__int:
              ; Function Header:
                 ; Setup stack frame
                    push rbp
                    mov rbp, rsp
                 ; Parameters
                    ; Param: a [rbp + 16]
                 ; Local Variables - Each variable is currently 64-bit (sorry not sorry)

              ; Body
         ;---------------------------------------------------------------
                 ; Code Block
                    ; Return
                       ; Multiplication - int, int
                          ; LHS
                             ; Identifier - a
                                push qword [rbp - -16]
                          ; RHS
                             ; Int Literal
                                push 2
                          pop rdx
                          pop rax
                          imul rax, rdx
                          push rax
                       pop rax
                       ; Clean up stack and return
                       mov rsp, rbp ; remove local vars + unpopped pushes
                       pop rbp
                       ret
         ;---------------------------------------------------------------
              ret ; ensure function returns
.__end____main__block__21____mul2__int:
           ; End Function Declaration - mul2(int) -> int
   ; =====================================================================

           ; Function Call - println(int) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Function Call - mul2(int) -> int
                       ; Make space for 1 arg(s)
                       sub rsp, 8
                       ; Arguments
                          ; Eval arg0
                             ; Function Call - mul2(int) -> int
                                ; Make space for 1 arg(s)
                                sub rsp, 8
                                ; Arguments
                                   ; Eval arg0
                                      ; Function Call - mul2(int) -> int
                                         ; Make space for 1 arg(s)
                                         sub rsp, 8
                                         ; Arguments
                                            ; Eval arg0
                                               ; Int Literal
                                                  push 16
                                            ; Move arg0's result to reverse order position on stack
                                            pop rax
                                            mov qword [rsp + 0], rax
                                         ; Call mul2(int)
                                         call .__main__block__21____mul2__int
                                         ; Remove args
                                         add rsp, 8
                                         ; Push return value
                                         push rax
                                   ; Move arg0's result to reverse order position on stack
                                   pop rax
                                   mov qword [rsp + 0], rax
                                ; Call mul2(int)
                                call .__main__block__21____mul2__int
                                ; Remove args
                                add rsp, 8
                                ; Push return value
                                push rax
                          ; Move arg0's result to reverse order position on stack
                          pop rax
                          mov qword [rsp + 0], rax
                       ; Call mul2(int)
                       call .__main__block__21____mul2__int
                       ; Remove args
                       add rsp, 8
                       ; Push return value
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call println(int)
              call println__int
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
   ; =====================================================================
           ; Function Declaration - add(int, int, int) -> int
           ; Skip over function declaration
           jmp .__end____main__block__21____add__int__int__int
.__main__block__21____add__int__int__int:
              ; Function Header:
                 ; Setup stack frame
                    push rbp
                    mov rbp, rsp
                 ; Parameters
                    ; Param: a [rbp + 16]
                    ; Param: b [rbp + 24]
                    ; Param: c [rbp + 32]
                 ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
                    ; d [rbp - 8]

              ; Body
         ;---------------------------------------------------------------
                 ; Code Block
                    ; Assignment - '='
                       ; RHS
                          ; Addition - int, int
                             ; LHS
                                ; Addition - int, int
                                   ; LHS
                                      ; Identifier - a
                                         push qword [rbp - -16]
                                   ; RHS
                                      ; Identifier - b
                                         push qword [rbp - -24]
                                   pop rdx ; rhs
                                   pop rax ; lhs
                                   add rax, rdx
                                   push rax
                             ; RHS
                                ; Identifier - c
                                   push qword [rbp - -32]
                             pop rdx ; rhs
                             pop rax ; lhs
                             add rax, rdx
                             push rax
                       ; LHS
                          ; Variable Declaration - d
                             mov rax, qword [rbp - 8]  ; __main__block__21__add__block__23__d
                       pop rdx ; __rhs
                       mov qword [rbp - 8], rdx
                       push rdx
                    ; Statement results can be ignored
                    pop rdx
                    ; Return
                       ; Identifier - d
                          push qword [rbp - 8]
                       pop rax
                       ; Clean up stack and return
                       mov rsp, rbp ; remove local vars + unpopped pushes
                       pop rbp
                       ret
         ;---------------------------------------------------------------
              ret ; ensure function returns
.__end____main__block__21____add__int__int__int:
           ; End Function Declaration - add(int, int, int) -> int
   ; =====================================================================

           ; Function Call - print(char[]) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; String Literal
                       ; "add (7, 4, 21) -> "
                       mov rax, .str15
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(char[])
              call print__char__1
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - println(int) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Function Call - add(int, int, int) -> int
                       ; Make space for 3 arg(s)
                       sub rsp, 24
                       ; Arguments
                          ; Eval arg0
                             ; Int Literal
                                push 7
                          ; Move arg0's result to reverse order position on stack
                          pop rax
                          mov qword [rsp + 0], rax
                          ; Eval arg1
                             ; Int Literal
                                push 4
                          ; Move arg1's result to reverse order position on stack
                          pop rax
                          mov qword [rsp + 8], rax
                          ; Eval arg2
                             ; Int Literal
                                push 21
                          ; Move arg2's result to reverse order position on stack
                          pop rax
                          mov qword [rsp + 16], rax
                       ; Call add(int, int, int)
                       call .__main__block__21____add__int__int__int
                       ; Remove args
                       add rsp, 24
                       ; Push return value
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call println(int)
              call println__int
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Assignment - '='
              ; RHS
                 ; Int Literal
                    push 10
              ; LHS
                 ; Variable Declaration - x
                    mov rax, qword [rbp - 120]  ; __main__block__21__x
              pop rdx ; __rhs
              mov qword [rbp - 120], rdx
              push rdx
           ; Statement results can be ignored
           pop rdx
   ; =====================================================================
           ; Function Declaration - mulx(int) -> int
           ; Skip over function declaration
           jmp .__end____main__block__21____mulx__int
.__main__block__21____mulx__int:
              ; Function Header:
                 ; Setup stack frame
                    push rbp
                    mov rbp, rsp
                 ; Parameters
                    ; Param: a [rbp + 16]
                 ; Local Variables - Each variable is currently 64-bit (sorry not sorry)

              ; Body
         ;---------------------------------------------------------------
                 ; Code Block
                    ; Return
                       ; Multiplication - int, int
                          ; LHS
                             ; Identifier - a
                                push qword [rbp - -16]
                          ; RHS
                             ; Identifier - x
                                push qword [rbp - 120]
                          pop rdx
                          pop rax
                          imul rax, rdx
                          push rax
                       pop rax
                       ; Clean up stack and return
                       mov rsp, rbp ; remove local vars + unpopped pushes
                       pop rbp
                       ret
         ;---------------------------------------------------------------
              ret ; ensure function returns
.__end____main__block__21____mulx__int:
           ; End Function Declaration - mulx(int) -> int
   ; =====================================================================

           ; Function Call - print(char[]) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; String Literal
                       ; "x = "
                       mov rax, .str16
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(char[])
              call print__char__1
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - print(int) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Identifier - x
                       push qword [rbp - 120]
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(int)
              call print__int
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - print(char[]) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; String Literal
                       ; "; mulx (7) -> "
                       mov rax, .str17
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(char[])
              call print__char__1
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - println(int) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Function Call - mulx(int) -> int
                       ; Make space for 1 arg(s)
                       sub rsp, 8
                       ; Arguments
                          ; Eval arg0
                             ; Int Literal
                                push 7
                          ; Move arg0's result to reverse order position on stack
                          pop rax
                          mov qword [rsp + 0], rax
                       ; Call mulx(int)
                       call .__main__block__21____mulx__int
                       ; Remove args
                       add rsp, 8
                       ; Push return value
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call println(int)
              call println__int
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
;------------------------------------------------------------------------
        ; Function Call - println(char[]) -> void
           ; Make space for 1 arg(s)
           sub rsp, 8
           ; Arguments
              ; Eval arg0
                 ; String Literal
                    ; "=== Testing Conversions ==="
                    mov rax, .str18
                    push rax
              ; Move arg0's result to reverse order position on stack
              pop rax
              mov qword [rsp + 0], rax
           ; Call println(char[])
           call println__char__1
           ; Remove args
           add rsp, 8
           ; Push return value
           push rax
        ; Statement results can be ignored
        pop rdx
;------------------------------------------------------------------------
        ; Code Block
           ; Function Call - print(char[]) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; String Literal
                       ; "stringToInt (\"-47\") - 2 = "
                       mov rax, .str19
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(char[])
              call print__char__1
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - println(int) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Subtraction - int, int
                       ; LHS
                          ; Function Call - stringToInt(char[]) -> int
                             ; Make space for 1 arg(s)
                             sub rsp, 8
                             ; Arguments
                                ; Eval arg0
                                   ; String Literal
                                      ; "-47 "
                                      mov rax, .str20
                                      push rax
                                ; Move arg0's result to reverse order position on stack
                                pop rax
                                mov qword [rsp + 0], rax
                             ; Call stringToInt(char[])
                             call stringToInt__char__1
                             ; Remove args
                             add rsp, 8
                             ; Push return value
                             push rax
                       ; RHS
                          ; Int Literal
                             push 2
                       pop rdx ; rhs
                       pop rax ; lhs
                       sub rax, rdx
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call println(int)
              call println__int
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - print(char[]) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; String Literal
                       ; "stringToFloat (\"31415e-4\") = "
                       mov rax, .str21
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(char[])
              call print__char__1
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - println(float) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Function Call - stringToFloat(char[]) -> float
                       ; Make space for 1 arg(s)
                       sub rsp, 8
                       ; Arguments
                          ; Eval arg0
                             ; String Literal
                                ; "31415e-4"
                                mov rax, .str22
                                push rax
                          ; Move arg0's result to reverse order position on stack
                          pop rax
                          mov qword [rsp + 0], rax
                       ; Call stringToFloat(char[])
                       call stringToFloat__char__1
                       ; Remove args
                       add rsp, 8
                       ; Push return value
                       movq rax, xmm0
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call println(float)
              call println__float
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
;------------------------------------------------------------------------
        ; Function Call - println(char[]) -> void
           ; Make space for 1 arg(s)
           sub rsp, 8
           ; Arguments
              ; Eval arg0
                 ; String Literal
                    ; "=== Testing Integer Arithmetic ==="
                    mov rax, .str23
                    push rax
              ; Move arg0's result to reverse order position on stack
              pop rax
              mov qword [rsp + 0], rax
           ; Call println(char[])
           call println__char__1
           ; Remove args
           add rsp, 8
           ; Push return value
           push rax
        ; Statement results can be ignored
        pop rdx
;------------------------------------------------------------------------
        ; Code Block
           ; Function Call - print(char[]) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; String Literal
                       ; "-(7) = "
                       mov rax, .str24
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(char[])
              call print__char__1
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - println(int) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Negative - int
                       ; RHS
                          ; Int Literal
                             push 7
                       pop rdx
                       ; val = 0 - val
                       mov rax, 0
                       sub rax, rdx
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call println(int)
              call println__int
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - print(char[]) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; String Literal
                       ; "-(-(7)) = "
                       mov rax, .str25
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(char[])
              call print__char__1
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - println(int) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Negative - int
                       ; RHS
                          ; Negative - int
                             ; RHS
                                ; Int Literal
                                   push 7
                             pop rdx
                             ; val = 0 - val
                             mov rax, 0
                             sub rax, rdx
                             push rax
                       pop rdx
                       ; val = 0 - val
                       mov rax, 0
                       sub rax, rdx
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call println(int)
              call println__int
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - print(char[]) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; String Literal
                       ; "7 + 14 = "
                       mov rax, .str26
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(char[])
              call print__char__1
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - println(int) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Addition - int, int
                       ; LHS
                          ; Int Literal
                             push 7
                       ; RHS
                          ; Int Literal
                             push 14
                       pop rdx ; rhs
                       pop rax ; lhs
                       add rax, rdx
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call println(int)
              call println__int
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - print(char[]) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; String Literal
                       ; "-43 + 3 + -7 + 3 = "
                       mov rax, .str27
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(char[])
              call print__char__1
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - println(int) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Addition - int, int
                       ; LHS
                          ; Addition - int, int
                             ; LHS
                                ; Addition - int, int
                                   ; LHS
                                      ; Int Literal
                                         push -43
                                   ; RHS
                                      ; Int Literal
                                         push 3
                                   pop rdx ; rhs
                                   pop rax ; lhs
                                   add rax, rdx
                                   push rax
                             ; RHS
                                ; Int Literal
                                   push -7
                             pop rdx ; rhs
                             pop rax ; lhs
                             add rax, rdx
                             push rax
                       ; RHS
                          ; Int Literal
                             push 3
                       pop rdx ; rhs
                       pop rax ; lhs
                       add rax, rdx
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call println(int)
              call println__int
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - print(char[]) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; String Literal
                       ; " 7 -  14 = "
                       mov rax, .str28
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(char[])
              call print__char__1
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - println(int) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Subtraction - int, int
                       ; LHS
                          ; Int Literal
                             push 7
                       ; RHS
                          ; Int Literal
                             push 14
                       pop rdx ; rhs
                       pop rax ; lhs
                       sub rax, rdx
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call println(int)
              call println__int
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - print(char[]) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; String Literal
                       ; "-7 - -14 = "
                       mov rax, .str29
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(char[])
              call print__char__1
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - println(int) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Subtraction - int, int
                       ; LHS
                          ; Int Literal
                             push -7
                       ; RHS
                          ; Int Literal
                             push -14
                       pop rdx ; rhs
                       pop rax ; lhs
                       sub rax, rdx
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call println(int)
              call println__int
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - print(char[]) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; String Literal
                       ; " 7 - -14 = "
                       mov rax, .str30
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(char[])
              call print__char__1
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - println(int) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Subtraction - int, int
                       ; LHS
                          ; Int Literal
                             push 7
                       ; RHS
                          ; Int Literal
                             push -14
                       pop rdx ; rhs
                       pop rax ; lhs
                       sub rax, rdx
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call println(int)
              call println__int
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - print(char[]) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; String Literal
                       ; "-7 -  14 = "
                       mov rax, .str31
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(char[])
              call print__char__1
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - println(int) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Subtraction - int, int
                       ; LHS
                          ; Int Literal
                             push -7
                       ; RHS
                          ; Int Literal
                             push 14
                       pop rdx ; rhs
                       pop rax ; lhs
                       sub rax, rdx
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call println(int)
              call println__int
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - print(char[]) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; String Literal
                       ; "-7 -  14 - 21 + -14 + 7 = "
                       mov rax, .str32
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(char[])
              call print__char__1
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - println(int) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Addition - int, int
                       ; LHS
                          ; Subtraction - int, int
                             ; LHS
                                ; Subtraction - int, int
                                   ; LHS
                                      ; Subtraction - int, int
                                         ; LHS
                                            ; Int Literal
                                               push -7
                                         ; RHS
                                            ; Int Literal
                                               push 14
                                         pop rdx ; rhs
                                         pop rax ; lhs
                                         sub rax, rdx
                                         push rax
                                   ; RHS
                                      ; Int Literal
                                         push 21
                                   pop rdx ; rhs
                                   pop rax ; lhs
                                   sub rax, rdx
                                   push rax
                             ; RHS
                                ; Int Literal
                                   push -14
                             pop rdx ; rhs
                             pop rax ; lhs
                             sub rax, rdx
                             push rax
                       ; RHS
                          ; Int Literal
                             push 7
                       pop rdx ; rhs
                       pop rax ; lhs
                       add rax, rdx
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call println(int)
              call println__int
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - print(char[]) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; String Literal
                       ; " 7 *  14 = "
                       mov rax, .str33
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(char[])
              call print__char__1
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - println(int) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Multiplication - int, int
                       ; LHS
                          ; Int Literal
                             push 7
                       ; RHS
                          ; Int Literal
                             push 14
                       pop rdx
                       pop rax
                       imul rax, rdx
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call println(int)
              call println__int
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - print(char[]) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; String Literal
                       ; "-7 * -14 = "
                       mov rax, .str34
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(char[])
              call print__char__1
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - println(int) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Multiplication - int, int
                       ; LHS
                          ; Int Literal
                             push -7
                       ; RHS
                          ; Int Literal
                             push -14
                       pop rdx
                       pop rax
                       imul rax, rdx
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call println(int)
              call println__int
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - print(char[]) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; String Literal
                       ; " 7 * -14 = "
                       mov rax, .str35
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(char[])
              call print__char__1
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - println(int) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Multiplication - int, int
                       ; LHS
                          ; Int Literal
                             push 7
                       ; RHS
                          ; Int Literal
                             push -14
                       pop rdx
                       pop rax
                       imul rax, rdx
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call println(int)
              call println__int
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - print(char[]) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; String Literal
                       ; "-7 *  14 = "
                       mov rax, .str36
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(char[])
              call print__char__1
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - println(int) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Multiplication - int, int
                       ; LHS
                          ; Int Literal
                             push -7
                       ; RHS
                          ; Int Literal
                             push 14
                       pop rdx
                       pop rax
                       imul rax, rdx
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call println(int)
              call println__int
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - print(char[]) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; String Literal
                       ; "10 / 2 = "
                       mov rax, .str37
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(char[])
              call print__char__1
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - println(int) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Division - int, int
                       ; LHS
                          ; Int Literal
                             push 10
                       ; RHS
                          ; Int Literal
                             push 2
                       pop rdx
                       pop rax
                       mov esi, edx
                       mov edx, 0
                       cdq
                       idiv esi
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call println(int)
              call println__int
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - print(char[]) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; String Literal
                       ; "10 / 3 = "
                       mov rax, .str38
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(char[])
              call print__char__1
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - println(int) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Division - int, int
                       ; LHS
                          ; Int Literal
                             push 10
                       ; RHS
                          ; Int Literal
                             push 3
                       pop rdx
                       pop rax
                       mov esi, edx
                       mov edx, 0
                       cdq
                       idiv esi
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call println(int)
              call println__int
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - print(char[]) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; String Literal
                       ; " 1 / 2 = "
                       mov rax, .str39
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(char[])
              call print__char__1
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - println(int) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Division - int, int
                       ; LHS
                          ; Int Literal
                             push 1
                       ; RHS
                          ; Int Literal
                             push 2
                       pop rdx
                       pop rax
                       mov esi, edx
                       mov edx, 0
                       cdq
                       idiv esi
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call println(int)
              call println__int
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - print(char[]) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; String Literal
                       ; "10 % 3 = "
                       mov rax, .str40
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(char[])
              call print__char__1
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - println(int) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Mod - int, int
                       ; LHS
                          ; Int Literal
                             push 10
                       ; RHS
                          ; Int Literal
                             push 3
                       pop rdx
                       pop rax
                       mov esi, edx
                       mov edx, 0
                       cdq
                       idiv esi
                       mov rax, rdx
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call println(int)
              call println__int
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - print(char[]) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; String Literal
                       ; "10 % 2 = "
                       mov rax, .str41
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(char[])
              call print__char__1
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - println(int) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Mod - int, int
                       ; LHS
                          ; Int Literal
                             push 10
                       ; RHS
                          ; Int Literal
                             push 2
                       pop rdx
                       pop rax
                       mov esi, edx
                       mov edx, 0
                       cdq
                       idiv esi
                       mov rax, rdx
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call println(int)
              call println__int
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - print(char[]) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; String Literal
                       ; "4526 % 645 = "
                       mov rax, .str42
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(char[])
              call print__char__1
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - println(int) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Mod - int, int
                       ; LHS
                          ; Int Literal
                             push 4526
                       ; RHS
                          ; Int Literal
                             push 645
                       pop rdx
                       pop rax
                       mov esi, edx
                       mov edx, 0
                       cdq
                       idiv esi
                       mov rax, rdx
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call println(int)
              call println__int
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - print(char[]) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; String Literal
                       ; "-10 % 3 = "
                       mov rax, .str43
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(char[])
              call print__char__1
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - println(int) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Mod - int, int
                       ; LHS
                          ; Int Literal
                             push -10
                       ; RHS
                          ; Int Literal
                             push 3
                       pop rdx
                       pop rax
                       mov esi, edx
                       mov edx, 0
                       cdq
                       idiv esi
                       mov rax, rdx
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call println(int)
              call println__int
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - print(char[]) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; String Literal
                       ; " 1 % 2 = "
                       mov rax, .str44
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(char[])
              call print__char__1
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - println(int) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Mod - int, int
                       ; LHS
                          ; Int Literal
                             push 1
                       ; RHS
                          ; Int Literal
                             push 2
                       pop rdx
                       pop rax
                       mov esi, edx
                       mov edx, 0
                       cdq
                       idiv esi
                       mov rax, rdx
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call println(int)
              call println__int
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - print(char[]) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; String Literal
                       ; "((7 - 49) / 2 * -1 + 3 * 3) % (3 + 4) == 2 = "
                       mov rax, .str45
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(char[])
              call print__char__1
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - println(int) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Equal
                       ; LHS
                          ; Mod - int, int
                             ; LHS
                                ; Addition - int, int
                                   ; LHS
                                      ; Multiplication - int, int
                                         ; LHS
                                            ; Division - int, int
                                               ; LHS
                                                  ; Subtraction - int, int
                                                     ; LHS
                                                        ; Int Literal
                                                           push 7
                                                     ; RHS
                                                        ; Int Literal
                                                           push 49
                                                     pop rdx ; rhs
                                                     pop rax ; lhs
                                                     sub rax, rdx
                                                     push rax
                                               ; RHS
                                                  ; Int Literal
                                                     push 2
                                               pop rdx
                                               pop rax
                                               mov esi, edx
                                               mov edx, 0
                                               cdq
                                               idiv esi
                                               push rax
                                         ; RHS
                                            ; Int Literal
                                               push -1
                                         pop rdx
                                         pop rax
                                         imul rax, rdx
                                         push rax
                                   ; RHS
                                      ; Multiplication - int, int
                                         ; LHS
                                            ; Int Literal
                                               push 3
                                         ; RHS
                                            ; Int Literal
                                               push 3
                                         pop rdx
                                         pop rax
                                         imul rax, rdx
                                         push rax
                                   pop rdx ; rhs
                                   pop rax ; lhs
                                   add rax, rdx
                                   push rax
                             ; RHS
                                ; Addition - int, int
                                   ; LHS
                                      ; Int Literal
                                         push 3
                                   ; RHS
                                      ; Int Literal
                                         push 4
                                   pop rdx ; rhs
                                   pop rax ; lhs
                                   add rax, rdx
                                   push rax
                             pop rdx
                             pop rax
                             mov esi, edx
                             mov edx, 0
                             cdq
                             idiv esi
                             mov rax, rdx
                             push rax
                       ; RHS
                          ; Int Literal
                             push 2
                       pop rdx ; rhs
                       pop rax ; lhs
                       cmp rax, rdx
                       sete al
                       movzx eax, al
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call println(int)
              call println__int
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
;------------------------------------------------------------------------
        ; Function Call - println(char[]) -> void
           ; Make space for 1 arg(s)
           sub rsp, 8
           ; Arguments
              ; Eval arg0
                 ; String Literal
                    ; "=== Testing Floating Point Arithmetic ==="
                    mov rax, .str46
                    push rax
              ; Move arg0's result to reverse order position on stack
              pop rax
              mov qword [rsp + 0], rax
           ; Call println(char[])
           call println__char__1
           ; Remove args
           add rsp, 8
           ; Push return value
           push rax
        ; Statement results can be ignored
        pop rdx
;------------------------------------------------------------------------
        ; Code Block
           ; Assignment - '='
              ; RHS
                 ; Float Literal
                    mov rax, qword [.float0]
                    push rax
              ; LHS
                 ; Variable Declaration - x
                    mov rax, qword [rbp - 128]  ; __main__block__27__x
              pop rdx ; __rhs
              mov qword [rbp - 128], rdx
              push rdx
           ; Statement results can be ignored
           pop rdx
           ; Assignment - '='
              ; RHS
                 ; Float Literal
                    mov rax, qword [.float1]
                    push rax
              ; LHS
                 ; Variable Declaration - y
                    mov rax, qword [rbp - 136]  ; __main__block__27__y
              pop rdx ; __rhs
              mov qword [rbp - 136], rdx
              push rdx
           ; Statement results can be ignored
           pop rdx
           ; Function Call - print(char[]) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; String Literal
                       ; "3.14 + 0.0015 = "
                       mov rax, .str47
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(char[])
              call print__char__1
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - println(float) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Addition - float, float
                       ; LHS
                          ; Identifier - x
                             push qword [rbp - 128]
                       ; RHS
                          ; Identifier - y
                             push qword [rbp - 136]
                       pop rdx ; rhs
                       pop rax ; lhs
                       ; Move to big boi reg
                       movq xmm0, rax ; lhs
                       movq xmm1, rdx ; rhs
                       addsd xmm0, xmm1 ; perform addition
                       movq rax, xmm0
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call println(float)
              call println__float
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - print(char[]) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; String Literal
                       ; "64.0 + 8.123 + 0.63001 = "
                       mov rax, .str48
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(char[])
              call print__char__1
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - println(float) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Addition - float, float
                       ; LHS
                          ; Addition - float, float
                             ; LHS
                                ; Float Literal
                                   mov rax, qword [.float2]
                                   push rax
                             ; RHS
                                ; Float Literal
                                   mov rax, qword [.float3]
                                   push rax
                             pop rdx ; rhs
                             pop rax ; lhs
                             ; Move to big boi reg
                             movq xmm0, rax ; lhs
                             movq xmm1, rdx ; rhs
                             addsd xmm0, xmm1 ; perform addition
                             movq rax, xmm0
                             push rax
                       ; RHS
                          ; Float Literal
                             mov rax, qword [.float4]
                             push rax
                       pop rdx ; rhs
                       pop rax ; lhs
                       ; Move to big boi reg
                       movq xmm0, rax ; lhs
                       movq xmm1, rdx ; rhs
                       addsd xmm0, xmm1 ; perform addition
                       movq rax, xmm0
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call println(float)
              call println__float
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - print(char[]) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; String Literal
                       ; "-(3.14) = "
                       mov rax, .str49
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(char[])
              call print__char__1
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - println(float) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Negative - float
                       ; RHS
                          ; Float Literal
                             mov rax, qword [.float5]
                             push rax
                       pop rdx
                       ; Implemented as multiplying by -1.0
                       movsd xmm1, qword [__builtin__neg] ; -1.0
                       movq xmm0, rax
                       mulsd xmm0, xmm1 ; v = v * -1.0
                       movq rax, xmm0
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call println(float)
              call println__float
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - print(char[]) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; String Literal
                       ; "3.14159 - 1.234 = "
                       mov rax, .str50
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(char[])
              call print__char__1
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - println(float) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Subtraction - float, float
                       ; LHS
                          ; Float Literal
                             mov rax, qword [.float6]
                             push rax
                       ; RHS
                          ; Float Literal
                             mov rax, qword [.float7]
                             push rax
                       pop rdx ; rhs
                       pop rax ; lhs
                       ; Move to big boi reg
                       movq xmm0, rax ; lhs
                       movq xmm1, rdx ; rhs
                       subsd xmm0, xmm1 ; perform subtraction
                       movq rax, xmm0
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call println(float)
              call println__float
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - print(char[]) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; String Literal
                       ; "1.5943 * 2.0 = "
                       mov rax, .str51
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(char[])
              call print__char__1
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - println(float) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Multiplication - float, float
                       ; LHS
                          ; Float Literal
                             mov rax, qword [.float8]
                             push rax
                       ; RHS
                          ; Float Literal
                             mov rax, qword [.float9]
                             push rax
                       pop rdx
                       pop rax
                       ; Move to big boi reg
                       movq xmm0, rax ; lhs
                       movq xmm1, rdx ; rhs
                       mulsd xmm0, xmm1 ; perform multiplication
                       movq rax, xmm0
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call println(float)
              call println__float
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - print(char[]) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; String Literal
                       ; "0.000043 * 1.0e5 = "
                       mov rax, .str52
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(char[])
              call print__char__1
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - println(float) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Multiplication - float, float
                       ; LHS
                          ; Float Literal
                             mov rax, qword [.float10]
                             push rax
                       ; RHS
                          ; Float Literal
                             mov rax, qword [.float11]
                             push rax
                       pop rdx
                       pop rax
                       ; Move to big boi reg
                       movq xmm0, rax ; lhs
                       movq xmm1, rdx ; rhs
                       mulsd xmm0, xmm1 ; perform multiplication
                       movq rax, xmm0
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call println(float)
              call println__float
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - print(char[]) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; String Literal
                       ; "42.5 / 2.0 = "
                       mov rax, .str53
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(char[])
              call print__char__1
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - println(float) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Division - float, float
                       ; LHS
                          ; Float Literal
                             mov rax, qword [.float12]
                             push rax
                       ; RHS
                          ; Float Literal
                             mov rax, qword [.float13]
                             push rax
                       pop rdx
                       pop rax
                       ; Move to big boi reg
                       movq xmm0, rax ; lhs
                       movq xmm1, rdx ; rhs
                       divsd xmm0, xmm1 ; perform division
                       movq rax, xmm0
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call println(float)
              call println__float
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - print(char[]) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; String Literal
                       ; "12.5 / 0.125 = "
                       mov rax, .str54
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(char[])
              call print__char__1
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - println(float) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Division - float, float
                       ; LHS
                          ; Float Literal
                             mov rax, qword [.float14]
                             push rax
                       ; RHS
                          ; Float Literal
                             mov rax, qword [.float15]
                             push rax
                       pop rdx
                       pop rax
                       ; Move to big boi reg
                       movq xmm0, rax ; lhs
                       movq xmm1, rdx ; rhs
                       divsd xmm0, xmm1 ; perform division
                       movq rax, xmm0
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call println(float)
              call println__float
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
;------------------------------------------------------------------------
        ; Function Call - exit(int) -> void
           ; Make space for 1 arg(s)
           sub rsp, 8
           ; Arguments
              ; Eval arg0
                 ; Int Literal
                    push 0
              ; Move arg0's result to reverse order position on stack
              pop rax
              mov qword [rsp + 0], rax
           ; Call exit(int)
           call exit__int
           ; Remove args
           add rsp, 8
           ; Push return value
           push rax
        ; Statement results can be ignored
        pop rdx
;------------------------------------------------------------------------
        ; Code Block
           ; Function Call - print(char[]) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; String Literal
                       ; "Enter a phrase => "
                       mov rax, .str55
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(char[])
              call print__char__1
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Assignment - '='
              ; RHS
                 ; Function Call - input() -> char[]
                    ; Make space for 0 arg(s)
                    sub rsp, 0
                    ; Arguments
                    ; Call input()
                    call input
                    ; Remove args
                    add rsp, 0
                    ; Push return value
                    push rax
              ; LHS
                 ; Variable Declaration - line
                    mov rax, qword [rbp - 144]  ; __main__block__28__line
              pop rdx ; __rhs
              mov qword [rbp - 144], rdx
              push rdx
           ; Statement results can be ignored
           pop rdx
           ; Function Call - print(char[]) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Identifier - line
                       push qword [rbp - 144]
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(char[])
              call print__char__1
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - print(char[]) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; String Literal
                       ; "Enter integer ==> "
                       mov rax, .str56
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(char[])
              call print__char__1
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Assignment - '='
              ; RHS
                 ; Function Call - input() -> char[]
                    ; Make space for 0 arg(s)
                    sub rsp, 0
                    ; Arguments
                    ; Call input()
                    call input
                    ; Remove args
                    add rsp, 0
                    ; Push return value
                    push rax
              pop rdx ; __rhs
              mov qword [rbp - 144], rdx
              push rdx
           ; Statement results can be ignored
           pop rdx
           ; Assignment - '='
              ; RHS
                 ; Function Call - stringToInt(char[]) -> int
                    ; Make space for 1 arg(s)
                    sub rsp, 8
                    ; Arguments
                       ; Eval arg0
                          ; Identifier - line
                             push qword [rbp - 144]
                       ; Move arg0's result to reverse order position on stack
                       pop rax
                       mov qword [rsp + 0], rax
                    ; Call stringToInt(char[])
                    call stringToInt__char__1
                    ; Remove args
                    add rsp, 8
                    ; Push return value
                    push rax
              ; LHS
                 ; Variable Declaration - x
                    mov rax, qword [rbp - 152]  ; __main__block__28__x
              pop rdx ; __rhs
              mov qword [rbp - 152], rdx
              push rdx
           ; Statement results can be ignored
           pop rdx
           ; Function Call - print(char[]) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; String Literal
                       ; "x * x => "
                       mov rax, .str57
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(char[])
              call print__char__1
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - println(int) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Multiplication - int, int
                       ; LHS
                          ; Identifier - x
                             push qword [rbp - 152]
                       ; RHS
                          ; Identifier - x
                             push qword [rbp - 152]
                       pop rdx
                       pop rax
                       imul rax, rdx
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call println(int)
              call println__int
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - print(char[]) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; String Literal
                       ; "Enter float ==> "
                       mov rax, .str58
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(char[])
              call print__char__1
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Assignment - '='
              ; RHS
                 ; Function Call - input() -> char[]
                    ; Make space for 0 arg(s)
                    sub rsp, 0
                    ; Arguments
                    ; Call input()
                    call input
                    ; Remove args
                    add rsp, 0
                    ; Push return value
                    push rax
              pop rdx ; __rhs
              mov qword [rbp - 144], rdx
              push rdx
           ; Statement results can be ignored
           pop rdx
           ; Assignment - '='
              ; RHS
                 ; Function Call - stringToFloat(char[]) -> float
                    ; Make space for 1 arg(s)
                    sub rsp, 8
                    ; Arguments
                       ; Eval arg0
                          ; Identifier - line
                             push qword [rbp - 144]
                       ; Move arg0's result to reverse order position on stack
                       pop rax
                       mov qword [rsp + 0], rax
                    ; Call stringToFloat(char[])
                    call stringToFloat__char__1
                    ; Remove args
                    add rsp, 8
                    ; Push return value
                    movq rax, xmm0
                    push rax
              ; LHS
                 ; Variable Declaration - y
                    mov rax, qword [rbp - 160]  ; __main__block__28__y
              pop rdx ; __rhs
              mov qword [rbp - 160], rdx
              push rdx
           ; Statement results can be ignored
           pop rdx
           ; Function Call - print(char[]) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; String Literal
                       ; "y => "
                       mov rax, .str59
                       push rax
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call print(char[])
              call print__char__1
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
           ; Function Call - println(float) -> void
              ; Make space for 1 arg(s)
              sub rsp, 8
              ; Arguments
                 ; Eval arg0
                    ; Identifier - y
                       push qword [rbp - 160]
                 ; Move arg0's result to reverse order position on stack
                 pop rax
                 mov qword [rsp + 0], rax
              ; Call println(float)
              call println__float
              ; Remove args
              add rsp, 8
              ; Push return value
              push rax
           ; Statement results can be ignored
           pop rdx
;------------------------------------------------------------------------
        ; Function Call - exit(int) -> void
           ; Make space for 1 arg(s)
           sub rsp, 8
           ; Arguments
              ; Eval arg0
                 ; Int Literal
                    push 0
              ; Move arg0's result to reverse order position on stack
              pop rax
              mov qword [rsp + 0], rax
           ; Call exit(int)
           call exit__int
           ; Remove args
           add rsp, 8
           ; Push return value
           push rax
        ; Statement results can be ignored
        pop rdx
; ========================================================================
; ### END OF CODE ########################################################
; ========================================================================

        push 0
        call exit__int
; ========================================================================
; ### DATA SECTION #######################################################
; ========================================================================

        section .data
.str0: db 'H', 'e', 'l', 'l', 'o', ',', ' ', 0
.str1: db 'W', 'o', 'r', 'l', 'd', '!', 0
.str2: db 10, 0
.str3: db 'x', ':', ' ', 0
.str4: db ' ', 'x', ' ', '<', ' ', ' ', '0', ' ', '-', '>', ' ', 0
.str5: db ' ', 'x', ' ', '<', '=', ' ', '0', ' ', '-', '>', ' ', 0
.str6: db ' ', 'x', ' ', '=', '=', ' ', '0', ' ', '-', '>', ' ', 0
.str7: db ' ', 'x', ' ', '>', '=', ' ', '0', ' ', '-', '>', ' ', 0
.str8: db ' ', 'x', ' ', '>', ' ', ' ', '0', ' ', '-', '>', ' ', 0
.str9: db 'y', ' ', '<', ' ', '0', 0
.str10: db 'y', ' ', '=', '=', ' ', '0', 0
.str11: db 'y', ' ', '>', ' ', '0', 0
.str12: db 'z', ' ', '<', ' ', '0', 0
.str13: db 'z', ' ', '=', '=', ' ', '0', 0
.str14: db 'z', ' ', '>', ' ', '0', 0
.str15: db 'a', 'd', 'd', ' ', '(', '7', ',', ' ', '4', ',', ' ', '2', '1', ')', ' ', '-', '>', ' ', 0
.str16: db 'x', ' ', '=', ' ', 0
.str17: db ';', ' ', 'm', 'u', 'l', 'x', ' ', '(', '7', ')', ' ', '-', '>', ' ', 0
.str18: db '=', '=', '=', ' ', 'T', 'e', 's', 't', 'i', 'n', 'g', ' ', 'C', 'o', 'n', 'v', 'e', 'r', 's', 'i', 'o', 'n', 's', ' ', '=', '=', '=', 0
.str19: db 's', 't', 'r', 'i', 'n', 'g', 'T', 'o', 'I', 'n', 't', ' ', '(', '"', '-', '4', '7', '"', ')', ' ', '-', ' ', '2', ' ', '=', ' ', 0
.str20: db '-', '4', '7', ' ', 0
.str21: db 's', 't', 'r', 'i', 'n', 'g', 'T', 'o', 'F', 'l', 'o', 'a', 't', ' ', '(', '"', '3', '1', '4', '1', '5', 'e', '-', '4', '"', ')', ' ', '=', ' ', 0
.str22: db '3', '1', '4', '1', '5', 'e', '-', '4', 0
.str23: db '=', '=', '=', ' ', 'T', 'e', 's', 't', 'i', 'n', 'g', ' ', 'I', 'n', 't', 'e', 'g', 'e', 'r', ' ', 'A', 'r', 'i', 't', 'h', 'm', 'e', 't', 'i', 'c', ' ', '=', '=', '=', 0
.str24: db '-', '(', '7', ')', ' ', '=', ' ', 0
.str25: db '-', '(', '-', '(', '7', ')', ')', ' ', '=', ' ', 0
.str26: db '7', ' ', '+', ' ', '1', '4', ' ', '=', ' ', 0
.str27: db '-', '4', '3', ' ', '+', ' ', '3', ' ', '+', ' ', '-', '7', ' ', '+', ' ', '3', ' ', '=', ' ', 0
.str28: db ' ', '7', ' ', '-', ' ', ' ', '1', '4', ' ', '=', ' ', 0
.str29: db '-', '7', ' ', '-', ' ', '-', '1', '4', ' ', '=', ' ', 0
.str30: db ' ', '7', ' ', '-', ' ', '-', '1', '4', ' ', '=', ' ', 0
.str31: db '-', '7', ' ', '-', ' ', ' ', '1', '4', ' ', '=', ' ', 0
.str32: db '-', '7', ' ', '-', ' ', ' ', '1', '4', ' ', '-', ' ', '2', '1', ' ', '+', ' ', '-', '1', '4', ' ', '+', ' ', '7', ' ', '=', ' ', 0
.str33: db ' ', '7', ' ', '*', ' ', ' ', '1', '4', ' ', '=', ' ', 0
.str34: db '-', '7', ' ', '*', ' ', '-', '1', '4', ' ', '=', ' ', 0
.str35: db ' ', '7', ' ', '*', ' ', '-', '1', '4', ' ', '=', ' ', 0
.str36: db '-', '7', ' ', '*', ' ', ' ', '1', '4', ' ', '=', ' ', 0
.str37: db '1', '0', ' ', '/', ' ', '2', ' ', '=', ' ', 0
.str38: db '1', '0', ' ', '/', ' ', '3', ' ', '=', ' ', 0
.str39: db ' ', '1', ' ', '/', ' ', '2', ' ', '=', ' ', 0
.str40: db '1', '0', ' ', '%', ' ', '3', ' ', '=', ' ', 0
.str41: db '1', '0', ' ', '%', ' ', '2', ' ', '=', ' ', 0
.str42: db '4', '5', '2', '6', ' ', '%', ' ', '6', '4', '5', ' ', '=', ' ', 0
.str43: db '-', '1', '0', ' ', '%', ' ', '3', ' ', '=', ' ', 0
.str44: db ' ', '1', ' ', '%', ' ', '2', ' ', '=', ' ', 0
.str45: db '(', '(', '7', ' ', '-', ' ', '4', '9', ')', ' ', '/', ' ', '2', ' ', '*', ' ', '-', '1', ' ', '+', ' ', '3', ' ', '*', ' ', '3', ')', ' ', '%', ' ', '(', '3', ' ', '+', ' ', '4', ')', ' ', '=', '=', ' ', '2', ' ', '=', ' ', 0
.str46: db '=', '=', '=', ' ', 'T', 'e', 's', 't', 'i', 'n', 'g', ' ', 'F', 'l', 'o', 'a', 't', 'i', 'n', 'g', ' ', 'P', 'o', 'i', 'n', 't', ' ', 'A', 'r', 'i', 't', 'h', 'm', 'e', 't', 'i', 'c', ' ', '=', '=', '=', 0
.str47: db '3', '.', '1', '4', ' ', '+', ' ', '0', '.', '0', '0', '1', '5', ' ', '=', ' ', 0
.str48: db '6', '4', '.', '0', ' ', '+', ' ', '8', '.', '1', '2', '3', ' ', '+', ' ', '0', '.', '6', '3', '0', '0', '1', ' ', '=', ' ', 0
.str49: db '-', '(', '3', '.', '1', '4', ')', ' ', '=', ' ', 0
.str50: db '3', '.', '1', '4', '1', '5', '9', ' ', '-', ' ', '1', '.', '2', '3', '4', ' ', '=', ' ', 0
.str51: db '1', '.', '5', '9', '4', '3', ' ', '*', ' ', '2', '.', '0', ' ', '=', ' ', 0
.str52: db '0', '.', '0', '0', '0', '0', '4', '3', ' ', '*', ' ', '1', '.', '0', 'e', '5', ' ', '=', ' ', 0
.str53: db '4', '2', '.', '5', ' ', '/', ' ', '2', '.', '0', ' ', '=', ' ', 0
.str54: db '1', '2', '.', '5', ' ', '/', ' ', '0', '.', '1', '2', '5', ' ', '=', ' ', 0
.str55: db 'E', 'n', 't', 'e', 'r', ' ', 'a', ' ', 'p', 'h', 'r', 'a', 's', 'e', ' ', '=', '>', ' ', 0
.str56: db 'E', 'n', 't', 'e', 'r', ' ', 'i', 'n', 't', 'e', 'g', 'e', 'r', ' ', '=', '=', '>', ' ', 0
.str57: db 'x', ' ', '*', ' ', 'x', ' ', '=', '>', ' ', 0
.str58: db 'E', 'n', 't', 'e', 'r', ' ', 'f', 'l', 'o', 'a', 't', ' ', '=', '=', '>', ' ', 0
.str59: db 'y', ' ', '=', '>', ' ', 0
.float0: dq 3.14
.float1: dq 0.0015
.float2: dq 64.0
.float3: dq 8.123
.float4: dq 0.63001
.float5: dq 3.14
.float6: dq 3.14159
.float7: dq 1.234
.float8: dq 1.5943
.float9: dq 2.0
.float10: dq 4.3e-05
.float11: dq 100000.0
.float12: dq 42.5
.float13: dq 2.0
.float14: dq 12.5
.float15: dq 0.125
