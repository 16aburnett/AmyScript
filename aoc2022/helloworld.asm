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
print__int:
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
print__char:
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
print__float:
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
println__char__1:
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
println__int:
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
println__float:
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
println__char:
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
; // float intToFloat (int value);
; value : [rbp + 16]
intToFloat__int:
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
         sub rsp, 144
         ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
         ; [rbp - 8] - char[] line (<unset-scope-name>)
         ; [rbp - 16] - char ROCK0 (<unset-scope-name>)
         ; [rbp - 24] - char PAPER0 (<unset-scope-name>)
         ; [rbp - 32] - char SCISSORS0 (<unset-scope-name>)
         ; [rbp - 40] - char LOSE (<unset-scope-name>)
         ; [rbp - 48] - char DRAW (<unset-scope-name>)
         ; [rbp - 56] - char WIN (<unset-scope-name>)
         ; [rbp - 64] - int SCORE_ROCK (<unset-scope-name>)
         ; [rbp - 72] - int SCORE_PAPER (<unset-scope-name>)
         ; [rbp - 80] - int SCORE_SCISSORS (<unset-scope-name>)
         ; [rbp - 88] - int SCORE_LOSE (<unset-scope-name>)
         ; [rbp - 96] - int SCORE_DRAW (<unset-scope-name>)
         ; [rbp - 104] - int SCORE_WIN (<unset-scope-name>)
         ; [rbp - 112] - int totalScore (<unset-scope-name>)
         ; [rbp - 120] - char lhs (<unset-scope-name>)
         ; [rbp - 128] - char rhs (<unset-scope-name>)
         ; [rbp - 136] - int localScore (<unset-scope-name>)

         ; Body
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
                  mov rax, qword [rbp - 8]  ; __main__line
            pop rdx ; rhs value
            mov qword [rbp - 8], rdx
            push rdx
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
            ; RHS
               ; Char Literal
                  push 'A'
            ; LHS
               ; Variable Declaration - ROCK0
                  mov rax, qword [rbp - 16]  ; __main__ROCK0
            pop rdx ; rhs value
            mov byte [rbp - 16], dl
            push rdx
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
            ; RHS
               ; Char Literal
                  push 'B'
            ; LHS
               ; Variable Declaration - PAPER0
                  mov rax, qword [rbp - 24]  ; __main__PAPER0
            pop rdx ; rhs value
            mov byte [rbp - 24], dl
            push rdx
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
            ; RHS
               ; Char Literal
                  push 'C'
            ; LHS
               ; Variable Declaration - SCISSORS0
                  mov rax, qword [rbp - 32]  ; __main__SCISSORS0
            pop rdx ; rhs value
            mov byte [rbp - 32], dl
            push rdx
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
            ; RHS
               ; Char Literal
                  push 'X'
            ; LHS
               ; Variable Declaration - LOSE
                  mov rax, qword [rbp - 40]  ; __main__LOSE
            pop rdx ; rhs value
            mov byte [rbp - 40], dl
            push rdx
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
            ; RHS
               ; Char Literal
                  push 'Y'
            ; LHS
               ; Variable Declaration - DRAW
                  mov rax, qword [rbp - 48]  ; __main__DRAW
            pop rdx ; rhs value
            mov byte [rbp - 48], dl
            push rdx
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
            ; RHS
               ; Char Literal
                  push 'Z'
            ; LHS
               ; Variable Declaration - WIN
                  mov rax, qword [rbp - 56]  ; __main__WIN
            pop rdx ; rhs value
            mov byte [rbp - 56], dl
            push rdx
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
            ; RHS
               ; Int Literal
                  mov rax, 1
                  push rax
            ; LHS
               ; Variable Declaration - SCORE_ROCK
                  mov rax, qword [rbp - 64]  ; __main__SCORE_ROCK
            pop rdx ; rhs value
            mov qword [rbp - 64], rdx
            push rdx
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
            ; RHS
               ; Int Literal
                  mov rax, 2
                  push rax
            ; LHS
               ; Variable Declaration - SCORE_PAPER
                  mov rax, qword [rbp - 72]  ; __main__SCORE_PAPER
            pop rdx ; rhs value
            mov qword [rbp - 72], rdx
            push rdx
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
            ; RHS
               ; Int Literal
                  mov rax, 3
                  push rax
            ; LHS
               ; Variable Declaration - SCORE_SCISSORS
                  mov rax, qword [rbp - 80]  ; __main__SCORE_SCISSORS
            pop rdx ; rhs value
            mov qword [rbp - 80], rdx
            push rdx
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
            ; RHS
               ; Int Literal
                  mov rax, 0
                  push rax
            ; LHS
               ; Variable Declaration - SCORE_LOSE
                  mov rax, qword [rbp - 88]  ; __main__SCORE_LOSE
            pop rdx ; rhs value
            mov qword [rbp - 88], rdx
            push rdx
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
            ; RHS
               ; Int Literal
                  mov rax, 3
                  push rax
            ; LHS
               ; Variable Declaration - SCORE_DRAW
                  mov rax, qword [rbp - 96]  ; __main__SCORE_DRAW
            pop rdx ; rhs value
            mov qword [rbp - 96], rdx
            push rdx
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
            ; RHS
               ; Int Literal
                  mov rax, 6
                  push rax
            ; LHS
               ; Variable Declaration - SCORE_WIN
                  mov rax, qword [rbp - 104]  ; __main__SCORE_WIN
            pop rdx ; rhs value
            mov qword [rbp - 104], rdx
            push rdx
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
            ; RHS
               ; Int Literal
                  mov rax, 0
                  push rax
            ; LHS
               ; Variable Declaration - totalScore
                  mov rax, qword [rbp - 112]  ; __main__totalScore
            pop rdx ; rhs value
            mov qword [rbp - 112], rdx
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
                           ; Int Literal
                              mov rax, 0
                              push rax
                        pop rdx ; __offset
                        pop rax ; __pointer
                        push qword [rax + rdx] ; pointer + sizeof(data_t) * offset
                  ; RHS
                     ; Char Literal
                        push '$'
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
      ;------------------------------------------------------------------
               ; Code Block
                  ; Assignment - '='
                     ; RHS
                        ; Subscript
                           ; LHS
                              ; Identifier - char[] line
                                 push qword [rbp - 8]
                           ; OFFSET
                              ; Int Literal
                                 mov rax, 0
                                 push rax
                           pop rdx ; __offset
                           pop rax ; __pointer
                           push qword [rax + rdx] ; pointer + sizeof(data_t) * offset
                     ; LHS
                        ; Variable Declaration - lhs
                           mov rax, qword [rbp - 120]  ; __main__while__0__block__1__lhs
                     pop rdx ; rhs value
                     mov byte [rbp - 120], dl
                     push rdx
                  ; Statement results can be ignored
                  pop rdx
                  ; Assignment - '='
                     ; RHS
                        ; Subscript
                           ; LHS
                              ; Identifier - char[] line
                                 push qword [rbp - 8]
                           ; OFFSET
                              ; Int Literal
                                 mov rax, 2
                                 push rax
                           pop rdx ; __offset
                           pop rax ; __pointer
                           push qword [rax + rdx] ; pointer + sizeof(data_t) * offset
                     ; LHS
                        ; Variable Declaration - rhs
                           mov rax, qword [rbp - 128]  ; __main__while__0__block__1__rhs
                     pop rdx ; rhs value
                     mov byte [rbp - 128], dl
                     push rdx
                  ; Statement results can be ignored
                  pop rdx
                  ; Assignment - '='
                     ; RHS
                        ; Int Literal
                           mov rax, 0
                           push rax
                     ; LHS
                        ; Variable Declaration - localScore
                           mov rax, qword [rbp - 136]  ; __main__while__0__block__1__localScore
                     pop rdx ; rhs value
                     mov qword [rbp - 136], rdx
                     push rdx
                  ; Statement results can be ignored
                  pop rdx
         ;---------------------------------------------------------------
                  ; If-Statement
                     ; Condition
                        ; Equal
                           ; LHS
                              ; Identifier - char rhs
                                 push qword [rbp - 128]
                           ; RHS
                              ; Identifier - char WIN
                                 push qword [rbp - 56]
                           pop rdx ; rhs
                           pop rax ; lhs
                           cmp rax, rdx
                           sete al
                           movzx eax, al
                           push rax
                        pop rdx ; __cond
                        cmp rdx, 0 ; ensure condition is true
                        je .__elif__2x0 ; jump to first elif
                     ; Body
               ;---------------------------------------------------------
                        ; Code Block
                  ;------------------------------------------------------
                           ; If-Statement
                              ; Condition
                                 ; Equal
                                    ; LHS
                                       ; Identifier - char lhs
                                          push qword [rbp - 120]
                                    ; RHS
                                       ; Identifier - char ROCK0
                                          push qword [rbp - 16]
                                    pop rdx ; rhs
                                    pop rax ; lhs
                                    cmp rax, rdx
                                    sete al
                                    movzx eax, al
                                    push rax
                                 pop rdx ; __cond
                                 cmp rdx, 0 ; ensure condition is true
                                 je .__elif__4x0 ; jump to first elif
                              ; Body
                        ;------------------------------------------------
                                 ; Code Block
                                    ; Assignment - '+='
                                       ; RHS
                                          ; Identifier - int SCORE_PAPER
                                             push qword [rbp - 72]
                                       pop rdx ; rhs value
                                       mov rax, qword [rbp - 136] ; read lhs value
                                       add rax, rdx      ; add lhs and rhs
                                       mov qword [rbp - 136], rax ; write back to lhs
                                       push rax          ; push result for other expressions
                                    ; Statement results can be ignored
                                    pop rdx
                        ;------------------------------------------------
                              jmp .__endif__4 ; jump to end of condition chain
                     ;---------------------------------------------------
                              ; Elif-Statement
