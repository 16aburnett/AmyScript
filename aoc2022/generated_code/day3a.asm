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
         sub rsp, 112
         ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
         ; [rbp - 8] - char[] letters (<unset-scope-name>)
         ; [rbp - 16] - int letters_size (<unset-scope-name>)
         ; [rbp - 24] - char[] line (<unset-scope-name>)
         ; [rbp - 32] - int total (<unset-scope-name>)
         ; [rbp - 40] - int size (<unset-scope-name>)
         ; [rbp - 48] - int c0 (<unset-scope-name>)
         ; [rbp - 56] - int e0 (<unset-scope-name>)
         ; [rbp - 64] - int c1 (<unset-scope-name>)
         ; [rbp - 72] - int e1 (<unset-scope-name>)
         ; [rbp - 80] - char common (<unset-scope-name>)
         ; [rbp - 88] - int i (<unset-scope-name>)
         ; [rbp - 96] - int j (<unset-scope-name>)
         ; [rbp - 104] - int score (<unset-scope-name>)
         ; [rbp - 112] - int i (<unset-scope-name>)

         ; Body
; ========================================================================
         ; Class Template - 
            ; Instances:
         ; End Class Template - 
; ========================================================================

; ========================================================================
         ; Function Template - 
            ; Instances:
         ; End Function Template - 
; ========================================================================

; ========================================================================
         ; Function Template - 
            ; Instances:
         ; End Function Template - 
; ========================================================================

         ; Assignment - '='
            ; RHS
               ; String Literal
                  ; " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
                  mov rax, .str0
                  push rax
            ; LHS
               ; Variable Declaration - letters
                  mov rax, qword [rbp - 8]  ; __main__letters
            pop rdx ; rhs value
            mov qword [rbp - 8], rdx
            push rdx
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
            ; RHS
               ; Int Literal
                  mov rax, 53
                  push rax
            ; LHS
               ; Variable Declaration - letters_size
                  mov rax, qword [rbp - 16]  ; __main__letters_size
            pop rdx ; rhs value
            mov qword [rbp - 16], rdx
            push rdx
         ; Statement results can be ignored
         pop rdx
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
                  mov rax, qword [rbp - 24]  ; __main__line
            pop rdx ; rhs value
            mov qword [rbp - 24], rdx
            push rdx
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
            ; RHS
               ; Int Literal
                  mov rax, 0
                  push rax
            ; LHS
               ; Variable Declaration - total
                  mov rax, qword [rbp - 32]  ; __main__total
            pop rdx ; rhs value
            mov qword [rbp - 32], rdx
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
                              push qword [rbp - 24]
                        ; OFFSET
                           ; Int Literal
                              mov rax, 0
                              push rax
                        pop rdx ; __offset
                        pop rax ; __pointer
                        mov al, byte [rax + rdx] ; pointer + sizeof(data_t) * offset
                        movzx rax, al ; zero extend because we need to push 64bit to stack
                        push rax ; push char onto stack
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
                        ; Int Literal
                           mov rax, 0
                           push rax
                     ; LHS
                        ; Variable Declaration - size
                           mov rax, qword [rbp - 40]  ; __main__while__0__block__1__size
                     pop rdx ; rhs value
                     mov qword [rbp - 40], rdx
                     push rdx
                  ; Statement results can be ignored
                  pop rdx
         ;---------------------------------------------------------------
                  ; While-Loop
.__while__2:
                     ; Condition
                        ; Not Equal
                           ; LHS
                              ; Subscript
                                 ; LHS
                                    ; Identifier - char[] line
                                       push qword [rbp - 24]
                                 ; OFFSET
                                    ; Post-Increment
                                       mov rax, qword [rbp - 40]
                                       add qword [rbp - 40], 1
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
                        je .__endwhile__2
                     ; Body
                     jmp .__while__2
                     ; End of While
