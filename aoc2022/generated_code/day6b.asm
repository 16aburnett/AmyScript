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
__builtin__exit__int: 
        push    rbp 
        mov     rbp, rsp 
        and     rsp, -16                 ; ensure stack is 16-byte aligned
        
        mov     rdi, qword [rbp + 16]
        call exit                          ; invoke operating system to exit

        mov     rsp, rbp                 ; restore stack pointer
        pop     rbp 
        ret

; ========================================================================

; Frees memory of the given pointer
; void free()
; - exit_code : [rbp + 16]
; - uses external exit function from libc
; __builtin__free__void__: 
;         push    rbp 
;         mov     rbp, rsp 
        


;         pop     rbp 
;         ret

; ========================================================================
; Prints a given string to the screen
; void print (char[] stringToPrint);
; stringToPrint : [rbp + 16]
; *requires null at the end of the string
__builtin__print__char__1:
        push rbp
        mov rbp, rsp
        and     rsp, -16                 ; ensure stack is 16-byte aligned

        mov     rsi, qword [rbp + 16]
        mov     rdi, __data__print__char__1__format
        mov     eax, 0
        call    printf 

        mov     rsp, rbp                 ; restore stack pointer
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
__builtin__print__int:
        push    rbp 
        mov     rbp, rsp
        and     rsp, -16                 ; ensure stack is 16-byte aligned

        mov     rsi, qword [rbp + 16]
        mov     rdi, __data__print__int__format
        mov     eax, 0
        call    printf 

        mov     rsp, rbp                 ; restore stack pointer
        pop     rbp
        ret 

section .data
__data__print__int__format: db "%ld", 0
section .text

; Prints an int to the screen
; void print (int intToPrint);
; - intToPrint : [rbp + 16] (8-bytes)
; Usage:
;        push rdx
;        call print__int
;        pop
; manual_print__int:
;         push    rbp
;         mov     rbp, rsp  
;         sub     rsp, 4                   ; num        [rbp -  4] [int 4-bytes]
;         sub     rsp, 4                   ; isNegative [rbp -  8] [int 4-bytes]
;         sub     rsp, 4                   ; digit      [rbp - 12] [int 4-bytes]
;         sub     rsp, 4                   ; char       [rbp - 16] [int 4-bytes]
;         sub     rsp, 4                   ; numDigits  [rbp - 20] [int 4-bytes]

;         ; initialize local vars
;         mov     edx, dword [rbp + 16]
;         mov     dword [rbp - 4], edx
;         mov     dword [rbp - 8], 0
;         mov     dword [rbp - 12], 0
;         mov     dword [rbp - 16], 0
;         mov     dword [rbp - 20], 0

;         ; account for negative numbers
;         ; if num < 0:
;         ;   isNegative = 1
;         ;   num = -num
;         cmp     dword [rbp - 4], 0
;         jge     positive0
;         mov     dword [rbp - 8], 1
;         neg     dword [rbp - 4]
; positive0: nop

;         ; while num > 9:
; while0:
;         cmp     dword [rbp - 4], 9 
;         jle     endwhile0 
;         ;   digit = num % 10
;         ;   num = num / 10
;         mov     edi, 10
;         mov     eax, dword [rbp - 4]
;         cdq     
;         idiv    edi
;         mov     dword [rbp - 12], edx  ; digit = num % 10
;         mov     dword [rbp - 4], eax   ; num = num / 10

;         ;   char = digit + '0'
;         mov     eax, dword [rbp - 12]
;         add     eax, '0'
;         ;   push char
;         push    rax
;         ;   numDigits++ 
;         inc     dword [rbp - 20]
;         ; repeat
;         jmp     while0
; endwhile0: 

;         ;   char = num + '0'
;         mov     eax, dword [rbp - 4]
;         add     eax, '0'
;         ;   push char
;         push    rax
;         ;   numDigits++ 
;         inc     dword [rbp - 20]
        