.__elif__4x0:
                                 ; Condition
                                 ; Equal
                                    ; LHS
                                       ; Identifier - char lhs
                                          push qword [rbp - 120]
                                    ; RHS
                                       ; Identifier - char PAPER0
                                          push qword [rbp - 24]
                                    pop rdx ; rhs
                                    pop rax ; lhs
                                    cmp rax, rdx
                                    sete al
                                    movzx eax, al
                                    push rax
                                 pop rdx ; __cond
                                 cmp rdx, 0 ; ensure condition is true
                                 je .__elif__4x1
                                 ; Body
                        ;------------------------------------------------
                                 ; Code Block
                                    ; Assignment - '+='
                                       ; RHS
                                          ; Identifier - int SCORE_SCISSORS
                                             push qword [rbp - 80]
                                       pop rdx ; rhs value
                                       mov rax, qword [rbp - 136] ; read lhs value
                                       add rax, rdx      ; add lhs and rhs
                                       mov qword [rbp - 136], rax ; write back to lhs
                                       push rax          ; push result for other expressions
                                    ; Statement results can be ignored
                                    pop rdx
                        ;------------------------------------------------
                                 jmp .__endif__4
                     ;---------------------------------------------------
                     ;---------------------------------------------------
                              ; Elif-Statement
.__elif__4x1:
                                 ; Condition
                                 ; Equal
                                    ; LHS
                                       ; Identifier - char lhs
                                          push qword [rbp - 120]
                                    ; RHS
                                       ; Identifier - char SCISSORS0
                                          push qword [rbp - 32]
                                    pop rdx ; rhs
                                    pop rax ; lhs
                                    cmp rax, rdx
                                    sete al
                                    movzx eax, al
                                    push rax
                                 pop rdx ; __cond
                                 cmp rdx, 0 ; ensure condition is true
                                 je .__endif__4
                                 ; Body
                        ;------------------------------------------------
                                 ; Code Block
                                    ; Assignment - '+='
                                       ; RHS
                                          ; Identifier - int SCORE_ROCK
                                             push qword [rbp - 64]
                                       pop rdx ; rhs value
                                       mov rax, qword [rbp - 136] ; read lhs value
                                       add rax, rdx      ; add lhs and rhs
                                       mov qword [rbp - 136], rax ; write back to lhs
                                       push rax          ; push result for other expressions
                                    ; Statement results can be ignored
                                    pop rdx
                        ;------------------------------------------------
                                 jmp .__endif__4
                     ;---------------------------------------------------
                              ; End of if