.__endwhile__2:
         ;---------------------------------------------------------------
                  ; Pre-Decrement - int
                     ; RHS
                        ; Identifier - int size
                           push qword [rbp - 40]
                     pop rdx
                     sub qword [rbp - 40], 1
                     mov rax, qword [rbp - 40]
                     push rax ; push result
                  ; Statement results can be ignored
                  pop rdx
                  ; Assignment - '='
                     ; RHS
                        ; Int Literal
                           mov rax, 0
                           push rax
                     ; LHS
                        ; Variable Declaration - c0
                           mov rax, qword [rbp - 48]  ; __main__while__0__block__1__c0
                     pop rdx ; rhs value
                     mov qword [rbp - 48], rdx
                     push rdx
                  ; Statement results can be ignored
                  pop rdx
                  ; Assignment - '='
                     ; RHS
                        ; Division - int, int
                           ; LHS
                              ; Identifier - int size
                                 push qword [rbp - 40]
                           ; RHS
                              ; Int Literal
                                 mov rax, 2
                                 push rax
                           pop rdx
                           pop rax
                           mov rsi, rdx
                           xor rdx, rdx
                           cqo ; sign extend rax into rdx (specifically for 64bit -> 128bit)
                           idiv rsi ; perform rdx:rax (128bit) / rsi (64bit) = rax
                           push rax
                     ; LHS
                        ; Variable Declaration - e0
                           mov rax, qword [rbp - 56]  ; __main__while__0__block__1__e0
                     pop rdx ; rhs value
                     mov qword [rbp - 56], rdx
                     push rdx
                  ; Statement results can be ignored
                  pop rdx
                  ; Assignment - '='
                     ; RHS
                        ; Identifier - int e0
                           push qword [rbp - 56]
                     ; LHS
                        ; Variable Declaration - c1
                           mov rax, qword [rbp - 64]  ; __main__while__0__block__1__c1
                     pop rdx ; rhs value
                     mov qword [rbp - 64], rdx
                     push rdx
                  ; Statement results can be ignored
                  pop rdx
                  ; Assignment - '='
                     ; RHS
                        ; Identifier - int size
                           push qword [rbp - 40]
                     ; LHS
                        ; Variable Declaration - e1
                           mov rax, qword [rbp - 72]  ; __main__while__0__block__1__e1
                     pop rdx ; rhs value
                     mov qword [rbp - 72], rdx
                     push rdx
                  ; Statement results can be ignored
                  pop rdx
                  ; Assignment - '='
                     ; RHS
                        ; Char Literal
                           push '0'
                     ; LHS
                        ; Variable Declaration - common
                           mov rax, qword [rbp - 80]  ; __main__while__0__block__1__common
                     pop rdx ; rhs value
                     mov byte [rbp - 80], dl
                     push rdx
                  ; Statement results can be ignored
                  pop rdx
         ;---------------------------------------------------------------
                  ; For-Loop
                  ; Init
                     ; Assignment - '='
                        ; RHS
                           ; Identifier - int c0
                              push qword [rbp - 48]
                        ; LHS
                           ; Variable Declaration - i
                              mov rax, qword [rbp - 88]  ; __main__while__0__block__1__for__3__i
                        pop rdx ; rhs value
                        mov qword [rbp - 88], rdx
                        push rdx
                     ; Loop init result can be discarded
                     pop rax
                  jmp .__forcond__3
.__for__3:
                     ; Update
                        ; Pre-Increment - int
                           ; RHS
                              ; Identifier - int i
                                 push qword [rbp - 88]
                           pop rdx
                           add qword [rbp - 88], 1
                           mov rax, qword [rbp - 88]
                           push rax ; push result
                        ; Loop update result can be discarded
                        pop rax
.__forcond__3:
                     ; Condition
                        ; Less Than
                           ; LHS
                              ; Identifier - int i
                                 push qword [rbp - 88]
                           ; RHS
                              ; Identifier - int e0
                                 push qword [rbp - 56]
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
                                    ; Identifier - int c1
                                       push qword [rbp - 64]
                                 ; LHS
                                    ; Variable Declaration - j
                                       mov rax, qword [rbp - 96]  ; __main__while__0__block__1__for__3__block__4__for__5__j
                                 pop rdx ; rhs value
                                 mov qword [rbp - 96], rdx
                                 push rdx
                              ; Loop init result can be discarded
                              pop rax
                           jmp .__forcond__5
.__for__5:
                              ; Update
                                 ; Pre-Increment - int
                                    ; RHS
                                       ; Identifier - int j
                                          push qword [rbp - 96]
                                    pop rdx
                                    add qword [rbp - 96], 1
                                    mov rax, qword [rbp - 96]
                                    push rax ; push result
                                 ; Loop update result can be discarded
                                 pop rax
.__forcond__5:
                              ; Condition
                                 ; Less Than
                                    ; LHS
                                       ; Identifier - int j
                                          push qword [rbp - 96]
                                    ; RHS
                                       ; Identifier - int e1
                                          push qword [rbp - 72]
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
                                                         push qword [rbp - 24]
                                                   ; OFFSET
                                                      ; Identifier - int i
                                                         push qword [rbp - 88]
                                                   pop rdx ; __offset
                                                   pop rax ; __pointer
                                                   mov al, byte [rax + rdx] ; pointer + sizeof(data_t) * offset
                                                   movzx rax, al ; zero extend because we need to push 64bit to stack
                                                   push rax ; push char onto stack
                                             ; RHS
                                                ; Subscript
                                                   ; LHS
                                                      ; Identifier - char[] line
                                                         push qword [rbp - 24]
                                                   ; OFFSET
                                                      ; Identifier - int j
                                                         push qword [rbp - 96]
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
                                                   ; Subscript
                                                      ; LHS
                                                         ; Identifier - char[] line
                                                            push qword [rbp - 24]
                                                      ; OFFSET
                                                         ; Identifier - int i
                                                            push qword [rbp - 88]
                                                      pop rdx ; __offset
                                                      pop rax ; __pointer
                                                      mov al, byte [rax + rdx] ; pointer + sizeof(data_t) * offset
                                                      movzx rax, al ; zero extend because we need to push 64bit to stack
                                                      push rax ; push char onto stack
                                                pop rdx ; rhs value
                                                mov byte [rbp - 80], dl
                                                push rdx
                                             ; Statement results can be ignored
                                             pop rdx
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
               ;---------------------------------------------------------
                     ; Repeat