;         ; if isNegative == 1:
;         cmp     dword [rbp - 8], 1
;         jne     positive1
;         ;   push '-'
;         push    '-'
;         ;   numDigits++
;         inc     dword [rbp - 20]

; positive1: 
;         nop
        
;         ; while numDigits > 0:
; while1:
;         cmp     dword [rbp - 20], 0
;         jle     endwhile1
;         ;   pop char
;         pop     rdx
;         ;   printchar char
;         push    rdx   ; arg0
;         call    print__char 
;         pop     rdx    ; arg0
;         ;   numDigits--
;         dec     dword [rbp - 20]
;         ;   repeat 
;         jmp     while1
; endwhile1:

;         mov     rsp, rbp                 ; pop local vars 
;         pop     rbp
;         ret

; ========================================================================

; Prints a char to the screen
; Utilizes printf "%c"
; void print (char valueToPrint);
; valueToPrint : [rbp + 16]
__builtin__print__char:
        push    rbp 
        mov     rbp, rsp
        and     rsp, -16                 ; ensure stack is 16-byte aligned

        mov     rsi, qword [rbp + 16]
        mov     rdi, __data__print__char__format
        mov     eax, 0
        call    printf 

        mov     rsp, rbp                 ; restore stack pointer
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

        mov     rsp, rbp                 ; restore stack pointer
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
__builtin__print__float:
        push    rbp 
        mov     rbp, rsp
        and     rsp, -16                 ; ensure stack is 16-byte aligned

        movsd   xmm0, qword [rbp + 16]
        mov     rdi, __data__print__float__format
        mov     eax, 1
        call    printf 

        mov     rsp, rbp                 ; pop local vars 
        pop     rbp
        ret 

section .data
__data__print__float__format: db "%g", 0
section .text

; //========================================================================
; // Prints a given string to the screen with a newline at the end
; // void println (char[] stringToPrint);
; stringToPrint : [rbp + 16]
__builtin__println__char__1:
        push rbp
        mov rbp, rsp
        and     rsp, -16                 ; ensure stack is 16-byte aligned

        mov     rsi, qword [rbp + 16]
        mov     rdi, __data__println__char__1__format
        mov     eax, 0
        call    printf 

        mov     rsp, rbp                 ; pop local vars 
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
__builtin__println__int:
        push    rbp 
        mov     rbp, rsp
        and     rsp, -16                 ; ensure stack is 16-byte aligned

        mov     rsi, qword [rbp + 16]
        mov     rdi, __data__println__int__format
        mov     eax, 0
        call    printf

        mov     rsp, rbp                 ; pop local vars 
        pop     rbp
        ret 

section .data
__data__println__int__format: db "%ld", 10, 0
section .text

; ========================================================================
; // Prints a float to the screen with a newline
; // void println (float floatToPrint);
; valueToPrint : [rbp + 16]
__builtin__println__float:
        push    rbp 
        mov     rbp, rsp
        and     rsp, -16                 ; ensure stack is 16-byte aligned

        movsd   xmm0, qword [rbp + 16]
        mov     rdi, __data__println__float__format
        mov     eax, 1                   ; one floating point
        call    printf

        mov     rsp, rbp                 ; pop local vars 
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
__builtin__println__char:
        push    rbp 
        mov     rbp, rsp

        mov     rsi, qword [rbp + 16]
        mov     rdi, __data__println__char__format
        mov     eax, 0
        call    printf 

        mov     rsp, rbp                 ; pop local vars 
        pop     rbp
        ret 

section .data
__data__println__char__format: db "%c", 10, 0
section .text

; //========================================================================
; // Prints an enum's integer value with a newline
; // void println (Enum e);
; __builtin__println__Enum:
;     stackget __e 0
;     println __e
;     return 0