.__endif__4:
                  ;------------------------------------------------------
                           ; Assignment - '+='
                              ; RHS
                                 ; Identifier - int SCORE_WIN
                                    push qword [rbp - 104]
                              pop rdx ; rhs value
                              mov rax, qword [rbp - 136] ; read lhs value
                              add rax, rdx      ; add lhs and rhs
                              mov qword [rbp - 136], rax ; write back to lhs
                              push rax          ; push result for other expressions
                           ; Statement results can be ignored
                           pop rdx
               ;---------------------------------------------------------
                     jmp .__endif__2 ; jump to end of condition chain
            ;------------------------------------------------------------
                     ; Elif-Statement
.__elif__2x0:
                        ; Condition
                        ; Equal
                           ; LHS
                              ; Identifier - char rhs
                                 push qword [rbp - 128]
                           ; RHS
                              ; Identifier - char DRAW
                                 push qword [rbp - 48]
                           pop rdx ; rhs
                           pop rax ; lhs
                           cmp rax, rdx
                           sete al
                           movzx eax, al
                           push rax
                        pop rdx ; __cond
                        cmp rdx, 0 ; ensure condition is true
                        je .__elif__2x1
                        ; Body
               ;---------------------------------------------------------
                        ; Code Block
                  ;------------------------------------------------------
                           ; If-Statement
                              ; Condition
                                 ; Equal
                                    ; LHS
                                       ; Identifier - char lhs
                                          push qword [rbp - 120]
                                    ; RHS
                                       ; Identifier - char ROCK0
                                          push qword [rbp - 16]
                                    pop rdx ; rhs
                                    pop rax ; lhs
                                    cmp rax, rdx
                                    sete al
                                    movzx eax, al
                                    push rax
                                 pop rdx ; __cond
                                 cmp rdx, 0 ; ensure condition is true
                                 je .__elif__9x0 ; jump to first elif
                              ; Body
                        ;------------------------------------------------
                                 ; Code Block
                                    ; Assignment - '+='
                                       ; RHS
                                          ; Identifier - int SCORE_ROCK
                                             push qword [rbp - 64]
                                       pop rdx ; rhs value
                                       mov rax, qword [rbp - 136] ; read lhs value
                                       add rax, rdx      ; add lhs and rhs
                                       mov qword [rbp - 136], rax ; write back to lhs
                                       push rax          ; push result for other expressions
                                    ; Statement results can be ignored
                                    pop rdx
                        ;------------------------------------------------
                              jmp .__endif__9 ; jump to end of condition chain
                     ;---------------------------------------------------
                              ; Elif-Statement