jmp .__for__3
                     ; End of For
.__endfor__3:
         ;---------------------------------------------------------------
                  ; Assignment - '='
                     ; RHS
                        ; Int Literal
                           mov rax, 0
                           push rax
                     ; LHS
                        ; Variable Declaration - score
                           mov rax, qword [rbp - 104]  ; __main__while__0__block__1__score
                     pop rdx ; rhs value
                     mov qword [rbp - 104], rdx
                     push rdx
                  ; Statement results can be ignored
                  pop rdx
         ;---------------------------------------------------------------
                  ; For-Loop
                  ; Init
                     ; Assignment - '='
                        ; RHS
                           ; Int Literal
                              mov rax, 0
                              push rax
                        ; LHS
                           ; Variable Declaration - i
                              mov rax, qword [rbp - 112]  ; __main__while__0__block__1__for__9__i
                        pop rdx ; rhs value
                        mov qword [rbp - 112], rdx
                        push rdx
                     ; Loop init result can be discarded
                     pop rax
                  jmp .__forcond__9
.__for__9:
                     ; Update
                        ; Pre-Increment - int
                           ; RHS
                              ; Identifier - int i
                                 push qword [rbp - 112]
                           pop rdx
                           add qword [rbp - 112], 1
                           mov rax, qword [rbp - 112]
                           push rax ; push result
                        ; Loop update result can be discarded
                        pop rax
.__forcond__9:
                     ; Condition
                        ; Less Than
                           ; LHS
                              ; Identifier - int i
                                 push qword [rbp - 112]
                           ; RHS
                              ; Identifier - int letters_size
                                 push qword [rbp - 16]
                           pop rdx ; rhs
                           pop rax ; lhs
                           cmp rax, rdx
                           setl al
                           movzx eax, al
                           push rax
                        pop rax ; __cond
                        cmp rax, 0 ; __cond
                        je .__endfor__9
                     ; Body
               ;---------------------------------------------------------
                        ; Code Block
                  ;------------------------------------------------------
                           ; If-Statement
                              ; Condition
                                 ; Equal
                                    ; LHS
                                       ; Subscript
                                          ; LHS
                                             ; Identifier - char[] letters
                                                push qword [rbp - 8]
                                          ; OFFSET
                                             ; Identifier - int i
                                                push qword [rbp - 112]
                                          pop rdx ; __offset
                                          pop rax ; __pointer
                                          mov al, byte [rax + rdx] ; pointer + sizeof(data_t) * offset
                                          movzx rax, al ; zero extend because we need to push 64bit to stack
                                          push rax ; push char onto stack
                                    ; RHS
                                       ; Identifier - char common
                                          mov al, byte [rbp - 80]
                                          movzx rax, al
                                          push rax
                                    pop rdx ; rhs
                                    pop rax ; lhs
                                    cmp rax, rdx
                                    sete al
                                    movzx eax, al
                                    push rax
                                 pop rdx ; __cond
                                 cmp rdx, 0 ; ensure condition is true
                                 je .__endif__11 ; jump to end
                              ; Body
                                 ; Assignment - '='
                                    ; RHS
                                       ; Identifier - int i
                                          push qword [rbp - 112]
                                    pop rdx ; rhs value
                                    mov qword [rbp - 104], rdx
                                    push rdx
                                 ; Statement results can be ignored
                                 pop rdx
                              jmp .__endif__11 ; jump to end of condition chain
                              ; End of if
.__endif__11:
                  ;------------------------------------------------------
               ;---------------------------------------------------------
                     ; Repeat
jmp .__for__9
                     ; End of For
.__endfor__9:
         ;---------------------------------------------------------------
                  ; Assignment - '+='
                     ; RHS
                        ; Identifier - int score
                           push qword [rbp - 104]
                     pop rdx ; rhs value
                     mov rax, qword [rbp - 32] ; read lhs value
                     add rax, rdx      ; add lhs and rhs
                     mov qword [rbp - 32], rax ; write back to lhs
                     push rax          ; push result for other expressions
                  ; Statement results can be ignored
                  pop rdx
                  ; Free Operator
                     ; RHS
                        ; Identifier - char[] line
                           push qword [rbp - 24]
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
                           call __builtin__input
                           ; Remove args
                           add rsp, 0
                           ; Push return value
                           push rax
                     pop rdx ; rhs value
                     mov qword [rbp - 24], rdx
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
                  ; Identifier - int total
                     push qword [rbp - 32]
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
; ========================================================================
; ### END OF CODE ########################################################
; ========================================================================

         push 0
         call __builtin__exit__int
; ========================================================================
; ### DATA SECTION #######################################################
; ========================================================================

         section .data
.str0: db ' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 0
.floatNegOne: dq -1.0
.floatZero: dq 0.0
.floatOne: dq 1.0