; //========================================================================
; // Prints a newline to the console
; // void println ();
__builtin__println:
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
__builtin__input:
        ; function setup
        push    rbp
        mov     rbp, rsp
        sub     rsp, 16
        ; function body 
        mov     qword [rbp-8], 0    ; char* buffer = nullptr;
        mov     qword [rbp-16], 0   ; size_t buflen = 0;
        ; num_chars = getline (&buffer, &buflen, stdin);
        mov     rdx, qword [stdin]  ; stdin
        lea     rcx, [rbp-16]
        lea     rax, [rbp-8]
        mov     rsi, rcx
        mov     rdi, rax
        call    getline
        ; check for eof
        cmp     rax, -1
        je      __builtin__input__eof
        ; return pointer to the line
        mov     rax, qword [rbp-8]
        jmp     __builtin__input__end

__builtin__input__eof:
        ; set rax to null
        mov     rax, 0

__builtin__input__end:
        add     rsp, 16
        pop     rbp
        ret 

; //========================================================================
; // returns default float value
; // float float ();
; __builtin__float:
;     return 0.0

; //========================================================================
; // converts int to float
; // float intToFloat (int value);
; value : [rbp + 16]
__builtin__intToFloat__int:
        ; function prologue
        push    rbp
        mov     rbp, rsp
        
        cvtsi2sd xmm0, qword [rbp + 16] ; xmm0 = float(value)

        ; function epilogue
        mov     rsp, rbp
        pop     rbp
        ret 

; //========================================================================
; // parses a float from a given char[]
; // float stringToFloat (char[]);
; str : [rbp + 16]
__builtin__stringToFloat__char__1:
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
; __builtin__int:
;     return 0

; //========================================================================
; // returns default char value
; // char char ();
; __builtin__char:
;     return '0'

; //========================================================================
; // converts float to int
; // int floatToInt (float);
; __builtin__floatToInt__float:
;     stackget val 0
;     ftoi res val
;     return res

; //========================================================================
; // parses an int from a given char[]
; // int stringToInt (char[] str);
; str : [rbp + 16]
__builtin__stringToInt__char__1:
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
__builtin__charToInt__char:
        ; function setup
        push    rbp
        mov     rbp, rsp

        mov     rax, qword [rbp+16]
        mov     rdx, '0'
        sub     rax, rdx

        pop rbp
        ret

; //========================================================================
; // converts int to string
; // char[] string (int);
; __builtin__string__int:
;     stackget val 0
;     string res val
;     return res

; //========================================================================
; // converts float to string
; // char[] string (float);
; __builtin__string__float:
;     stackget val 0
;     string res val
;     return res

; //========================================================================

; // returns default value for array and object (null)
; // null null ();
; __builtin__null:
;     return __null

; //========================================================================



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
         sub rsp, 48
         ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
         ; [rbp - 8] - char[] line (<unset-scope-name>)
         ; [rbp - 16] - int size (<unset-scope-name>)
         ; [rbp - 24] - int i (<unset-scope-name>)
         ; [rbp - 32] - int is_unique (<unset-scope-name>)
         ; [rbp - 40] - int j (<unset-scope-name>)
         ; [rbp - 48] - int k (<unset-scope-name>)

         ; Body
         ; Assignment - '='
            ; RHS
               ; Function Call - input() -> char[]
                  ; Make space for 0 arg(s)
                  sub rsp, 0
                  ; Arguments
                  ; Call input()
                  call __builtin__input
                  ; Remove args
                  add rsp, 0
                  ; Push return value
                  push rax
            ; LHS
               ; Variable Declaration - line
                  mov rax, qword [rbp - 8]  ; __main__line
            pop rdx ; rhs value
            mov qword [rbp - 8], rdx
            push rdx
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
            ; RHS
               ; Int Literal
                  mov rax, 0
                  push rax
            ; LHS
               ; Variable Declaration - size
                  mov rax, qword [rbp - 16]  ; __main__size
            pop rdx ; rhs value
            mov qword [rbp - 16], rdx
            push rdx
         ; Statement results can be ignored
         pop rdx
;------------------------------------------------------------------------
         ; While-Loop