.__elif__9x0:
                                 ; Condition
                                 ; Equal
                                    ; LHS
                                       ; Identifier - char lhs
                                          push qword [rbp - 120]
                                    ; RHS
                                       ; Identifier - char PAPER0
                                          push qword [rbp - 24]
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
                        ;------------------------------------------------
                                 ; Code Block
                                    ; Assignment - '+='
                                       ; RHS
                                          ; Identifier - int SCORE_PAPER
                                             push qword [rbp - 72]
                                       pop rdx ; rhs value
                                       mov rax, qword [rbp - 136] ; read lhs value
                                       add rax, rdx      ; add lhs and rhs
                                       mov qword [rbp - 136], rax ; write back to lhs
                                       push rax          ; push result for other expressions
                                    ; Statement results can be ignored
                                    pop rdx
                        ;------------------------------------------------
                                 jmp .__endif__9
                     ;---------------------------------------------------
                     ;---------------------------------------------------
                              ; Elif-Statement
.__elif__9x1:
                                 ; Condition
                                 ; Equal
                                    ; LHS
                                       ; Identifier - char lhs
                                          push qword [rbp - 120]
                                    ; RHS
                                       ; Identifier - char SCISSORS0
                                          push qword [rbp - 32]
                                    pop rdx ; rhs
                                    pop rax ; lhs
                                    cmp rax, rdx
                                    sete al
                                    movzx eax, al
                                    push rax
                                 pop rdx ; __cond
                                 cmp rdx, 0 ; ensure condition is true
                                 je .__endif__9
                                 ; Body
                        ;------------------------------------------------
                                 ; Code Block
                                    ; Assignment - '+='
                                       ; RHS
                                          ; Identifier - int SCORE_SCISSORS
                                             push qword [rbp - 80]
                                       pop rdx ; rhs value
                                       mov rax, qword [rbp - 136] ; read lhs value
                                       add rax, rdx      ; add lhs and rhs
                                       mov qword [rbp - 136], rax ; write back to lhs
                                       push rax          ; push result for other expressions
                                    ; Statement results can be ignored
                                    pop rdx
                        ;------------------------------------------------
                                 jmp .__endif__9
                     ;---------------------------------------------------
                              ; End of if