.__while__0:
            ; Condition
               ; Not Equal
                  ; LHS
                     ; Subscript
                        ; LHS
                           ; Identifier - char[] line
                              push qword [rbp - 8]
                        ; OFFSET
                           ; Post-Increment
                              mov rax, qword [rbp - 16]
                              add qword [rbp - 16], 1
                              push rax
                        pop rdx ; __offset
                        pop rax ; __pointer
                        mov al, byte [rax + rdx] ; pointer + sizeof(data_t) * offset
                        movzx rax, al ; zero extend because we need to push 64bit to stack
                        push rax ; push char onto stack
                  ; RHS
                     ; Char Literal
                        push 0 ; \0
                  pop rdx ; rhs
                  pop rax ; lhs
                  cmp rax, rdx
                  setne al
                  movzx eax, al
                  push rax
               pop rax ; __cond
               cmp rax, 0 ; __cond
               je .__endwhile__0
            ; Body
            jmp .__while__0
            ; End of While
.__endwhile__0:
;------------------------------------------------------------------------
;------------------------------------------------------------------------
         ; For-Loop
         ; Init
            ; Assignment - '='
               ; RHS
                  ; Int Literal
                     mov rax, 0
                     push rax
               ; LHS
                  ; Variable Declaration - i
                     mov rax, qword [rbp - 24]  ; __main__for__1__i
               pop rdx ; rhs value
               mov qword [rbp - 24], rdx
               push rdx
            ; Loop init result can be discarded
            pop rax
         jmp .__forcond__1
.__for__1:
            ; Update
               ; Pre-Increment - int
                  ; RHS
                     ; Identifier - int i
                        push qword [rbp - 24]
                  pop rdx
                  add qword [rbp - 24], 1
                  mov rax, qword [rbp - 24]
                  push rax ; push result
               ; Loop update result can be discarded
               pop rax
.__forcond__1:
            ; Condition
               ; Less Than
                  ; LHS
                     ; Identifier - int i
                        push qword [rbp - 24]
                  ; RHS
                     ; Subtraction - int, int
                        ; LHS
                           ; Identifier - int size
                              push qword [rbp - 16]
                        ; RHS
                           ; Int Literal
                              mov rax, 3
                              push rax
                        pop rdx ; rhs
                        pop rax ; lhs
                        sub rax, rdx
                        push rax
                  pop rdx ; rhs
                  pop rax ; lhs
                  cmp rax, rdx
                  setl al
                  movzx eax, al
                  push rax
               pop rax ; __cond
               cmp rax, 0 ; __cond
               je .__endfor__1
            ; Body
      ;------------------------------------------------------------------
               ; Code Block
                  ; Assignment - '='
                     ; RHS
                        ; Int Literal
                           mov rax, 1
                           push rax
                     ; LHS
                        ; Variable Declaration - is_unique
                           mov rax, qword [rbp - 32]  ; __main__for__1__block__2__is_unique
                     pop rdx ; rhs value
                     mov qword [rbp - 32], rdx
                     push rdx
                  ; Statement results can be ignored
                  pop rdx
         ;---------------------------------------------------------------
                  ; For-Loop
                  ; Init
                     ; Assignment - '='
                        ; RHS
                           ; Identifier - int i
                              push qword [rbp - 24]
                        ; LHS
                           ; Variable Declaration - j
                              mov rax, qword [rbp - 40]  ; __main__for__1__block__2__for__3__j
                        pop rdx ; rhs value
                        mov qword [rbp - 40], rdx
                        push rdx
                     ; Loop init result can be discarded
                     pop rax
                  jmp .__forcond__3
.__for__3:
                     ; Update
                        ; Pre-Increment - int
                           ; RHS
                              ; Identifier - int j
                                 push qword [rbp - 40]
                           pop rdx
                           add qword [rbp - 40], 1
                           mov rax, qword [rbp - 40]
                           push rax ; push result
                        ; Loop update result can be discarded
                        pop rax
.__forcond__3:
                     ; Condition
                        ; Less Than
                           ; LHS
                              ; Identifier - int j
                                 push qword [rbp - 40]
                           ; RHS
                              ; Addition - int, int
                                 ; LHS
                                    ; Identifier - int i
                                       push qword [rbp - 24]
                                 ; RHS
                                    ; Int Literal
                                       mov rax, 14
                                       push rax
                                 pop rdx ; rhs
                                 pop rax ; lhs
                                 add rax, rdx
                                 push rax
                           pop rdx ; rhs
                           pop rax ; lhs
                           cmp rax, rdx
                           setl al
                           movzx eax, al
                           push rax
                        pop rax ; __cond
                        cmp rax, 0 ; __cond
                        je .__endfor__3
                     ; Body
               ;---------------------------------------------------------
                        ; Code Block
                  ;------------------------------------------------------
                           ; For-Loop
                           ; Init
                              ; Assignment - '='
                                 ; RHS
                                    ; Addition - int, int
                                       ; LHS
                                          ; Identifier - int j
                                             push qword [rbp - 40]
                                       ; RHS
                                          ; Int Literal
                                             mov rax, 1
                                             push rax
                                       pop rdx ; rhs
                                       pop rax ; lhs
                                       add rax, rdx
                                       push rax
                                 ; LHS
                                    ; Variable Declaration - k
                                       mov rax, qword [rbp - 48]  ; __main__for__1__block__2__for__3__block__4__for__5__k
                                 pop rdx ; rhs value
                                 mov qword [rbp - 48], rdx
                                 push rdx
                              ; Loop init result can be discarded
                              pop rax
                           jmp .__forcond__5
.__for__5:
                              ; Update
                                 ; Pre-Increment - int
                                    ; RHS
                                       ; Identifier - int k
                                          push qword [rbp - 48]
                                    pop rdx
                                    add qword [rbp - 48], 1
                                    mov rax, qword [rbp - 48]
                                    push rax ; push result
                                 ; Loop update result can be discarded
                                 pop rax
.__forcond__5:
                              ; Condition
                                 ; Less Than
                                    ; LHS
                                       ; Identifier - int k
                                          push qword [rbp - 48]
                                    ; RHS
                                       ; Addition - int, int
                                          ; LHS
                                             ; Identifier - int i
                                                push qword [rbp - 24]
                                          ; RHS
                                             ; Int Literal
                                                mov rax, 14
                                                push rax
                                          pop rdx ; rhs
                                          pop rax ; lhs
                                          add rax, rdx
                                          push rax
                                    pop rdx ; rhs
                                    pop rax ; lhs
                                    cmp rax, rdx
                                    setl al
                                    movzx eax, al
                                    push rax
                                 pop rax ; __cond
                                 cmp rax, 0 ; __cond
                                 je .__endfor__5
                              ; Body
                        ;------------------------------------------------
                                 ; Code Block
                           ;---------------------------------------------
                                    ; If-Statement
                                       ; Condition
                                          ; Equal
                                             ; LHS
                                                ; Subscript
                                                   ; LHS
                                                      ; Identifier - char[] line
                                                         push qword [rbp - 8]
                                                   ; OFFSET
                                                      ; Identifier - int j
                                                         push qword [rbp - 40]
                                                   pop rdx ; __offset
                                                   pop rax ; __pointer
                                                   mov al, byte [rax + rdx] ; pointer + sizeof(data_t) * offset
                                                   movzx rax, al ; zero extend because we need to push 64bit to stack
                                                   push rax ; push char onto stack
                                             ; RHS
                                                ; Subscript
                                                   ; LHS
                                                      ; Identifier - char[] line
                                                         push qword [rbp - 8]
                                                   ; OFFSET
                                                      ; Identifier - int k
                                                         push qword [rbp - 48]
                                                   pop rdx ; __offset
                                                   pop rax ; __pointer
                                                   mov al, byte [rax + rdx] ; pointer + sizeof(data_t) * offset
                                                   movzx rax, al ; zero extend because we need to push 64bit to stack
                                                   push rax ; push char onto stack
                                             pop rdx ; rhs
                                             pop rax ; lhs
                                             cmp rax, rdx
                                             sete al
                                             movzx eax, al
                                             push rax
                                          pop rdx ; __cond
                                          cmp rdx, 0 ; ensure condition is true
                                          je .__endif__7 ; jump to end
                                       ; Body
                                 ;---------------------------------------
                                          ; Code Block
                                             ; Assignment - '='
                                                ; RHS
                                                   ; Int Literal
                                                      mov rax, 0
                                                      push rax
                                                pop rdx ; rhs value
                                                mov qword [rbp - 32], rdx
                                                push rdx
                                             ; Statement results can be ignored
                                             pop rdx
                                             ; Break out of __for__5
                                             jmp .__endfor__5
                                 ;---------------------------------------
                                       jmp .__endif__7 ; jump to end of condition chain
                                       ; End of if