.__endif__9:
                  ;------------------------------------------------------
                           ; Assignment - '+='
                              ; RHS
                                 ; Identifier - int SCORE_DRAW
                                    push qword [rbp - 96]
                              pop rdx ; rhs value
                              mov rax, qword [rbp - 136] ; read lhs value
                              add rax, rdx      ; add lhs and rhs
                              mov qword [rbp - 136], rax ; write back to lhs
                              push rax          ; push result for other expressions
                           ; Statement results can be ignored
                           pop rdx
               ;---------------------------------------------------------
                        jmp .__endif__2
            ;------------------------------------------------------------
            ;------------------------------------------------------------
                     ; Elif-Statement
.__elif__2x1:
                        ; Condition
                        ; Equal
                           ; LHS
                              ; Identifier - char rhs
                                 push qword [rbp - 128]
                           ; RHS
                              ; Identifier - char LOSE
                                 push qword [rbp - 40]
                           pop rdx ; rhs
                           pop rax ; lhs
                           cmp rax, rdx
                           sete al
                           movzx eax, al
                           push rax
                        pop rdx ; __cond
                        cmp rdx, 0 ; ensure condition is true
                        je .__endif__2
                        ; Body
               ;---------------------------------------------------------
                        ; Code Block
                  ;------------------------------------------------------
                           ; If-Statement
                              ; Condition
                                 ; Equal
                                    ; LHS
                                       ; Identifier - char lhs
                                          push qword [rbp - 120]
                                    ; RHS
                                       ; Identifier - char ROCK0
                                          push qword [rbp - 16]
                                    pop rdx ; rhs
                                    pop rax ; lhs
                                    cmp rax, rdx
                                    sete al
                                    movzx eax, al
                                    push rax
                                 pop rdx ; __cond
                                 cmp rdx, 0 ; ensure condition is true
                                 je .__elif__14x0 ; jump to first elif
                              ; Body
                        ;------------------------------------------------
                                 ; Code Block
                                    ; Assignment - '+='
                                       ; RHS
                                          ; Identifier - int SCORE_SCISSORS
                                             push qword [rbp - 80]
                                       pop rdx ; rhs value
                                       mov rax, qword [rbp - 136] ; read lhs value
                                       add rax, rdx      ; add lhs and rhs
                                       mov qword [rbp - 136], rax ; write back to lhs
                                       push rax          ; push result for other expressions
                                    ; Statement results can be ignored
                                    pop rdx
                        ;------------------------------------------------
                              jmp .__endif__14 ; jump to end of condition chain
                     ;---------------------------------------------------
                              ; Elif-Statement