.__endif__7:
                           ;---------------------------------------------
                        ;------------------------------------------------
                              ; Repeat
jmp .__for__5
                              ; End of For
.__endfor__5:
                  ;------------------------------------------------------
                  ;------------------------------------------------------
                           ; If-Statement
                              ; Condition
                                 ; Negate - int
                                    ; RHS
                                       ; Identifier - int is_unique
                                          push qword [rbp - 32]
                                    pop rdx
                                    cmp rdx, 0
                                    sete al
                                    movzx eax, al
                                    push rax ; push result
                                 pop rdx ; __cond
                                 cmp rdx, 0 ; ensure condition is true
                                 je .__endif__9 ; jump to end
                              ; Body
                                 ; Break out of __for__3
                                 jmp .__endfor__3
                              jmp .__endif__9 ; jump to end of condition chain
                              ; End of if
.__endif__9:
                  ;------------------------------------------------------
               ;---------------------------------------------------------
                     ; Repeat
jmp .__for__3
                     ; End of For
.__endfor__3:
         ;---------------------------------------------------------------
         ;---------------------------------------------------------------
                  ; If-Statement
                     ; Condition
                        ; Identifier - int is_unique
                           push qword [rbp - 32]
                        pop rdx ; __cond
                        cmp rdx, 0 ; ensure condition is true
                        je .__endif__10 ; jump to end
                     ; Body
               ;---------------------------------------------------------
                        ; Code Block
                           ; Function Call - println(int) -> void
                              ; Make space for 1 arg(s)
                              sub rsp, 8
                              ; Arguments
                                 ; Eval arg0
                                    ; Addition - int, int
                                       ; LHS
                                          ; Identifier - int i
                                             push qword [rbp - 24]
                                       ; RHS
                                          ; Int Literal
                                             mov rax, 14
                                             push rax
                                       pop rdx ; rhs
                                       pop rax ; lhs
                                       add rax, rdx
                                       push rax
                                 ; Move arg0's result to reverse order position on stack
                                 pop rax
                                 mov qword [rsp + 0], rax
                              ; Call println(int)
                              call __builtin__println__int
                              ; Remove args
                              add rsp, 8
                              ; Push return value
                              push rax
                           ; Statement results can be ignored
                           pop rdx
                           ; Break out of __for__1
                           jmp .__endfor__1
               ;---------------------------------------------------------
                     jmp .__endif__10 ; jump to end of condition chain
                     ; End of if
.__endif__10:
         ;---------------------------------------------------------------
      ;------------------------------------------------------------------
            ; Repeat
jmp .__for__1
            ; End of For
.__endfor__1:
;------------------------------------------------------------------------
; ========================================================================
; ### END OF CODE ########################################################
; ========================================================================

         push 0
         call __builtin__exit__int
; ========================================================================
; ### DATA SECTION #######################################################
; ========================================================================

         section .data
.floatNegOne: dq -1.0
.floatZero: dq 0.0
.floatOne: dq 1.0