.__elif__14x0:
                                 ; Condition
                                 ; Equal
                                    ; LHS
                                       ; Identifier - char lhs
                                          push qword [rbp - 120]
                                    ; RHS
                                       ; Identifier - char PAPER0
                                          push qword [rbp - 24]
                                    pop rdx ; rhs
                                    pop rax ; lhs
                                    cmp rax, rdx
                                    sete al
                                    movzx eax, al
                                    push rax
                                 pop rdx ; __cond
                                 cmp rdx, 0 ; ensure condition is true
                                 je .__elif__14x1
                                 ; Body
                        ;------------------------------------------------
                                 ; Code Block
                                    ; Assignment - '+='
                                       ; RHS
                                          ; Identifier - int SCORE_ROCK
                                             push qword [rbp - 64]
                                       pop rdx ; rhs value
                                       mov rax, qword [rbp - 136] ; read lhs value
                                       add rax, rdx      ; add lhs and rhs
                                       mov qword [rbp - 136], rax ; write back to lhs
                                       push rax          ; push result for other expressions
                                    ; Statement results can be ignored
                                    pop rdx
                        ;------------------------------------------------
                                 jmp .__endif__14
                     ;---------------------------------------------------
                     ;---------------------------------------------------
                              ; Elif-Statement
.__elif__14x1:
                                 ; Condition
                                 ; Equal
                                    ; LHS
                                       ; Identifier - char lhs
                                          push qword [rbp - 120]
                                    ; RHS
                                       ; Identifier - char SCISSORS0
                                          push qword [rbp - 32]
                                    pop rdx ; rhs
                                    pop rax ; lhs
                                    cmp rax, rdx
                                    sete al
                                    movzx eax, al
                                    push rax
                                 pop rdx ; __cond
                                 cmp rdx, 0 ; ensure condition is true
                                 je .__endif__14
                                 ; Body
                        ;------------------------------------------------
                                 ; Code Block
                                    ; Assignment - '+='
                                       ; RHS
                                          ; Identifier - int SCORE_PAPER
                                             push qword [rbp - 72]
                                       pop rdx ; rhs value
                                       mov rax, qword [rbp - 136] ; read lhs value
                                       add rax, rdx      ; add lhs and rhs
                                       mov qword [rbp - 136], rax ; write back to lhs
                                       push rax          ; push result for other expressions
                                    ; Statement results can be ignored
                                    pop rdx
                        ;------------------------------------------------
                                 jmp .__endif__14
                     ;---------------------------------------------------
                              ; End of if
.__endif__14:
                  ;------------------------------------------------------
                           ; Assignment - '+='
                              ; RHS
                                 ; Identifier - int SCORE_LOSE
                                    push qword [rbp - 88]
                              pop rdx ; rhs value
                              mov rax, qword [rbp - 136] ; read lhs value
                              add rax, rdx      ; add lhs and rhs
                              mov qword [rbp - 136], rax ; write back to lhs
                              push rax          ; push result for other expressions
                           ; Statement results can be ignored
                           pop rdx
               ;---------------------------------------------------------
                        jmp .__endif__2
            ;------------------------------------------------------------
                     ; End of if
.__endif__2:
         ;---------------------------------------------------------------
                  ; Assignment - '+='
                     ; RHS
                        ; Identifier - int localScore
                           push qword [rbp - 136]
                     pop rdx ; rhs value
                     mov rax, qword [rbp - 112] ; read lhs value
                     add rax, rdx      ; add lhs and rhs
                     mov qword [rbp - 112], rax ; write back to lhs
                     push rax          ; push result for other expressions
                  ; Statement results can be ignored
                  pop rdx
                  ; Free Operator
                     ; RHS
                        ; Identifier - char[] line
                           push qword [rbp - 8]
                     ; Free pointer
                     pop rdi   ; pointer
                     call free ; free the pointer
                     push rax  ; undefined return value
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
                     pop rdx ; rhs value
                     mov qword [rbp - 8], rdx
                     push rdx
                  ; Statement results can be ignored
                  pop rdx
      ;------------------------------------------------------------------
            jmp .__while__0
            ; End of While
.__endwhile__0:
;------------------------------------------------------------------------
         ; Function Call - println(int) -> void
            ; Make space for 1 arg(s)
            sub rsp, 8
            ; Arguments
               ; Eval arg0
                  ; Identifier - int totalScore
                     push qword [rbp - 112]
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
; ========================================================================
; ### END OF CODE ########################################################
; ========================================================================

         push 0
         call exit__int
; ========================================================================
; ### DATA SECTION #######################################################
; ========================================================================

         section .data
.floatNegOne: dq -1.0
.floatZero: dq 0.0
.floatOne: dq 1.0
