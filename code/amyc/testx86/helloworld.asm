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
         sub rsp, 432
         ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
         ; [rbp - 8] - int x (<unset-scope-name>)
         ; [rbp - 16] - int y (<unset-scope-name>)
         ; [rbp - 24] - char c0 (<unset-scope-name>)
         ; [rbp - 32] - char c1 (<unset-scope-name>)
         ; [rbp - 40] - char c2 (<unset-scope-name>)
         ; [rbp - 48] - char c3 (<unset-scope-name>)
         ; [rbp - 56] - char[] string0 (<unset-scope-name>)
         ; [rbp - 64] - char[] string1 (<unset-scope-name>)
         ; [rbp - 72] - int x (<unset-scope-name>)
         ; [rbp - 80] - int y (<unset-scope-name>)
         ; [rbp - 88] - int z (<unset-scope-name>)
         ; [rbp - 96] - int i (<unset-scope-name>)
         ; [rbp - 104] - int i (<unset-scope-name>)
         ; [rbp - 112] - int j (<unset-scope-name>)
         ; [rbp - 120] - int x (<unset-scope-name>)
         ; [rbp - 128] - float x (<unset-scope-name>)
         ; [rbp - 136] - float y (<unset-scope-name>)
         ; [rbp - 144] - int x (<unset-scope-name>)
         ; [rbp - 152] - float y (<unset-scope-name>)
         ; [rbp - 160] - char c (<unset-scope-name>)
         ; [rbp - 168] - int a (<unset-scope-name>)
         ; [rbp - 176] - float b (<unset-scope-name>)
         ; [rbp - 184] - int[] nums (<unset-scope-name>)
         ; [rbp - 192] - float[] floats (<unset-scope-name>)
         ; [rbp - 200] - char[] str (<unset-scope-name>)
         ; [rbp - 208] - int[] ints (<unset-scope-name>)
         ; [rbp - 216] - int n (<unset-scope-name>)
         ; [rbp - 224] - int[] arr (<unset-scope-name>)
         ; [rbp - 232] - int i (<unset-scope-name>)
         ; [rbp - 240] - int i (<unset-scope-name>)
         ; [rbp - 248] - int i (<unset-scope-name>)
         ; [rbp - 256] - float[] floats (<unset-scope-name>)
         ; [rbp - 264] - int i (<unset-scope-name>)
         ; [rbp - 272] - int i (<unset-scope-name>)
         ; [rbp - 280] - char[] str (<unset-scope-name>)
         ; [rbp - 288] - int[] a (<unset-scope-name>)
         ; [rbp - 296] - int[] b (<unset-scope-name>)
         ; [rbp - 304] - int[] c (<unset-scope-name>)
         ; [rbp - 312] - int[][] A (<unset-scope-name>)
         ; [rbp - 320] - int[][] B (<unset-scope-name>)
         ; [rbp - 328] - int[][] C (<unset-scope-name>)
         ; [rbp - 336] - int[][] D (<unset-scope-name>)
         ; [rbp - 344] - float[][] mat (<unset-scope-name>)
         ; [rbp - 352] - Vector2D v (<unset-scope-name>)
         ; [rbp - 360] - Vector2D v2 (<unset-scope-name>)
         ; [rbp - 368] - Vector3D v3 (<unset-scope-name>)
         ; [rbp - 376] - Vector3D v4 (<unset-scope-name>)
         ; [rbp - 384] - Vector<:int:> myArray (<unset-scope-name>)
         ; [rbp - 392] - int i (<unset-scope-name>)
         ; [rbp - 400] - Vector<:float:> vals (<unset-scope-name>)
         ; [rbp - 408] - int i (<unset-scope-name>)
         ; [rbp - 416] - char[] line (<unset-scope-name>)
         ; [rbp - 424] - int x (<unset-scope-name>)
         ; [rbp - 432] - float y (<unset-scope-name>)

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
                                             mov rax, -17
                                             push rax
                                       ; RHS
                                          ; Multiplication - int, int
                                             ; LHS
                                                ; Int Literal
                                                   mov rax, 42
                                                   push rax
                                             ; RHS
                                                ; Addition - int, int
                                                   ; LHS
                                                      ; Int Literal
                                                         mov rax, 2
                                                         push rax
                                                   ; RHS
                                                      ; Int Literal
                                                         mov rax, 2
                                                         push rax
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
                                       mov rax, 1
                                       push rax
                                 pop rdx ; rhs
                                 pop rax ; lhs
                                 add rax, rdx
                                 push rax
                           ; RHS
                              ; Int Literal
                                 mov rax, -1
                                 push rax
                           pop rdx
                           pop rax
                           imul rax, rdx
                           push rax
                     ; RHS
                        ; Int Literal
                           mov rax, 3
                           push rax
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
               pop rdx ; rhs value
               mov qword [rbp - 8], rdx
               push rdx
            ; Statement results can be ignored
            pop rdx
            ; Assignment - '='
               ; RHS
                  ; Multiplication - int, int
                     ; LHS
                        ; Identifier - int x
                           push qword [rbp - 8]
                     ; RHS
                        ; Int Literal
                           mov rax, 23
                           push rax
                     pop rdx
                     pop rax
                     imul rax, rdx
                     push rax
               ; LHS
                  ; Variable Declaration - y
                     mov rax, qword [rbp - 16]  ; __main__block__0__y
               pop rdx ; rhs value
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
                           ; Identifier - int y
                              push qword [rbp - 16]
                        ; RHS
                           ; Identifier - int x
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
               pop rdx ; rhs value
               mov byte [rbp - 24], dl
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
               pop rdx ; rhs value
               mov byte [rbp - 32], dl
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
               pop rdx ; rhs value
               mov byte [rbp - 40], dl
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
               pop rdx ; rhs value
               mov byte [rbp - 48], dl
               push rdx
            ; Statement results can be ignored
            pop rdx
            ; Function Call - print(char) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; Identifier - char c0
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
                     ; Identifier - char c1
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
                     ; Identifier - char c2
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
                     ; Identifier - char c3
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
               pop rdx ; rhs value
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
               pop rdx ; rhs value
               mov qword [rbp - 64], rdx
               push rdx
            ; Statement results can be ignored
            pop rdx
            ; Function Call - print(char[]) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; Identifier - char[] string0
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
                     ; Identifier - char[] string1
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
                     mov rax, 1
                     push rax
               ; LHS
                  ; Variable Declaration - x
                     mov rax, qword [rbp - 72]  ; __main__block__3__x
               pop rdx ; rhs value
               mov qword [rbp - 72], rdx
               push rdx
            ; Statement results can be ignored
            pop rdx
            ; Assignment - '='
               ; RHS
                  ; Bitwise Negation - int
                     ; RHS
                        ; Identifier - int x
                           push qword [rbp - 72]
                     pop rdx
                     not rdx
                     mov rax, rdx
                     push rax ; push result
               ; LHS
                  ; Variable Declaration - y
                     mov rax, qword [rbp - 80]  ; __main__block__3__y
               pop rdx ; rhs value
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
                                          ; Identifier - int x
                                             push qword [rbp - 72]
                                       ; RHS
                                          ; Identifier - int y
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
                                          ; Identifier - int y
                                             push qword [rbp - 80]
                                       pop rdx
                                       add qword [rbp - 80], 1
                                       mov rax, qword [rbp - 80]
                                       push rax ; push result
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
                                    ; Identifier - int x
                                       push qword [rbp - 72]
                                 pop rdx
                                 sub qword [rbp - 72], 1
                                 mov rax, qword [rbp - 72]
                                 push rax ; push result
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
                           push rax ; push result
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
               pop rdx ; rhs value
               mov qword [rbp - 88], rdx
               push rdx
            ; Statement results can be ignored
            pop rdx
            ; Function Call - print(int) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; Identifier - int x
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
                     ; Identifier - int y
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
                     ; Identifier - int z
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
                        ; Identifier - int x
                           push qword [rbp - 72]
                     ; RHS
                        ; Int Literal
                           mov rax, 1
                           push rax
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
                        ; Identifier - int y
                           push qword [rbp - 80]
                     ; RHS
                        ; Int Literal
                           mov rax, -1
                           push rax
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
                     ; Identifier - int x
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
                           ; Identifier - int x
                              push qword [rbp - 72]
                        ; RHS
                           ; Int Literal
                              mov rax, 0
                              push rax
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
                           ; Identifier - int x
                              push qword [rbp - 72]
                        ; RHS
                           ; Int Literal
                              mov rax, 0
                              push rax
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
                           ; Identifier - int x
                              push qword [rbp - 72]
                        ; RHS
                           ; Int Literal
                              mov rax, 0
                              push rax
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
                           ; Identifier - int x
                              push qword [rbp - 72]
                        ; RHS
                           ; Int Literal
                              mov rax, 0
                              push rax
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
                           ; Identifier - int x
                              push qword [rbp - 72]
                        ; RHS
                           ; Int Literal
                              mov rax, 0
                              push rax
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
                        ; Identifier - int y
                           push qword [rbp - 80]
                     ; RHS
                        ; Int Literal
                           mov rax, 0
                           push rax
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
                        ; Identifier - int y
                           push qword [rbp - 80]
                     ; RHS
                        ; Int Literal
                           mov rax, 0
                           push rax
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
                        ; Identifier - int y
                           push qword [rbp - 80]
                     ; RHS
                        ; Int Literal
                           mov rax, 0
                           push rax
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
                        ; Identifier - int z
                           push qword [rbp - 88]
                     ; RHS
                        ; Int Literal
                           mov rax, 0
                           push rax
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
                              ; Identifier - int z
                                 push qword [rbp - 88]
                           ; RHS
                              ; Int Literal
                                 mov rax, 0
                                 push rax
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
                        ; Identifier - int z
                           push qword [rbp - 88]
                     ; RHS
                        ; Int Literal
                           mov rax, 0
                           push rax
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
                        mov rax, 0
                        push rax
                  ; LHS
                     ; Variable Declaration - i
                        mov rax, qword [rbp - 96]  ; __main__block__12__for__13__i
                  pop rdx ; rhs value
                  mov qword [rbp - 96], rdx
                  push rdx
               ; Loop init result can be discarded
               pop rax
            jmp .__forcond__13
.__for__13:
               ; Update
                  ; Pre-Increment - int
                     ; RHS
                        ; Identifier - int i
                           push qword [rbp - 96]
                     pop rdx
                     add qword [rbp - 96], 1
                     mov rax, qword [rbp - 96]
                     push rax ; push result
                  ; Loop update result can be discarded
                  pop rax
.__forcond__13:
               ; Condition
                  ; Less Than
                     ; LHS
                        ; Identifier - int i
                           push qword [rbp - 96]
                     ; RHS
                        ; Int Literal
                           mov rax, 10
                           push rax
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
                              ; Identifier - int i
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
                        mov rax, 10
                        push rax
                  ; LHS
                     ; Variable Declaration - i
                        mov rax, qword [rbp - 104]  ; __main__block__12__for__15__i
                  pop rdx ; rhs value
                  mov qword [rbp - 104], rdx
                  push rdx
               ; Loop init result can be discarded
               pop rax
            jmp .__forcond__15
.__for__15:
               ; Update
                  ; Pre-Decrement - int
                     ; RHS
                        ; Identifier - int i
                           push qword [rbp - 104]
                     pop rdx
                     sub qword [rbp - 104], 1
                     mov rax, qword [rbp - 104]
                     push rax ; push result
                  ; Loop update result can be discarded
                  pop rax
.__forcond__15:
               ; Condition
                  ; Greater Than
                     ; LHS
                        ; Identifier - int i
                           push qword [rbp - 104]
                     ; RHS
                        ; Int Literal
                           mov rax, -5
                           push rax
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
                              ; Identifier - int i
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
                                 ; Identifier - int i
                                    push qword [rbp - 104]
                              ; RHS
                                 ; Int Literal
                                    mov rax, 0
                                    push rax
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
                     mov rax, 1
                     push rax
               ; LHS
                  ; Variable Declaration - j
                     mov rax, qword [rbp - 112]  ; __main__block__12__j
               pop rdx ; rhs value
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
                        ; Identifier - int j
                           push qword [rbp - 112]
                     ; RHS
                        ; Int Literal
                           mov rax, 100
                           push rax
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
                                    ; Identifier - int j
                                       push qword [rbp - 112]
                                 ; RHS
                                    ; Identifier - int j
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
                           ; Identifier - int j
                              push qword [rbp - 112]
                        pop rdx
                        add qword [rbp - 112], 1
                        mov rax, qword [rbp - 112]
                        push rax ; push result
                     ; Statement results can be ignored
                     pop rdx
            ;------------------------------------------------------------
                     ; If-Statement
                        ; Condition
                           ; Less Than
                              ; LHS
                                 ; Identifier - int j
                                    push qword [rbp - 112]
                              ; RHS
                                 ; Int Literal
                                    mov rax, 10
                                    push rax
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
                           ; Identifier - int j
                              push qword [rbp - 112]
                        pop rdx
                        sub qword [rbp - 112], 1
                        mov rax, qword [rbp - 112]
                        push rax ; push result
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
                     sub rsp, 0
                  ; Parameters
                     ; Param: a [rbp + 16]
                  ; Local Variables - Each variable is currently 64-bit (sorry not sorry)

               ; Body
         ;---------------------------------------------------------------
                  ; Code Block
                     ; Return
                        ; Multiplication - int, int
                           ; LHS
                              ; Identifier - int a
                                 push qword [rbp - -16]
                           ; RHS
                              ; Int Literal
                                 mov rax, 2
                                 push rax
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
               ; Function Epilogue
               mov rsp, rbp ; remove local vars + unpopped pushes
               pop rbp
               ret
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
                                                   mov rax, 16
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
                     sub rsp, 16
                  ; Parameters
                     ; Param: a [rbp + 16]
                     ; Param: b [rbp + 24]
                     ; Param: c [rbp + 32]
                  ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
                     ; [rbp - 8] - int d (<unset-scope-name>)

               ; Body
         ;---------------------------------------------------------------
                  ; Code Block
                     ; Assignment - '='
                        ; RHS
                           ; Addition - int, int
                              ; LHS
                                 ; Addition - int, int
                                    ; LHS
                                       ; Identifier - int a
                                          push qword [rbp - -16]
                                    ; RHS
                                       ; Identifier - int b
                                          push qword [rbp - -24]
                                    pop rdx ; rhs
                                    pop rax ; lhs
                                    add rax, rdx
                                    push rax
                              ; RHS
                                 ; Identifier - int c
                                    push qword [rbp - -32]
                              pop rdx ; rhs
                              pop rax ; lhs
                              add rax, rdx
                              push rax
                        ; LHS
                           ; Variable Declaration - d
                              mov rax, qword [rbp - 8]  ; __main__block__21__add__block__23__d
                        pop rdx ; rhs value
                        mov qword [rbp - 8], rdx
                        push rdx
                     ; Statement results can be ignored
                     pop rdx
                     ; Return
                        ; Identifier - int d
                           push qword [rbp - 8]
                        pop rax
                        ; Clean up stack and return
                        mov rsp, rbp ; remove local vars + unpopped pushes
                        pop rbp
                        ret
         ;---------------------------------------------------------------
               ; Function Epilogue
               mov rsp, rbp ; remove local vars + unpopped pushes
               pop rbp
               ret
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
                                 mov rax, 7
                                 push rax
                           ; Move arg0's result to reverse order position on stack
                           pop rax
                           mov qword [rsp + 0], rax
                           ; Eval arg1
                              ; Int Literal
                                 mov rax, 4
                                 push rax
                           ; Move arg1's result to reverse order position on stack
                           pop rax
                           mov qword [rsp + 8], rax
                           ; Eval arg2
                              ; Int Literal
                                 mov rax, 21
                                 push rax
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
                     mov rax, 10
                     push rax
               ; LHS
                  ; Variable Declaration - x
                     mov rax, qword [rbp - 120]  ; __main__block__21__x
               pop rdx ; rhs value
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
                     sub rsp, 0
                  ; Parameters
                     ; Param: a [rbp + 16]
                  ; Local Variables - Each variable is currently 64-bit (sorry not sorry)

               ; Body
         ;---------------------------------------------------------------
                  ; Code Block
                     ; Return
                        ; Multiplication - int, int
                           ; LHS
                              ; Identifier - int a
                                 push qword [rbp - -16]
                           ; RHS
                              ; Identifier - int x
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
               ; Function Epilogue
               mov rsp, rbp ; remove local vars + unpopped pushes
               pop rbp
               ret
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
                     ; Identifier - int x
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
                                 mov rax, 7
                                 push rax
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
                              mov rax, 2
                              push rax
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
                              mov rax, 7
                              push rax
                        pop rdx
                        ; val = 0 - val
                        mov rax, 0
                        sub rax, rdx
                        push rax ; push result
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
                                    mov rax, 7
                                    push rax
                              pop rdx
                              ; val = 0 - val
                              mov rax, 0
                              sub rax, rdx
                              push rax ; push result
                        pop rdx
                        ; val = 0 - val
                        mov rax, 0
                        sub rax, rdx
                        push rax ; push result
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
                              mov rax, 7
                              push rax
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
                                          mov rax, -43
                                          push rax
                                    ; RHS
                                       ; Int Literal
                                          mov rax, 3
                                          push rax
                                    pop rdx ; rhs
                                    pop rax ; lhs
                                    add rax, rdx
                                    push rax
                              ; RHS
                                 ; Int Literal
                                    mov rax, -7
                                    push rax
                              pop rdx ; rhs
                              pop rax ; lhs
                              add rax, rdx
                              push rax
                        ; RHS
                           ; Int Literal
                              mov rax, 3
                              push rax
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
                              mov rax, 7
                              push rax
                        ; RHS
                           ; Int Literal
                              mov rax, 14
                              push rax
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
                              mov rax, -7
                              push rax
                        ; RHS
                           ; Int Literal
                              mov rax, -14
                              push rax
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
                              mov rax, 7
                              push rax
                        ; RHS
                           ; Int Literal
                              mov rax, -14
                              push rax
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
                              mov rax, -7
                              push rax
                        ; RHS
                           ; Int Literal
                              mov rax, 14
                              push rax
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
                                                mov rax, -7
                                                push rax
                                          ; RHS
                                             ; Int Literal
                                                mov rax, 14
                                                push rax
                                          pop rdx ; rhs
                                          pop rax ; lhs
                                          sub rax, rdx
                                          push rax
                                    ; RHS
                                       ; Int Literal
                                          mov rax, 21
                                          push rax
                                    pop rdx ; rhs
                                    pop rax ; lhs
                                    sub rax, rdx
                                    push rax
                              ; RHS
                                 ; Int Literal
                                    mov rax, -14
                                    push rax
                              pop rdx ; rhs
                              pop rax ; lhs
                              sub rax, rdx
                              push rax
                        ; RHS
                           ; Int Literal
                              mov rax, 7
                              push rax
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
                              mov rax, 7
                              push rax
                        ; RHS
                           ; Int Literal
                              mov rax, 14
                              push rax
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
                              mov rax, -7
                              push rax
                        ; RHS
                           ; Int Literal
                              mov rax, -14
                              push rax
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
                              mov rax, 7
                              push rax
                        ; RHS
                           ; Int Literal
                              mov rax, -14
                              push rax
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
                              mov rax, -7
                              push rax
                        ; RHS
                           ; Int Literal
                              mov rax, 14
                              push rax
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
                              mov rax, 10
                              push rax
                        ; RHS
                           ; Int Literal
                              mov rax, 2
                              push rax
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
                              mov rax, 10
                              push rax
                        ; RHS
                           ; Int Literal
                              mov rax, 3
                              push rax
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
                              mov rax, 1
                              push rax
                        ; RHS
                           ; Int Literal
                              mov rax, 2
                              push rax
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
                              mov rax, 10
                              push rax
                        ; RHS
                           ; Int Literal
                              mov rax, 3
                              push rax
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
                              mov rax, 10
                              push rax
                        ; RHS
                           ; Int Literal
                              mov rax, 2
                              push rax
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
                              mov rax, 4526
                              push rax
                        ; RHS
                           ; Int Literal
                              mov rax, 645
                              push rax
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
                              mov rax, -10
                              push rax
                        ; RHS
                           ; Int Literal
                              mov rax, 3
                              push rax
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
                              mov rax, 1
                              push rax
                        ; RHS
                           ; Int Literal
                              mov rax, 2
                              push rax
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
                                                            mov rax, 7
                                                            push rax
                                                      ; RHS
                                                         ; Int Literal
                                                            mov rax, 49
                                                            push rax
                                                      pop rdx ; rhs
                                                      pop rax ; lhs
                                                      sub rax, rdx
                                                      push rax
                                                ; RHS
                                                   ; Int Literal
                                                      mov rax, 2
                                                      push rax
                                                pop rdx
                                                pop rax
                                                mov esi, edx
                                                mov edx, 0
                                                cdq
                                                idiv esi
                                                push rax
                                          ; RHS
                                             ; Int Literal
                                                mov rax, -1
                                                push rax
                                          pop rdx
                                          pop rax
                                          imul rax, rdx
                                          push rax
                                    ; RHS
                                       ; Multiplication - int, int
                                          ; LHS
                                             ; Int Literal
                                                mov rax, 3
                                                push rax
                                          ; RHS
                                             ; Int Literal
                                                mov rax, 3
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
                                 ; Addition - int, int
                                    ; LHS
                                       ; Int Literal
                                          mov rax, 3
                                          push rax
                                    ; RHS
                                       ; Int Literal
                                          mov rax, 4
                                          push rax
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
                              mov rax, 2
                              push rax
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
                     mov rax, qword [.float0] ; 3.14
                     push rax
               ; LHS
                  ; Variable Declaration - x
                     mov rax, qword [rbp - 128]  ; __main__block__27__x
               pop rdx ; rhs value
               mov qword [rbp - 128], rdx
               push rdx
            ; Statement results can be ignored
            pop rdx
            ; Assignment - '='
               ; RHS
                  ; Float Literal
                     mov rax, qword [.float1] ; 0.0015
                     push rax
               ; LHS
                  ; Variable Declaration - y
                     mov rax, qword [rbp - 136]  ; __main__block__27__y
               pop rdx ; rhs value
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
                           ; Identifier - float x
                              push qword [rbp - 128]
                        ; RHS
                           ; Identifier - float y
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
                                    mov rax, qword [.float2] ; 64.0
                                    push rax
                              ; RHS
                                 ; Float Literal
                                    mov rax, qword [.float3] ; 8.123
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
                              mov rax, qword [.float4] ; 0.63001
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
                              mov rax, qword [.float5] ; 3.14
                              push rax
                        pop rdx
                        ; Implemented as multiplying by -1.0
                        movsd xmm1, qword [__builtin__neg] ; -1.0
                        movq xmm0, rdx
                        mulsd xmm0, xmm1 ; v = v * -1.0
                        movq rax, xmm0
                        push rax ; push result
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
                              mov rax, qword [.float6] ; 3.14159
                              push rax
                        ; RHS
                           ; Float Literal
                              mov rax, qword [.float7] ; 1.234
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
                              mov rax, qword [.float8] ; 1.5943
                              push rax
                        ; RHS
                           ; Float Literal
                              mov rax, qword [.float9] ; 2.0
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
                              mov rax, qword [.float10] ; 4.3e-05
                              push rax
                        ; RHS
                           ; Float Literal
                              mov rax, qword [.float11] ; 100000.0
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
                              mov rax, qword [.float12] ; 42.5
                              push rax
                        ; RHS
                           ; Float Literal
                              mov rax, qword [.float13] ; 2.0
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
                              mov rax, qword [.float14] ; 12.5
                              push rax
                        ; RHS
                           ; Float Literal
                              mov rax, qword [.float15] ; 0.125
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
         ; Function Call - println(char[]) -> void
            ; Make space for 1 arg(s)
            sub rsp, 8
            ; Arguments
               ; Eval arg0
                  ; String Literal
                     ; "=== Testing Assignment Arithmetic ==="
                     mov rax, .str55
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
                  ; Int Literal
                     mov rax, 21
                     push rax
               ; LHS
                  ; Variable Declaration - x
                     mov rax, qword [rbp - 144]  ; __main__block__28__x
               pop rdx ; rhs value
               mov qword [rbp - 144], rdx
               push rdx
            ; Statement results can be ignored
            pop rdx
            ; Function Call - print(char[]) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; String Literal
                        ; "int x = 21; => "
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
            ; Function Call - println(int) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; Identifier - int x
                        push qword [rbp - 144]
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
                  ; Float Literal
                     mov rax, qword [.float16] ; 3.14
                     push rax
               ; LHS
                  ; Variable Declaration - y
                     mov rax, qword [rbp - 152]  ; __main__block__28__y
               pop rdx ; rhs value
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
                        ; "float y = 3.14; => "
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
            ; Function Call - println(float) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; Identifier - float y
                        push qword [rbp - 152]
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
            ; Assignment - '='
               ; RHS
                  ; Float Literal
                     mov rax, qword [.float17] ; 0.0021
                     push rax
               pop rdx ; rhs value
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
                        ; "y = 0.0021; => "
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
            ; Function Call - println(float) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; Identifier - float y
                        push qword [rbp - 152]
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
            ; Assignment - '='
               ; RHS
                  ; Char Literal
                     push 'A'
               ; LHS
                  ; Variable Declaration - c
                     mov rax, qword [rbp - 160]  ; __main__block__28__c
               pop rdx ; rhs value
               mov byte [rbp - 160], dl
               push rdx
            ; Statement results can be ignored
            pop rdx
            ; Function Call - print(char[]) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; String Literal
                        ; "char c = 'A'; => "
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
            ; Function Call - println(char) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; Identifier - char c
                        push qword [rbp - 160]
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
            ; Assignment - '='
               ; RHS
                  ; Char Literal
                     push 'm'
               pop rdx ; rhs value
               mov byte [rbp - 160], dl
               push rdx
            ; Statement results can be ignored
            pop rdx
            ; Function Call - print(char[]) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; String Literal
                        ; "c = 'm'; => "
                        mov rax, .str60
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
            ; Function Call - println(char) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; Identifier - char c
                        push qword [rbp - 160]
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
            ; Function Call - print(char[]) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; String Literal
                        ; "print(c = 'y') => "
                        mov rax, .str61
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
            ; Function Call - println(char) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; Assignment - '='
                        ; RHS
                           ; Char Literal
                              push 'y'
                        pop rdx ; rhs value
                        mov byte [rbp - 160], dl
                        push rdx
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
            ; Assignment - '='
               ; RHS
                  ; Int Literal
                     mov rax, 16
                     push rax
               ; LHS
                  ; Variable Declaration - a
                     mov rax, qword [rbp - 168]  ; __main__block__28__a
               pop rdx ; rhs value
               mov qword [rbp - 168], rdx
               push rdx
            ; Statement results can be ignored
            pop rdx
            ; Function Call - print(char[]) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; String Literal
                        ; "a = 16; ++a => "
                        mov rax, .str62
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
                     ; Pre-Increment - int
                        ; RHS
                           ; Identifier - int a
                              push qword [rbp - 168]
                        pop rdx
                        add qword [rbp - 168], 1
                        mov rax, qword [rbp - 168]
                        push rax ; push result
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
                        ; "a => "
                        mov rax, .str63
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
                     ; Identifier - int a
                        push qword [rbp - 168]
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
                  ; Float Literal
                     mov rax, qword [.float18] ; 3.14
                     push rax
               ; LHS
                  ; Variable Declaration - b
                     mov rax, qword [rbp - 176]  ; __main__block__28__b
               pop rdx ; rhs value
               mov qword [rbp - 176], rdx
               push rdx
            ; Statement results can be ignored
            pop rdx
            ; Function Call - print(char[]) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; String Literal
                        ; "b = 3.14; ++b => "
                        mov rax, .str64
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
                     ; Pre-Increment - float
                        ; RHS
                           ; Identifier - float b
                              push qword [rbp - 176]
                        pop rdx
                        movsd xmm0, qword [.floatOne] ; xmm0 = 1.0, zero
                        addsd xmm0, qword [rbp - 176] ; rhs + 1.0
                        movsd qword [rbp - 176], xmm0 ; update rhs
                        mov rax, qword [rbp - 176] ; return rhs
                        push rax ; push result
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
                        ; "b => "
                        mov rax, .str65
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
                     ; Identifier - float b
                        push qword [rbp - 176]
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
            ; Assignment - '='
               ; RHS
                  ; Int Literal
                     mov rax, 42
                     push rax
               pop rdx ; rhs value
               mov qword [rbp - 168], rdx
               push rdx
            ; Statement results can be ignored
            pop rdx
            ; Function Call - print(char[]) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; String Literal
                        ; "a = 42; a++ => "
                        mov rax, .str66
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
                     ; Post-Increment
                        mov rax, qword [rbp - 168]
                        add qword [rbp - 168], 1
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
                        ; "a => "
                        mov rax, .str67
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
                     ; Identifier - int a
                        push qword [rbp - 168]
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
                  ; Float Literal
                     mov rax, qword [.float19] ; 6.28
                     push rax
               pop rdx ; rhs value
               mov qword [rbp - 176], rdx
               push rdx
            ; Statement results can be ignored
            pop rdx
            ; Function Call - print(char[]) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; String Literal
                        ; "b = 6.28; b++ => "
                        mov rax, .str68
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
                     ; Post-Increment
                        movsd xmm0, qword [rbp - 176] ; xmm0 = mem[0], zero
                        movsd xmm2, qword [.floatOne] ; xmm2 = 1.0, zero
                        movaps xmm1, xmm0
                        addsd xmm1, xmm2
                        movsd qword [rbp - 176], xmm1 ; update lhs
                        movq rax, xmm0 ; return lhs
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
                        ; "b => "
                        mov rax, .str69
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
                     ; Identifier - float b
                        push qword [rbp - 176]
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
            ; Assignment - '='
               ; RHS
                  ; Int Literal
                     mov rax, 16
                     push rax
               pop rdx ; rhs value
               mov qword [rbp - 168], rdx
               push rdx
            ; Statement results can be ignored
            pop rdx
            ; Function Call - print(char[]) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; String Literal
                        ; "a = 16; --a => "
                        mov rax, .str70
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
                     ; Pre-Decrement - int
                        ; RHS
                           ; Identifier - int a
                              push qword [rbp - 168]
                        pop rdx
                        sub qword [rbp - 168], 1
                        mov rax, qword [rbp - 168]
                        push rax ; push result
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
                        ; "a => "
                        mov rax, .str71
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
                     ; Identifier - int a
                        push qword [rbp - 168]
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
                  ; Float Literal
                     mov rax, qword [.float20] ; 3.14
                     push rax
               pop rdx ; rhs value
               mov qword [rbp - 176], rdx
               push rdx
            ; Statement results can be ignored
            pop rdx
            ; Function Call - print(char[]) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; String Literal
                        ; "b = 3.14; --b => "
                        mov rax, .str72
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
                     ; Pre-Decrement - float
                        ; RHS
                           ; Identifier - float b
                              push qword [rbp - 176]
                        pop rdx
                        movsd xmm0, qword [.floatNegOne] ; xmm0 = -1.0, zero
                        addsd xmm0, qword [rbp - 176] ; rhs + -1.0
                        movsd qword [rbp - 176], xmm0 ; update rhs
                        mov rax, qword [rbp - 176] ; return rhs
                        push rax ; push result
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
                        ; "b => "
                        mov rax, .str73
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
                     ; Identifier - float b
                        push qword [rbp - 176]
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
            ; Assignment - '='
               ; RHS
                  ; Int Literal
                     mov rax, 42
                     push rax
               pop rdx ; rhs value
               mov qword [rbp - 168], rdx
               push rdx
            ; Statement results can be ignored
            pop rdx
            ; Function Call - print(char[]) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; String Literal
                        ; "a = 42; a-- => "
                        mov rax, .str74
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
                     ; Post-Decrement
                        mov rax, qword [rbp - 168]
                        sub qword [rbp - 168], 1
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
                        ; "a => "
                        mov rax, .str75
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
                     ; Identifier - int a
                        push qword [rbp - 168]
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
                  ; Float Literal
                     mov rax, qword [.float21] ; -6.28
                     push rax
               pop rdx ; rhs value
               mov qword [rbp - 176], rdx
               push rdx
            ; Statement results can be ignored
            pop rdx
            ; Function Call - print(char[]) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; String Literal
                        ; "b = -6.28; b-- => "
                        mov rax, .str76
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
                     ; Post-Decrement
                        movsd xmm0, qword [rbp - 176] ; xmm0 = mem[0], zero
                        movsd xmm2, qword [.floatNegOne] ; xmm2 = -1.0, zero
                        movaps xmm1, xmm0
                        addsd xmm1, xmm2
                        movsd qword [rbp - 176], xmm1 ; update lhs
                        movq rax, xmm0 ; return lhs
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
                        ; "b => "
                        mov rax, .str77
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
                     ; Identifier - float b
                        push qword [rbp - 176]
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
                        ; "a = 32; a += 63 => "
                        mov rax, .str78
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
                  ; Int Literal
                     mov rax, 32
                     push rax
               pop rdx ; rhs value
               mov qword [rbp - 168], rdx
               push rdx
            ; Statement results can be ignored
            pop rdx
            ; Function Call - println(int) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; Assignment - '+='
                        ; RHS
                           ; Int Literal
                              mov rax, 63
                              push rax
                        pop rdx ; rhs value
                        mov rax, qword [rbp - 168] ; read lhs value
                        add rax, rdx      ; add lhs and rhs
                        mov qword [rbp - 168], rax ; write back to lhs
                        push rax          ; push result for other expressions
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
                        ; "b = 3.14; b += 0.25 => "
                        mov rax, .str79
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
                  ; Float Literal
                     mov rax, qword [.float22] ; 3.14
                     push rax
               pop rdx ; rhs value
               mov qword [rbp - 176], rdx
               push rdx
            ; Statement results can be ignored
            pop rdx
            ; Function Call - println(float) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; Assignment - '+='
                        ; RHS
                           ; Float Literal
                              mov rax, qword [.float23] ; 0.25
                              push rax
                        pop rdx ; rhs value
                        movq xmm0, rdx    ; load rhs value, xmm0 = mem[0], zero
                        addsd xmm0, qword [rbp - 176] ; add lhs and rhs
                        movsd qword [rbp - 176], xmm0 ; write back to lhs
                        movq rax, xmm0
                        push rax          ; push result for other expressions
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
                        ; "a = 32; a -= 47 => "
                        mov rax, .str80
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
                  ; Int Literal
                     mov rax, 32
                     push rax
               pop rdx ; rhs value
               mov qword [rbp - 168], rdx
               push rdx
            ; Statement results can be ignored
            pop rdx
            ; Function Call - println(int) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; Assignment - '-='
                        ; RHS
                           ; Int Literal
                              mov rax, 47
                              push rax
                        pop rdx ; rhs value
                        mov rax, qword [rbp - 168] ; read lhs value
                        sub rax, rdx      ; lhs = lhs - rhs
                        mov qword [rbp - 168], rax ; write back to lhs
                        push rax          ; push result for other expressions
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
                        ; "b = -3.14; b -= 1.21 => "
                        mov rax, .str81
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
                  ; Float Literal
                     mov rax, qword [.float24] ; -3.14
                     push rax
               pop rdx ; rhs value
               mov qword [rbp - 176], rdx
               push rdx
            ; Statement results can be ignored
            pop rdx
            ; Function Call - println(float) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; Assignment - '-='
                        ; RHS
                           ; Float Literal
                              mov rax, qword [.float25] ; 1.21
                              push rax
                        pop rdx ; rhs value
                        movq xmm0, qword [rbp - 176] ; load lhs value, xmm0 = mem[0], zero
                        movq xmm1, rdx ; load rhs value, xmm1 = mem[0], zero
                        subsd xmm0, xmm1 ; lhs = lhs - rhs
                        movsd qword [rbp - 176], xmm0 ; write back to lhs
                        movq rax, xmm0
                        push rax          ; push result for other expressions
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
                        ; "a = 2; a *= 16 => "
                        mov rax, .str82
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
                  ; Int Literal
                     mov rax, 2
                     push rax
               pop rdx ; rhs value
               mov qword [rbp - 168], rdx
               push rdx
            ; Statement results can be ignored
            pop rdx
            ; Function Call - println(int) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; Assignment - '*='
                        ; RHS
                           ; Int Literal
                              mov rax, 16
                              push rax
                        pop rdx ; rhs value
                        mov rax, qword [rbp - 168] ; read lhs value
                        imul rax, rdx      ; lhs = lhs * rhs
                        mov qword [rbp - 168], rax ; write back to lhs
                        push rax          ; push result for other expressions
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
                        ; "b = 0.5; b *= 57.0 => "
                        mov rax, .str83
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
                  ; Float Literal
                     mov rax, qword [.float26] ; 0.5
                     push rax
               pop rdx ; rhs value
               mov qword [rbp - 176], rdx
               push rdx
            ; Statement results can be ignored
            pop rdx
            ; Function Call - println(float) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; Assignment - '*='
                        ; RHS
                           ; Float Literal
                              mov rax, qword [.float27] ; 57.0
                              push rax
                        pop rdx ; rhs value
                        movq xmm0, qword [rbp - 176] ; load lhs value, xmm0 = mem[0], zero
                        movq xmm1, rdx ; load rhs value, xmm1 = mem[0], zero
                        mulsd xmm0, xmm1 ; lhs = lhs * rhs
                        movsd qword [rbp - 176], xmm0 ; write back to lhs
                        movq rax, xmm0
                        push rax          ; push result for other expressions
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
                        ; "a = 256; a /= 64 => "
                        mov rax, .str84
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
                  ; Int Literal
                     mov rax, 256
                     push rax
               pop rdx ; rhs value
               mov qword [rbp - 168], rdx
               push rdx
            ; Statement results can be ignored
            pop rdx
            ; Function Call - println(int) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; Assignment - '/='
                        ; RHS
                           ; Int Literal
                              mov rax, 64
                              push rax
                        pop rdx ; rhs value
                        mov rax, qword [rbp - 168] ; read lhs value
                        mov esi, edx
                        mov edx, 0
                        cdq
                        idiv esi ; lhs = lhs / rhs
                        mov qword [rbp - 168], rax ; write back to lhs
                        push rax          ; push result for other expressions
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
                        ; "a = 256; a /= 65 => "
                        mov rax, .str85
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
                  ; Int Literal
                     mov rax, 256
                     push rax
               pop rdx ; rhs value
               mov qword [rbp - 168], rdx
               push rdx
            ; Statement results can be ignored
            pop rdx
            ; Function Call - println(int) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; Assignment - '/='
                        ; RHS
                           ; Int Literal
                              mov rax, 65
                              push rax
                        pop rdx ; rhs value
                        mov rax, qword [rbp - 168] ; read lhs value
                        mov esi, edx
                        mov edx, 0
                        cdq
                        idiv esi ; lhs = lhs / rhs
                        mov qword [rbp - 168], rax ; write back to lhs
                        push rax          ; push result for other expressions
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
                        ; "b = 25.0; b /= 3.0 => "
                        mov rax, .str86
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
                  ; Float Literal
                     mov rax, qword [.float28] ; 25.0
                     push rax
               pop rdx ; rhs value
               mov qword [rbp - 176], rdx
               push rdx
            ; Statement results can be ignored
            pop rdx
            ; Function Call - println(float) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; Assignment - '/='
                        ; RHS
                           ; Float Literal
                              mov rax, qword [.float29] ; 3.0
                              push rax
                        pop rdx ; rhs value
                        movq xmm0, qword [rbp - 176] ; load lhs value, xmm0 = mem[0], zero
                        movq xmm1, rdx      ; load rhs value, xmm1 = mem[0], zero
                        divsd xmm0, xmm1    ; lhs = lhs / rhs
                        movsd qword [rbp - 176], xmm0 ; write back to lhs
                        movq rax, xmm0
                        push rax          ; push result for other expressions
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
                        ; "b = 0.435; b /= 435.0 => "
                        mov rax, .str87
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
                  ; Float Literal
                     mov rax, qword [.float30] ; 0.435
                     push rax
               pop rdx ; rhs value
               mov qword [rbp - 176], rdx
               push rdx
            ; Statement results can be ignored
            pop rdx
            ; Function Call - println(float) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; Assignment - '/='
                        ; RHS
                           ; Float Literal
                              mov rax, qword [.float31] ; 435.0
                              push rax
                        pop rdx ; rhs value
                        movq xmm0, qword [rbp - 176] ; load lhs value, xmm0 = mem[0], zero
                        movq xmm1, rdx      ; load rhs value, xmm1 = mem[0], zero
                        divsd xmm0, xmm1    ; lhs = lhs / rhs
                        movsd qword [rbp - 176], xmm0 ; write back to lhs
                        movq rax, xmm0
                        push rax          ; push result for other expressions
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
                        ; "a = 2352; a %= 2 => "
                        mov rax, .str88
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
                  ; Int Literal
                     mov rax, 2352
                     push rax
               pop rdx ; rhs value
               mov qword [rbp - 168], rdx
               push rdx
            ; Statement results can be ignored
            pop rdx
            ; Function Call - println(int) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; Assignment - '%='
                        ; RHS
                           ; Int Literal
                              mov rax, 2
                              push rax
                        pop rdx ; rhs value
                        mov rax, qword [rbp - 168] ; read lhs value
                        mov esi, edx
                        mov edx, 0
                        cdq
                        idiv esi ; lhs = lhs / rhs
                        mov qword [rbp - 168], rdx ; write back to lhs
                        push rdx          ; push result for other expressions
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
                        ; "a = 137; a %= 3 => "
                        mov rax, .str89
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
                  ; Int Literal
                     mov rax, 137
                     push rax
               pop rdx ; rhs value
               mov qword [rbp - 168], rdx
               push rdx
            ; Statement results can be ignored
            pop rdx
            ; Function Call - println(int) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; Assignment - '%='
                        ; RHS
                           ; Int Literal
                              mov rax, 3
                              push rax
                        pop rdx ; rhs value
                        mov rax, qword [rbp - 168] ; read lhs value
                        mov esi, edx
                        mov edx, 0
                        cdq
                        idiv esi ; lhs = lhs / rhs
                        mov qword [rbp - 168], rdx ; write back to lhs
                        push rdx          ; push result for other expressions
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
                        ; "a = 2353; a %= 5 => "
                        mov rax, .str90
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
                  ; Int Literal
                     mov rax, 2353
                     push rax
               pop rdx ; rhs value
               mov qword [rbp - 168], rdx
               push rdx
            ; Statement results can be ignored
            pop rdx
            ; Function Call - println(int) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; Assignment - '%='
                        ; RHS
                           ; Int Literal
                              mov rax, 5
                              push rax
                        pop rdx ; rhs value
                        mov rax, qword [rbp - 168] ; read lhs value
                        mov esi, edx
                        mov edx, 0
                        cdq
                        idiv esi ; lhs = lhs / rhs
                        mov qword [rbp - 168], rdx ; write back to lhs
                        push rdx          ; push result for other expressions
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
                        ; "a = -7; a %= 2 => "
                        mov rax, .str91
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
                  ; Int Literal
                     mov rax, -7
                     push rax
               pop rdx ; rhs value
               mov qword [rbp - 168], rdx
               push rdx
            ; Statement results can be ignored
            pop rdx
            ; Function Call - println(int) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; Assignment - '%='
                        ; RHS
                           ; Int Literal
                              mov rax, 2
                              push rax
                        pop rdx ; rhs value
                        mov rax, qword [rbp - 168] ; read lhs value
                        mov esi, edx
                        mov edx, 0
                        cdq
                        idiv esi ; lhs = lhs / rhs
                        mov qword [rbp - 168], rdx ; write back to lhs
                        push rdx          ; push result for other expressions
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
                     ; "=== Testing Equality ==="
                     mov rax, .str92
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
         ; Function Call - println(char[]) -> void
            ; Make space for 1 arg(s)
            sub rsp, 8
            ; Arguments
               ; Eval arg0
                  ; String Literal
                     ; "=== Testing Inequality ==="
                     mov rax, .str93
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
         ; Function Call - println(char[]) -> void
            ; Make space for 1 arg(s)
            sub rsp, 8
            ; Arguments
               ; Eval arg0
                  ; String Literal
                     ; "=== Testing Arrays ==="
                     mov rax, .str94
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
                  ; Array Constructor
                     ; Elements
                     ; Int Literal
                        mov rax, 7
                        push rax
                     ; Int Literal
                        mov rax, 3
                        push rax
                     ; Int Literal
                        mov rax, 19
                        push rax
                     ; Int Literal
                        mov rax, -42
                        push rax
                     mov edi, 32 ; number of bytes to allocate (nArgs * 8bytes)
                     call malloc ; allocates edi bytes on heap and stores pointer in rax
                     ; Populate array values
                     pop rdx ; get array element 3
                     mov qword [rax + 24], rdx ; arr[3] = rdx
                     pop rdx ; get array element 2
                     mov qword [rax + 16], rdx ; arr[2] = rdx
                     pop rdx ; get array element 1
                     mov qword [rax + 8], rdx ; arr[1] = rdx
                     pop rdx ; get array element 0
                     mov qword [rax + 0], rdx ; arr[0] = rdx
                     push rax
               ; LHS
                  ; Variable Declaration - nums
                     mov rax, qword [rbp - 184]  ; __main__block__29__nums
               pop rdx ; rhs value
               mov qword [rbp - 184], rdx
               push rdx
            ; Statement results can be ignored
            pop rdx
            ; Function Call - println(char[]) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; String Literal
                        ; "int[] nums = [7, 3, 19, -42];"
                        mov rax, .str95
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
            ; Assignment - '='
               ; RHS
                  ; Array Constructor
                     ; Elements
                     ; Float Literal
                        mov rax, qword [.float32] ; 3.14
                        push rax
                     ; Float Literal
                        mov rax, qword [.float33] ; 0.25
                        push rax
                     ; Float Literal
                        mov rax, qword [.float34] ; 2.0
                        push rax
                     ; Float Literal
                        mov rax, qword [.float35] ; 6.28
                        push rax
                     mov edi, 32 ; number of bytes to allocate (nArgs * 8bytes)
                     call malloc ; allocates edi bytes on heap and stores pointer in rax
                     ; Populate array values
                     pop rdx ; get array element 3
                     mov qword [rax + 24], rdx ; arr[3] = rdx
                     pop rdx ; get array element 2
                     mov qword [rax + 16], rdx ; arr[2] = rdx
                     pop rdx ; get array element 1
                     mov qword [rax + 8], rdx ; arr[1] = rdx
                     pop rdx ; get array element 0
                     mov qword [rax + 0], rdx ; arr[0] = rdx
                     push rax
               ; LHS
                  ; Variable Declaration - floats
                     mov rax, qword [rbp - 192]  ; __main__block__29__floats
               pop rdx ; rhs value
               mov qword [rbp - 192], rdx
               push rdx
            ; Statement results can be ignored
            pop rdx
            ; Function Call - println(char[]) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; String Literal
                        ; "float[] floats = [3.14, 0.25, 2.0, 6.28];"
                        mov rax, .str96
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
            ; Assignment - '='
               ; RHS
                  ; Array Constructor
                     ; Elements
                     ; Char Literal
                        push 'H'
                     ; Char Literal
                        push 'e'
                     ; Char Literal
                        push 'l'
                     ; Char Literal
                        push 'l'
                     ; Char Literal
                        push 'o'
                     mov edi, 5 ; number of bytes to allocate (nArgs * 1byte (char))
                     call malloc ; allocates edi bytes on heap and stores pointer in rax
                     ; Populate array values
                     pop rdx ; get array element 4
                     mov byte [rax + 4], dl ; arr[4] = rdx
                     pop rdx ; get array element 3
                     mov byte [rax + 3], dl ; arr[3] = rdx
                     pop rdx ; get array element 2
                     mov byte [rax + 2], dl ; arr[2] = rdx
                     pop rdx ; get array element 1
                     mov byte [rax + 1], dl ; arr[1] = rdx
                     pop rdx ; get array element 0
                     mov byte [rax + 0], dl ; arr[0] = rdx
                     push rax
               ; LHS
                  ; Variable Declaration - str
                     mov rax, qword [rbp - 200]  ; __main__block__29__str
               pop rdx ; rhs value
               mov qword [rbp - 200], rdx
               push rdx
            ; Statement results can be ignored
            pop rdx
            ; Function Call - println(char[]) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; String Literal
                        ; "char[] str = ['H', 'e', 'l', 'l', 'o'];"
                        mov rax, .str97
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
            ; Assignment - '='
               ; RHS
                  ; Array Allocator
                     ; Int Literal
                        mov rax, 3
                        push rax
                     pop rdx ; num elements for dimension[0]
                     imul rdx, 8 ; 8 bytes per element
                     mov rdi, rdx ; num bytes to allocate
                     call malloc ; allocates edi bytes on heap and stores pointer in rax
                     push rax ; __ptr
               ; LHS
                  ; Variable Declaration - ints
                     mov rax, qword [rbp - 208]  ; __main__block__29__ints
               pop rdx ; rhs value
               mov qword [rbp - 208], rdx
               push rdx
            ; Statement results can be ignored
            pop rdx
            ; Function Call - println(char[]) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; String Literal
                        ; "int[] ints = new int[3];"
                        mov rax, .str98
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
            ; Function Call - print(char[]) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; String Literal
                        ; "nums[0] => "
                        mov rax, .str99
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
                     ; Subscript
                        ; LHS
                           ; Identifier - int[] nums
                              push qword [rbp - 184]
                        ; OFFSET
                           ; Int Literal
                              mov rax, 0
                              push rax
                        pop rdx ; __offset
                        pop rax ; __pointer
                        push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
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
                        ; "nums[1] => "
                        mov rax, .str100
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
                     ; Subscript
                        ; LHS
                           ; Identifier - int[] nums
                              push qword [rbp - 184]
                        ; OFFSET
                           ; Int Literal
                              mov rax, 1
                              push rax
                        pop rdx ; __offset
                        pop rax ; __pointer
                        push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
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
                        ; "nums[2] => "
                        mov rax, .str101
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
                     ; Subscript
                        ; LHS
                           ; Identifier - int[] nums
                              push qword [rbp - 184]
                        ; OFFSET
                           ; Int Literal
                              mov rax, 2
                              push rax
                        pop rdx ; __offset
                        pop rax ; __pointer
                        push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
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
                        ; "nums[3] => "
                        mov rax, .str102
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
                     ; Subscript
                        ; LHS
                           ; Identifier - int[] nums
                              push qword [rbp - 184]
                        ; OFFSET
                           ; Int Literal
                              mov rax, 3
                              push rax
                        pop rdx ; __offset
                        pop rax ; __pointer
                        push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
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
                        ; "floats[0] => "
                        mov rax, .str103
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
                     ; Subscript
                        ; LHS
                           ; Identifier - float[] floats
                              push qword [rbp - 192]
                        ; OFFSET
                           ; Int Literal
                              mov rax, 0
                              push rax
                        pop rdx ; __offset
                        pop rax ; __pointer
                        push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
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
                        ; "floats[1] => "
                        mov rax, .str104
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
                     ; Subscript
                        ; LHS
                           ; Identifier - float[] floats
                              push qword [rbp - 192]
                        ; OFFSET
                           ; Int Literal
                              mov rax, 1
                              push rax
                        pop rdx ; __offset
                        pop rax ; __pointer
                        push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
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
                        ; "floats[2] => "
                        mov rax, .str105
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
                     ; Subscript
                        ; LHS
                           ; Identifier - float[] floats
                              push qword [rbp - 192]
                        ; OFFSET
                           ; Int Literal
                              mov rax, 2
                              push rax
                        pop rdx ; __offset
                        pop rax ; __pointer
                        push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
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
                        ; "floats[3] => "
                        mov rax, .str106
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
                     ; Subscript
                        ; LHS
                           ; Identifier - float[] floats
                              push qword [rbp - 192]
                        ; OFFSET
                           ; Int Literal
                              mov rax, 3
                              push rax
                        pop rdx ; __offset
                        pop rax ; __pointer
                        push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
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
                        ; "str[0] => "
                        mov rax, .str107
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
            ; Function Call - println(char) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; Subscript
                        ; LHS
                           ; Identifier - char[] str
                              push qword [rbp - 200]
                        ; OFFSET
                           ; Int Literal
                              mov rax, 0
                              push rax
                        pop rdx ; __offset
                        pop rax ; __pointer
                        push qword [rax + rdx] ; pointer + sizeof(data_t) * offset
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
            ; Function Call - print(char[]) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; String Literal
                        ; "str[1] => "
                        mov rax, .str108
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
            ; Function Call - println(char) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; Subscript
                        ; LHS
                           ; Identifier - char[] str
                              push qword [rbp - 200]
                        ; OFFSET
                           ; Int Literal
                              mov rax, 1
                              push rax
                        pop rdx ; __offset
                        pop rax ; __pointer
                        push qword [rax + rdx] ; pointer + sizeof(data_t) * offset
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
            ; Function Call - print(char[]) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; String Literal
                        ; "str[2] => "
                        mov rax, .str109
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
            ; Function Call - println(char) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; Subscript
                        ; LHS
                           ; Identifier - char[] str
                              push qword [rbp - 200]
                        ; OFFSET
                           ; Int Literal
                              mov rax, 2
                              push rax
                        pop rdx ; __offset
                        pop rax ; __pointer
                        push qword [rax + rdx] ; pointer + sizeof(data_t) * offset
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
            ; Function Call - print(char[]) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; String Literal
                        ; "str[3] => "
                        mov rax, .str110
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
            ; Function Call - println(char) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; Subscript
                        ; LHS
                           ; Identifier - char[] str
                              push qword [rbp - 200]
                        ; OFFSET
                           ; Int Literal
                              mov rax, 3
                              push rax
                        pop rdx ; __offset
                        pop rax ; __pointer
                        push qword [rax + rdx] ; pointer + sizeof(data_t) * offset
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
            ; Function Call - print(char[]) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; String Literal
                        ; "str[4] => "
                        mov rax, .str111
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
            ; Function Call - println(char) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; Subscript
                        ; LHS
                           ; Identifier - char[] str
                              push qword [rbp - 200]
                        ; OFFSET
                           ; Int Literal
                              mov rax, 4
                              push rax
                        pop rdx ; __offset
                        pop rax ; __pointer
                        push qword [rax + rdx] ; pointer + sizeof(data_t) * offset
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
            ; Function Call - print(char[]) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; String Literal
                        ; "println (str); => "
                        mov rax, .str112
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
            ; Function Call - println(char[]) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; Identifier - char[] str
                        push qword [rbp - 200]
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
            ; Function Call - print(char[]) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; String Literal
                        ; "ints[0] => "
                        mov rax, .str113
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
                     ; Subscript
                        ; LHS
                           ; Identifier - int[] ints
                              push qword [rbp - 208]
                        ; OFFSET
                           ; Int Literal
                              mov rax, 0
                              push rax
                        pop rdx ; __offset
                        pop rax ; __pointer
                        push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
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
                        ; "ints[1] => "
                        mov rax, .str114
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
                     ; Subscript
                        ; LHS
                           ; Identifier - int[] ints
                              push qword [rbp - 208]
                        ; OFFSET
                           ; Int Literal
                              mov rax, 1
                              push rax
                        pop rdx ; __offset
                        pop rax ; __pointer
                        push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
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
                        ; "ints[2] => "
                        mov rax, .str115
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
                     ; Subscript
                        ; LHS
                           ; Identifier - int[] ints
                              push qword [rbp - 208]
                        ; OFFSET
                           ; Int Literal
                              mov rax, 2
                              push rax
                        pop rdx ; __offset
                        pop rax ; __pointer
                        push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
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
                        ; "nums[2] = -17; => "
                        mov rax, .str116
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
                     ; Assignment - '='
                        ; RHS
                           ; Int Literal
                              mov rax, -17
                              push rax
                        ; LHS
                           ; Subscript assignment
                              ; LHS
                                 ; Identifier - int[] nums
                                    push qword [rbp - 184]
                              ; OFFSET
                                 ; Int Literal
                                    mov rax, 2
                                    push rax
                              pop rdi ; __offset
                              pop rbx ; __pointer
                        pop rdx ; rhs value
                        mov qword [rbx + 8*rdi], rdx
                        push rdx
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
                        ; "nums[2] => "
                        mov rax, .str117
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
                     ; Subscript
                        ; LHS
                           ; Identifier - int[] nums
                              push qword [rbp - 184]
                        ; OFFSET
                           ; Int Literal
                              mov rax, 2
                              push rax
                        pop rdx ; __offset
                        pop rax ; __pointer
                        push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
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
                        ; "floats[1] = 123.456; => "
                        mov rax, .str118
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
                     ; Assignment - '='
                        ; RHS
                           ; Float Literal
                              mov rax, qword [.float36] ; 123.456
                              push rax
                        ; LHS
                           ; Subscript assignment
                              ; LHS
                                 ; Identifier - float[] floats
                                    push qword [rbp - 192]
                              ; OFFSET
                                 ; Int Literal
                                    mov rax, 1
                                    push rax
                              pop rdi ; __offset
                              pop rbx ; __pointer
                        pop rdx ; rhs value
                        mov qword [rbx + 8*rdi], rdx
                        push rdx
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
                        ; "floats[1] => "
                        mov rax, .str119
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
                     ; Subscript
                        ; LHS
                           ; Identifier - float[] floats
                              push qword [rbp - 192]
                        ; OFFSET
                           ; Int Literal
                              mov rax, 1
                              push rax
                        pop rdx ; __offset
                        pop rax ; __pointer
                        push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
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
                        ; "str[0] = 'A' => "
                        mov rax, .str120
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
            ; Function Call - println(char) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; Assignment - '='
                        ; RHS
                           ; Char Literal
                              push 'A'
                        ; LHS
                           ; Subscript assignment
                              ; LHS
                                 ; Identifier - char[] str
                                    push qword [rbp - 200]
                              ; OFFSET
                                 ; Int Literal
                                    mov rax, 0
                                    push rax
                              pop rdi ; __offset
                              pop rbx ; __pointer
                        pop rdx ; rhs value
                        mov byte [rbx + rdi], dl
                        push rdx
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
            ; Function Call - print(char[]) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; String Literal
                        ; "str[0] => "
                        mov rax, .str121
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
            ; Function Call - println(char) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; Subscript
                        ; LHS
                           ; Identifier - char[] str
                              push qword [rbp - 200]
                        ; OFFSET
                           ; Int Literal
                              mov rax, 0
                              push rax
                        pop rdx ; __offset
                        pop rax ; __pointer
                        push qword [rax + rdx] ; pointer + sizeof(data_t) * offset
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
            ; Function Call - print(char[]) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; String Literal
                        ; "str[1] = 'm' => "
                        mov rax, .str122
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
            ; Function Call - println(char) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; Assignment - '='
                        ; RHS
                           ; Char Literal
                              push 'm'
                        ; LHS
                           ; Subscript assignment
                              ; LHS
                                 ; Identifier - char[] str
                                    push qword [rbp - 200]
                              ; OFFSET
                                 ; Int Literal
                                    mov rax, 1
                                    push rax
                              pop rdi ; __offset
                              pop rbx ; __pointer
                        pop rdx ; rhs value
                        mov byte [rbx + rdi], dl
                        push rdx
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
            ; Function Call - print(char[]) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; String Literal
                        ; "str[1] => "
                        mov rax, .str123
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
            ; Function Call - println(char) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; Subscript
                        ; LHS
                           ; Identifier - char[] str
                              push qword [rbp - 200]
                        ; OFFSET
                           ; Int Literal
                              mov rax, 1
                              push rax
                        pop rdx ; __offset
                        pop rax ; __pointer
                        push qword [rax + rdx] ; pointer + sizeof(data_t) * offset
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
            ; Function Call - print(char[]) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; String Literal
                        ; "str[2] = 'y' => "
                        mov rax, .str124
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
            ; Function Call - println(char) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; Assignment - '='
                        ; RHS
                           ; Char Literal
                              push 'y'
                        ; LHS
                           ; Subscript assignment
                              ; LHS
                                 ; Identifier - char[] str
                                    push qword [rbp - 200]
                              ; OFFSET
                                 ; Int Literal
                                    mov rax, 2
                                    push rax
                              pop rdi ; __offset
                              pop rbx ; __pointer
                        pop rdx ; rhs value
                        mov byte [rbx + rdi], dl
                        push rdx
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
            ; Function Call - print(char[]) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; String Literal
                        ; "str[2] => "
                        mov rax, .str125
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
            ; Function Call - println(char) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; Subscript
                        ; LHS
                           ; Identifier - char[] str
                              push qword [rbp - 200]
                        ; OFFSET
                           ; Int Literal
                              mov rax, 2
                              push rax
                        pop rdx ; __offset
                        pop rax ; __pointer
                        push qword [rax + rdx] ; pointer + sizeof(data_t) * offset
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
            ; Function Call - print(char[]) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; String Literal
                        ; "str[3] = '\\0' => "
                        mov rax, .str126
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
            ; Function Call - println(char) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; Assignment - '='
                        ; RHS
                           ; Char Literal
                              push 0 ; \0
                        ; LHS
                           ; Subscript assignment
                              ; LHS
                                 ; Identifier - char[] str
                                    push qword [rbp - 200]
                              ; OFFSET
                                 ; Int Literal
                                    mov rax, 3
                                    push rax
                              pop rdi ; __offset
                              pop rbx ; __pointer
                        pop rdx ; rhs value
                        mov byte [rbx + rdi], dl
                        push rdx
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
            ; Function Call - print(char[]) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; String Literal
                        ; "str[3] => "
                        mov rax, .str127
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
            ; Function Call - println(char) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; Subscript
                        ; LHS
                           ; Identifier - char[] str
                              push qword [rbp - 200]
                        ; OFFSET
                           ; Int Literal
                              mov rax, 3
                              push rax
                        pop rdx ; __offset
                        pop rax ; __pointer
                        push qword [rax + rdx] ; pointer + sizeof(data_t) * offset
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
            ; Function Call - print(char[]) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; String Literal
                        ; "str[4] => "
                        mov rax, .str128
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
            ; Function Call - println(char) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; Subscript
                        ; LHS
                           ; Identifier - char[] str
                              push qword [rbp - 200]
                        ; OFFSET
                           ; Int Literal
                              mov rax, 4
                              push rax
                        pop rdx ; __offset
                        pop rax ; __pointer
                        push qword [rax + rdx] ; pointer + sizeof(data_t) * offset
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
            ; Function Call - print(char[]) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; String Literal
                        ; "println (str); => "
                        mov rax, .str129
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
            ; Function Call - println(char[]) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; Identifier - char[] str
                        push qword [rbp - 200]
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
            ; Function Call - print(char[]) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; String Literal
                        ; "ints[0] = nums[0] => "
                        mov rax, .str130
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
                     ; Assignment - '='
                        ; RHS
                           ; Subscript
                              ; LHS
                                 ; Identifier - int[] nums
                                    push qword [rbp - 184]
                              ; OFFSET
                                 ; Int Literal
                                    mov rax, 0
                                    push rax
                              pop rdx ; __offset
                              pop rax ; __pointer
                              push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                        ; LHS
                           ; Subscript assignment
                              ; LHS
                                 ; Identifier - int[] ints
                                    push qword [rbp - 208]
                              ; OFFSET
                                 ; Int Literal
                                    mov rax, 0
                                    push rax
                              pop rdi ; __offset
                              pop rbx ; __pointer
                        pop rdx ; rhs value
                        mov qword [rbx + 8*rdi], rdx
                        push rdx
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
                        ; "ints[1] = nums[1] => "
                        mov rax, .str131
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
                     ; Assignment - '='
                        ; RHS
                           ; Subscript
                              ; LHS
                                 ; Identifier - int[] nums
                                    push qword [rbp - 184]
                              ; OFFSET
                                 ; Int Literal
                                    mov rax, 1
                                    push rax
                              pop rdx ; __offset
                              pop rax ; __pointer
                              push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                        ; LHS
                           ; Subscript assignment
                              ; LHS
                                 ; Identifier - int[] ints
                                    push qword [rbp - 208]
                              ; OFFSET
                                 ; Int Literal
                                    mov rax, 1
                                    push rax
                              pop rdi ; __offset
                              pop rbx ; __pointer
                        pop rdx ; rhs value
                        mov qword [rbx + 8*rdi], rdx
                        push rdx
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
                        ; "ints[2] = nums[2] => "
                        mov rax, .str132
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
                     ; Assignment - '='
                        ; RHS
                           ; Subscript
                              ; LHS
                                 ; Identifier - int[] nums
                                    push qword [rbp - 184]
                              ; OFFSET
                                 ; Int Literal
                                    mov rax, 2
                                    push rax
                              pop rdx ; __offset
                              pop rax ; __pointer
                              push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                        ; LHS
                           ; Subscript assignment
                              ; LHS
                                 ; Identifier - int[] ints
                                    push qword [rbp - 208]
                              ; OFFSET
                                 ; Int Literal
                                    mov rax, 2
                                    push rax
                              pop rdi ; __offset
                              pop rbx ; __pointer
                        pop rdx ; rhs value
                        mov qword [rbx + 8*rdi], rdx
                        push rdx
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
                     ; "=== Testing Array Cont ==="
                     mov rax, .str133
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
   ; =====================================================================
            ; Function Template - 
               ; Instances:
         ; ===============================================================
                  ; Function Declaration - printArray<:int:>(int[], int) -> void
                  ; Skip over function declaration
                  jmp .__end____main__block__30____printArray__int____int__1__int
.__main__block__30____printArray__int____int__1__int:
                     ; Function Header:
                        ; Setup stack frame
                           push rbp
                           mov rbp, rsp
                           sub rsp, 16
                        ; Parameters
                           ; Param: arr [rbp + 16]
                           ; Param: size [rbp + 24]
                        ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
                           ; [rbp - 8] - int i (<unset-scope-name>)

                     ; Body
               ;---------------------------------------------------------
                        ; Code Block
                           ; Function Call - print(char) -> void
                              ; Make space for 1 arg(s)
                              sub rsp, 8
                              ; Arguments
                                 ; Eval arg0
                                    ; Char Literal
                                       push '['
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
                  ;------------------------------------------------------
                           ; If-Statement
                              ; Condition
                                 ; Greater Than
                                    ; LHS
                                       ; Identifier - int size
                                          push qword [rbp - -24]
                                    ; RHS
                                       ; Int Literal
                                          mov rax, 0
                                          push rax
                                    pop rdx ; rhs
                                    pop rax ; lhs
                                    cmp rax, rdx
                                    setg al
                                    movzx eax, al
                                    push rax
                                 pop rdx ; __cond
                                 cmp rdx, 0 ; ensure condition is true
                                 je .__endif__32 ; jump to end
                              ; Body
                                 ; Function Call - print(int) -> void
                                    ; Make space for 1 arg(s)
                                    sub rsp, 8
                                    ; Arguments
                                       ; Eval arg0
                                          ; Subscript
                                             ; LHS
                                                ; Identifier - int[] arr
                                                   push qword [rbp - -16]
                                             ; OFFSET
                                                ; Int Literal
                                                   mov rax, 0
                                                   push rax
                                             pop rdx ; __offset
                                             pop rax ; __pointer
                                             push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
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
                              jmp .__endif__32 ; jump to end of condition chain
                              ; End of if
.__endif__32:
                  ;------------------------------------------------------
                  ;------------------------------------------------------
                           ; For-Loop
                           ; Init
                              ; Assignment - '='
                                 ; RHS
                                    ; Int Literal
                                       mov rax, 1
                                       push rax
                                 ; LHS
                                    ; Variable Declaration - i
                                       mov rax, qword [rbp - 8]  ; __main__block__30__printArray__block__31__for__33__i
                                 pop rdx ; rhs value
                                 mov qword [rbp - 8], rdx
                                 push rdx
                              ; Loop init result can be discarded
                              pop rax
                           jmp .__forcond__33
.__for__33:
                              ; Update
                                 ; Pre-Increment - int
                                    ; RHS
                                       ; Identifier - int i
                                          push qword [rbp - 8]
                                    pop rdx
                                    add qword [rbp - 8], 1
                                    mov rax, qword [rbp - 8]
                                    push rax ; push result
                                 ; Loop update result can be discarded
                                 pop rax
.__forcond__33:
                              ; Condition
                                 ; Less Than
                                    ; LHS
                                       ; Identifier - int i
                                          push qword [rbp - 8]
                                    ; RHS
                                       ; Identifier - int size
                                          push qword [rbp - -24]
                                    pop rdx ; rhs
                                    pop rax ; lhs
                                    cmp rax, rdx
                                    setl al
                                    movzx eax, al
                                    push rax
                                 pop rax ; __cond
                                 cmp rax, 0 ; __cond
                                 je .__endfor__33
                              ; Body
                        ;------------------------------------------------
                                 ; Code Block
                                    ; Function Call - print(char[]) -> void
                                       ; Make space for 1 arg(s)
                                       sub rsp, 8
                                       ; Arguments
                                          ; Eval arg0
                                             ; String Literal
                                                ; ", "
                                                mov rax, .str135
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
                                             ; Subscript
                                                ; LHS
                                                   ; Identifier - int[] arr
                                                      push qword [rbp - -16]
                                                ; OFFSET
                                                   ; Identifier - int i
                                                      push qword [rbp - 8]
                                                pop rdx ; __offset
                                                pop rax ; __pointer
                                                push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
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
                        ;------------------------------------------------
                              ; Repeat
jmp .__for__33
                              ; End of For
.__endfor__33:
                  ;------------------------------------------------------
                           ; Function Call - println(char) -> void
                              ; Make space for 1 arg(s)
                              sub rsp, 8
                              ; Arguments
                                 ; Eval arg0
                                    ; Char Literal
                                       push ']'
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
               ;---------------------------------------------------------
                     ; Function Epilogue
                     mov rsp, rbp ; remove local vars + unpopped pushes
                     pop rbp
                     ret
.__end____main__block__30____printArray__int____int__1__int:
                  ; End Function Declaration - printArray<:int:>(int[], int) -> void
         ; ===============================================================

         ; ===============================================================
                  ; Function Declaration - printArray<:float:>(float[], int) -> void
                  ; Skip over function declaration
                  jmp .__end____main__block__30____printArray__float____float__1__int
.__main__block__30____printArray__float____float__1__int:
                     ; Function Header:
                        ; Setup stack frame
                           push rbp
                           mov rbp, rsp
                           sub rsp, 16
                        ; Parameters
                           ; Param: arr [rbp + 16]
                           ; Param: size [rbp + 24]
                        ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
                           ; [rbp - 8] - int i (<unset-scope-name>)

                     ; Body
               ;---------------------------------------------------------
                        ; Code Block
                           ; Function Call - print(char) -> void
                              ; Make space for 1 arg(s)
                              sub rsp, 8
                              ; Arguments
                                 ; Eval arg0
                                    ; Char Literal
                                       push '['
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
                  ;------------------------------------------------------
                           ; If-Statement
                              ; Condition
                                 ; Greater Than
                                    ; LHS
                                       ; Identifier - int size
                                          push qword [rbp - -24]
                                    ; RHS
                                       ; Int Literal
                                          mov rax, 0
                                          push rax
                                    pop rdx ; rhs
                                    pop rax ; lhs
                                    cmp rax, rdx
                                    setg al
                                    movzx eax, al
                                    push rax
                                 pop rdx ; __cond
                                 cmp rdx, 0 ; ensure condition is true
                                 je .__endif__36 ; jump to end
                              ; Body
                                 ; Function Call - print(float) -> void
                                    ; Make space for 1 arg(s)
                                    sub rsp, 8
                                    ; Arguments
                                       ; Eval arg0
                                          ; Subscript
                                             ; LHS
                                                ; Identifier - float[] arr
                                                   push qword [rbp - -16]
                                             ; OFFSET
                                                ; Int Literal
                                                   mov rax, 0
                                                   push rax
                                             pop rdx ; __offset
                                             pop rax ; __pointer
                                             push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                                       ; Move arg0's result to reverse order position on stack
                                       pop rax
                                       mov qword [rsp + 0], rax
                                    ; Call print(float)
                                    call print__float
                                    ; Remove args
                                    add rsp, 8
                                    ; Push return value
                                    push rax
                                 ; Statement results can be ignored
                                 pop rdx
                              jmp .__endif__36 ; jump to end of condition chain
                              ; End of if
.__endif__36:
                  ;------------------------------------------------------
                  ;------------------------------------------------------
                           ; For-Loop
                           ; Init
                              ; Assignment - '='
                                 ; RHS
                                    ; Int Literal
                                       mov rax, 1
                                       push rax
                                 ; LHS
                                    ; Variable Declaration - i
                                       mov rax, qword [rbp - 8]  ; __main__block__30__printArray__block__35__for__37__i
                                 pop rdx ; rhs value
                                 mov qword [rbp - 8], rdx
                                 push rdx
                              ; Loop init result can be discarded
                              pop rax
                           jmp .__forcond__37
.__for__37:
                              ; Update
                                 ; Pre-Increment - int
                                    ; RHS
                                       ; Identifier - int i
                                          push qword [rbp - 8]
                                    pop rdx
                                    add qword [rbp - 8], 1
                                    mov rax, qword [rbp - 8]
                                    push rax ; push result
                                 ; Loop update result can be discarded
                                 pop rax
.__forcond__37:
                              ; Condition
                                 ; Less Than
                                    ; LHS
                                       ; Identifier - int i
                                          push qword [rbp - 8]
                                    ; RHS
                                       ; Identifier - int size
                                          push qword [rbp - -24]
                                    pop rdx ; rhs
                                    pop rax ; lhs
                                    cmp rax, rdx
                                    setl al
                                    movzx eax, al
                                    push rax
                                 pop rax ; __cond
                                 cmp rax, 0 ; __cond
                                 je .__endfor__37
                              ; Body
                        ;------------------------------------------------
                                 ; Code Block
                                    ; Function Call - print(char[]) -> void
                                       ; Make space for 1 arg(s)
                                       sub rsp, 8
                                       ; Arguments
                                          ; Eval arg0
                                             ; String Literal
                                                ; ", "
                                                mov rax, .str136
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
                                    ; Function Call - print(float) -> void
                                       ; Make space for 1 arg(s)
                                       sub rsp, 8
                                       ; Arguments
                                          ; Eval arg0
                                             ; Subscript
                                                ; LHS
                                                   ; Identifier - float[] arr
                                                      push qword [rbp - -16]
                                                ; OFFSET
                                                   ; Identifier - int i
                                                      push qword [rbp - 8]
                                                pop rdx ; __offset
                                                pop rax ; __pointer
                                                push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                                          ; Move arg0's result to reverse order position on stack
                                          pop rax
                                          mov qword [rsp + 0], rax
                                       ; Call print(float)
                                       call print__float
                                       ; Remove args
                                       add rsp, 8
                                       ; Push return value
                                       push rax
                                    ; Statement results can be ignored
                                    pop rdx
                        ;------------------------------------------------
                              ; Repeat
jmp .__for__37
                              ; End of For
.__endfor__37:
                  ;------------------------------------------------------
                           ; Function Call - println(char) -> void
                              ; Make space for 1 arg(s)
                              sub rsp, 8
                              ; Arguments
                                 ; Eval arg0
                                    ; Char Literal
                                       push ']'
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
               ;---------------------------------------------------------
                     ; Function Epilogue
                     mov rsp, rbp ; remove local vars + unpopped pushes
                     pop rbp
                     ret
.__end____main__block__30____printArray__float____float__1__int:
                  ; End Function Declaration - printArray<:float:>(float[], int) -> void
         ; ===============================================================

            ; End Function Template - 
   ; =====================================================================

   ; =====================================================================
            ; Function Declaration - printArray(char[], int) -> void
            ; Skip over function declaration
            jmp .__end____main__block__30____printArray__char__1__int
.__main__block__30____printArray__char__1__int:
               ; Function Header:
                  ; Setup stack frame
                     push rbp
                     mov rbp, rsp
                     sub rsp, 16
                  ; Parameters
                     ; Param: arr [rbp + 16]
                     ; Param: size [rbp + 24]
                  ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
                     ; [rbp - 8] - int i (<unset-scope-name>)

               ; Body
         ;---------------------------------------------------------------
                  ; Code Block
                     ; Function Call - print(char) -> void
                        ; Make space for 1 arg(s)
                        sub rsp, 8
                        ; Arguments
                           ; Eval arg0
                              ; Char Literal
                                 push '['
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
                           ; Greater Than
                              ; LHS
                                 ; Identifier - int size
                                    push qword [rbp - -24]
                              ; RHS
                                 ; Int Literal
                                    mov rax, 0
                                    push rax
                              pop rdx ; rhs
                              pop rax ; lhs
                              cmp rax, rdx
                              setg al
                              movzx eax, al
                              push rax
                           pop rdx ; __cond
                           cmp rdx, 0 ; ensure condition is true
                           je .__endif__40 ; jump to end
                        ; Body
                  ;------------------------------------------------------
                           ; Code Block
                              ; Function Call - print(char) -> void
                                 ; Make space for 1 arg(s)
                                 sub rsp, 8
                                 ; Arguments
                                    ; Eval arg0
                                       ; Char Literal
                                          push 39 ; \'
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
                                       ; Subscript
                                          ; LHS
                                             ; Identifier - char[] arr
                                                push qword [rbp - -16]
                                          ; OFFSET
                                             ; Int Literal
                                                mov rax, 0
                                                push rax
                                          pop rdx ; __offset
                                          pop rax ; __pointer
                                          push qword [rax + rdx] ; pointer + sizeof(data_t) * offset
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
                                       ; Char Literal
                                          push 39 ; \'
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
                  ;------------------------------------------------------
                        jmp .__endif__40 ; jump to end of condition chain
                        ; End of if
.__endif__40:
            ;------------------------------------------------------------
            ;------------------------------------------------------------
                     ; For-Loop
                     ; Init
                        ; Assignment - '='
                           ; RHS
                              ; Int Literal
                                 mov rax, 1
                                 push rax
                           ; LHS
                              ; Variable Declaration - i
                                 mov rax, qword [rbp - 8]  ; __main__block__30__printArray__block__39__for__42__i
                           pop rdx ; rhs value
                           mov qword [rbp - 8], rdx
                           push rdx
                        ; Loop init result can be discarded
                        pop rax
                     jmp .__forcond__42
.__for__42:
                        ; Update
                           ; Pre-Increment - int
                              ; RHS
                                 ; Identifier - int i
                                    push qword [rbp - 8]
                              pop rdx
                              add qword [rbp - 8], 1
                              mov rax, qword [rbp - 8]
                              push rax ; push result
                           ; Loop update result can be discarded
                           pop rax
.__forcond__42:
                        ; Condition
                           ; Less Than
                              ; LHS
                                 ; Identifier - int i
                                    push qword [rbp - 8]
                              ; RHS
                                 ; Identifier - int size
                                    push qword [rbp - -24]
                              pop rdx ; rhs
                              pop rax ; lhs
                              cmp rax, rdx
                              setl al
                              movzx eax, al
                              push rax
                           pop rax ; __cond
                           cmp rax, 0 ; __cond
                           je .__endfor__42
                        ; Body
                  ;------------------------------------------------------
                           ; Code Block
                              ; Function Call - print(char[]) -> void
                                 ; Make space for 1 arg(s)
                                 sub rsp, 8
                                 ; Arguments
                                    ; Eval arg0
                                       ; String Literal
                                          ; ", "
                                          mov rax, .str134
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
                              ; Function Call - print(char) -> void
                                 ; Make space for 1 arg(s)
                                 sub rsp, 8
                                 ; Arguments
                                    ; Eval arg0
                                       ; Char Literal
                                          push 39 ; \'
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
                                       ; Subscript
                                          ; LHS
                                             ; Identifier - char[] arr
                                                push qword [rbp - -16]
                                          ; OFFSET
                                             ; Identifier - int i
                                                push qword [rbp - 8]
                                          pop rdx ; __offset
                                          pop rax ; __pointer
                                          push qword [rax + rdx] ; pointer + sizeof(data_t) * offset
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
                                       ; Char Literal
                                          push 39 ; \'
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
                  ;------------------------------------------------------
                        ; Repeat
jmp .__for__42
                        ; End of For
.__endfor__42:
            ;------------------------------------------------------------
                     ; Function Call - println(char) -> void
                        ; Make space for 1 arg(s)
                        sub rsp, 8
                        ; Arguments
                           ; Eval arg0
                              ; Char Literal
                                 push ']'
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
               ; Function Epilogue
               mov rsp, rbp ; remove local vars + unpopped pushes
               pop rbp
               ret
.__end____main__block__30____printArray__char__1__int:
            ; End Function Declaration - printArray(char[], int) -> void
   ; =====================================================================

            ; Assignment - '='
               ; RHS
                  ; Int Literal
                     mov rax, 10
                     push rax
               ; LHS
                  ; Variable Declaration - n
                     mov rax, qword [rbp - 216]  ; __main__block__30__n
               pop rdx ; rhs value
               mov qword [rbp - 216], rdx
               push rdx
            ; Statement results can be ignored
            pop rdx
            ; Assignment - '='
               ; RHS
                  ; Array Allocator
                     ; Identifier - int n
                        push qword [rbp - 216]
                     pop rdx ; num elements for dimension[0]
                     imul rdx, 8 ; 8 bytes per element
                     mov rdi, rdx ; num bytes to allocate
                     call malloc ; allocates edi bytes on heap and stores pointer in rax
                     push rax ; __ptr
               ; LHS
                  ; Variable Declaration - arr
                     mov rax, qword [rbp - 224]  ; __main__block__30__arr
               pop rdx ; rhs value
               mov qword [rbp - 224], rdx
               push rdx
            ; Statement results can be ignored
            pop rdx
   ;---------------------------------------------------------------------
            ; For-Loop
            ; Init
               ; Assignment - '='
                  ; RHS
                     ; Int Literal
                        mov rax, 0
                        push rax
                  ; LHS
                     ; Variable Declaration - i
                        mov rax, qword [rbp - 232]  ; __main__block__30__for__44__i
                  pop rdx ; rhs value
                  mov qword [rbp - 232], rdx
                  push rdx
               ; Loop init result can be discarded
               pop rax
            jmp .__forcond__44
.__for__44:
               ; Update
                  ; Pre-Increment - int
                     ; RHS
                        ; Identifier - int i
                           push qword [rbp - 232]
                     pop rdx
                     add qword [rbp - 232], 1
                     mov rax, qword [rbp - 232]
                     push rax ; push result
                  ; Loop update result can be discarded
                  pop rax
.__forcond__44:
               ; Condition
                  ; Less Than
                     ; LHS
                        ; Identifier - int i
                           push qword [rbp - 232]
                     ; RHS
                        ; Identifier - int n
                           push qword [rbp - 216]
                     pop rdx ; rhs
                     pop rax ; lhs
                     cmp rax, rdx
                     setl al
                     movzx eax, al
                     push rax
                  pop rax ; __cond
                  cmp rax, 0 ; __cond
                  je .__endfor__44
               ; Body
         ;---------------------------------------------------------------
                  ; Code Block
                     ; Assignment - '='
                        ; RHS
                           ; Identifier - int i
                              push qword [rbp - 232]
                        ; LHS
                           ; Subscript assignment
                              ; LHS
                                 ; Identifier - int[] arr
                                    push qword [rbp - 224]
                              ; OFFSET
                                 ; Identifier - int i
                                    push qword [rbp - 232]
                              pop rdi ; __offset
                              pop rbx ; __pointer
                        pop rdx ; rhs value
                        mov qword [rbx + 8*rdi], rdx
                        push rdx
                     ; Statement results can be ignored
                     pop rdx
         ;---------------------------------------------------------------
               ; Repeat
jmp .__for__44
               ; End of For
.__endfor__44:
   ;---------------------------------------------------------------------
            ; Function Call - printArray<:int:>(int[], int) -> void
               ; Make space for 2 arg(s)
               sub rsp, 16
               ; Arguments
                  ; Eval arg0
                     ; Identifier - int[] arr
                        push qword [rbp - 224]
                  ; Move arg0's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 0], rax
                  ; Eval arg1
                     ; Identifier - int n
                        push qword [rbp - 216]
                  ; Move arg1's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 8], rax
               ; Call printArray<:int:>(int[], int)
               call .__main__block__30____printArray__int____int__1__int
               ; Remove args
               add rsp, 16
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
                        mov rax, 0
                        push rax
                  ; LHS
                     ; Variable Declaration - i
                        mov rax, qword [rbp - 240]  ; __main__block__30__for__46__i
                  pop rdx ; rhs value
                  mov qword [rbp - 240], rdx
                  push rdx
               ; Loop init result can be discarded
               pop rax
            jmp .__forcond__46
.__for__46:
               ; Update
                  ; Pre-Increment - int
                     ; RHS
                        ; Identifier - int i
                           push qword [rbp - 240]
                     pop rdx
                     add qword [rbp - 240], 1
                     mov rax, qword [rbp - 240]
                     push rax ; push result
                  ; Loop update result can be discarded
                  pop rax
.__forcond__46:
               ; Condition
                  ; Less Than
                     ; LHS
                        ; Identifier - int i
                           push qword [rbp - 240]
                     ; RHS
                        ; Identifier - int n
                           push qword [rbp - 216]
                     pop rdx ; rhs
                     pop rax ; lhs
                     cmp rax, rdx
                     setl al
                     movzx eax, al
                     push rax
                  pop rax ; __cond
                  cmp rax, 0 ; __cond
                  je .__endfor__46
               ; Body
                  ; Assignment - '*='
                     ; RHS
                        ; Int Literal
                           mov rax, 2
                           push rax
                     ; LHS
                        ; Subscript assignment
                           ; LHS
                              ; Identifier - int[] arr
                                 push qword [rbp - 224]
                           ; OFFSET
                              ; Identifier - int i
                                 push qword [rbp - 240]
                           pop rdi ; __offset
                           pop rbx ; __pointer
                     pop rdx ; rhs value
                     mov rax, qword [rbx + 8*rdi] ; read lhs value
                     imul rax, rdx      ; lhs = lhs * rhs
                     mov qword [rbx + 8*rdi], rax ; write back to lhs
                     push rax          ; push result for other expressions
                  ; Statement results can be ignored
                  pop rdx
               ; Repeat
jmp .__for__46
               ; End of For
.__endfor__46:
   ;---------------------------------------------------------------------
            ; Function Call - printArray<:int:>(int[], int) -> void
               ; Make space for 2 arg(s)
               sub rsp, 16
               ; Arguments
                  ; Eval arg0
                     ; Identifier - int[] arr
                        push qword [rbp - 224]
                  ; Move arg0's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 0], rax
                  ; Eval arg1
                     ; Identifier - int n
                        push qword [rbp - 216]
                  ; Move arg1's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 8], rax
               ; Call printArray<:int:>(int[], int)
               call .__main__block__30____printArray__int____int__1__int
               ; Remove args
               add rsp, 16
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
                        mov rax, 0
                        push rax
                  ; LHS
                     ; Variable Declaration - i
                        mov rax, qword [rbp - 248]  ; __main__block__30__for__47__i
                  pop rdx ; rhs value
                  mov qword [rbp - 248], rdx
                  push rdx
               ; Loop init result can be discarded
               pop rax
            jmp .__forcond__47
.__for__47:
               ; Update
                  ; Pre-Increment - int
                     ; RHS
                        ; Identifier - int i
                           push qword [rbp - 248]
                     pop rdx
                     add qword [rbp - 248], 1
                     mov rax, qword [rbp - 248]
                     push rax ; push result
                  ; Loop update result can be discarded
                  pop rax
.__forcond__47:
               ; Condition
                  ; Less Than
                     ; LHS
                        ; Identifier - int i
                           push qword [rbp - 248]
                     ; RHS
                        ; Identifier - int n
                           push qword [rbp - 216]
                     pop rdx ; rhs
                     pop rax ; lhs
                     cmp rax, rdx
                     setl al
                     movzx eax, al
                     push rax
                  pop rax ; __cond
                  cmp rax, 0 ; __cond
                  je .__endfor__47
               ; Body
                  ; Assignment - '+='
                     ; RHS
                        ; Int Literal
                           mov rax, 2
                           push rax
                     ; LHS
                        ; Subscript assignment
                           ; LHS
                              ; Identifier - int[] arr
                                 push qword [rbp - 224]
                           ; OFFSET
                              ; Identifier - int i
                                 push qword [rbp - 248]
                           pop rdi ; __offset
                           pop rbx ; __pointer
                     pop rdx ; rhs value
                     mov rax, qword [rbx + 8*rdi] ; read lhs value
                     add rax, rdx      ; add lhs and rhs
                     mov qword [rbx + 8*rdi], rax ; write back to lhs
                     push rax          ; push result for other expressions
                  ; Statement results can be ignored
                  pop rdx
               ; Repeat
jmp .__for__47
               ; End of For
.__endfor__47:
   ;---------------------------------------------------------------------
            ; Function Call - printArray<:int:>(int[], int) -> void
               ; Make space for 2 arg(s)
               sub rsp, 16
               ; Arguments
                  ; Eval arg0
                     ; Identifier - int[] arr
                        push qword [rbp - 224]
                  ; Move arg0's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 0], rax
                  ; Eval arg1
                     ; Identifier - int n
                        push qword [rbp - 216]
                  ; Move arg1's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 8], rax
               ; Call printArray<:int:>(int[], int)
               call .__main__block__30____printArray__int____int__1__int
               ; Remove args
               add rsp, 16
               ; Push return value
               push rax
            ; Statement results can be ignored
            pop rdx
            ; Assignment - '='
               ; RHS
                  ; Array Allocator
                     ; Int Literal
                        mov rax, 3
                        push rax
                     pop rdx ; num elements for dimension[0]
                     imul rdx, 8 ; 8 bytes per element
                     mov rdi, rdx ; num bytes to allocate
                     call malloc ; allocates edi bytes on heap and stores pointer in rax
                     push rax ; __ptr
               ; LHS
                  ; Variable Declaration - floats
                     mov rax, qword [rbp - 256]  ; __main__block__30__floats
               pop rdx ; rhs value
               mov qword [rbp - 256], rdx
               push rdx
            ; Statement results can be ignored
            pop rdx
   ;---------------------------------------------------------------------
            ; For-Loop
            ; Init
               ; Assignment - '='
                  ; RHS
                     ; Int Literal
                        mov rax, 0
                        push rax
                  ; LHS
                     ; Variable Declaration - i
                        mov rax, qword [rbp - 264]  ; __main__block__30__for__48__i
                  pop rdx ; rhs value
                  mov qword [rbp - 264], rdx
                  push rdx
               ; Loop init result can be discarded
               pop rax
            jmp .__forcond__48
.__for__48:
               ; Update
                  ; Pre-Increment - int
                     ; RHS
                        ; Identifier - int i
                           push qword [rbp - 264]
                     pop rdx
                     add qword [rbp - 264], 1
                     mov rax, qword [rbp - 264]
                     push rax ; push result
                  ; Loop update result can be discarded
                  pop rax
.__forcond__48:
               ; Condition
                  ; Less Than
                     ; LHS
                        ; Identifier - int i
                           push qword [rbp - 264]
                     ; RHS
                        ; Int Literal
                           mov rax, 3
                           push rax
                     pop rdx ; rhs
                     pop rax ; lhs
                     cmp rax, rdx
                     setl al
                     movzx eax, al
                     push rax
                  pop rax ; __cond
                  cmp rax, 0 ; __cond
                  je .__endfor__48
               ; Body
         ;---------------------------------------------------------------
                  ; Code Block
                     ; Assignment - '='
                        ; RHS
                           ; Function Call - intToFloat(int) -> float
                              ; Make space for 1 arg(s)
                              sub rsp, 8
                              ; Arguments
                                 ; Eval arg0
                                    ; Identifier - int i
                                       push qword [rbp - 264]
                                 ; Move arg0's result to reverse order position on stack
                                 pop rax
                                 mov qword [rsp + 0], rax
                              ; Call intToFloat(int)
                              call intToFloat__int
                              ; Remove args
                              add rsp, 8
                              ; Push return value
                              movq rax, xmm0
                              push rax
                        ; LHS
                           ; Subscript assignment
                              ; LHS
                                 ; Identifier - float[] floats
                                    push qword [rbp - 256]
                              ; OFFSET
                                 ; Identifier - int i
                                    push qword [rbp - 264]
                              pop rdi ; __offset
                              pop rbx ; __pointer
                        pop rdx ; rhs value
                        mov qword [rbx + 8*rdi], rdx
                        push rdx
                     ; Statement results can be ignored
                     pop rdx
         ;---------------------------------------------------------------
               ; Repeat
jmp .__for__48
               ; End of For
.__endfor__48:
   ;---------------------------------------------------------------------
            ; Function Call - printArray<:float:>(float[], int) -> void
               ; Make space for 2 arg(s)
               sub rsp, 16
               ; Arguments
                  ; Eval arg0
                     ; Identifier - float[] floats
                        push qword [rbp - 256]
                  ; Move arg0's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 0], rax
                  ; Eval arg1
                     ; Int Literal
                        mov rax, 3
                        push rax
                  ; Move arg1's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 8], rax
               ; Call printArray<:float:>(float[], int)
               call .__main__block__30____printArray__float____float__1__int
               ; Remove args
               add rsp, 16
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
                        mov rax, 0
                        push rax
                  ; LHS
                     ; Variable Declaration - i
                        mov rax, qword [rbp - 272]  ; __main__block__30__for__50__i
                  pop rdx ; rhs value
                  mov qword [rbp - 272], rdx
                  push rdx
               ; Loop init result can be discarded
               pop rax
            jmp .__forcond__50
.__for__50:
               ; Update
                  ; Pre-Increment - int
                     ; RHS
                        ; Identifier - int i
                           push qword [rbp - 272]
                     pop rdx
                     add qword [rbp - 272], 1
                     mov rax, qword [rbp - 272]
                     push rax ; push result
                  ; Loop update result can be discarded
                  pop rax
.__forcond__50:
               ; Condition
                  ; Less Than
                     ; LHS
                        ; Identifier - int i
                           push qword [rbp - 272]
                     ; RHS
                        ; Int Literal
                           mov rax, 3
                           push rax
                     pop rdx ; rhs
                     pop rax ; lhs
                     cmp rax, rdx
                     setl al
                     movzx eax, al
                     push rax
                  pop rax ; __cond
                  cmp rax, 0 ; __cond
                  je .__endfor__50
               ; Body
         ;---------------------------------------------------------------
                  ; Code Block
                     ; Assignment - '/='
                        ; RHS
                           ; Float Literal
                              mov rax, qword [.float37] ; 3.25
                              push rax
                        ; LHS
                           ; Subscript assignment
                              ; LHS
                                 ; Identifier - float[] floats
                                    push qword [rbp - 256]
                              ; OFFSET
                                 ; Identifier - int i
                                    push qword [rbp - 272]
                              pop rdi ; __offset
                              pop rbx ; __pointer
                        pop rdx ; rhs value
                        movq xmm0, qword [rbx + 8*rdi] ; load lhs value, xmm0 = mem[0], zero
                        movq xmm1, rdx      ; load rhs value, xmm1 = mem[0], zero
                        divsd xmm0, xmm1    ; lhs = lhs / rhs
                        movsd qword [rbx + 8*rdi], xmm0 ; write back to lhs
                        movq rax, xmm0
                        push rax          ; push result for other expressions
                     ; Statement results can be ignored
                     pop rdx
         ;---------------------------------------------------------------
               ; Repeat
jmp .__for__50
               ; End of For
.__endfor__50:
   ;---------------------------------------------------------------------
            ; Function Call - printArray<:float:>(float[], int) -> void
               ; Make space for 2 arg(s)
               sub rsp, 16
               ; Arguments
                  ; Eval arg0
                     ; Identifier - float[] floats
                        push qword [rbp - 256]
                  ; Move arg0's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 0], rax
                  ; Eval arg1
                     ; Int Literal
                        mov rax, 3
                        push rax
                  ; Move arg1's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 8], rax
               ; Call printArray<:float:>(float[], int)
               call .__main__block__30____printArray__float____float__1__int
               ; Remove args
               add rsp, 16
               ; Push return value
               push rax
            ; Statement results can be ignored
            pop rdx
            ; Assignment - '='
               ; RHS
                  ; String Literal
                     ; "Hello, world!"
                     mov rax, .str137
                     push rax
               ; LHS
                  ; Variable Declaration - str
                     mov rax, qword [rbp - 280]  ; __main__block__30__str
               pop rdx ; rhs value
               mov qword [rbp - 280], rdx
               push rdx
            ; Statement results can be ignored
            pop rdx
            ; Function Call - printArray(char[], int) -> void
               ; Make space for 2 arg(s)
               sub rsp, 16
               ; Arguments
                  ; Eval arg0
                     ; Identifier - char[] str
                        push qword [rbp - 280]
                  ; Move arg0's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 0], rax
                  ; Eval arg1
                     ; Int Literal
                        mov rax, 13
                        push rax
                  ; Move arg1's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 8], rax
               ; Call printArray(char[], int)
               call .__main__block__30____printArray__char__1__int
               ; Remove args
               add rsp, 16
               ; Push return value
               push rax
            ; Statement results can be ignored
            pop rdx
            ; Function Call - println(char[]) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; Identifier - char[] str
                        push qword [rbp - 280]
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
   ; =====================================================================
            ; Function Declaration - add(int[], int[], int[], int) -> void
            ; Skip over function declaration
            jmp .__end____main__block__30____add__int__1__int__1__int__1__int
.__main__block__30____add__int__1__int__1__int__1__int:
               ; Function Header:
                  ; Setup stack frame
                     push rbp
                     mov rbp, rsp
                     sub rsp, 16
                  ; Parameters
                     ; Param: a [rbp + 16]
                     ; Param: b [rbp + 24]
                     ; Param: c [rbp + 32]
                     ; Param: n [rbp + 40]
                  ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
                     ; [rbp - 8] - int i (<unset-scope-name>)

               ; Body
         ;---------------------------------------------------------------
                  ; Code Block
            ;------------------------------------------------------------
                     ; For-Loop
                     ; Init
                        ; Assignment - '='
                           ; RHS
                              ; Int Literal
                                 mov rax, 0
                                 push rax
                           ; LHS
                              ; Variable Declaration - i
                                 mov rax, qword [rbp - 8]  ; __main__block__30__add__block__52__for__53__i
                           pop rdx ; rhs value
                           mov qword [rbp - 8], rdx
                           push rdx
                        ; Loop init result can be discarded
                        pop rax
                     jmp .__forcond__53
.__for__53:
                        ; Update
                           ; Pre-Increment - int
                              ; RHS
                                 ; Identifier - int i
                                    push qword [rbp - 8]
                              pop rdx
                              add qword [rbp - 8], 1
                              mov rax, qword [rbp - 8]
                              push rax ; push result
                           ; Loop update result can be discarded
                           pop rax
.__forcond__53:
                        ; Condition
                           ; Less Than
                              ; LHS
                                 ; Identifier - int i
                                    push qword [rbp - 8]
                              ; RHS
                                 ; Identifier - int n
                                    push qword [rbp - -40]
                              pop rdx ; rhs
                              pop rax ; lhs
                              cmp rax, rdx
                              setl al
                              movzx eax, al
                              push rax
                           pop rax ; __cond
                           cmp rax, 0 ; __cond
                           je .__endfor__53
                        ; Body
                           ; Assignment - '='
                              ; RHS
                                 ; Addition - int, int
                                    ; LHS
                                       ; Subscript
                                          ; LHS
                                             ; Identifier - int[] a
                                                push qword [rbp - -16]
                                          ; OFFSET
                                             ; Identifier - int i
                                                push qword [rbp - 8]
                                          pop rdx ; __offset
                                          pop rax ; __pointer
                                          push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                                    ; RHS
                                       ; Subscript
                                          ; LHS
                                             ; Identifier - int[] b
                                                push qword [rbp - -24]
                                          ; OFFSET
                                             ; Identifier - int i
                                                push qword [rbp - 8]
                                          pop rdx ; __offset
                                          pop rax ; __pointer
                                          push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                                    pop rdx ; rhs
                                    pop rax ; lhs
                                    add rax, rdx
                                    push rax
                              ; LHS
                                 ; Subscript assignment
                                    ; LHS
                                       ; Identifier - int[] c
                                          push qword [rbp - -32]
                                    ; OFFSET
                                       ; Identifier - int i
                                          push qword [rbp - 8]
                                    pop rdi ; __offset
                                    pop rbx ; __pointer
                              pop rdx ; rhs value
                              mov qword [rbx + 8*rdi], rdx
                              push rdx
                           ; Statement results can be ignored
                           pop rdx
                        ; Repeat
jmp .__for__53
                        ; End of For
.__endfor__53:
            ;------------------------------------------------------------
         ;---------------------------------------------------------------
               ; Function Epilogue
               mov rsp, rbp ; remove local vars + unpopped pushes
               pop rbp
               ret
.__end____main__block__30____add__int__1__int__1__int__1__int:
            ; End Function Declaration - add(int[], int[], int[], int) -> void
   ; =====================================================================

            ; Assignment - '='
               ; RHS
                  ; Array Constructor
                     ; Elements
                     ; Int Literal
                        mov rax, 0
                        push rax
                     ; Int Literal
                        mov rax, 1
                        push rax
                     ; Int Literal
                        mov rax, 2
                        push rax
                     ; Int Literal
                        mov rax, 3
                        push rax
                     ; Int Literal
                        mov rax, 4
                        push rax
                     ; Int Literal
                        mov rax, 5
                        push rax
                     mov edi, 48 ; number of bytes to allocate (nArgs * 8bytes)
                     call malloc ; allocates edi bytes on heap and stores pointer in rax
                     ; Populate array values
                     pop rdx ; get array element 5
                     mov qword [rax + 40], rdx ; arr[5] = rdx
                     pop rdx ; get array element 4
                     mov qword [rax + 32], rdx ; arr[4] = rdx
                     pop rdx ; get array element 3
                     mov qword [rax + 24], rdx ; arr[3] = rdx
                     pop rdx ; get array element 2
                     mov qword [rax + 16], rdx ; arr[2] = rdx
                     pop rdx ; get array element 1
                     mov qword [rax + 8], rdx ; arr[1] = rdx
                     pop rdx ; get array element 0
                     mov qword [rax + 0], rdx ; arr[0] = rdx
                     push rax
               ; LHS
                  ; Variable Declaration - a
                     mov rax, qword [rbp - 288]  ; __main__block__30__a
               pop rdx ; rhs value
               mov qword [rbp - 288], rdx
               push rdx
            ; Statement results can be ignored
            pop rdx
            ; Assignment - '='
               ; RHS
                  ; Array Constructor
                     ; Elements
                     ; Int Literal
                        mov rax, 5
                        push rax
                     ; Int Literal
                        mov rax, 4
                        push rax
                     ; Int Literal
                        mov rax, 3
                        push rax
                     ; Int Literal
                        mov rax, 2
                        push rax
                     ; Int Literal
                        mov rax, 1
                        push rax
                     ; Int Literal
                        mov rax, 0
                        push rax
                     mov edi, 48 ; number of bytes to allocate (nArgs * 8bytes)
                     call malloc ; allocates edi bytes on heap and stores pointer in rax
                     ; Populate array values
                     pop rdx ; get array element 5
                     mov qword [rax + 40], rdx ; arr[5] = rdx
                     pop rdx ; get array element 4
                     mov qword [rax + 32], rdx ; arr[4] = rdx
                     pop rdx ; get array element 3
                     mov qword [rax + 24], rdx ; arr[3] = rdx
                     pop rdx ; get array element 2
                     mov qword [rax + 16], rdx ; arr[2] = rdx
                     pop rdx ; get array element 1
                     mov qword [rax + 8], rdx ; arr[1] = rdx
                     pop rdx ; get array element 0
                     mov qword [rax + 0], rdx ; arr[0] = rdx
                     push rax
               ; LHS
                  ; Variable Declaration - b
                     mov rax, qword [rbp - 296]  ; __main__block__30__b
               pop rdx ; rhs value
               mov qword [rbp - 296], rdx
               push rdx
            ; Statement results can be ignored
            pop rdx
            ; Assignment - '='
               ; RHS
                  ; Array Constructor
                     ; Elements
                     ; Int Literal
                        mov rax, 0
                        push rax
                     ; Int Literal
                        mov rax, 0
                        push rax
                     ; Int Literal
                        mov rax, 0
                        push rax
                     ; Int Literal
                        mov rax, 0
                        push rax
                     ; Int Literal
                        mov rax, 0
                        push rax
                     ; Int Literal
                        mov rax, 0
                        push rax
                     mov edi, 48 ; number of bytes to allocate (nArgs * 8bytes)
                     call malloc ; allocates edi bytes on heap and stores pointer in rax
                     ; Populate array values
                     pop rdx ; get array element 5
                     mov qword [rax + 40], rdx ; arr[5] = rdx
                     pop rdx ; get array element 4
                     mov qword [rax + 32], rdx ; arr[4] = rdx
                     pop rdx ; get array element 3
                     mov qword [rax + 24], rdx ; arr[3] = rdx
                     pop rdx ; get array element 2
                     mov qword [rax + 16], rdx ; arr[2] = rdx
                     pop rdx ; get array element 1
                     mov qword [rax + 8], rdx ; arr[1] = rdx
                     pop rdx ; get array element 0
                     mov qword [rax + 0], rdx ; arr[0] = rdx
                     push rax
               ; LHS
                  ; Variable Declaration - c
                     mov rax, qword [rbp - 304]  ; __main__block__30__c
               pop rdx ; rhs value
               mov qword [rbp - 304], rdx
               push rdx
            ; Statement results can be ignored
            pop rdx
            ; Function Call - print(char[]) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; String Literal
                        ; "a = "
                        mov rax, .str138
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
            ; Function Call - printArray<:int:>(int[], int) -> void
               ; Make space for 2 arg(s)
               sub rsp, 16
               ; Arguments
                  ; Eval arg0
                     ; Identifier - int[] a
                        push qword [rbp - 288]
                  ; Move arg0's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 0], rax
                  ; Eval arg1
                     ; Int Literal
                        mov rax, 6
                        push rax
                  ; Move arg1's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 8], rax
               ; Call printArray<:int:>(int[], int)
               call .__main__block__30____printArray__int____int__1__int
               ; Remove args
               add rsp, 16
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
                        ; "b = "
                        mov rax, .str139
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
            ; Function Call - printArray<:int:>(int[], int) -> void
               ; Make space for 2 arg(s)
               sub rsp, 16
               ; Arguments
                  ; Eval arg0
                     ; Identifier - int[] b
                        push qword [rbp - 296]
                  ; Move arg0's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 0], rax
                  ; Eval arg1
                     ; Int Literal
                        mov rax, 6
                        push rax
                  ; Move arg1's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 8], rax
               ; Call printArray<:int:>(int[], int)
               call .__main__block__30____printArray__int____int__1__int
               ; Remove args
               add rsp, 16
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
                        ; "c = "
                        mov rax, .str140
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
            ; Function Call - printArray<:int:>(int[], int) -> void
               ; Make space for 2 arg(s)
               sub rsp, 16
               ; Arguments
                  ; Eval arg0
                     ; Identifier - int[] c
                        push qword [rbp - 304]
                  ; Move arg0's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 0], rax
                  ; Eval arg1
                     ; Int Literal
                        mov rax, 6
                        push rax
                  ; Move arg1's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 8], rax
               ; Call printArray<:int:>(int[], int)
               call .__main__block__30____printArray__int____int__1__int
               ; Remove args
               add rsp, 16
               ; Push return value
               push rax
            ; Statement results can be ignored
            pop rdx
            ; Function Call - println(char[]) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; String Literal
                        ; "c = a + b"
                        mov rax, .str141
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
            ; Function Call - add(int[], int[], int[], int) -> void
               ; Make space for 4 arg(s)
               sub rsp, 32
               ; Arguments
                  ; Eval arg0
                     ; Identifier - int[] a
                        push qword [rbp - 288]
                  ; Move arg0's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 0], rax
                  ; Eval arg1
                     ; Identifier - int[] b
                        push qword [rbp - 296]
                  ; Move arg1's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 8], rax
                  ; Eval arg2
                     ; Identifier - int[] c
                        push qword [rbp - 304]
                  ; Move arg2's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 16], rax
                  ; Eval arg3
                     ; Int Literal
                        mov rax, 6
                        push rax
                  ; Move arg3's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 24], rax
               ; Call add(int[], int[], int[], int)
               call .__main__block__30____add__int__1__int__1__int__1__int
               ; Remove args
               add rsp, 32
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
                        ; "c = "
                        mov rax, .str142
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
            ; Function Call - printArray<:int:>(int[], int) -> void
               ; Make space for 2 arg(s)
               sub rsp, 16
               ; Arguments
                  ; Eval arg0
                     ; Identifier - int[] c
                        push qword [rbp - 304]
                  ; Move arg0's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 0], rax
                  ; Eval arg1
                     ; Int Literal
                        mov rax, 6
                        push rax
                  ; Move arg1's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 8], rax
               ; Call printArray<:int:>(int[], int)
               call .__main__block__30____printArray__int____int__1__int
               ; Remove args
               add rsp, 16
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
                     ; "=== Testing Multidimensional Arrays ==="
                     mov rax, .str143
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
   ; =====================================================================
            ; Function Template - 
               ; Instances:
         ; ===============================================================
                  ; Function Declaration - printMatrix<:int:>(int[][], int, int) -> void
                  ; Skip over function declaration
                  jmp .__end____main__block__54____printMatrix__int____int__2__int__int
.__main__block__54____printMatrix__int____int__2__int__int:
                     ; Function Header:
                        ; Setup stack frame
                           push rbp
                           mov rbp, rsp
                           sub rsp, 16
                        ; Parameters
                           ; Param: mat [rbp + 16]
                           ; Param: r [rbp + 24]
                           ; Param: c [rbp + 32]
                        ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
                           ; [rbp - 8] - int i (<unset-scope-name>)
                           ; [rbp - 16] - int j (<unset-scope-name>)

                     ; Body
               ;---------------------------------------------------------
                        ; Code Block
                  ;------------------------------------------------------
                           ; For-Loop
                           ; Init
                              ; Assignment - '='
                                 ; RHS
                                    ; Int Literal
                                       mov rax, 0
                                       push rax
                                 ; LHS
                                    ; Variable Declaration - i
                                       mov rax, qword [rbp - 8]  ; __main__block__54__printMatrix__block__55__for__56__i
                                 pop rdx ; rhs value
                                 mov qword [rbp - 8], rdx
                                 push rdx
                              ; Loop init result can be discarded
                              pop rax
                           jmp .__forcond__56
.__for__56:
                              ; Update
                                 ; Pre-Increment - int
                                    ; RHS
                                       ; Identifier - int i
                                          push qword [rbp - 8]
                                    pop rdx
                                    add qword [rbp - 8], 1
                                    mov rax, qword [rbp - 8]
                                    push rax ; push result
                                 ; Loop update result can be discarded
                                 pop rax
.__forcond__56:
                              ; Condition
                                 ; Less Than
                                    ; LHS
                                       ; Identifier - int i
                                          push qword [rbp - 8]
                                    ; RHS
                                       ; Identifier - int r
                                          push qword [rbp - -24]
                                    pop rdx ; rhs
                                    pop rax ; lhs
                                    cmp rax, rdx
                                    setl al
                                    movzx eax, al
                                    push rax
                                 pop rax ; __cond
                                 cmp rax, 0 ; __cond
                                 je .__endfor__56
                              ; Body
                        ;------------------------------------------------
                                 ; Code Block
                           ;---------------------------------------------
                                    ; For-Loop
                                    ; Init
                                       ; Assignment - '='
                                          ; RHS
                                             ; Int Literal
                                                mov rax, 0
                                                push rax
                                          ; LHS
                                             ; Variable Declaration - j
                                                mov rax, qword [rbp - 16]  ; __main__block__54__printMatrix__block__55__for__56__block__57__for__58__j
                                          pop rdx ; rhs value
                                          mov qword [rbp - 16], rdx
                                          push rdx
                                       ; Loop init result can be discarded
                                       pop rax
                                    jmp .__forcond__58
.__for__58:
                                       ; Update
                                          ; Pre-Increment - int
                                             ; RHS
                                                ; Identifier - int j
                                                   push qword [rbp - 16]
                                             pop rdx
                                             add qword [rbp - 16], 1
                                             mov rax, qword [rbp - 16]
                                             push rax ; push result
                                          ; Loop update result can be discarded
                                          pop rax
.__forcond__58:
                                       ; Condition
                                          ; Less Than
                                             ; LHS
                                                ; Identifier - int j
                                                   push qword [rbp - 16]
                                             ; RHS
                                                ; Identifier - int c
                                                   push qword [rbp - -32]
                                             pop rdx ; rhs
                                             pop rax ; lhs
                                             cmp rax, rdx
                                             setl al
                                             movzx eax, al
                                             push rax
                                          pop rax ; __cond
                                          cmp rax, 0 ; __cond
                                          je .__endfor__58
                                       ; Body
                                 ;---------------------------------------
                                          ; Code Block
                                             ; Function Call - print(int) -> void
                                                ; Make space for 1 arg(s)
                                                sub rsp, 8
                                                ; Arguments
                                                   ; Eval arg0
                                                      ; Subscript
                                                         ; LHS
                                                            ; Subscript
                                                               ; LHS
                                                                  ; Identifier - int[][] mat
                                                                     push qword [rbp - -16]
                                                               ; OFFSET
                                                                  ; Identifier - int i
                                                                     push qword [rbp - 8]
                                                               pop rdx ; __offset
                                                               pop rax ; __pointer
                                                               push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                                                         ; OFFSET
                                                            ; Identifier - int j
                                                               push qword [rbp - 16]
                                                         pop rdx ; __offset
                                                         pop rax ; __pointer
                                                         push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
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
                                 ;---------------------------------------
                                       ; Repeat
jmp .__for__58
                                       ; End of For
.__endfor__58:
                           ;---------------------------------------------
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
                        ;------------------------------------------------
                              ; Repeat
jmp .__for__56
                              ; End of For
.__endfor__56:
                  ;------------------------------------------------------
               ;---------------------------------------------------------
                     ; Function Epilogue
                     mov rsp, rbp ; remove local vars + unpopped pushes
                     pop rbp
                     ret
.__end____main__block__54____printMatrix__int____int__2__int__int:
                  ; End Function Declaration - printMatrix<:int:>(int[][], int, int) -> void
         ; ===============================================================

         ; ===============================================================
                  ; Function Declaration - printMatrix<:float:>(float[][], int, int) -> void
                  ; Skip over function declaration
                  jmp .__end____main__block__54____printMatrix__float____float__2__int__int
.__main__block__54____printMatrix__float____float__2__int__int:
                     ; Function Header:
                        ; Setup stack frame
                           push rbp
                           mov rbp, rsp
                           sub rsp, 16
                        ; Parameters
                           ; Param: mat [rbp + 16]
                           ; Param: r [rbp + 24]
                           ; Param: c [rbp + 32]
                        ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
                           ; [rbp - 8] - int i (<unset-scope-name>)
                           ; [rbp - 16] - int j (<unset-scope-name>)

                     ; Body
               ;---------------------------------------------------------
                        ; Code Block
                  ;------------------------------------------------------
                           ; For-Loop
                           ; Init
                              ; Assignment - '='
                                 ; RHS
                                    ; Int Literal
                                       mov rax, 0
                                       push rax
                                 ; LHS
                                    ; Variable Declaration - i
                                       mov rax, qword [rbp - 8]  ; __main__block__54__printMatrix__block__60__for__61__i
                                 pop rdx ; rhs value
                                 mov qword [rbp - 8], rdx
                                 push rdx
                              ; Loop init result can be discarded
                              pop rax
                           jmp .__forcond__61
.__for__61:
                              ; Update
                                 ; Pre-Increment - int
                                    ; RHS
                                       ; Identifier - int i
                                          push qword [rbp - 8]
                                    pop rdx
                                    add qword [rbp - 8], 1
                                    mov rax, qword [rbp - 8]
                                    push rax ; push result
                                 ; Loop update result can be discarded
                                 pop rax
.__forcond__61:
                              ; Condition
                                 ; Less Than
                                    ; LHS
                                       ; Identifier - int i
                                          push qword [rbp - 8]
                                    ; RHS
                                       ; Identifier - int r
                                          push qword [rbp - -24]
                                    pop rdx ; rhs
                                    pop rax ; lhs
                                    cmp rax, rdx
                                    setl al
                                    movzx eax, al
                                    push rax
                                 pop rax ; __cond
                                 cmp rax, 0 ; __cond
                                 je .__endfor__61
                              ; Body
                        ;------------------------------------------------
                                 ; Code Block
                           ;---------------------------------------------
                                    ; For-Loop
                                    ; Init
                                       ; Assignment - '='
                                          ; RHS
                                             ; Int Literal
                                                mov rax, 0
                                                push rax
                                          ; LHS
                                             ; Variable Declaration - j
                                                mov rax, qword [rbp - 16]  ; __main__block__54__printMatrix__block__60__for__61__block__62__for__63__j
                                          pop rdx ; rhs value
                                          mov qword [rbp - 16], rdx
                                          push rdx
                                       ; Loop init result can be discarded
                                       pop rax
                                    jmp .__forcond__63
.__for__63:
                                       ; Update
                                          ; Pre-Increment - int
                                             ; RHS
                                                ; Identifier - int j
                                                   push qword [rbp - 16]
                                             pop rdx
                                             add qword [rbp - 16], 1
                                             mov rax, qword [rbp - 16]
                                             push rax ; push result
                                          ; Loop update result can be discarded
                                          pop rax
.__forcond__63:
                                       ; Condition
                                          ; Less Than
                                             ; LHS
                                                ; Identifier - int j
                                                   push qword [rbp - 16]
                                             ; RHS
                                                ; Identifier - int c
                                                   push qword [rbp - -32]
                                             pop rdx ; rhs
                                             pop rax ; lhs
                                             cmp rax, rdx
                                             setl al
                                             movzx eax, al
                                             push rax
                                          pop rax ; __cond
                                          cmp rax, 0 ; __cond
                                          je .__endfor__63
                                       ; Body
                                 ;---------------------------------------
                                          ; Code Block
                                             ; Function Call - print(float) -> void
                                                ; Make space for 1 arg(s)
                                                sub rsp, 8
                                                ; Arguments
                                                   ; Eval arg0
                                                      ; Subscript
                                                         ; LHS
                                                            ; Subscript
                                                               ; LHS
                                                                  ; Identifier - float[][] mat
                                                                     push qword [rbp - -16]
                                                               ; OFFSET
                                                                  ; Identifier - int i
                                                                     push qword [rbp - 8]
                                                               pop rdx ; __offset
                                                               pop rax ; __pointer
                                                               push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                                                         ; OFFSET
                                                            ; Identifier - int j
                                                               push qword [rbp - 16]
                                                         pop rdx ; __offset
                                                         pop rax ; __pointer
                                                         push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                                                   ; Move arg0's result to reverse order position on stack
                                                   pop rax
                                                   mov qword [rsp + 0], rax
                                                ; Call print(float)
                                                call print__float
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
                                 ;---------------------------------------
                                       ; Repeat
jmp .__for__63
                                       ; End of For
.__endfor__63:
                           ;---------------------------------------------
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
                        ;------------------------------------------------
                              ; Repeat
jmp .__for__61
                              ; End of For
.__endfor__61:
                  ;------------------------------------------------------
               ;---------------------------------------------------------
                     ; Function Epilogue
                     mov rsp, rbp ; remove local vars + unpopped pushes
                     pop rbp
                     ret
.__end____main__block__54____printMatrix__float____float__2__int__int:
                  ; End Function Declaration - printMatrix<:float:>(float[][], int, int) -> void
         ; ===============================================================

            ; End Function Template - 
   ; =====================================================================

   ; =====================================================================
            ; Function Declaration - matmul_square(int[][], int[][], int[][], int) -> void
            ; Skip over function declaration
            jmp .__end____main__block__54____matmul_square__int__2__int__2__int__2__int
.__main__block__54____matmul_square__int__2__int__2__int__2__int:
               ; Function Header:
                  ; Setup stack frame
                     push rbp
                     mov rbp, rsp
                     sub rsp, 32
                  ; Parameters
                     ; Param: A [rbp + 16]
                     ; Param: B [rbp + 24]
                     ; Param: C [rbp + 32]
                     ; Param: n [rbp + 40]
                  ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
                     ; [rbp - 8] - int i (<unset-scope-name>)
                     ; [rbp - 16] - int j (<unset-scope-name>)
                     ; [rbp - 24] - int k (<unset-scope-name>)

               ; Body
         ;---------------------------------------------------------------
                  ; Code Block
            ;------------------------------------------------------------
                     ; For-Loop
                     ; Init
                        ; Assignment - '='
                           ; RHS
                              ; Int Literal
                                 mov rax, 0
                                 push rax
                           ; LHS
                              ; Variable Declaration - i
                                 mov rax, qword [rbp - 8]  ; __main__block__54__matmul_square__block__65__for__66__i
                           pop rdx ; rhs value
                           mov qword [rbp - 8], rdx
                           push rdx
                        ; Loop init result can be discarded
                        pop rax
                     jmp .__forcond__66
.__for__66:
                        ; Update
                           ; Pre-Increment - int
                              ; RHS
                                 ; Identifier - int i
                                    push qword [rbp - 8]
                              pop rdx
                              add qword [rbp - 8], 1
                              mov rax, qword [rbp - 8]
                              push rax ; push result
                           ; Loop update result can be discarded
                           pop rax
.__forcond__66:
                        ; Condition
                           ; Less Than
                              ; LHS
                                 ; Identifier - int i
                                    push qword [rbp - 8]
                              ; RHS
                                 ; Identifier - int n
                                    push qword [rbp - -40]
                              pop rdx ; rhs
                              pop rax ; lhs
                              cmp rax, rdx
                              setl al
                              movzx eax, al
                              push rax
                           pop rax ; __cond
                           cmp rax, 0 ; __cond
                           je .__endfor__66
                        ; Body
                  ;------------------------------------------------------
                           ; Code Block
                     ;---------------------------------------------------
                              ; For-Loop
                              ; Init
                                 ; Assignment - '='
                                    ; RHS
                                       ; Int Literal
                                          mov rax, 0
                                          push rax
                                    ; LHS
                                       ; Variable Declaration - j
                                          mov rax, qword [rbp - 16]  ; __main__block__54__matmul_square__block__65__for__66__block__67__for__68__j
                                    pop rdx ; rhs value
                                    mov qword [rbp - 16], rdx
                                    push rdx
                                 ; Loop init result can be discarded
                                 pop rax
                              jmp .__forcond__68
.__for__68:
                                 ; Update
                                    ; Pre-Increment - int
                                       ; RHS
                                          ; Identifier - int j
                                             push qword [rbp - 16]
                                       pop rdx
                                       add qword [rbp - 16], 1
                                       mov rax, qword [rbp - 16]
                                       push rax ; push result
                                    ; Loop update result can be discarded
                                    pop rax
.__forcond__68:
                                 ; Condition
                                    ; Less Than
                                       ; LHS
                                          ; Identifier - int j
                                             push qword [rbp - 16]
                                       ; RHS
                                          ; Identifier - int n
                                             push qword [rbp - -40]
                                       pop rdx ; rhs
                                       pop rax ; lhs
                                       cmp rax, rdx
                                       setl al
                                       movzx eax, al
                                       push rax
                                    pop rax ; __cond
                                    cmp rax, 0 ; __cond
                                    je .__endfor__68
                                 ; Body
                           ;---------------------------------------------
                                    ; Code Block
                              ;------------------------------------------
                                       ; For-Loop
                                       ; Init
                                          ; Assignment - '='
                                             ; RHS
                                                ; Int Literal
                                                   mov rax, 0
                                                   push rax
                                             ; LHS
                                                ; Variable Declaration - k
                                                   mov rax, qword [rbp - 24]  ; __main__block__54__matmul_square__block__65__for__66__block__67__for__68__block__69__for__70__k
                                             pop rdx ; rhs value
                                             mov qword [rbp - 24], rdx
                                             push rdx
                                          ; Loop init result can be discarded
                                          pop rax
                                       jmp .__forcond__70
.__for__70:
                                          ; Update
                                             ; Pre-Increment - int
                                                ; RHS
                                                   ; Identifier - int k
                                                      push qword [rbp - 24]
                                                pop rdx
                                                add qword [rbp - 24], 1
                                                mov rax, qword [rbp - 24]
                                                push rax ; push result
                                             ; Loop update result can be discarded
                                             pop rax
.__forcond__70:
                                          ; Condition
                                             ; Less Than
                                                ; LHS
                                                   ; Identifier - int k
                                                      push qword [rbp - 24]
                                                ; RHS
                                                   ; Identifier - int n
                                                      push qword [rbp - -40]
                                                pop rdx ; rhs
                                                pop rax ; lhs
                                                cmp rax, rdx
                                                setl al
                                                movzx eax, al
                                                push rax
                                             pop rax ; __cond
                                             cmp rax, 0 ; __cond
                                             je .__endfor__70
                                          ; Body
                                    ;------------------------------------
                                             ; Code Block
                                                ; Assignment - '+='
                                                   ; RHS
                                                      ; Multiplication - int, int
                                                         ; LHS
                                                            ; Subscript
                                                               ; LHS
                                                                  ; Subscript
                                                                     ; LHS
                                                                        ; Identifier - int[][] A
                                                                           push qword [rbp - -16]
                                                                     ; OFFSET
                                                                        ; Identifier - int i
                                                                           push qword [rbp - 8]
                                                                     pop rdx ; __offset
                                                                     pop rax ; __pointer
                                                                     push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                                                               ; OFFSET
                                                                  ; Identifier - int k
                                                                     push qword [rbp - 24]
                                                               pop rdx ; __offset
                                                               pop rax ; __pointer
                                                               push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                                                         ; RHS
                                                            ; Subscript
                                                               ; LHS
                                                                  ; Subscript
                                                                     ; LHS
                                                                        ; Identifier - int[][] B
                                                                           push qword [rbp - -24]
                                                                     ; OFFSET
                                                                        ; Identifier - int k
                                                                           push qword [rbp - 24]
                                                                     pop rdx ; __offset
                                                                     pop rax ; __pointer
                                                                     push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                                                               ; OFFSET
                                                                  ; Identifier - int j
                                                                     push qword [rbp - 16]
                                                               pop rdx ; __offset
                                                               pop rax ; __pointer
                                                               push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                                                         pop rdx
                                                         pop rax
                                                         imul rax, rdx
                                                         push rax
                                                   ; LHS
                                                      ; Subscript assignment
                                                         ; LHS
                                                            ; Subscript
                                                               ; LHS
                                                                  ; Identifier - int[][] C
                                                                     push qword [rbp - -32]
                                                               ; OFFSET
                                                                  ; Identifier - int i
                                                                     push qword [rbp - 8]
                                                               pop rdx ; __offset
                                                               pop rax ; __pointer
                                                               push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                                                         ; OFFSET
                                                            ; Identifier - int j
                                                               push qword [rbp - 16]
                                                         pop rdi ; __offset
                                                         pop rbx ; __pointer
                                                   pop rdx ; rhs value
                                                   mov rax, qword [rbx + 8*rdi] ; read lhs value
                                                   add rax, rdx      ; add lhs and rhs
                                                   mov qword [rbx + 8*rdi], rax ; write back to lhs
                                                   push rax          ; push result for other expressions
                                                ; Statement results can be ignored
                                                pop rdx
                                    ;------------------------------------
                                          ; Repeat
jmp .__for__70
                                          ; End of For
.__endfor__70:
                              ;------------------------------------------
                           ;---------------------------------------------
                                 ; Repeat
jmp .__for__68
                                 ; End of For
.__endfor__68:
                     ;---------------------------------------------------
                  ;------------------------------------------------------
                        ; Repeat
jmp .__for__66
                        ; End of For
.__endfor__66:
            ;------------------------------------------------------------
         ;---------------------------------------------------------------
               ; Function Epilogue
               mov rsp, rbp ; remove local vars + unpopped pushes
               pop rbp
               ret
.__end____main__block__54____matmul_square__int__2__int__2__int__2__int:
            ; End Function Declaration - matmul_square(int[][], int[][], int[][], int) -> void
   ; =====================================================================

   ; =====================================================================
            ; Function Declaration - mat_add(int[][], int[][], int[][], int) -> void
            ; Skip over function declaration
            jmp .__end____main__block__54____mat_add__int__2__int__2__int__2__int
.__main__block__54____mat_add__int__2__int__2__int__2__int:
               ; Function Header:
                  ; Setup stack frame
                     push rbp
                     mov rbp, rsp
                     sub rsp, 16
                  ; Parameters
                     ; Param: A [rbp + 16]
                     ; Param: B [rbp + 24]
                     ; Param: C [rbp + 32]
                     ; Param: n [rbp + 40]
                  ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
                     ; [rbp - 8] - int i (<unset-scope-name>)
                     ; [rbp - 16] - int j (<unset-scope-name>)

               ; Body
         ;---------------------------------------------------------------
                  ; Code Block
            ;------------------------------------------------------------
                     ; For-Loop
                     ; Init
                        ; Assignment - '='
                           ; RHS
                              ; Int Literal
                                 mov rax, 0
                                 push rax
                           ; LHS
                              ; Variable Declaration - i
                                 mov rax, qword [rbp - 8]  ; __main__block__54__mat_add__block__72__for__73__i
                           pop rdx ; rhs value
                           mov qword [rbp - 8], rdx
                           push rdx
                        ; Loop init result can be discarded
                        pop rax
                     jmp .__forcond__73
.__for__73:
                        ; Update
                           ; Pre-Increment - int
                              ; RHS
                                 ; Identifier - int i
                                    push qword [rbp - 8]
                              pop rdx
                              add qword [rbp - 8], 1
                              mov rax, qword [rbp - 8]
                              push rax ; push result
                           ; Loop update result can be discarded
                           pop rax
.__forcond__73:
                        ; Condition
                           ; Less Than
                              ; LHS
                                 ; Identifier - int i
                                    push qword [rbp - 8]
                              ; RHS
                                 ; Identifier - int n
                                    push qword [rbp - -40]
                              pop rdx ; rhs
                              pop rax ; lhs
                              cmp rax, rdx
                              setl al
                              movzx eax, al
                              push rax
                           pop rax ; __cond
                           cmp rax, 0 ; __cond
                           je .__endfor__73
                        ; Body
                  ;------------------------------------------------------
                           ; Code Block
                     ;---------------------------------------------------
                              ; For-Loop
                              ; Init
                                 ; Assignment - '='
                                    ; RHS
                                       ; Int Literal
                                          mov rax, 0
                                          push rax
                                    ; LHS
                                       ; Variable Declaration - j
                                          mov rax, qword [rbp - 16]  ; __main__block__54__mat_add__block__72__for__73__block__74__for__75__j
                                    pop rdx ; rhs value
                                    mov qword [rbp - 16], rdx
                                    push rdx
                                 ; Loop init result can be discarded
                                 pop rax
                              jmp .__forcond__75
.__for__75:
                                 ; Update
                                    ; Pre-Increment - int
                                       ; RHS
                                          ; Identifier - int j
                                             push qword [rbp - 16]
                                       pop rdx
                                       add qword [rbp - 16], 1
                                       mov rax, qword [rbp - 16]
                                       push rax ; push result
                                    ; Loop update result can be discarded
                                    pop rax
.__forcond__75:
                                 ; Condition
                                    ; Less Than
                                       ; LHS
                                          ; Identifier - int j
                                             push qword [rbp - 16]
                                       ; RHS
                                          ; Identifier - int n
                                             push qword [rbp - -40]
                                       pop rdx ; rhs
                                       pop rax ; lhs
                                       cmp rax, rdx
                                       setl al
                                       movzx eax, al
                                       push rax
                                    pop rax ; __cond
                                    cmp rax, 0 ; __cond
                                    je .__endfor__75
                                 ; Body
                           ;---------------------------------------------
                                    ; Code Block
                                       ; Assignment - '='
                                          ; RHS
                                             ; Addition - int, int
                                                ; LHS
                                                   ; Subscript
                                                      ; LHS
                                                         ; Subscript
                                                            ; LHS
                                                               ; Identifier - int[][] A
                                                                  push qword [rbp - -16]
                                                            ; OFFSET
                                                               ; Identifier - int i
                                                                  push qword [rbp - 8]
                                                            pop rdx ; __offset
                                                            pop rax ; __pointer
                                                            push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                                                      ; OFFSET
                                                         ; Identifier - int j
                                                            push qword [rbp - 16]
                                                      pop rdx ; __offset
                                                      pop rax ; __pointer
                                                      push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                                                ; RHS
                                                   ; Subscript
                                                      ; LHS
                                                         ; Subscript
                                                            ; LHS
                                                               ; Identifier - int[][] B
                                                                  push qword [rbp - -24]
                                                            ; OFFSET
                                                               ; Identifier - int i
                                                                  push qword [rbp - 8]
                                                            pop rdx ; __offset
                                                            pop rax ; __pointer
                                                            push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                                                      ; OFFSET
                                                         ; Identifier - int j
                                                            push qword [rbp - 16]
                                                      pop rdx ; __offset
                                                      pop rax ; __pointer
                                                      push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                                                pop rdx ; rhs
                                                pop rax ; lhs
                                                add rax, rdx
                                                push rax
                                          ; LHS
                                             ; Subscript assignment
                                                ; LHS
                                                   ; Subscript
                                                      ; LHS
                                                         ; Identifier - int[][] C
                                                            push qword [rbp - -32]
                                                      ; OFFSET
                                                         ; Identifier - int i
                                                            push qword [rbp - 8]
                                                      pop rdx ; __offset
                                                      pop rax ; __pointer
                                                      push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                                                ; OFFSET
                                                   ; Identifier - int j
                                                      push qword [rbp - 16]
                                                pop rdi ; __offset
                                                pop rbx ; __pointer
                                          pop rdx ; rhs value
                                          mov qword [rbx + 8*rdi], rdx
                                          push rdx
                                       ; Statement results can be ignored
                                       pop rdx
                           ;---------------------------------------------
                                 ; Repeat
jmp .__for__75
                                 ; End of For
.__endfor__75:
                     ;---------------------------------------------------
                  ;------------------------------------------------------
                        ; Repeat
jmp .__for__73
                        ; End of For
.__endfor__73:
            ;------------------------------------------------------------
         ;---------------------------------------------------------------
               ; Function Epilogue
               mov rsp, rbp ; remove local vars + unpopped pushes
               pop rbp
               ret
.__end____main__block__54____mat_add__int__2__int__2__int__2__int:
            ; End Function Declaration - mat_add(int[][], int[][], int[][], int) -> void
   ; =====================================================================

            ; Assignment - '='
               ; RHS
                  ; Array Constructor
                     ; Elements
                     ; Array Constructor
                        ; Elements
                        ; Int Literal
                           mov rax, 0
                           push rax
                        ; Int Literal
                           mov rax, 1
                           push rax
                        ; Int Literal
                           mov rax, 2
                           push rax
                        mov edi, 24 ; number of bytes to allocate (nArgs * 8bytes)
                        call malloc ; allocates edi bytes on heap and stores pointer in rax
                        ; Populate array values
                        pop rdx ; get array element 2
                        mov qword [rax + 16], rdx ; arr[2] = rdx
                        pop rdx ; get array element 1
                        mov qword [rax + 8], rdx ; arr[1] = rdx
                        pop rdx ; get array element 0
                        mov qword [rax + 0], rdx ; arr[0] = rdx
                        push rax
                     ; Array Constructor
                        ; Elements
                        ; Int Literal
                           mov rax, 3
                           push rax
                        ; Int Literal
                           mov rax, 4
                           push rax
                        ; Int Literal
                           mov rax, 5
                           push rax
                        mov edi, 24 ; number of bytes to allocate (nArgs * 8bytes)
                        call malloc ; allocates edi bytes on heap and stores pointer in rax
                        ; Populate array values
                        pop rdx ; get array element 2
                        mov qword [rax + 16], rdx ; arr[2] = rdx
                        pop rdx ; get array element 1
                        mov qword [rax + 8], rdx ; arr[1] = rdx
                        pop rdx ; get array element 0
                        mov qword [rax + 0], rdx ; arr[0] = rdx
                        push rax
                     ; Array Constructor
                        ; Elements
                        ; Int Literal
                           mov rax, 6
                           push rax
                        ; Int Literal
                           mov rax, 7
                           push rax
                        ; Int Literal
                           mov rax, 8
                           push rax
                        mov edi, 24 ; number of bytes to allocate (nArgs * 8bytes)
                        call malloc ; allocates edi bytes on heap and stores pointer in rax
                        ; Populate array values
                        pop rdx ; get array element 2
                        mov qword [rax + 16], rdx ; arr[2] = rdx
                        pop rdx ; get array element 1
                        mov qword [rax + 8], rdx ; arr[1] = rdx
                        pop rdx ; get array element 0
                        mov qword [rax + 0], rdx ; arr[0] = rdx
                        push rax
                     mov edi, 24 ; number of bytes to allocate (nArgs * 8bytes)
                     call malloc ; allocates edi bytes on heap and stores pointer in rax
                     ; Populate array values
                     pop rdx ; get array element 2
                     mov qword [rax + 16], rdx ; arr[2] = rdx
                     pop rdx ; get array element 1
                     mov qword [rax + 8], rdx ; arr[1] = rdx
                     pop rdx ; get array element 0
                     mov qword [rax + 0], rdx ; arr[0] = rdx
                     push rax
               ; LHS
                  ; Variable Declaration - A
                     mov rax, qword [rbp - 312]  ; __main__block__54__A
               pop rdx ; rhs value
               mov qword [rbp - 312], rdx
               push rdx
            ; Statement results can be ignored
            pop rdx
            ; Assignment - '='
               ; RHS
                  ; Array Constructor
                     ; Elements
                     ; Array Constructor
                        ; Elements
                        ; Int Literal
                           mov rax, 8
                           push rax
                        ; Int Literal
                           mov rax, 7
                           push rax
                        ; Int Literal
                           mov rax, 6
                           push rax
                        mov edi, 24 ; number of bytes to allocate (nArgs * 8bytes)
                        call malloc ; allocates edi bytes on heap and stores pointer in rax
                        ; Populate array values
                        pop rdx ; get array element 2
                        mov qword [rax + 16], rdx ; arr[2] = rdx
                        pop rdx ; get array element 1
                        mov qword [rax + 8], rdx ; arr[1] = rdx
                        pop rdx ; get array element 0
                        mov qword [rax + 0], rdx ; arr[0] = rdx
                        push rax
                     ; Array Constructor
                        ; Elements
                        ; Int Literal
                           mov rax, 5
                           push rax
                        ; Int Literal
                           mov rax, 4
                           push rax
                        ; Int Literal
                           mov rax, 3
                           push rax
                        mov edi, 24 ; number of bytes to allocate (nArgs * 8bytes)
                        call malloc ; allocates edi bytes on heap and stores pointer in rax
                        ; Populate array values
                        pop rdx ; get array element 2
                        mov qword [rax + 16], rdx ; arr[2] = rdx
                        pop rdx ; get array element 1
                        mov qword [rax + 8], rdx ; arr[1] = rdx
                        pop rdx ; get array element 0
                        mov qword [rax + 0], rdx ; arr[0] = rdx
                        push rax
                     ; Array Constructor
                        ; Elements
                        ; Int Literal
                           mov rax, 2
                           push rax
                        ; Int Literal
                           mov rax, 1
                           push rax
                        ; Int Literal
                           mov rax, 0
                           push rax
                        mov edi, 24 ; number of bytes to allocate (nArgs * 8bytes)
                        call malloc ; allocates edi bytes on heap and stores pointer in rax
                        ; Populate array values
                        pop rdx ; get array element 2
                        mov qword [rax + 16], rdx ; arr[2] = rdx
                        pop rdx ; get array element 1
                        mov qword [rax + 8], rdx ; arr[1] = rdx
                        pop rdx ; get array element 0
                        mov qword [rax + 0], rdx ; arr[0] = rdx
                        push rax
                     mov edi, 24 ; number of bytes to allocate (nArgs * 8bytes)
                     call malloc ; allocates edi bytes on heap and stores pointer in rax
                     ; Populate array values
                     pop rdx ; get array element 2
                     mov qword [rax + 16], rdx ; arr[2] = rdx
                     pop rdx ; get array element 1
                     mov qword [rax + 8], rdx ; arr[1] = rdx
                     pop rdx ; get array element 0
                     mov qword [rax + 0], rdx ; arr[0] = rdx
                     push rax
               ; LHS
                  ; Variable Declaration - B
                     mov rax, qword [rbp - 320]  ; __main__block__54__B
               pop rdx ; rhs value
               mov qword [rbp - 320], rdx
               push rdx
            ; Statement results can be ignored
            pop rdx
            ; Assignment - '='
               ; RHS
                  ; Array Constructor
                     ; Elements
                     ; Array Constructor
                        ; Elements
                        ; Int Literal
                           mov rax, 0
                           push rax
                        ; Int Literal
                           mov rax, 0
                           push rax
                        ; Int Literal
                           mov rax, 0
                           push rax
                        mov edi, 24 ; number of bytes to allocate (nArgs * 8bytes)
                        call malloc ; allocates edi bytes on heap and stores pointer in rax
                        ; Populate array values
                        pop rdx ; get array element 2
                        mov qword [rax + 16], rdx ; arr[2] = rdx
                        pop rdx ; get array element 1
                        mov qword [rax + 8], rdx ; arr[1] = rdx
                        pop rdx ; get array element 0
                        mov qword [rax + 0], rdx ; arr[0] = rdx
                        push rax
                     ; Array Constructor
                        ; Elements
                        ; Int Literal
                           mov rax, 0
                           push rax
                        ; Int Literal
                           mov rax, 0
                           push rax
                        ; Int Literal
                           mov rax, 0
                           push rax
                        mov edi, 24 ; number of bytes to allocate (nArgs * 8bytes)
                        call malloc ; allocates edi bytes on heap and stores pointer in rax
                        ; Populate array values
                        pop rdx ; get array element 2
                        mov qword [rax + 16], rdx ; arr[2] = rdx
                        pop rdx ; get array element 1
                        mov qword [rax + 8], rdx ; arr[1] = rdx
                        pop rdx ; get array element 0
                        mov qword [rax + 0], rdx ; arr[0] = rdx
                        push rax
                     ; Array Constructor
                        ; Elements
                        ; Int Literal
                           mov rax, 0
                           push rax
                        ; Int Literal
                           mov rax, 0
                           push rax
                        ; Int Literal
                           mov rax, 0
                           push rax
                        mov edi, 24 ; number of bytes to allocate (nArgs * 8bytes)
                        call malloc ; allocates edi bytes on heap and stores pointer in rax
                        ; Populate array values
                        pop rdx ; get array element 2
                        mov qword [rax + 16], rdx ; arr[2] = rdx
                        pop rdx ; get array element 1
                        mov qword [rax + 8], rdx ; arr[1] = rdx
                        pop rdx ; get array element 0
                        mov qword [rax + 0], rdx ; arr[0] = rdx
                        push rax
                     mov edi, 24 ; number of bytes to allocate (nArgs * 8bytes)
                     call malloc ; allocates edi bytes on heap and stores pointer in rax
                     ; Populate array values
                     pop rdx ; get array element 2
                     mov qword [rax + 16], rdx ; arr[2] = rdx
                     pop rdx ; get array element 1
                     mov qword [rax + 8], rdx ; arr[1] = rdx
                     pop rdx ; get array element 0
                     mov qword [rax + 0], rdx ; arr[0] = rdx
                     push rax
               ; LHS
                  ; Variable Declaration - C
                     mov rax, qword [rbp - 328]  ; __main__block__54__C
               pop rdx ; rhs value
               mov qword [rbp - 328], rdx
               push rdx
            ; Statement results can be ignored
            pop rdx
            ; Function Call - println(char[]) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; String Literal
                        ; "A = "
                        mov rax, .str144
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
            ; Function Call - printMatrix<:int:>(int[][], int, int) -> void
               ; Make space for 3 arg(s)
               sub rsp, 24
               ; Arguments
                  ; Eval arg0
                     ; Identifier - int[][] A
                        push qword [rbp - 312]
                  ; Move arg0's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 0], rax
                  ; Eval arg1
                     ; Int Literal
                        mov rax, 3
                        push rax
                  ; Move arg1's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 8], rax
                  ; Eval arg2
                     ; Int Literal
                        mov rax, 3
                        push rax
                  ; Move arg2's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 16], rax
               ; Call printMatrix<:int:>(int[][], int, int)
               call .__main__block__54____printMatrix__int____int__2__int__int
               ; Remove args
               add rsp, 24
               ; Push return value
               push rax
            ; Statement results can be ignored
            pop rdx
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
            ; Function Call - println(char[]) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; String Literal
                        ; "B = "
                        mov rax, .str145
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
            ; Function Call - printMatrix<:int:>(int[][], int, int) -> void
               ; Make space for 3 arg(s)
               sub rsp, 24
               ; Arguments
                  ; Eval arg0
                     ; Identifier - int[][] B
                        push qword [rbp - 320]
                  ; Move arg0's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 0], rax
                  ; Eval arg1
                     ; Int Literal
                        mov rax, 3
                        push rax
                  ; Move arg1's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 8], rax
                  ; Eval arg2
                     ; Int Literal
                        mov rax, 3
                        push rax
                  ; Move arg2's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 16], rax
               ; Call printMatrix<:int:>(int[][], int, int)
               call .__main__block__54____printMatrix__int____int__2__int__int
               ; Remove args
               add rsp, 24
               ; Push return value
               push rax
            ; Statement results can be ignored
            pop rdx
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
            ; Function Call - println(char[]) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; String Literal
                        ; "C = "
                        mov rax, .str146
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
            ; Function Call - printMatrix<:int:>(int[][], int, int) -> void
               ; Make space for 3 arg(s)
               sub rsp, 24
               ; Arguments
                  ; Eval arg0
                     ; Identifier - int[][] C
                        push qword [rbp - 328]
                  ; Move arg0's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 0], rax
                  ; Eval arg1
                     ; Int Literal
                        mov rax, 3
                        push rax
                  ; Move arg1's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 8], rax
                  ; Eval arg2
                     ; Int Literal
                        mov rax, 3
                        push rax
                  ; Move arg2's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 16], rax
               ; Call printMatrix<:int:>(int[][], int, int)
               call .__main__block__54____printMatrix__int____int__2__int__int
               ; Remove args
               add rsp, 24
               ; Push return value
               push rax
            ; Statement results can be ignored
            pop rdx
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
            ; Function Call - println(char[]) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; String Literal
                        ; "C = A (dot) B"
                        mov rax, .str147
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
            ; Function Call - matmul_square(int[][], int[][], int[][], int) -> void
               ; Make space for 4 arg(s)
               sub rsp, 32
               ; Arguments
                  ; Eval arg0
                     ; Identifier - int[][] A
                        push qword [rbp - 312]
                  ; Move arg0's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 0], rax
                  ; Eval arg1
                     ; Identifier - int[][] B
                        push qword [rbp - 320]
                  ; Move arg1's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 8], rax
                  ; Eval arg2
                     ; Identifier - int[][] C
                        push qword [rbp - 328]
                  ; Move arg2's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 16], rax
                  ; Eval arg3
                     ; Int Literal
                        mov rax, 3
                        push rax
                  ; Move arg3's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 24], rax
               ; Call matmul_square(int[][], int[][], int[][], int)
               call .__main__block__54____matmul_square__int__2__int__2__int__2__int
               ; Remove args
               add rsp, 32
               ; Push return value
               push rax
            ; Statement results can be ignored
            pop rdx
            ; Function Call - println(char[]) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; String Literal
                        ; "C = "
                        mov rax, .str148
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
            ; Function Call - printMatrix<:int:>(int[][], int, int) -> void
               ; Make space for 3 arg(s)
               sub rsp, 24
               ; Arguments
                  ; Eval arg0
                     ; Identifier - int[][] C
                        push qword [rbp - 328]
                  ; Move arg0's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 0], rax
                  ; Eval arg1
                     ; Int Literal
                        mov rax, 3
                        push rax
                  ; Move arg1's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 8], rax
                  ; Eval arg2
                     ; Int Literal
                        mov rax, 3
                        push rax
                  ; Move arg2's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 16], rax
               ; Call printMatrix<:int:>(int[][], int, int)
               call .__main__block__54____printMatrix__int____int__2__int__int
               ; Remove args
               add rsp, 24
               ; Push return value
               push rax
            ; Statement results can be ignored
            pop rdx
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
                  ; Array Allocator
                     ; Int Literal
                        mov rax, 3
                        push rax
                     pop rdx ; num elements for dimension[0]
                     imul rdx, 8 ; 8 bytes per element
                     mov rdi, rdx ; num bytes to allocate
                     call malloc ; allocates edi bytes on heap and stores pointer in rax
                     push rax ; __ptr
               ; LHS
                  ; Variable Declaration - D
                     mov rax, qword [rbp - 336]  ; __main__block__54__D
               pop rdx ; rhs value
               mov qword [rbp - 336], rdx
               push rdx
            ; Statement results can be ignored
            pop rdx
            ; Assignment - '='
               ; RHS
                  ; Array Allocator
                     ; Int Literal
                        mov rax, 3
                        push rax
                     pop rdx ; num elements for dimension[0]
                     imul rdx, 8 ; 8 bytes per element
                     mov rdi, rdx ; num bytes to allocate
                     call malloc ; allocates edi bytes on heap and stores pointer in rax
                     push rax ; __ptr
               ; LHS
                  ; Subscript assignment
                     ; LHS
                        ; Identifier - int[][] D
                           push qword [rbp - 336]
                     ; OFFSET
                        ; Int Literal
                           mov rax, 0
                           push rax
                     pop rdi ; __offset
                     pop rbx ; __pointer
               pop rdx ; rhs value
               mov qword [rbx + 8*rdi], rdx
               push rdx
            ; Statement results can be ignored
            pop rdx
            ; Assignment - '='
               ; RHS
                  ; Array Allocator
                     ; Int Literal
                        mov rax, 3
                        push rax
                     pop rdx ; num elements for dimension[0]
                     imul rdx, 8 ; 8 bytes per element
                     mov rdi, rdx ; num bytes to allocate
                     call malloc ; allocates edi bytes on heap and stores pointer in rax
                     push rax ; __ptr
               ; LHS
                  ; Subscript assignment
                     ; LHS
                        ; Identifier - int[][] D
                           push qword [rbp - 336]
                     ; OFFSET
                        ; Int Literal
                           mov rax, 1
                           push rax
                     pop rdi ; __offset
                     pop rbx ; __pointer
               pop rdx ; rhs value
               mov qword [rbx + 8*rdi], rdx
               push rdx
            ; Statement results can be ignored
            pop rdx
            ; Assignment - '='
               ; RHS
                  ; Array Allocator
                     ; Int Literal
                        mov rax, 3
                        push rax
                     pop rdx ; num elements for dimension[0]
                     imul rdx, 8 ; 8 bytes per element
                     mov rdi, rdx ; num bytes to allocate
                     call malloc ; allocates edi bytes on heap and stores pointer in rax
                     push rax ; __ptr
               ; LHS
                  ; Subscript assignment
                     ; LHS
                        ; Identifier - int[][] D
                           push qword [rbp - 336]
                     ; OFFSET
                        ; Int Literal
                           mov rax, 2
                           push rax
                     pop rdi ; __offset
                     pop rbx ; __pointer
               pop rdx ; rhs value
               mov qword [rbx + 8*rdi], rdx
               push rdx
            ; Statement results can be ignored
            pop rdx
            ; Function Call - println(char[]) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; String Literal
                        ; "D = A + B"
                        mov rax, .str149
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
            ; Function Call - mat_add(int[][], int[][], int[][], int) -> void
               ; Make space for 4 arg(s)
               sub rsp, 32
               ; Arguments
                  ; Eval arg0
                     ; Identifier - int[][] A
                        push qword [rbp - 312]
                  ; Move arg0's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 0], rax
                  ; Eval arg1
                     ; Identifier - int[][] B
                        push qword [rbp - 320]
                  ; Move arg1's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 8], rax
                  ; Eval arg2
                     ; Identifier - int[][] D
                        push qword [rbp - 336]
                  ; Move arg2's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 16], rax
                  ; Eval arg3
                     ; Int Literal
                        mov rax, 3
                        push rax
                  ; Move arg3's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 24], rax
               ; Call mat_add(int[][], int[][], int[][], int)
               call .__main__block__54____mat_add__int__2__int__2__int__2__int
               ; Remove args
               add rsp, 32
               ; Push return value
               push rax
            ; Statement results can be ignored
            pop rdx
            ; Function Call - println(char[]) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; String Literal
                        ; "D = "
                        mov rax, .str150
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
            ; Function Call - printMatrix<:int:>(int[][], int, int) -> void
               ; Make space for 3 arg(s)
               sub rsp, 24
               ; Arguments
                  ; Eval arg0
                     ; Identifier - int[][] D
                        push qword [rbp - 336]
                  ; Move arg0's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 0], rax
                  ; Eval arg1
                     ; Int Literal
                        mov rax, 3
                        push rax
                  ; Move arg1's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 8], rax
                  ; Eval arg2
                     ; Int Literal
                        mov rax, 3
                        push rax
                  ; Move arg2's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 16], rax
               ; Call printMatrix<:int:>(int[][], int, int)
               call .__main__block__54____printMatrix__int____int__2__int__int
               ; Remove args
               add rsp, 24
               ; Push return value
               push rax
            ; Statement results can be ignored
            pop rdx
            ; Assignment - '='
               ; RHS
                  ; Array Constructor
                     ; Elements
                     ; Array Constructor
                        ; Elements
                        ; Float Literal
                           mov rax, qword [.float38] ; 1.0
                           push rax
                        ; Float Literal
                           mov rax, qword [.float39] ; 0.0
                           push rax
                        ; Float Literal
                           mov rax, qword [.float40] ; 0.0
                           push rax
                        mov edi, 24 ; number of bytes to allocate (nArgs * 8bytes)
                        call malloc ; allocates edi bytes on heap and stores pointer in rax
                        ; Populate array values
                        pop rdx ; get array element 2
                        mov qword [rax + 16], rdx ; arr[2] = rdx
                        pop rdx ; get array element 1
                        mov qword [rax + 8], rdx ; arr[1] = rdx
                        pop rdx ; get array element 0
                        mov qword [rax + 0], rdx ; arr[0] = rdx
                        push rax
                     ; Array Constructor
                        ; Elements
                        ; Float Literal
                           mov rax, qword [.float41] ; 0.0
                           push rax
                        ; Float Literal
                           mov rax, qword [.float42] ; 1.0
                           push rax
                        ; Float Literal
                           mov rax, qword [.float43] ; 0.0
                           push rax
                        mov edi, 24 ; number of bytes to allocate (nArgs * 8bytes)
                        call malloc ; allocates edi bytes on heap and stores pointer in rax
                        ; Populate array values
                        pop rdx ; get array element 2
                        mov qword [rax + 16], rdx ; arr[2] = rdx
                        pop rdx ; get array element 1
                        mov qword [rax + 8], rdx ; arr[1] = rdx
                        pop rdx ; get array element 0
                        mov qword [rax + 0], rdx ; arr[0] = rdx
                        push rax
                     ; Array Constructor
                        ; Elements
                        ; Float Literal
                           mov rax, qword [.float44] ; 0.0
                           push rax
                        ; Float Literal
                           mov rax, qword [.float45] ; 0.0
                           push rax
                        ; Float Literal
                           mov rax, qword [.float46] ; 1.0
                           push rax
                        mov edi, 24 ; number of bytes to allocate (nArgs * 8bytes)
                        call malloc ; allocates edi bytes on heap and stores pointer in rax
                        ; Populate array values
                        pop rdx ; get array element 2
                        mov qword [rax + 16], rdx ; arr[2] = rdx
                        pop rdx ; get array element 1
                        mov qword [rax + 8], rdx ; arr[1] = rdx
                        pop rdx ; get array element 0
                        mov qword [rax + 0], rdx ; arr[0] = rdx
                        push rax
                     mov edi, 24 ; number of bytes to allocate (nArgs * 8bytes)
                     call malloc ; allocates edi bytes on heap and stores pointer in rax
                     ; Populate array values
                     pop rdx ; get array element 2
                     mov qword [rax + 16], rdx ; arr[2] = rdx
                     pop rdx ; get array element 1
                     mov qword [rax + 8], rdx ; arr[1] = rdx
                     pop rdx ; get array element 0
                     mov qword [rax + 0], rdx ; arr[0] = rdx
                     push rax
               ; LHS
                  ; Variable Declaration - mat
                     mov rax, qword [rbp - 344]  ; __main__block__54__mat
               pop rdx ; rhs value
               mov qword [rbp - 344], rdx
               push rdx
            ; Statement results can be ignored
            pop rdx
            ; Function Call - println(float) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; Subscript
                        ; LHS
                           ; Subscript
                              ; LHS
                                 ; Identifier - float[][] mat
                                    push qword [rbp - 344]
                              ; OFFSET
                                 ; Int Literal
                                    mov rax, 0
                                    push rax
                              pop rdx ; __offset
                              pop rax ; __pointer
                              push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                        ; OFFSET
                           ; Int Literal
                              mov rax, 0
                              push rax
                        pop rdx ; __offset
                        pop rax ; __pointer
                        push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
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
            ; Function Call - printMatrix<:float:>(float[][], int, int) -> void
               ; Make space for 3 arg(s)
               sub rsp, 24
               ; Arguments
                  ; Eval arg0
                     ; Identifier - float[][] mat
                        push qword [rbp - 344]
                  ; Move arg0's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 0], rax
                  ; Eval arg1
                     ; Int Literal
                        mov rax, 3
                        push rax
                  ; Move arg1's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 8], rax
                  ; Eval arg2
                     ; Int Literal
                        mov rax, 3
                        push rax
                  ; Move arg2's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 16], rax
               ; Call printMatrix<:float:>(float[][], int, int)
               call .__main__block__54____printMatrix__float____float__2__int__int
               ; Remove args
               add rsp, 24
               ; Push return value
               push rax
            ; Statement results can be ignored
            pop rdx
            ; Free Operator
               ; RHS
                  ; Subscript
                     ; LHS
                        ; Identifier - float[][] mat
                           push qword [rbp - 344]
                     ; OFFSET
                        ; Int Literal
                           mov rax, 0
                           push rax
                     pop rdx ; __offset
                     pop rax ; __pointer
                     push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
               ; Free pointer
               pop rdi   ; pointer
               call free ; free the pointer
               push rax  ; undefined return value
            ; Statement results can be ignored
            pop rdx
            ; Free Operator
               ; RHS
                  ; Subscript
                     ; LHS
                        ; Identifier - float[][] mat
                           push qword [rbp - 344]
                     ; OFFSET
                        ; Int Literal
                           mov rax, 1
                           push rax
                     pop rdx ; __offset
                     pop rax ; __pointer
                     push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
               ; Free pointer
               pop rdi   ; pointer
               call free ; free the pointer
               push rax  ; undefined return value
            ; Statement results can be ignored
            pop rdx
            ; Free Operator
               ; RHS
                  ; Subscript
                     ; LHS
                        ; Identifier - float[][] mat
                           push qword [rbp - 344]
                     ; OFFSET
                        ; Int Literal
                           mov rax, 2
                           push rax
                     pop rdx ; __offset
                     pop rax ; __pointer
                     push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
               ; Free pointer
               pop rdi   ; pointer
               call free ; free the pointer
               push rax  ; undefined return value
            ; Statement results can be ignored
            pop rdx
            ; Free Operator
               ; RHS
                  ; Identifier - float[][] mat
                     push qword [rbp - 344]
               ; Free pointer
               pop rdi   ; pointer
               call free ; free the pointer
               push rax  ; undefined return value
            ; Statement results can be ignored
            pop rdx
;------------------------------------------------------------------------
         ; Function Call - println(char[]) -> void
            ; Make space for 1 arg(s)
            sub rsp, 8
            ; Arguments
               ; Eval arg0
                  ; String Literal
                     ; "=== Testing Classes ==="
                     mov rax, .str151
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
   ; =====================================================================
            ; Class Declaration - __main__block__77____Vector2D inherits __main__Object
               ; Class data
               section .data
                  ; Dispatch Table - this might need to be a malloc**
                  .__dtable____main__block__77____Vector2D:
                  ; Dispatch Table Entries
                  dq .__method____main__block__77____Vector2D____set__float__float ; 0
                  dq .__method____main__block__77____Vector2D____set__Vector2D ; 1
                  dq .__method____main__block__77____Vector2D____add__Vector2D ; 2
               section .text
      ;------------------------------------------------------------------
               ; Field - float Vector2D::x
               section .data
               .__field____main__block__77____Vector2D____x: dq 1
               section .text
      ;------------------------------------------------------------------
      ;------------------------------------------------------------------
               ; Field - float Vector2D::y
               section .data
               .__field____main__block__77____Vector2D____y: dq 2
               section .text
      ;------------------------------------------------------------------
            ; skip over class methods
            jmp .__endclass____main__block__77____Vector2D
      ;------------------------------------------------------------------
               ; Constructor Declaration - Vector2D::Vector2D(float, float) -> Vector2D
               jmp .__end__ctor____main__block__77____Vector2D____Vector2D__float__float
               .__ctor____main__block__77____Vector2D____Vector2D__float__float:
               ; Function Header:
                  ; Setup stack frame
                     push rbp
                     mov rbp, rsp
                     ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
                        sub rsp, 16 ; space for local variables (16-byte aligned)
                        ; [rbp - 8] - this - Reference to 'this' object instance
                  ; Creating Class Instance
                     mov rdi, 24 ; [dtable, field0, field1, ..., fieldN] each 8 bytes
                     call malloc
                     mov qword [rbp - 8], rax ; save class instance as 'this'
                     ; Add Dispatch Table
                     mov rax, qword [rbp - 8] ; this
                     mov qword [rax + 0], .__dtable____main__block__77____Vector2D ; this[0] = &dtable
                  ; Parameters
                     ; Param: x [rbp + 16]
                     ; Param: y [rbp + 24]
               ; Body
         ;---------------------------------------------------------------
                  ; Code Block
                     ; Assignment - '='
                        ; RHS
                           ; Identifier - float x
                              push qword [rbp - -16]
                        ; LHS
                           ; Member Accessor Assignment
                              ; LHS
                                 ; This keyword
                                    push qword [rbp - 8] ; __this
                              ; RHS
                                 push qword [.__field____main__block__77____Vector2D____x] ; 
                              pop rdi ; rhs
                              pop rbx ; lhs
                        pop rdx ; rhs value
                        mov qword [rbx + 8*rdi], rdx
                        push rdx
                     ; Statement results can be ignored
                     pop rdx
                     ; Assignment - '='
                        ; RHS
                           ; Identifier - float y
                              push qword [rbp - -24]
                        ; LHS
                           ; Member Accessor Assignment
                              ; LHS
                                 ; This keyword
                                    push qword [rbp - 8] ; __this
                              ; RHS
                                 push qword [.__field____main__block__77____Vector2D____y] ; 
                              pop rdi ; rhs
                              pop rbx ; lhs
                        pop rdx ; rhs value
                        mov qword [rbx + 8*rdi], rdx
                        push rdx
                     ; Statement results can be ignored
                     pop rdx
         ;---------------------------------------------------------------
               mov rax, qword [rbp - 8] ; __this
               ; Function Epilogue
               mov rsp, rbp ; remove local vars + unpopped pushes
               pop rbp
               ret
            .__end__ctor____main__block__77____Vector2D____Vector2D__float__float:
            ; End Constructor Declaration - __ctor____main__block__77____Vector2D____Vector2D__float__float
   ;---------------------------------------------------------------------

   ;---------------------------------------------------------------------
            ; Method Declaration - Vector2D::set(float, float) -> void
            jmp .__end__method____main__block__77____Vector2D____set__float__float
            .__method____main__block__77____Vector2D____set__float__float:
               ; Function Header:
               ; Setup stack frame
                  push rbp
                  mov rbp, rsp
                  ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
                     sub rsp, 16 ; space for local variables (16-byte aligned)
                     ; [rbp - 8] - this - Reference to 'this' object instance
                     mov rdx, qword [rbp + 16] ; param passed 'this'
                     mov qword [rbp - 8], rdx ; save this to a local
               ; Parameters
                  ; Param: x [rbp + 24] (__main__block__77____Vector2D__set__x)
                  ; Param: y [rbp + 32] (__main__block__77____Vector2D__set__y)
               ; Body
         ;---------------------------------------------------------------
                  ; Code Block
                     ; Assignment - '='
                        ; RHS
                           ; Identifier - float x
                              push qword [rbp - -24]
                        ; LHS
                           ; Member Accessor Assignment
                              ; LHS
                                 ; This keyword
                                    push qword [rbp - 8] ; __this
                              ; RHS
                                 push qword [.__field____main__block__77____Vector2D____x] ; 
                              pop rdi ; rhs
                              pop rbx ; lhs
                        pop rdx ; rhs value
                        mov qword [rbx + 8*rdi], rdx
                        push rdx
                     ; Statement results can be ignored
                     pop rdx
                     ; Assignment - '='
                        ; RHS
                           ; Identifier - float y
                              push qword [rbp - -32]
                        ; LHS
                           ; Member Accessor Assignment
                              ; LHS
                                 ; This keyword
                                    push qword [rbp - 8] ; __this
                              ; RHS
                                 push qword [.__field____main__block__77____Vector2D____y] ; 
                              pop rdi ; rhs
                              pop rbx ; lhs
                        pop rdx ; rhs value
                        mov qword [rbx + 8*rdi], rdx
                        push rdx
                     ; Statement results can be ignored
                     pop rdx
         ;---------------------------------------------------------------
               ; Function Epilogue
               mov rsp, rbp ; remove local vars + unpopped pushes
               pop rbp
               ret
            .__end__method____main__block__77____Vector2D____set__float__float:
            ; End Method Declaration - .__method____main__block__77____Vector2D____set__float__float
   ;---------------------------------------------------------------------

   ;---------------------------------------------------------------------
            ; Method Declaration - Vector2D::set(Vector2D) -> void
            jmp .__end__method____main__block__77____Vector2D____set__Vector2D
            .__method____main__block__77____Vector2D____set__Vector2D:
               ; Function Header:
               ; Setup stack frame
                  push rbp
                  mov rbp, rsp
                  ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
                     sub rsp, 16 ; space for local variables (16-byte aligned)
                     ; [rbp - 8] - this - Reference to 'this' object instance
                     mov rdx, qword [rbp + 16] ; param passed 'this'
                     mov qword [rbp - 8], rdx ; save this to a local
               ; Parameters
                  ; Param: other [rbp + 24] (__main__block__77____Vector2D__set__other)
               ; Body
         ;---------------------------------------------------------------
                  ; Code Block
                     ; Assignment - '='
                        ; RHS
                           ; Member Accessor
                              ; LHS
                                 ; Identifier - Vector2D other
                                    push qword [rbp - -24]
                              ; RHS
                                 push qword [.__field____main__block__77____Vector2D____x] ; stored index associated with field that is being accessed
                              pop rdx ; rhs
                              pop rax ; lhs
                              push qword [rax + 8*rdx] ; lhs.rhs
                        ; LHS
                           ; Member Accessor Assignment
                              ; LHS
                                 ; This keyword
                                    push qword [rbp - 8] ; __this
                              ; RHS
                                 push qword [.__field____main__block__77____Vector2D____x] ; 
                              pop rdi ; rhs
                              pop rbx ; lhs
                        pop rdx ; rhs value
                        mov qword [rbx + 8*rdi], rdx
                        push rdx
                     ; Statement results can be ignored
                     pop rdx
                     ; Assignment - '='
                        ; RHS
                           ; Member Accessor
                              ; LHS
                                 ; Identifier - Vector2D other
                                    push qword [rbp - -24]
                              ; RHS
                                 push qword [.__field____main__block__77____Vector2D____y] ; stored index associated with field that is being accessed
                              pop rdx ; rhs
                              pop rax ; lhs
                              push qword [rax + 8*rdx] ; lhs.rhs
                        ; LHS
                           ; Member Accessor Assignment
                              ; LHS
                                 ; This keyword
                                    push qword [rbp - 8] ; __this
                              ; RHS
                                 push qword [.__field____main__block__77____Vector2D____y] ; 
                              pop rdi ; rhs
                              pop rbx ; lhs
                        pop rdx ; rhs value
                        mov qword [rbx + 8*rdi], rdx
                        push rdx
                     ; Statement results can be ignored
                     pop rdx
         ;---------------------------------------------------------------
               ; Function Epilogue
               mov rsp, rbp ; remove local vars + unpopped pushes
               pop rbp
               ret
            .__end__method____main__block__77____Vector2D____set__Vector2D:
            ; End Method Declaration - .__method____main__block__77____Vector2D____set__Vector2D
   ;---------------------------------------------------------------------

   ;---------------------------------------------------------------------
            ; Method Declaration - Vector2D::add(Vector2D) -> void
            jmp .__end__method____main__block__77____Vector2D____add__Vector2D
            .__method____main__block__77____Vector2D____add__Vector2D:
               ; Function Header:
               ; Setup stack frame
                  push rbp
                  mov rbp, rsp
                  ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
                     sub rsp, 16 ; space for local variables (16-byte aligned)
                     ; [rbp - 8] - this - Reference to 'this' object instance
                     mov rdx, qword [rbp + 16] ; param passed 'this'
                     mov qword [rbp - 8], rdx ; save this to a local
               ; Parameters
                  ; Param: other [rbp + 24] (__main__block__77____Vector2D__add__other)
               ; Body
         ;---------------------------------------------------------------
                  ; Code Block
                     ; Assignment - '+='
                        ; RHS
                           ; Member Accessor
                              ; LHS
                                 ; Identifier - Vector2D other
                                    push qword [rbp - -24]
                              ; RHS
                                 push qword [.__field____main__block__77____Vector2D____x] ; stored index associated with field that is being accessed
                              pop rdx ; rhs
                              pop rax ; lhs
                              push qword [rax + 8*rdx] ; lhs.rhs
                        ; LHS
                           ; Member Accessor Assignment
                              ; LHS
                                 ; This keyword
                                    push qword [rbp - 8] ; __this
                              ; RHS
                                 push qword [.__field____main__block__77____Vector2D____x] ; 
                              pop rdi ; rhs
                              pop rbx ; lhs
                        pop rdx ; rhs value
                        movq xmm0, rdx    ; load rhs value, xmm0 = mem[0], zero
                        addsd xmm0, qword [rbx + 8*rdi] ; add lhs and rhs
                        movsd qword [rbx + 8*rdi], xmm0 ; write back to lhs
                        movq rax, xmm0
                        push rax          ; push result for other expressions
                     ; Statement results can be ignored
                     pop rdx
                     ; Assignment - '+='
                        ; RHS
                           ; Member Accessor
                              ; LHS
                                 ; Identifier - Vector2D other
                                    push qword [rbp - -24]
                              ; RHS
                                 push qword [.__field____main__block__77____Vector2D____y] ; stored index associated with field that is being accessed
                              pop rdx ; rhs
                              pop rax ; lhs
                              push qword [rax + 8*rdx] ; lhs.rhs
                        ; LHS
                           ; Member Accessor Assignment
                              ; LHS
                                 ; This keyword
                                    push qword [rbp - 8] ; __this
                              ; RHS
                                 push qword [.__field____main__block__77____Vector2D____y] ; 
                              pop rdi ; rhs
                              pop rbx ; lhs
                        pop rdx ; rhs value
                        movq xmm0, rdx    ; load rhs value, xmm0 = mem[0], zero
                        addsd xmm0, qword [rbx + 8*rdi] ; add lhs and rhs
                        movsd qword [rbx + 8*rdi], xmm0 ; write back to lhs
                        movq rax, xmm0
                        push rax          ; push result for other expressions
                     ; Statement results can be ignored
                     pop rdx
         ;---------------------------------------------------------------
               ; Function Epilogue
               mov rsp, rbp ; remove local vars + unpopped pushes
               pop rbp
               ret
            .__end__method____main__block__77____Vector2D____add__Vector2D:
            ; End Method Declaration - .__method____main__block__77____Vector2D____add__Vector2D
   ;---------------------------------------------------------------------

.__endclass____main__block__77____Vector2D:
         ; End Class Declaration - __main__block__77____Vector2D
; ========================================================================

         ; Assignment - '='
            ; RHS
               ; Constructor Call - Vector2D::Vector2D(float, float) -> Vector2D
                  ; Make space for 2 arg(s)
                  sub rsp, 16
                  ; Arguments
                     ; Eval arg0
                        ; Float Literal
                           mov rax, qword [.float47] ; 0.5
                           push rax
                     ; Move arg0's result to reverse order position on stack
                     pop rax
                     mov qword [rsp + 0], rax
                     ; Eval arg1
                        ; Float Literal
                           mov rax, qword [.float48] ; 3.1415
                           push rax
                     ; Move arg1's result to reverse order position on stack
                     pop rax
                     mov qword [rsp + 8], rax
                  ; Call Vector2D::Vector2D(float, float)
                  call .__ctor____main__block__77____Vector2D____Vector2D__float__float
                  ; Remove args
                  add rsp, 16
                  ; Push return value
                  push rax
            ; LHS
               ; Variable Declaration - v
                  mov rax, qword [rbp - 352]  ; __main__block__77__v
            pop rdx ; rhs value
            mov qword [rbp - 352], rdx
            push rdx
         ; Statement results can be ignored
         pop rdx
         ; Function Call - print(char[]) -> void
            ; Make space for 1 arg(s)
            sub rsp, 8
            ; Arguments
               ; Eval arg0
                  ; String Literal
                     ; "v.x = "
                     mov rax, .str152
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
                  ; Member Accessor
                     ; LHS
                        ; Identifier - Vector2D v
                           push qword [rbp - 352]
                     ; RHS
                        push qword [.__field____main__block__77____Vector2D____x] ; stored index associated with field that is being accessed
                     pop rdx ; rhs
                     pop rax ; lhs
                     push qword [rax + 8*rdx] ; lhs.rhs
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
                     ; "v.y = "
                     mov rax, .str153
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
                  ; Member Accessor
                     ; LHS
                        ; Identifier - Vector2D v
                           push qword [rbp - 352]
                     ; RHS
                        push qword [.__field____main__block__77____Vector2D____y] ; stored index associated with field that is being accessed
                     pop rdx ; rhs
                     pop rax ; lhs
                     push qword [rax + 8*rdx] ; lhs.rhs
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
         ; Function Call - println(char[]) -> void
            ; Make space for 1 arg(s)
            sub rsp, 8
            ; Arguments
               ; Eval arg0
                  ; String Literal
                     ; "v.set (42.0, 0.0043);"
                     mov rax, .str154
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
         ; Method Call - Vector2D::set(float, float) -> void
            ; Make space for 2 arg(s) and object parameter
            sub rsp, 24
            ; LHS
               ; Identifier - Vector2D v
                  push qword [rbp - 352]
               pop rax ; object parameter
               mov qword [rsp + 0], rax ; place as first parameter
            ; RHS
            ; Arguments
               ; Eval arg0
                  ; Float Literal
                     mov rax, qword [.float49] ; 42.0
                     push rax
               ; Move arg0's result to reverse order position on stack
               pop rax
               mov qword [rsp + 8], rax
               ; Eval arg1
                  ; Float Literal
                     mov rax, qword [.float50] ; 0.0043
                     push rax
               ; Move arg1's result to reverse order position on stack
               pop rax
               mov qword [rsp + 16], rax
            call .__method____main__block__77____Vector2D____set__float__float
            ; Remove args
            add rsp, 24
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
                     ; "v.x = "
                     mov rax, .str155
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
                  ; Member Accessor
                     ; LHS
                        ; Identifier - Vector2D v
                           push qword [rbp - 352]
                     ; RHS
                        push qword [.__field____main__block__77____Vector2D____x] ; stored index associated with field that is being accessed
                     pop rdx ; rhs
                     pop rax ; lhs
                     push qword [rax + 8*rdx] ; lhs.rhs
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
                     ; "v.y = "
                     mov rax, .str156
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
                  ; Member Accessor
                     ; LHS
                        ; Identifier - Vector2D v
                           push qword [rbp - 352]
                     ; RHS
                        push qword [.__field____main__block__77____Vector2D____y] ; stored index associated with field that is being accessed
                     pop rdx ; rhs
                     pop rax ; lhs
                     push qword [rax + 8*rdx] ; lhs.rhs
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
         ; Assignment - '='
            ; RHS
               ; Constructor Call - Vector2D::Vector2D(float, float) -> Vector2D
                  ; Make space for 2 arg(s)
                  sub rsp, 16
                  ; Arguments
                     ; Eval arg0
                        ; Float Literal
                           mov rax, qword [.float51] ; 0.5
                           push rax
                     ; Move arg0's result to reverse order position on stack
                     pop rax
                     mov qword [rsp + 0], rax
                     ; Eval arg1
                        ; Float Literal
                           mov rax, qword [.float52] ; 3.1415
                           push rax
                     ; Move arg1's result to reverse order position on stack
                     pop rax
                     mov qword [rsp + 8], rax
                  ; Call Vector2D::Vector2D(float, float)
                  call .__ctor____main__block__77____Vector2D____Vector2D__float__float
                  ; Remove args
                  add rsp, 16
                  ; Push return value
                  push rax
            ; LHS
               ; Variable Declaration - v2
                  mov rax, qword [rbp - 360]  ; __main__block__77__v2
            pop rdx ; rhs value
            mov qword [rbp - 360], rdx
            push rdx
         ; Statement results can be ignored
         pop rdx
         ; Function Call - print(char[]) -> void
            ; Make space for 1 arg(s)
            sub rsp, 8
            ; Arguments
               ; Eval arg0
                  ; String Literal
                     ; "v2.x = "
                     mov rax, .str157
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
                  ; Member Accessor
                     ; LHS
                        ; Identifier - Vector2D v2
                           push qword [rbp - 360]
                     ; RHS
                        push qword [.__field____main__block__77____Vector2D____x] ; stored index associated with field that is being accessed
                     pop rdx ; rhs
                     pop rax ; lhs
                     push qword [rax + 8*rdx] ; lhs.rhs
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
                     ; "v2.y = "
                     mov rax, .str158
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
                  ; Member Accessor
                     ; LHS
                        ; Identifier - Vector2D v2
                           push qword [rbp - 360]
                     ; RHS
                        push qword [.__field____main__block__77____Vector2D____y] ; stored index associated with field that is being accessed
                     pop rdx ; rhs
                     pop rax ; lhs
                     push qword [rax + 8*rdx] ; lhs.rhs
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
         ; Function Call - println(char[]) -> void
            ; Make space for 1 arg(s)
            sub rsp, 8
            ; Arguments
               ; Eval arg0
                  ; String Literal
                     ; "v2.set (v);"
                     mov rax, .str159
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
         ; Method Call - Vector2D::set(Vector2D) -> void
            ; Make space for 1 arg(s) and object parameter
            sub rsp, 16
            ; LHS
               ; Identifier - Vector2D v2
                  push qword [rbp - 360]
               pop rax ; object parameter
               mov qword [rsp + 0], rax ; place as first parameter
            ; RHS
            ; Arguments
               ; Eval arg0
                  ; Identifier - Vector2D v
                     push qword [rbp - 352]
               ; Move arg0's result to reverse order position on stack
               pop rax
               mov qword [rsp + 8], rax
            call .__method____main__block__77____Vector2D____set__Vector2D
            ; Remove args
            add rsp, 16
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
                     ; "v2.x = "
                     mov rax, .str160
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
                  ; Member Accessor
                     ; LHS
                        ; Identifier - Vector2D v2
                           push qword [rbp - 360]
                     ; RHS
                        push qword [.__field____main__block__77____Vector2D____x] ; stored index associated with field that is being accessed
                     pop rdx ; rhs
                     pop rax ; lhs
                     push qword [rax + 8*rdx] ; lhs.rhs
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
                     ; "v2.y = "
                     mov rax, .str161
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
                  ; Member Accessor
                     ; LHS
                        ; Identifier - Vector2D v2
                           push qword [rbp - 360]
                     ; RHS
                        push qword [.__field____main__block__77____Vector2D____y] ; stored index associated with field that is being accessed
                     pop rdx ; rhs
                     pop rax ; lhs
                     push qword [rax + 8*rdx] ; lhs.rhs
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
         ; Function Call - println(char[]) -> void
            ; Make space for 1 arg(s)
            sub rsp, 8
            ; Arguments
               ; Eval arg0
                  ; String Literal
                     ; "v2.add (v);"
                     mov rax, .str162
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
         ; Method Call - Vector2D::add(Vector2D) -> void
            ; Make space for 1 arg(s) and object parameter
            sub rsp, 16
            ; LHS
               ; Identifier - Vector2D v2
                  push qword [rbp - 360]
               pop rax ; object parameter
               mov qword [rsp + 0], rax ; place as first parameter
            ; RHS
            ; Arguments
               ; Eval arg0
                  ; Identifier - Vector2D v
                     push qword [rbp - 352]
               ; Move arg0's result to reverse order position on stack
               pop rax
               mov qword [rsp + 8], rax
            call .__method____main__block__77____Vector2D____add__Vector2D
            ; Remove args
            add rsp, 16
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
                     ; "v2.x = "
                     mov rax, .str163
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
                  ; Member Accessor
                     ; LHS
                        ; Identifier - Vector2D v2
                           push qword [rbp - 360]
                     ; RHS
                        push qword [.__field____main__block__77____Vector2D____x] ; stored index associated with field that is being accessed
                     pop rdx ; rhs
                     pop rax ; lhs
                     push qword [rax + 8*rdx] ; lhs.rhs
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
                     ; "v2.y = "
                     mov rax, .str164
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
                  ; Member Accessor
                     ; LHS
                        ; Identifier - Vector2D v2
                           push qword [rbp - 360]
                     ; RHS
                        push qword [.__field____main__block__77____Vector2D____y] ; stored index associated with field that is being accessed
                     pop rdx ; rhs
                     pop rax ; lhs
                     push qword [rax + 8*rdx] ; lhs.rhs
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
         ; Function Call - println(char[]) -> void
            ; Make space for 1 arg(s)
            sub rsp, 8
            ; Arguments
               ; Eval arg0
                  ; String Literal
                     ; "v2.add (v);"
                     mov rax, .str165
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
         ; Method Call - Vector2D::add(Vector2D) -> void
            ; Make space for 1 arg(s) and object parameter
            sub rsp, 16
            ; LHS
               ; Identifier - Vector2D v2
                  push qword [rbp - 360]
               pop rax ; object parameter
               mov qword [rsp + 0], rax ; place as first parameter
            ; RHS
            ; Arguments
               ; Eval arg0
                  ; Identifier - Vector2D v
                     push qword [rbp - 352]
               ; Move arg0's result to reverse order position on stack
               pop rax
               mov qword [rsp + 8], rax
            call .__method____main__block__77____Vector2D____add__Vector2D
            ; Remove args
            add rsp, 16
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
                     ; "v2.x = "
                     mov rax, .str166
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
                  ; Member Accessor
                     ; LHS
                        ; Identifier - Vector2D v2
                           push qword [rbp - 360]
                     ; RHS
                        push qword [.__field____main__block__77____Vector2D____x] ; stored index associated with field that is being accessed
                     pop rdx ; rhs
                     pop rax ; lhs
                     push qword [rax + 8*rdx] ; lhs.rhs
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
                     ; "v2.y = "
                     mov rax, .str167
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
                  ; Member Accessor
                     ; LHS
                        ; Identifier - Vector2D v2
                           push qword [rbp - 360]
                     ; RHS
                        push qword [.__field____main__block__77____Vector2D____y] ; stored index associated with field that is being accessed
                     pop rdx ; rhs
                     pop rax ; lhs
                     push qword [rax + 8*rdx] ; lhs.rhs
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
         ; Function Call - println(char[]) -> void
            ; Make space for 1 arg(s)
            sub rsp, 8
            ; Arguments
               ; Eval arg0
                  ; String Literal
                     ; "v2.add (v);"
                     mov rax, .str168
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
         ; Method Call - Vector2D::add(Vector2D) -> void
            ; Make space for 1 arg(s) and object parameter
            sub rsp, 16
            ; LHS
               ; Identifier - Vector2D v2
                  push qword [rbp - 360]
               pop rax ; object parameter
               mov qword [rsp + 0], rax ; place as first parameter
            ; RHS
            ; Arguments
               ; Eval arg0
                  ; Identifier - Vector2D v
                     push qword [rbp - 352]
               ; Move arg0's result to reverse order position on stack
               pop rax
               mov qword [rsp + 8], rax
            call .__method____main__block__77____Vector2D____add__Vector2D
            ; Remove args
            add rsp, 16
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
                     ; "v2.x = "
                     mov rax, .str169
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
                  ; Member Accessor
                     ; LHS
                        ; Identifier - Vector2D v2
                           push qword [rbp - 360]
                     ; RHS
                        push qword [.__field____main__block__77____Vector2D____x] ; stored index associated with field that is being accessed
                     pop rdx ; rhs
                     pop rax ; lhs
                     push qword [rax + 8*rdx] ; lhs.rhs
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
                     ; "v2.y = "
                     mov rax, .str170
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
                  ; Member Accessor
                     ; LHS
                        ; Identifier - Vector2D v2
                           push qword [rbp - 360]
                     ; RHS
                        push qword [.__field____main__block__77____Vector2D____y] ; stored index associated with field that is being accessed
                     pop rdx ; rhs
                     pop rax ; lhs
                     push qword [rax + 8*rdx] ; lhs.rhs
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
; ========================================================================
         ; Class Declaration - __main__block__77____Vector3D inherits __main__block__77____Vector2D
            ; Class data
            section .data
               ; Dispatch Table - this might need to be a malloc**
               .__dtable____main__block__77____Vector3D:
               ; Dispatch Table Entries
               dq .__method____main__block__77____Vector2D____set__float__float ; 0
               dq .__method____main__block__77____Vector2D____set__Vector2D ; 1
               dq .__method____main__block__77____Vector2D____add__Vector2D ; 2
               dq .__method____main__block__77____Vector3D____set__Vector3D ; 3
               dq .__method____main__block__77____Vector3D____set__float__float__float ; 4
            section .text
   ;---------------------------------------------------------------------
            ; Field - float Vector3D::x
            ; Inherited from Vector2D
            section .data
            .__field____main__block__77____Vector3D____x: dq 1
            section .text
   ;---------------------------------------------------------------------
   ;---------------------------------------------------------------------
            ; Field - float Vector3D::y
            ; Inherited from Vector2D
            section .data
            .__field____main__block__77____Vector3D____y: dq 2
            section .text
   ;---------------------------------------------------------------------
   ;---------------------------------------------------------------------
            ; Field - float Vector3D::z
            section .data
            .__field____main__block__77____Vector3D____z: dq 3
            section .text
   ;---------------------------------------------------------------------
         ; skip over class methods
         jmp .__endclass____main__block__77____Vector3D
   ;---------------------------------------------------------------------
            ; Constructor Declaration - Vector3D::Vector3D(float, float, float) -> Vector3D
            jmp .__end__ctor____main__block__77____Vector3D____Vector3D__float__float__float
            .__ctor____main__block__77____Vector3D____Vector3D__float__float__float:
            ; Function Header:
               ; Setup stack frame
                  push rbp
                  mov rbp, rsp
                  ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
                     sub rsp, 16 ; space for local variables (16-byte aligned)
                     ; [rbp - 8] - this - Reference to 'this' object instance
               ; Creating Class Instance
                  mov rdi, 32 ; [dtable, field0, field1, ..., fieldN] each 8 bytes
                  call malloc
                  mov qword [rbp - 8], rax ; save class instance as 'this'
                  ; Add Dispatch Table
                  mov rax, qword [rbp - 8] ; this
                  mov qword [rax + 0], .__dtable____main__block__77____Vector3D ; this[0] = &dtable
               ; Parameters
                  ; Param: x [rbp + 16]
                  ; Param: y [rbp + 24]
                  ; Param: z [rbp + 32]
            ; Body
      ;------------------------------------------------------------------
               ; Code Block
                  ; Assignment - '='
                     ; RHS
                        ; Identifier - float x
                           push qword [rbp - -16]
                     ; LHS
                        ; Member Accessor Assignment
                           ; LHS
                              ; This keyword
                                 push qword [rbp - 8] ; __this
                           ; RHS
                              push qword [.__field____main__block__77____Vector3D____x] ; 
                           pop rdi ; rhs
                           pop rbx ; lhs
                     pop rdx ; rhs value
                     mov qword [rbx + 8*rdi], rdx
                     push rdx
                  ; Statement results can be ignored
                  pop rdx
                  ; Assignment - '='
                     ; RHS
                        ; Identifier - float y
                           push qword [rbp - -24]
                     ; LHS
                        ; Member Accessor Assignment
                           ; LHS
                              ; This keyword
                                 push qword [rbp - 8] ; __this
                           ; RHS
                              push qword [.__field____main__block__77____Vector3D____y] ; 
                           pop rdi ; rhs
                           pop rbx ; lhs
                     pop rdx ; rhs value
                     mov qword [rbx + 8*rdi], rdx
                     push rdx
                  ; Statement results can be ignored
                  pop rdx
                  ; Assignment - '='
                     ; RHS
                        ; Identifier - float z
                           push qword [rbp - -32]
                     ; LHS
                        ; Member Accessor Assignment
                           ; LHS
                              ; This keyword
                                 push qword [rbp - 8] ; __this
                           ; RHS
                              push qword [.__field____main__block__77____Vector3D____z] ; 
                           pop rdi ; rhs
                           pop rbx ; lhs
                     pop rdx ; rhs value
                     mov qword [rbx + 8*rdi], rdx
                     push rdx
                  ; Statement results can be ignored
                  pop rdx
      ;------------------------------------------------------------------
            mov rax, qword [rbp - 8] ; __this
            ; Function Epilogue
            mov rsp, rbp ; remove local vars + unpopped pushes
            pop rbp
            ret
         .__end__ctor____main__block__77____Vector3D____Vector3D__float__float__float:
         ; End Constructor Declaration - __ctor____main__block__77____Vector3D____Vector3D__float__float__float
;------------------------------------------------------------------------

;------------------------------------------------------------------------
         ; Method Declaration - Vector3D::set(float, float) -> void
         ; Inherited from Vector2D
         jmp .__end__method____main__block__77____Vector3D____set__float__float
         .__method____main__block__77____Vector3D____set__float__float:
            ; Jump to Vector2D's version
            jmp .__method____main__block__77____Vector2D____set__float__float
         .__end__method____main__block__77____Vector3D____set__float__float:
         ; End Method Declaration - .__method____main__block__77____Vector3D____set__float__float
;------------------------------------------------------------------------

;------------------------------------------------------------------------
         ; Method Declaration - Vector3D::set(Vector2D) -> void
         ; Inherited from Vector2D
         jmp .__end__method____main__block__77____Vector3D____set__Vector2D
         .__method____main__block__77____Vector3D____set__Vector2D:
            ; Jump to Vector2D's version
            jmp .__method____main__block__77____Vector2D____set__Vector2D
         .__end__method____main__block__77____Vector3D____set__Vector2D:
         ; End Method Declaration - .__method____main__block__77____Vector3D____set__Vector2D
;------------------------------------------------------------------------

;------------------------------------------------------------------------
         ; Method Declaration - Vector3D::add(Vector2D) -> void
         ; Inherited from Vector2D
         jmp .__end__method____main__block__77____Vector3D____add__Vector2D
         .__method____main__block__77____Vector3D____add__Vector2D:
            ; Jump to Vector2D's version
            jmp .__method____main__block__77____Vector2D____add__Vector2D
         .__end__method____main__block__77____Vector3D____add__Vector2D:
         ; End Method Declaration - .__method____main__block__77____Vector3D____add__Vector2D
;------------------------------------------------------------------------

;------------------------------------------------------------------------
         ; Method Declaration - Vector3D::set(Vector3D) -> void
         jmp .__end__method____main__block__77____Vector3D____set__Vector3D
         .__method____main__block__77____Vector3D____set__Vector3D:
            ; Function Header:
            ; Setup stack frame
               push rbp
               mov rbp, rsp
               ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
                  sub rsp, 16 ; space for local variables (16-byte aligned)
                  ; [rbp - 8] - this - Reference to 'this' object instance
                  mov rdx, qword [rbp + 16] ; param passed 'this'
                  mov qword [rbp - 8], rdx ; save this to a local
                  ; [rbp - 16] - Vector2D other2d (<unset-scope-name>)
            ; Parameters
               ; Param: other [rbp + 24] (__main__block__77____Vector3D__set__other)
            ; Body
      ;------------------------------------------------------------------
               ; Code Block
                  ; Assignment - '='
                     ; RHS
                        ; Constructor Call - Vector2D::Vector2D(float, float) -> Vector2D
                           ; Make space for 2 arg(s)
                           sub rsp, 16
                           ; Arguments
                              ; Eval arg0
                                 ; Member Accessor
                                    ; LHS
                                       ; Identifier - Vector3D other
                                          push qword [rbp - -24]
                                    ; RHS
                                       push qword [.__field____main__block__77____Vector3D____x] ; stored index associated with field that is being accessed
                                    pop rdx ; rhs
                                    pop rax ; lhs
                                    push qword [rax + 8*rdx] ; lhs.rhs
                              ; Move arg0's result to reverse order position on stack
                              pop rax
                              mov qword [rsp + 0], rax
                              ; Eval arg1
                                 ; Member Accessor
                                    ; LHS
                                       ; Identifier - Vector3D other
                                          push qword [rbp - -24]
                                    ; RHS
                                       push qword [.__field____main__block__77____Vector3D____y] ; stored index associated with field that is being accessed
                                    pop rdx ; rhs
                                    pop rax ; lhs
                                    push qword [rax + 8*rdx] ; lhs.rhs
                              ; Move arg1's result to reverse order position on stack
                              pop rax
                              mov qword [rsp + 8], rax
                           ; Call Vector2D::Vector2D(float, float)
                           call .__ctor____main__block__77____Vector2D____Vector2D__float__float
                           ; Remove args
                           add rsp, 16
                           ; Push return value
                           push rax
                     ; LHS
                        ; Variable Declaration - other2d
                           mov rax, qword [rbp - 16]  ; __main__block__77____Vector3D__set__block__83__other2d
                     pop rdx ; rhs value
                     mov qword [rbp - 16], rdx
                     push rdx
                  ; Statement results can be ignored
                  pop rdx
                  ; Method Call - Vector3D::set(Vector2D) -> void
                     ; Make space for 1 arg(s) and object parameter
                     sub rsp, 16
                     ; LHS
                        ; This keyword
                           push qword [rbp - 8] ; __this
                        pop rax ; object parameter
                        mov qword [rsp + 0], rax ; place as first parameter
                     ; RHS
                     ; Arguments
                        ; Eval arg0
                           ; Identifier - Vector2D other2d
                              push qword [rbp - 16]
                        ; Move arg0's result to reverse order position on stack
                        pop rax
                        mov qword [rsp + 8], rax
                     call .__method____main__block__77____Vector3D____set__Vector2D
                     ; Remove args
                     add rsp, 16
                     ; Push return value
                     push rax
                  ; Statement results can be ignored
                  pop rdx
                  ; Free Operator
                     ; RHS
                        ; Identifier - Vector2D other2d
                           push qword [rbp - 16]
                     ; Free pointer
                     pop rdi   ; pointer
                     call free ; free the pointer
                     push rax  ; undefined return value
                  ; Statement results can be ignored
                  pop rdx
                  ; Assignment - '='
                     ; RHS
                        ; Member Accessor
                           ; LHS
                              ; Identifier - Vector3D other
                                 push qword [rbp - -24]
                           ; RHS
                              push qword [.__field____main__block__77____Vector3D____z] ; stored index associated with field that is being accessed
                           pop rdx ; rhs
                           pop rax ; lhs
                           push qword [rax + 8*rdx] ; lhs.rhs
                     ; LHS
                        ; Member Accessor Assignment
                           ; LHS
                              ; This keyword
                                 push qword [rbp - 8] ; __this
                           ; RHS
                              push qword [.__field____main__block__77____Vector3D____z] ; 
                           pop rdi ; rhs
                           pop rbx ; lhs
                     pop rdx ; rhs value
                     mov qword [rbx + 8*rdi], rdx
                     push rdx
                  ; Statement results can be ignored
                  pop rdx
      ;------------------------------------------------------------------
            ; Function Epilogue
            mov rsp, rbp ; remove local vars + unpopped pushes
            pop rbp
            ret
         .__end__method____main__block__77____Vector3D____set__Vector3D:
         ; End Method Declaration - .__method____main__block__77____Vector3D____set__Vector3D
;------------------------------------------------------------------------

;------------------------------------------------------------------------
         ; Method Declaration - Vector3D::set(float, float, float) -> void
         jmp .__end__method____main__block__77____Vector3D____set__float__float__float
         .__method____main__block__77____Vector3D____set__float__float__float:
            ; Function Header:
            ; Setup stack frame
               push rbp
               mov rbp, rsp
               ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
                  sub rsp, 16 ; space for local variables (16-byte aligned)
                  ; [rbp - 8] - this - Reference to 'this' object instance
                  mov rdx, qword [rbp + 16] ; param passed 'this'
                  mov qword [rbp - 8], rdx ; save this to a local
            ; Parameters
               ; Param: x [rbp + 24] (__main__block__77____Vector3D__set__x)
               ; Param: y [rbp + 32] (__main__block__77____Vector3D__set__y)
               ; Param: z [rbp + 40] (__main__block__77____Vector3D__set__z)
            ; Body
      ;------------------------------------------------------------------
               ; Code Block
                  ; Assignment - '='
                     ; RHS
                        ; Identifier - float x
                           push qword [rbp - -24]
                     ; LHS
                        ; Member Accessor Assignment
                           ; LHS
                              ; This keyword
                                 push qword [rbp - 8] ; __this
                           ; RHS
                              push qword [.__field____main__block__77____Vector3D____x] ; 
                           pop rdi ; rhs
                           pop rbx ; lhs
                     pop rdx ; rhs value
                     mov qword [rbx + 8*rdi], rdx
                     push rdx
                  ; Statement results can be ignored
                  pop rdx
                  ; Assignment - '='
                     ; RHS
                        ; Identifier - float y
                           push qword [rbp - -32]
                     ; LHS
                        ; Member Accessor Assignment
                           ; LHS
                              ; This keyword
                                 push qword [rbp - 8] ; __this
                           ; RHS
                              push qword [.__field____main__block__77____Vector3D____y] ; 
                           pop rdi ; rhs
                           pop rbx ; lhs
                     pop rdx ; rhs value
                     mov qword [rbx + 8*rdi], rdx
                     push rdx
                  ; Statement results can be ignored
                  pop rdx
                  ; Assignment - '='
                     ; RHS
                        ; Identifier - float z
                           push qword [rbp - -40]
                     ; LHS
                        ; Member Accessor Assignment
                           ; LHS
                              ; This keyword
                                 push qword [rbp - 8] ; __this
                           ; RHS
                              push qword [.__field____main__block__77____Vector3D____z] ; 
                           pop rdi ; rhs
                           pop rbx ; lhs
                     pop rdx ; rhs value
                     mov qword [rbx + 8*rdi], rdx
                     push rdx
                  ; Statement results can be ignored
                  pop rdx
      ;------------------------------------------------------------------
            ; Function Epilogue
            mov rsp, rbp ; remove local vars + unpopped pushes
            pop rbp
            ret
         .__end__method____main__block__77____Vector3D____set__float__float__float:
         ; End Method Declaration - .__method____main__block__77____Vector3D____set__float__float__float
;------------------------------------------------------------------------

.__endclass____main__block__77____Vector3D:
         ; End Class Declaration - __main__block__77____Vector3D
; ===========================================================================

; ===========================================================================
         ; Function Declaration - print(Vector3D) -> void
         ; Skip over function declaration
         jmp .__end____main__block__77____print__Vector3D
.__main__block__77____print__Vector3D:
         ; Function Header:
            ; Setup stack frame
               push rbp
               mov rbp, rsp
               sub rsp, 0
            ; Parameters
               ; Param: v [rbp + 16]
            ; Local Variables - Each variable is currently 64-bit (sorry not sorry)

         ; Body
   ;---------------------------------------------------------------------
            ; Code Block
               ; Function Call - print(char) -> void
                  ; Make space for 1 arg(s)
                  sub rsp, 8
                  ; Arguments
                     ; Eval arg0
                        ; Char Literal
                           push '('
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
               ; Function Call - print(float) -> void
                  ; Make space for 1 arg(s)
                  sub rsp, 8
                  ; Arguments
                     ; Eval arg0
                        ; Member Accessor
                           ; LHS
                              ; Identifier - Vector3D v
                                 push qword [rbp - -16]
                           ; RHS
                              push qword [.__field____main__block__77____Vector3D____x] ; stored index associated with field that is being accessed
                           pop rdx ; rhs
                           pop rax ; lhs
                           push qword [rax + 8*rdx] ; lhs.rhs
                     ; Move arg0's result to reverse order position on stack
                     pop rax
                     mov qword [rsp + 0], rax
                  ; Call print(float)
                  call print__float
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
                           ; ", "
                           mov rax, .str171
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
               ; Function Call - print(float) -> void
                  ; Make space for 1 arg(s)
                  sub rsp, 8
                  ; Arguments
                     ; Eval arg0
                        ; Member Accessor
                           ; LHS
                              ; Identifier - Vector3D v
                                 push qword [rbp - -16]
                           ; RHS
                              push qword [.__field____main__block__77____Vector3D____y] ; stored index associated with field that is being accessed
                           pop rdx ; rhs
                           pop rax ; lhs
                           push qword [rax + 8*rdx] ; lhs.rhs
                     ; Move arg0's result to reverse order position on stack
                     pop rax
                     mov qword [rsp + 0], rax
                  ; Call print(float)
                  call print__float
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
                           ; ", "
                           mov rax, .str172
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
               ; Function Call - print(float) -> void
                  ; Make space for 1 arg(s)
                  sub rsp, 8
                  ; Arguments
                     ; Eval arg0
                        ; Member Accessor
                           ; LHS
                              ; Identifier - Vector3D v
                                 push qword [rbp - -16]
                           ; RHS
                              push qword [.__field____main__block__77____Vector3D____z] ; stored index associated with field that is being accessed
                           pop rdx ; rhs
                           pop rax ; lhs
                           push qword [rax + 8*rdx] ; lhs.rhs
                     ; Move arg0's result to reverse order position on stack
                     pop rax
                     mov qword [rsp + 0], rax
                  ; Call print(float)
                  call print__float
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
                           push ')'
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
   ;---------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
.__end____main__block__77____print__Vector3D:
         ; End Function Declaration - print(Vector3D) -> void
; ===========================================================================

; ===========================================================================
         ; Function Declaration - println(Vector3D) -> void
         ; Skip over function declaration
         jmp .__end____main__block__77____println__Vector3D
.__main__block__77____println__Vector3D:
         ; Function Header:
            ; Setup stack frame
               push rbp
               mov rbp, rsp
               sub rsp, 0
            ; Parameters
               ; Param: v [rbp + 16]
            ; Local Variables - Each variable is currently 64-bit (sorry not sorry)

         ; Body
   ;---------------------------------------------------------------------
            ; Code Block
               ; Function Call - print(char) -> void
                  ; Make space for 1 arg(s)
                  sub rsp, 8
                  ; Arguments
                     ; Eval arg0
                        ; Char Literal
                           push '('
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
               ; Function Call - print(float) -> void
                  ; Make space for 1 arg(s)
                  sub rsp, 8
                  ; Arguments
                     ; Eval arg0
                        ; Member Accessor
                           ; LHS
                              ; Identifier - Vector3D v
                                 push qword [rbp - -16]
                           ; RHS
                              push qword [.__field____main__block__77____Vector3D____x] ; stored index associated with field that is being accessed
                           pop rdx ; rhs
                           pop rax ; lhs
                           push qword [rax + 8*rdx] ; lhs.rhs
                     ; Move arg0's result to reverse order position on stack
                     pop rax
                     mov qword [rsp + 0], rax
                  ; Call print(float)
                  call print__float
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
                           ; ", "
                           mov rax, .str173
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
               ; Function Call - print(float) -> void
                  ; Make space for 1 arg(s)
                  sub rsp, 8
                  ; Arguments
                     ; Eval arg0
                        ; Member Accessor
                           ; LHS
                              ; Identifier - Vector3D v
                                 push qword [rbp - -16]
                           ; RHS
                              push qword [.__field____main__block__77____Vector3D____y] ; stored index associated with field that is being accessed
                           pop rdx ; rhs
                           pop rax ; lhs
                           push qword [rax + 8*rdx] ; lhs.rhs
                     ; Move arg0's result to reverse order position on stack
                     pop rax
                     mov qword [rsp + 0], rax
                  ; Call print(float)
                  call print__float
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
                           ; ", "
                           mov rax, .str174
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
               ; Function Call - print(float) -> void
                  ; Make space for 1 arg(s)
                  sub rsp, 8
                  ; Arguments
                     ; Eval arg0
                        ; Member Accessor
                           ; LHS
                              ; Identifier - Vector3D v
                                 push qword [rbp - -16]
                           ; RHS
                              push qword [.__field____main__block__77____Vector3D____z] ; stored index associated with field that is being accessed
                           pop rdx ; rhs
                           pop rax ; lhs
                           push qword [rax + 8*rdx] ; lhs.rhs
                     ; Move arg0's result to reverse order position on stack
                     pop rax
                     mov qword [rsp + 0], rax
                  ; Call print(float)
                  call print__float
                  ; Remove args
                  add rsp, 8
                  ; Push return value
                  push rax
               ; Statement results can be ignored
               pop rdx
               ; Function Call - println(char) -> void
                  ; Make space for 1 arg(s)
                  sub rsp, 8
                  ; Arguments
                     ; Eval arg0
                        ; Char Literal
                           push ')'
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
   ;---------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
.__end____main__block__77____println__Vector3D:
         ; End Function Declaration - println(Vector3D) -> void
; ===========================================================================

         ; Function Call - println(char[]) -> void
         ; Make space for 1 arg(s)
         sub rsp, 8
         ; Arguments
            ; Eval arg0
               ; String Literal
                  ; "Vector3D v3 = new Vector3D (1.0, 2.0, 3.0);"
                  mov rax, .str175
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
         ; Assignment - '='
         ; RHS
            ; Constructor Call - Vector3D::Vector3D(float, float, float) -> Vector3D
               ; Make space for 3 arg(s)
               sub rsp, 24
               ; Arguments
                  ; Eval arg0
                     ; Float Literal
                        mov rax, qword [.float53] ; 1.0
                        push rax
                  ; Move arg0's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 0], rax
                  ; Eval arg1
                     ; Float Literal
                        mov rax, qword [.float54] ; 2.0
                        push rax
                  ; Move arg1's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 8], rax
                  ; Eval arg2
                     ; Float Literal
                        mov rax, qword [.float55] ; 3.0
                        push rax
                  ; Move arg2's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 16], rax
               ; Call Vector3D::Vector3D(float, float, float)
               call .__ctor____main__block__77____Vector3D____Vector3D__float__float__float
               ; Remove args
               add rsp, 24
               ; Push return value
               push rax
         ; LHS
            ; Variable Declaration - v3
               mov rax, qword [rbp - 368]  ; __main__block__77__v3
         pop rdx ; rhs value
         mov qword [rbp - 368], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
         ; Function Call - println(Vector3D) -> void
         ; Make space for 1 arg(s)
         sub rsp, 8
         ; Arguments
            ; Eval arg0
               ; Identifier - Vector3D v3
                  push qword [rbp - 368]
            ; Move arg0's result to reverse order position on stack
            pop rax
            mov qword [rsp + 0], rax
         ; Call println(Vector3D)
         call .__main__block__77____println__Vector3D
         ; Remove args
         add rsp, 8
         ; Push return value
         push rax
         ; Statement results can be ignored
         pop rdx
         ; Function Call - println(char[]) -> void
         ; Make space for 1 arg(s)
         sub rsp, 8
         ; Arguments
            ; Eval arg0
               ; String Literal
                  ; "Vector3D v4 = new Vector3D (5.5, 6.25, 7.75);"
                  mov rax, .str176
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
         ; Assignment - '='
         ; RHS
            ; Constructor Call - Vector3D::Vector3D(float, float, float) -> Vector3D
               ; Make space for 3 arg(s)
               sub rsp, 24
               ; Arguments
                  ; Eval arg0
                     ; Float Literal
                        mov rax, qword [.float56] ; 5.5
                        push rax
                  ; Move arg0's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 0], rax
                  ; Eval arg1
                     ; Float Literal
                        mov rax, qword [.float57] ; 6.25
                        push rax
                  ; Move arg1's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 8], rax
                  ; Eval arg2
                     ; Float Literal
                        mov rax, qword [.float58] ; 7.75
                        push rax
                  ; Move arg2's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 16], rax
               ; Call Vector3D::Vector3D(float, float, float)
               call .__ctor____main__block__77____Vector3D____Vector3D__float__float__float
               ; Remove args
               add rsp, 24
               ; Push return value
               push rax
         ; LHS
            ; Variable Declaration - v4
               mov rax, qword [rbp - 376]  ; __main__block__77__v4
         pop rdx ; rhs value
         mov qword [rbp - 376], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
         ; Function Call - println(Vector3D) -> void
         ; Make space for 1 arg(s)
         sub rsp, 8
         ; Arguments
            ; Eval arg0
               ; Identifier - Vector3D v4
                  push qword [rbp - 376]
            ; Move arg0's result to reverse order position on stack
            pop rax
            mov qword [rsp + 0], rax
         ; Call println(Vector3D)
         call .__main__block__77____println__Vector3D
         ; Remove args
         add rsp, 8
         ; Push return value
         push rax
         ; Statement results can be ignored
         pop rdx
         ; Function Call - println(char[]) -> void
         ; Make space for 1 arg(s)
         sub rsp, 8
         ; Arguments
            ; Eval arg0
               ; String Literal
                  ; "v3.set (v2); // inherited from Vector2D"
                  mov rax, .str177
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
         ; Method Call - Vector3D::set(Vector2D) -> void
         ; Make space for 1 arg(s) and object parameter
         sub rsp, 16
         ; LHS
            ; Identifier - Vector3D v3
               push qword [rbp - 368]
            pop rax ; object parameter
            mov qword [rsp + 0], rax ; place as first parameter
         ; RHS
         ; Arguments
            ; Eval arg0
               ; Identifier - Vector2D v2
                  push qword [rbp - 360]
            ; Move arg0's result to reverse order position on stack
            pop rax
            mov qword [rsp + 8], rax
         call .__method____main__block__77____Vector3D____set__Vector2D
         ; Remove args
         add rsp, 16
         ; Push return value
         push rax
         ; Statement results can be ignored
         pop rdx
         ; Function Call - println(Vector3D) -> void
         ; Make space for 1 arg(s)
         sub rsp, 8
         ; Arguments
            ; Eval arg0
               ; Identifier - Vector3D v3
                  push qword [rbp - 368]
            ; Move arg0's result to reverse order position on stack
            pop rax
            mov qword [rsp + 0], rax
         ; Call println(Vector3D)
         call .__main__block__77____println__Vector3D
         ; Remove args
         add rsp, 8
         ; Push return value
         push rax
         ; Statement results can be ignored
         pop rdx
         ; Function Call - println(char[]) -> void
         ; Make space for 1 arg(s)
         sub rsp, 8
         ; Arguments
            ; Eval arg0
               ; String Literal
                  ; "v3.set (0.0, 0.0, 0.0);"
                  mov rax, .str178
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
         ; Method Call - Vector3D::set(float, float, float) -> void
         ; Make space for 3 arg(s) and object parameter
         sub rsp, 32
         ; LHS
            ; Identifier - Vector3D v3
               push qword [rbp - 368]
            pop rax ; object parameter
            mov qword [rsp + 0], rax ; place as first parameter
         ; RHS
         ; Arguments
            ; Eval arg0
               ; Float Literal
                  mov rax, qword [.float59] ; 0.0
                  push rax
            ; Move arg0's result to reverse order position on stack
            pop rax
            mov qword [rsp + 8], rax
            ; Eval arg1
               ; Float Literal
                  mov rax, qword [.float60] ; 0.0
                  push rax
            ; Move arg1's result to reverse order position on stack
            pop rax
            mov qword [rsp + 16], rax
            ; Eval arg2
               ; Float Literal
                  mov rax, qword [.float61] ; 0.0
                  push rax
            ; Move arg2's result to reverse order position on stack
            pop rax
            mov qword [rsp + 24], rax
         call .__method____main__block__77____Vector3D____set__float__float__float
         ; Remove args
         add rsp, 32
         ; Push return value
         push rax
         ; Statement results can be ignored
         pop rdx
         ; Function Call - println(char[]) -> void
         ; Make space for 1 arg(s)
         sub rsp, 8
         ; Arguments
            ; Eval arg0
               ; String Literal
                  ; "v3.set (v4);"
                  mov rax, .str179
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
         ; Method Call - Vector3D::set(Vector3D) -> void
         ; Make space for 1 arg(s) and object parameter
         sub rsp, 16
         ; LHS
            ; Identifier - Vector3D v3
               push qword [rbp - 368]
            pop rax ; object parameter
            mov qword [rsp + 0], rax ; place as first parameter
         ; RHS
         ; Arguments
            ; Eval arg0
               ; Identifier - Vector3D v4
                  push qword [rbp - 376]
            ; Move arg0's result to reverse order position on stack
            pop rax
            mov qword [rsp + 8], rax
         call .__method____main__block__77____Vector3D____set__Vector3D
         ; Remove args
         add rsp, 16
         ; Push return value
         push rax
         ; Statement results can be ignored
         pop rdx
         ; Function Call - println(Vector3D) -> void
         ; Make space for 1 arg(s)
         sub rsp, 8
         ; Arguments
            ; Eval arg0
               ; Identifier - Vector3D v3
                  push qword [rbp - 368]
            ; Move arg0's result to reverse order position on stack
            pop rax
            mov qword [rsp + 0], rax
         ; Call println(Vector3D)
         call .__main__block__77____println__Vector3D
         ; Remove args
         add rsp, 8
         ; Push return value
         push rax
         ; Statement results can be ignored
         pop rdx
;------------------------------------------------------------------------------
         ; Function Call - println(char[]) -> void
         ; Make space for 1 arg(s)
         sub rsp, 8
         ; Arguments
         ; Eval arg0
            ; String Literal
               ; "=== Testing ArrayList ==="
               mov rax, .str180
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
;------------------------------------------------------------------------------
         ; Code Block
; ===========================================================================
         ; Class Declaration - __main__block__87____Printable inherits __main__Object
         ; Class data
         section .data
            ; Dispatch Table - this might need to be a malloc**
            .__dtable____main__block__87____Printable:
            ; Dispatch Table Entries
            dq .__method____main__block__87____Printable____toString ; 0
         section .text
         ; skip over class methods
         jmp .__endclass____main__block__87____Printable
;------------------------------------------------------------------------
         ; Constructor Declaration - Printable::Printable() -> Printable
         jmp .__end__ctor____main__block__87____Printable____Printable
         .__ctor____main__block__87____Printable____Printable:
         ; Function Header:
            ; Setup stack frame
               push rbp
               mov rbp, rsp
               ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
                  sub rsp, 16 ; space for local variables (16-byte aligned)
                  ; [rbp - 8] - this - Reference to 'this' object instance
            ; Creating Class Instance
               mov rdi, 8 ; [dtable, field0, field1, ..., fieldN] each 8 bytes
               call malloc
               mov qword [rbp - 8], rax ; save class instance as 'this'
               ; Add Dispatch Table
               mov rax, qword [rbp - 8] ; this
               mov qword [rax + 0], .__dtable____main__block__87____Printable ; this[0] = &dtable
            ; Parameters
         ; Body
   ;---------------------------------------------------------------------
            ; Code Block
   ;---------------------------------------------------------------------
         mov rax, qword [rbp - 8] ; __this
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
         .__end__ctor____main__block__87____Printable____Printable:
         ; End Constructor Declaration - __ctor____main__block__87____Printable____Printable
;---------------------------------------------------------------------------

;---------------------------------------------------------------------------
         ; Method Declaration - Printable::toString() -> char[]
         jmp .__end__method____main__block__87____Printable____toString
         .__method____main__block__87____Printable____toString:
         ; Function Header:
         ; Setup stack frame
            push rbp
            mov rbp, rsp
            ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
               sub rsp, 16 ; space for local variables (16-byte aligned)
               ; [rbp - 8] - this - Reference to 'this' object instance
               mov rdx, qword [rbp + 16] ; param passed 'this'
               mov qword [rbp - 8], rdx ; save this to a local
         ; Parameters
         ; Body
   ;---------------------------------------------------------------------
            ; Code Block
               ; Return
                  ; String Literal
                     ; "<Object>"
                     mov rax, .str181
                     push rax
                  pop rax
                  ; Clean up stack and return
                  mov rsp, rbp ; remove local vars + unpopped pushes
                  pop rbp
                  ret
   ;---------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
         .__end__method____main__block__87____Printable____toString:
         ; End Method Declaration - .__method____main__block__87____Printable____toString
;---------------------------------------------------------------------------

.__endclass____main__block__87____Printable:
         ; End Class Declaration - __main__block__87____Printable
; ==============================================================================

; ==============================================================================
         ; Function Declaration - string(Printable) -> char[]
         ; Skip over function declaration
         jmp .__end____main__block__87____string__Printable
.__main__block__87____string__Printable:
         ; Function Header:
         ; Setup stack frame
            push rbp
            mov rbp, rsp
            sub rsp, 0
         ; Parameters
            ; Param: p [rbp + 16]
         ; Local Variables - Each variable is currently 64-bit (sorry not sorry)

         ; Body
;------------------------------------------------------------------------
         ; Code Block
            ; Return
               ; Virtual Method Call - toString() -> char[]
                  ; Make space for 0 arg(s) and object parameter
                  sub rsp, 8
                  ; LHS
                     ; Identifier - Printable p
                        push qword [rbp - -16]
                     pop rax ; object parameter
                     mov qword [rsp + 0], rax ; place as first parameter
                  ; RHS
                  ; Arguments
                  ; Virtual Function Dispatch
                  mov rdx, qword [rsp + 0] ;  rdx = object
                  mov rdi, qword [rdx + 0] ;  rdi = object[0] ; dtable
                  call qword [rdi + 0] ; dtable[0] ; __method____main__block__87____Printable____toString
                  ; Remove args
                  add rsp, 8
                  ; Push return value
                  push rax
               pop rax
               ; Clean up stack and return
               mov rsp, rbp ; remove local vars + unpopped pushes
               pop rbp
               ret
;------------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
.__end____main__block__87____string__Printable:
         ; End Function Declaration - string(Printable) -> char[]
; ==============================================================================

; ==============================================================================
         ; Class Template - 
         ; Instances:
; ========================================================================
         ; Class Declaration - __main__block__87____Vector__int inherits __main__block__87____Printable
            ; Class data
            section .data
               ; Dispatch Table - this might need to be a malloc**
               .__dtable____main__block__87____Vector__int:
               ; Dispatch Table Entries
               dq .__method____main__block__87____Vector__int____toString ; 0
               dq .__method____main__block__87____Vector__int____pushBack__int ; 1
               dq .__method____main__block__87____Vector__int____popBack ; 2
               dq .__method____main__block__87____Vector__int____get__int ; 3
            section .text
   ;---------------------------------------------------------------------
            ; Field - int[] Vector<:int:>::data
            section .data
            .__field____main__block__87____Vector__int____data: dq 1
            section .text
   ;---------------------------------------------------------------------
   ;---------------------------------------------------------------------
            ; Field - int Vector<:int:>::size
            section .data
            .__field____main__block__87____Vector__int____size: dq 2
            section .text
   ;---------------------------------------------------------------------
   ;---------------------------------------------------------------------
            ; Field - int Vector<:int:>::capacity
            section .data
            .__field____main__block__87____Vector__int____capacity: dq 3
            section .text
   ;---------------------------------------------------------------------
         ; skip over class methods
         jmp .__endclass____main__block__87____Vector__int
   ;---------------------------------------------------------------------
            ; Constructor Declaration - Vector<:int:>::Vector() -> Vector<:int:>
            jmp .__end__ctor____main__block__87____Vector__int____Vector
            .__ctor____main__block__87____Vector__int____Vector:
            ; Function Header:
               ; Setup stack frame
                  push rbp
                  mov rbp, rsp
                  ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
                     sub rsp, 16 ; space for local variables (16-byte aligned)
                     ; [rbp - 8] - this - Reference to 'this' object instance
               ; Creating Class Instance
                  mov rdi, 32 ; [dtable, field0, field1, ..., fieldN] each 8 bytes
                  call malloc
                  mov qword [rbp - 8], rax ; save class instance as 'this'
                  ; Add Dispatch Table
                  mov rax, qword [rbp - 8] ; this
                  mov qword [rax + 0], .__dtable____main__block__87____Vector__int ; this[0] = &dtable
               ; Parameters
            ; Body
      ;------------------------------------------------------------------
               ; Code Block
                  ; Assignment - '='
                     ; RHS
                        ; Int Literal
                           mov rax, 10
                           push rax
                     ; LHS
                        ; Member Accessor Assignment
                           ; LHS
                              ; This keyword
                                 push qword [rbp - 8] ; __this
                           ; RHS
                              push qword [.__field____main__block__87____Vector__int____capacity] ; 
                           pop rdi ; rhs
                           pop rbx ; lhs
                     pop rdx ; rhs value
                     mov qword [rbx + 8*rdi], rdx
                     push rdx
                  ; Statement results can be ignored
                  pop rdx
                  ; Assignment - '='
                     ; RHS
                        ; Array Allocator
                           ; Member Accessor
                              ; LHS
                                 ; This keyword
                                    push qword [rbp - 8] ; __this
                              ; RHS
                                 push qword [.__field____main__block__87____Vector__int____capacity] ; stored index associated with field that is being accessed
                              pop rdx ; rhs
                              pop rax ; lhs
                              push qword [rax + 8*rdx] ; lhs.rhs
                           pop rdx ; num elements for dimension[0]
                           imul rdx, 8 ; 8 bytes per element
                           mov rdi, rdx ; num bytes to allocate
                           call malloc ; allocates edi bytes on heap and stores pointer in rax
                           push rax ; __ptr
                     ; LHS
                        ; Member Accessor Assignment
                           ; LHS
                              ; This keyword
                                 push qword [rbp - 8] ; __this
                           ; RHS
                              push qword [.__field____main__block__87____Vector__int____data] ; 
                           pop rdi ; rhs
                           pop rbx ; lhs
                     pop rdx ; rhs value
                     mov qword [rbx + 8*rdi], rdx
                     push rdx
                  ; Statement results can be ignored
                  pop rdx
                  ; Assignment - '='
                     ; RHS
                        ; Int Literal
                           mov rax, 0
                           push rax
                     ; LHS
                        ; Member Accessor Assignment
                           ; LHS
                              ; This keyword
                                 push qword [rbp - 8] ; __this
                           ; RHS
                              push qword [.__field____main__block__87____Vector__int____size] ; 
                           pop rdi ; rhs
                           pop rbx ; lhs
                     pop rdx ; rhs value
                     mov qword [rbx + 8*rdi], rdx
                     push rdx
                  ; Statement results can be ignored
                  pop rdx
      ;------------------------------------------------------------------
            mov rax, qword [rbp - 8] ; __this
            ; Function Epilogue
            mov rsp, rbp ; remove local vars + unpopped pushes
            pop rbp
            ret
         .__end__ctor____main__block__87____Vector__int____Vector:
         ; End Constructor Declaration - __ctor____main__block__87____Vector__int____Vector
;------------------------------------------------------------------------

;------------------------------------------------------------------------
         ; Method Declaration - Vector<:int:>::pushBack(int) -> void
         jmp .__end__method____main__block__87____Vector__int____pushBack__int
         .__method____main__block__87____Vector__int____pushBack__int:
            ; Function Header:
            ; Setup stack frame
               push rbp
               mov rbp, rsp
               ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
                  sub rsp, 32 ; space for local variables (16-byte aligned)
                  ; [rbp - 8] - this - Reference to 'this' object instance
                  mov rdx, qword [rbp + 16] ; param passed 'this'
                  mov qword [rbp - 8], rdx ; save this to a local
                  ; [rbp - 16] - int[] nData (<unset-scope-name>)
                  ; [rbp - 24] - int i (<unset-scope-name>)
            ; Parameters
               ; Param: val [rbp + 24] (__main__block__87____Vector__int__pushBack__val)
            ; Body
      ;------------------------------------------------------------------
               ; Code Block
         ;---------------------------------------------------------------
                  ; If-Statement
                     ; Condition
                        ; Greater Than or Equal to
                           ; LHS
                              ; Addition - int, int
                                 ; LHS
                                    ; Member Accessor
                                       ; LHS
                                          ; This keyword
                                             push qword [rbp - 8] ; __this
                                       ; RHS
                                          push qword [.__field____main__block__87____Vector__int____size] ; stored index associated with field that is being accessed
                                       pop rdx ; rhs
                                       pop rax ; lhs
                                       push qword [rax + 8*rdx] ; lhs.rhs
                                 ; RHS
                                    ; Int Literal
                                       mov rax, 1
                                       push rax
                                 pop rdx ; rhs
                                 pop rax ; lhs
                                 add rax, rdx
                                 push rax
                           ; RHS
                              ; Member Accessor
                                 ; LHS
                                    ; This keyword
                                       push qword [rbp - 8] ; __this
                                 ; RHS
                                    push qword [.__field____main__block__87____Vector__int____capacity] ; stored index associated with field that is being accessed
                                 pop rdx ; rhs
                                 pop rax ; lhs
                                 push qword [rax + 8*rdx] ; lhs.rhs
                           pop rdx ; rhs
                           pop rax ; lhs
                           cmp rax, rdx
                           setge al
                           movzx eax, al
                           push rax
                        pop rdx ; __cond
                        cmp rdx, 0 ; ensure condition is true
                        je .__endif__93 ; jump to end
                     ; Body
               ;---------------------------------------------------------
                        ; Code Block
                           ; Assignment - '='
                              ; RHS
                                 ; Multiplication - int, int
                                    ; LHS
                                       ; Member Accessor
                                          ; LHS
                                             ; This keyword
                                                push qword [rbp - 8] ; __this
                                          ; RHS
                                             push qword [.__field____main__block__87____Vector__int____capacity] ; stored index associated with field that is being accessed
                                          pop rdx ; rhs
                                          pop rax ; lhs
                                          push qword [rax + 8*rdx] ; lhs.rhs
                                    ; RHS
                                       ; Int Literal
                                          mov rax, 2
                                          push rax
                                    pop rdx
                                    pop rax
                                    imul rax, rdx
                                    push rax
                              ; LHS
                                 ; Member Accessor Assignment
                                    ; LHS
                                       ; This keyword
                                          push qword [rbp - 8] ; __this
                                    ; RHS
                                       push qword [.__field____main__block__87____Vector__int____capacity] ; 
                                    pop rdi ; rhs
                                    pop rbx ; lhs
                              pop rdx ; rhs value
                              mov qword [rbx + 8*rdi], rdx
                              push rdx
                           ; Statement results can be ignored
                           pop rdx
                           ; Assignment - '='
                              ; RHS
                                 ; Array Allocator
                                    ; Member Accessor
                                       ; LHS
                                          ; This keyword
                                             push qword [rbp - 8] ; __this
                                       ; RHS
                                          push qword [.__field____main__block__87____Vector__int____capacity] ; stored index associated with field that is being accessed
                                       pop rdx ; rhs
                                       pop rax ; lhs
                                       push qword [rax + 8*rdx] ; lhs.rhs
                                    pop rdx ; num elements for dimension[0]
                                    imul rdx, 8 ; 8 bytes per element
                                    mov rdi, rdx ; num bytes to allocate
                                    call malloc ; allocates edi bytes on heap and stores pointer in rax
                                    push rax ; __ptr
                              ; LHS
                                 ; Variable Declaration - nData
                                    mov rax, qword [rbp - 16]  ; __main__block__87____Vector__int__pushBack__block__92__if__93__block__94__nData
                              pop rdx ; rhs value
                              mov qword [rbp - 16], rdx
                              push rdx
                           ; Statement results can be ignored
                           pop rdx
                  ;------------------------------------------------------
                           ; For-Loop
                           ; Init
                              ; Assignment - '='
                                 ; RHS
                                    ; Int Literal
                                       mov rax, 0
                                       push rax
                                 ; LHS
                                    ; Variable Declaration - i
                                       mov rax, qword [rbp - 24]  ; __main__block__87____Vector__int__pushBack__block__92__if__93__block__94__for__95__i
                                 pop rdx ; rhs value
                                 mov qword [rbp - 24], rdx
                                 push rdx
                              ; Loop init result can be discarded
                              pop rax
                           jmp .__forcond__95
.__for__95:
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
.__forcond__95:
                              ; Condition
                                 ; Less Than
                                    ; LHS
                                       ; Identifier - int i
                                          push qword [rbp - 24]
                                    ; RHS
                                       ; Member Accessor
                                          ; LHS
                                             ; This keyword
                                                push qword [rbp - 8] ; __this
                                          ; RHS
                                             push qword [.__field____main__block__87____Vector__int____size] ; stored index associated with field that is being accessed
                                          pop rdx ; rhs
                                          pop rax ; lhs
                                          push qword [rax + 8*rdx] ; lhs.rhs
                                    pop rdx ; rhs
                                    pop rax ; lhs
                                    cmp rax, rdx
                                    setl al
                                    movzx eax, al
                                    push rax
                                 pop rax ; __cond
                                 cmp rax, 0 ; __cond
                                 je .__endfor__95
                              ; Body
                        ;------------------------------------------------
                                 ; Code Block
                                    ; Assignment - '='
                                       ; RHS
                                          ; Subscript
                                             ; LHS
                                                ; Member Accessor
                                                   ; LHS
                                                      ; This keyword
                                                         push qword [rbp - 8] ; __this
                                                   ; RHS
                                                      push qword [.__field____main__block__87____Vector__int____data] ; stored index associated with field that is being accessed
                                                   pop rdx ; rhs
                                                   pop rax ; lhs
                                                   push qword [rax + 8*rdx] ; lhs.rhs
                                             ; OFFSET
                                                ; Identifier - int i
                                                   push qword [rbp - 24]
                                             pop rdx ; __offset
                                             pop rax ; __pointer
                                             push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                                       ; LHS
                                          ; Subscript assignment
                                             ; LHS
                                                ; Identifier - int[] nData
                                                   push qword [rbp - 16]
                                             ; OFFSET
                                                ; Identifier - int i
                                                   push qword [rbp - 24]
                                             pop rdi ; __offset
                                             pop rbx ; __pointer
                                       pop rdx ; rhs value
                                       mov qword [rbx + 8*rdi], rdx
                                       push rdx
                                    ; Statement results can be ignored
                                    pop rdx
                        ;------------------------------------------------
                              ; Repeat
jmp .__for__95
                              ; End of For
.__endfor__95:
                  ;------------------------------------------------------
                           ; Free Operator
                              ; RHS
                                 ; Member Accessor
                                    ; LHS
                                       ; This keyword
                                          push qword [rbp - 8] ; __this
                                    ; RHS
                                       push qword [.__field____main__block__87____Vector__int____data] ; stored index associated with field that is being accessed
                                    pop rdx ; rhs
                                    pop rax ; lhs
                                    push qword [rax + 8*rdx] ; lhs.rhs
                              ; Free pointer
                              pop rdi   ; pointer
                              call free ; free the pointer
                              push rax  ; undefined return value
                           ; Statement results can be ignored
                           pop rdx
                           ; Assignment - '='
                              ; RHS
                                 ; Identifier - int[] nData
                                    push qword [rbp - 16]
                              ; LHS
                                 ; Member Accessor Assignment
                                    ; LHS
                                       ; This keyword
                                          push qword [rbp - 8] ; __this
                                    ; RHS
                                       push qword [.__field____main__block__87____Vector__int____data] ; 
                                    pop rdi ; rhs
                                    pop rbx ; lhs
                              pop rdx ; rhs value
                              mov qword [rbx + 8*rdi], rdx
                              push rdx
                           ; Statement results can be ignored
                           pop rdx
               ;---------------------------------------------------------
                     jmp .__endif__93 ; jump to end of condition chain
                     ; End of if
.__endif__93:
         ;---------------------------------------------------------------
                  ; Assignment - '='
                     ; RHS
                        ; Identifier - int val
                           push qword [rbp - -24]
                     ; LHS
                        ; Subscript assignment
                           ; LHS
                              ; Member Accessor
                                 ; LHS
                                    ; This keyword
                                       push qword [rbp - 8] ; __this
                                 ; RHS
                                    push qword [.__field____main__block__87____Vector__int____data] ; stored index associated with field that is being accessed
                                 pop rdx ; rhs
                                 pop rax ; lhs
                                 push qword [rax + 8*rdx] ; lhs.rhs
                           ; OFFSET
                              ; Member Accessor
                                 ; LHS
                                    ; This keyword
                                       push qword [rbp - 8] ; __this
                                 ; RHS
                                    push qword [.__field____main__block__87____Vector__int____size] ; stored index associated with field that is being accessed
                                 pop rdx ; rhs
                                 pop rax ; lhs
                                 push qword [rax + 8*rdx] ; lhs.rhs
                           pop rdi ; __offset
                           pop rbx ; __pointer
                     pop rdx ; rhs value
                     mov qword [rbx + 8*rdi], rdx
                     push rdx
                  ; Statement results can be ignored
                  pop rdx
                  ; Pre-Increment - int
                     ; RHS
                        ; Member Accessor
                           ; LHS
                              ; This keyword
                                 push qword [rbp - 8] ; __this
                           ; RHS
                              push qword [.__field____main__block__87____Vector__int____size] ; stored index associated with field that is being accessed
                           pop rdx ; rhs
                           pop rax ; lhs
                           push qword [rax + 8*rdx] ; lhs.rhs
                     pop rdx
                     ; LHS
                        ; Member Accessor Assignment
                           ; LHS
                              ; This keyword
                                 push qword [rbp - 8] ; __this
                           ; RHS
                              push qword [.__field____main__block__87____Vector__int____size] ; size
                           pop rdi ; rhs
                           pop rbx ; lhs
                           mov rax, qword [rbx + 8*rdi]
                           add rax, 1
                           mov qword [rbx + 8*rdi], rax
                     push rax ; push result
                  ; Statement results can be ignored
                  pop rdx
      ;------------------------------------------------------------------
            ; Function Epilogue
            mov rsp, rbp ; remove local vars + unpopped pushes
            pop rbp
            ret
         .__end__method____main__block__87____Vector__int____pushBack__int:
         ; End Method Declaration - .__method____main__block__87____Vector__int____pushBack__int
;------------------------------------------------------------------------

;------------------------------------------------------------------------
         ; Method Declaration - Vector<:int:>::popBack() -> int
         jmp .__end__method____main__block__87____Vector__int____popBack
         .__method____main__block__87____Vector__int____popBack:
            ; Function Header:
            ; Setup stack frame
               push rbp
               mov rbp, rsp
               ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
                  sub rsp, 16 ; space for local variables (16-byte aligned)
                  ; [rbp - 8] - this - Reference to 'this' object instance
                  mov rdx, qword [rbp + 16] ; param passed 'this'
                  mov qword [rbp - 8], rdx ; save this to a local
            ; Parameters
            ; Body
      ;------------------------------------------------------------------
               ; Code Block
                  ; Return
                     ; Subscript
                        ; LHS
                           ; Member Accessor
                              ; LHS
                                 ; This keyword
                                    push qword [rbp - 8] ; __this
                              ; RHS
                                 push qword [.__field____main__block__87____Vector__int____data] ; stored index associated with field that is being accessed
                              pop rdx ; rhs
                              pop rax ; lhs
                              push qword [rax + 8*rdx] ; lhs.rhs
                        ; OFFSET
                           ; Pre-Decrement - int
                              ; RHS
                                 ; Member Accessor
                                    ; LHS
                                       ; This keyword
                                          push qword [rbp - 8] ; __this
                                    ; RHS
                                       push qword [.__field____main__block__87____Vector__int____size] ; stored index associated with field that is being accessed
                                    pop rdx ; rhs
                                    pop rax ; lhs
                                    push qword [rax + 8*rdx] ; lhs.rhs
                              pop rdx
                              ; LHS
                                 ; Member Accessor Assignment
                                    ; LHS
                                       ; This keyword
                                          push qword [rbp - 8] ; __this
                                    ; RHS
                                       push qword [.__field____main__block__87____Vector__int____size] ; size
                                    pop rdi ; rhs
                                    pop rbx ; lhs
                                    mov rax, qword [rbx + 8*rdi]
                                    sub rax, 1
                                    mov qword [rbx + 8*rdi], rax
                              push rax ; push result
                        pop rdx ; __offset
                        pop rax ; __pointer
                        push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                     pop rax
                     ; Clean up stack and return
                     mov rsp, rbp ; remove local vars + unpopped pushes
                     pop rbp
                     ret
      ;------------------------------------------------------------------
            ; Function Epilogue
            mov rsp, rbp ; remove local vars + unpopped pushes
            pop rbp
            ret
         .__end__method____main__block__87____Vector__int____popBack:
         ; End Method Declaration - .__method____main__block__87____Vector__int____popBack
;------------------------------------------------------------------------

;------------------------------------------------------------------------
         ; Method Declaration - Vector<:int:>::get(int) -> int
         jmp .__end__method____main__block__87____Vector__int____get__int
         .__method____main__block__87____Vector__int____get__int:
            ; Function Header:
            ; Setup stack frame
               push rbp
               mov rbp, rsp
               ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
                  sub rsp, 16 ; space for local variables (16-byte aligned)
                  ; [rbp - 8] - this - Reference to 'this' object instance
                  mov rdx, qword [rbp + 16] ; param passed 'this'
                  mov qword [rbp - 8], rdx ; save this to a local
            ; Parameters
               ; Param: index [rbp + 24] (__main__block__87____Vector__int__get__index)
            ; Body
      ;------------------------------------------------------------------
               ; Code Block
                  ; Return
                     ; Subscript
                        ; LHS
                           ; Member Accessor
                              ; LHS
                                 ; This keyword
                                    push qword [rbp - 8] ; __this
                              ; RHS
                                 push qword [.__field____main__block__87____Vector__int____data] ; stored index associated with field that is being accessed
                              pop rdx ; rhs
                              pop rax ; lhs
                              push qword [rax + 8*rdx] ; lhs.rhs
                        ; OFFSET
                           ; Identifier - int index
                              push qword [rbp - -24]
                        pop rdx ; __offset
                        pop rax ; __pointer
                        push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                     pop rax
                     ; Clean up stack and return
                     mov rsp, rbp ; remove local vars + unpopped pushes
                     pop rbp
                     ret
      ;------------------------------------------------------------------
            ; Function Epilogue
            mov rsp, rbp ; remove local vars + unpopped pushes
            pop rbp
            ret
         .__end__method____main__block__87____Vector__int____get__int:
         ; End Method Declaration - .__method____main__block__87____Vector__int____get__int
;------------------------------------------------------------------------

;------------------------------------------------------------------------
         ; Method Declaration - Vector<:int:>::toString() -> char[]
         jmp .__end__method____main__block__87____Vector__int____toString
         .__method____main__block__87____Vector__int____toString:
            ; Function Header:
            ; Setup stack frame
               push rbp
               mov rbp, rsp
               ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
                  sub rsp, 16 ; space for local variables (16-byte aligned)
                  ; [rbp - 8] - this - Reference to 'this' object instance
                  mov rdx, qword [rbp + 16] ; param passed 'this'
                  mov qword [rbp - 8], rdx ; save this to a local
            ; Parameters
            ; Body
      ;------------------------------------------------------------------
               ; Code Block
                  ; Return
                     ; String Literal
                        ; "<Vector>"
                        mov rax, .str182
                        push rax
                     pop rax
                     ; Clean up stack and return
                     mov rsp, rbp ; remove local vars + unpopped pushes
                     pop rbp
                     ret
      ;------------------------------------------------------------------
            ; Function Epilogue
            mov rsp, rbp ; remove local vars + unpopped pushes
            pop rbp
            ret
         .__end__method____main__block__87____Vector__int____toString:
         ; End Method Declaration - .__method____main__block__87____Vector__int____toString
;------------------------------------------------------------------------

.__endclass____main__block__87____Vector__int:
         ; End Class Declaration - __main__block__87____Vector__int
; ===========================================================================

; ===========================================================================
         ; Class Declaration - __main__block__87____Vector__float inherits __main__block__87____Printable
         ; Class data
         section .data
            ; Dispatch Table - this might need to be a malloc**
            .__dtable____main__block__87____Vector__float:
            ; Dispatch Table Entries
            dq .__method____main__block__87____Vector__float____toString ; 0
            dq .__method____main__block__87____Vector__float____pushBack__float ; 1
            dq .__method____main__block__87____Vector__float____popBack ; 2
            dq .__method____main__block__87____Vector__float____get__int ; 3
         section .text
;------------------------------------------------------------------------
         ; Field - float[] Vector<:float:>::data
         section .data
         .__field____main__block__87____Vector__float____data: dq 1
         section .text
;------------------------------------------------------------------------
;------------------------------------------------------------------------
         ; Field - int Vector<:float:>::size
         section .data
         .__field____main__block__87____Vector__float____size: dq 2
         section .text
;------------------------------------------------------------------------
;------------------------------------------------------------------------
         ; Field - int Vector<:float:>::capacity
         section .data
         .__field____main__block__87____Vector__float____capacity: dq 3
         section .text
;------------------------------------------------------------------------
         ; skip over class methods
         jmp .__endclass____main__block__87____Vector__float
;------------------------------------------------------------------------
         ; Constructor Declaration - Vector<:float:>::Vector() -> Vector<:float:>
         jmp .__end__ctor____main__block__87____Vector__float____Vector
         .__ctor____main__block__87____Vector__float____Vector:
         ; Function Header:
            ; Setup stack frame
               push rbp
               mov rbp, rsp
               ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
                  sub rsp, 16 ; space for local variables (16-byte aligned)
                  ; [rbp - 8] - this - Reference to 'this' object instance
            ; Creating Class Instance
               mov rdi, 32 ; [dtable, field0, field1, ..., fieldN] each 8 bytes
               call malloc
               mov qword [rbp - 8], rax ; save class instance as 'this'
               ; Add Dispatch Table
               mov rax, qword [rbp - 8] ; this
               mov qword [rax + 0], .__dtable____main__block__87____Vector__float ; this[0] = &dtable
            ; Parameters
         ; Body
   ;---------------------------------------------------------------------
            ; Code Block
               ; Assignment - '='
                  ; RHS
                     ; Int Literal
                        mov rax, 10
                        push rax
                  ; LHS
                     ; Member Accessor Assignment
                        ; LHS
                           ; This keyword
                              push qword [rbp - 8] ; __this
                        ; RHS
                           push qword [.__field____main__block__87____Vector__float____capacity] ; 
                        pop rdi ; rhs
                        pop rbx ; lhs
                  pop rdx ; rhs value
                  mov qword [rbx + 8*rdi], rdx
                  push rdx
               ; Statement results can be ignored
               pop rdx
               ; Assignment - '='
                  ; RHS
                     ; Array Allocator
                        ; Member Accessor
                           ; LHS
                              ; This keyword
                                 push qword [rbp - 8] ; __this
                           ; RHS
                              push qword [.__field____main__block__87____Vector__float____capacity] ; stored index associated with field that is being accessed
                           pop rdx ; rhs
                           pop rax ; lhs
                           push qword [rax + 8*rdx] ; lhs.rhs
                        pop rdx ; num elements for dimension[0]
                        imul rdx, 8 ; 8 bytes per element
                        mov rdi, rdx ; num bytes to allocate
                        call malloc ; allocates edi bytes on heap and stores pointer in rax
                        push rax ; __ptr
                  ; LHS
                     ; Member Accessor Assignment
                        ; LHS
                           ; This keyword
                              push qword [rbp - 8] ; __this
                        ; RHS
                           push qword [.__field____main__block__87____Vector__float____data] ; 
                        pop rdi ; rhs
                        pop rbx ; lhs
                  pop rdx ; rhs value
                  mov qword [rbx + 8*rdi], rdx
                  push rdx
               ; Statement results can be ignored
               pop rdx
               ; Assignment - '='
                  ; RHS
                     ; Int Literal
                        mov rax, 0
                        push rax
                  ; LHS
                     ; Member Accessor Assignment
                        ; LHS
                           ; This keyword
                              push qword [rbp - 8] ; __this
                        ; RHS
                           push qword [.__field____main__block__87____Vector__float____size] ; 
                        pop rdi ; rhs
                        pop rbx ; lhs
                  pop rdx ; rhs value
                  mov qword [rbx + 8*rdi], rdx
                  push rdx
               ; Statement results can be ignored
               pop rdx
   ;---------------------------------------------------------------------
         mov rax, qword [rbp - 8] ; __this
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
         .__end__ctor____main__block__87____Vector__float____Vector:
         ; End Constructor Declaration - __ctor____main__block__87____Vector__float____Vector
;---------------------------------------------------------------------------

;---------------------------------------------------------------------------
         ; Method Declaration - Vector<:float:>::pushBack(float) -> void
         jmp .__end__method____main__block__87____Vector__float____pushBack__float
         .__method____main__block__87____Vector__float____pushBack__float:
         ; Function Header:
         ; Setup stack frame
            push rbp
            mov rbp, rsp
            ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
               sub rsp, 32 ; space for local variables (16-byte aligned)
               ; [rbp - 8] - this - Reference to 'this' object instance
               mov rdx, qword [rbp + 16] ; param passed 'this'
               mov qword [rbp - 8], rdx ; save this to a local
               ; [rbp - 16] - float[] nData (<unset-scope-name>)
               ; [rbp - 24] - int i (<unset-scope-name>)
         ; Parameters
            ; Param: val [rbp + 24] (__main__block__87____Vector__float__pushBack__val)
         ; Body
   ;---------------------------------------------------------------------
            ; Code Block
      ;------------------------------------------------------------------
               ; If-Statement
                  ; Condition
                     ; Greater Than or Equal to
                        ; LHS
                           ; Addition - int, int
                              ; LHS
                                 ; Member Accessor
                                    ; LHS
                                       ; This keyword
                                          push qword [rbp - 8] ; __this
                                    ; RHS
                                       push qword [.__field____main__block__87____Vector__float____size] ; stored index associated with field that is being accessed
                                    pop rdx ; rhs
                                    pop rax ; lhs
                                    push qword [rax + 8*rdx] ; lhs.rhs
                              ; RHS
                                 ; Int Literal
                                    mov rax, 1
                                    push rax
                              pop rdx ; rhs
                              pop rax ; lhs
                              add rax, rdx
                              push rax
                        ; RHS
                           ; Member Accessor
                              ; LHS
                                 ; This keyword
                                    push qword [rbp - 8] ; __this
                              ; RHS
                                 push qword [.__field____main__block__87____Vector__float____capacity] ; stored index associated with field that is being accessed
                              pop rdx ; rhs
                              pop rax ; lhs
                              push qword [rax + 8*rdx] ; lhs.rhs
                        pop rdx ; rhs
                        pop rax ; lhs
                        cmp rax, rdx
                        setge al
                        movzx eax, al
                        push rax
                     pop rdx ; __cond
                     cmp rdx, 0 ; ensure condition is true
                     je .__endif__102 ; jump to end
                  ; Body
            ;------------------------------------------------------------
                     ; Code Block
                        ; Assignment - '='
                           ; RHS
                              ; Multiplication - int, int
                                 ; LHS
                                    ; Member Accessor
                                       ; LHS
                                          ; This keyword
                                             push qword [rbp - 8] ; __this
                                       ; RHS
                                          push qword [.__field____main__block__87____Vector__float____capacity] ; stored index associated with field that is being accessed
                                       pop rdx ; rhs
                                       pop rax ; lhs
                                       push qword [rax + 8*rdx] ; lhs.rhs
                                 ; RHS
                                    ; Int Literal
                                       mov rax, 2
                                       push rax
                                 pop rdx
                                 pop rax
                                 imul rax, rdx
                                 push rax
                           ; LHS
                              ; Member Accessor Assignment
                                 ; LHS
                                    ; This keyword
                                       push qword [rbp - 8] ; __this
                                 ; RHS
                                    push qword [.__field____main__block__87____Vector__float____capacity] ; 
                                 pop rdi ; rhs
                                 pop rbx ; lhs
                           pop rdx ; rhs value
                           mov qword [rbx + 8*rdi], rdx
                           push rdx
                        ; Statement results can be ignored
                        pop rdx
                        ; Assignment - '='
                           ; RHS
                              ; Array Allocator
                                 ; Member Accessor
                                    ; LHS
                                       ; This keyword
                                          push qword [rbp - 8] ; __this
                                    ; RHS
                                       push qword [.__field____main__block__87____Vector__float____capacity] ; stored index associated with field that is being accessed
                                    pop rdx ; rhs
                                    pop rax ; lhs
                                    push qword [rax + 8*rdx] ; lhs.rhs
                                 pop rdx ; num elements for dimension[0]
                                 imul rdx, 8 ; 8 bytes per element
                                 mov rdi, rdx ; num bytes to allocate
                                 call malloc ; allocates edi bytes on heap and stores pointer in rax
                                 push rax ; __ptr
                           ; LHS
                              ; Variable Declaration - nData
                                 mov rax, qword [rbp - 16]  ; __main__block__87____Vector__float__pushBack__block__101__if__102__block__103__nData
                           pop rdx ; rhs value
                           mov qword [rbp - 16], rdx
                           push rdx
                        ; Statement results can be ignored
                        pop rdx
               ;---------------------------------------------------------
                        ; For-Loop
                        ; Init
                           ; Assignment - '='
                              ; RHS
                                 ; Int Literal
                                    mov rax, 0
                                    push rax
                              ; LHS
                                 ; Variable Declaration - i
                                    mov rax, qword [rbp - 24]  ; __main__block__87____Vector__float__pushBack__block__101__if__102__block__103__for__104__i
                              pop rdx ; rhs value
                              mov qword [rbp - 24], rdx
                              push rdx
                           ; Loop init result can be discarded
                           pop rax
                        jmp .__forcond__104
.__for__104:
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
.__forcond__104:
                           ; Condition
                              ; Less Than
                                 ; LHS
                                    ; Identifier - int i
                                       push qword [rbp - 24]
                                 ; RHS
                                    ; Member Accessor
                                       ; LHS
                                          ; This keyword
                                             push qword [rbp - 8] ; __this
                                       ; RHS
                                          push qword [.__field____main__block__87____Vector__float____size] ; stored index associated with field that is being accessed
                                       pop rdx ; rhs
                                       pop rax ; lhs
                                       push qword [rax + 8*rdx] ; lhs.rhs
                                 pop rdx ; rhs
                                 pop rax ; lhs
                                 cmp rax, rdx
                                 setl al
                                 movzx eax, al
                                 push rax
                              pop rax ; __cond
                              cmp rax, 0 ; __cond
                              je .__endfor__104
                           ; Body
                     ;---------------------------------------------------
                              ; Code Block
                                 ; Assignment - '='
                                    ; RHS
                                       ; Subscript
                                          ; LHS
                                             ; Member Accessor
                                                ; LHS
                                                   ; This keyword
                                                      push qword [rbp - 8] ; __this
                                                ; RHS
                                                   push qword [.__field____main__block__87____Vector__float____data] ; stored index associated with field that is being accessed
                                                pop rdx ; rhs
                                                pop rax ; lhs
                                                push qword [rax + 8*rdx] ; lhs.rhs
                                          ; OFFSET
                                             ; Identifier - int i
                                                push qword [rbp - 24]
                                          pop rdx ; __offset
                                          pop rax ; __pointer
                                          push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                                    ; LHS
                                       ; Subscript assignment
                                          ; LHS
                                             ; Identifier - float[] nData
                                                push qword [rbp - 16]
                                          ; OFFSET
                                             ; Identifier - int i
                                                push qword [rbp - 24]
                                          pop rdi ; __offset
                                          pop rbx ; __pointer
                                    pop rdx ; rhs value
                                    mov qword [rbx + 8*rdi], rdx
                                    push rdx
                                 ; Statement results can be ignored
                                 pop rdx
                     ;---------------------------------------------------
                           ; Repeat
jmp .__for__104
                           ; End of For
.__endfor__104:
               ;---------------------------------------------------------
                        ; Free Operator
                           ; RHS
                              ; Member Accessor
                                 ; LHS
                                    ; This keyword
                                       push qword [rbp - 8] ; __this
                                 ; RHS
                                    push qword [.__field____main__block__87____Vector__float____data] ; stored index associated with field that is being accessed
                                 pop rdx ; rhs
                                 pop rax ; lhs
                                 push qword [rax + 8*rdx] ; lhs.rhs
                           ; Free pointer
                           pop rdi   ; pointer
                           call free ; free the pointer
                           push rax  ; undefined return value
                        ; Statement results can be ignored
                        pop rdx
                        ; Assignment - '='
                           ; RHS
                              ; Identifier - float[] nData
                                 push qword [rbp - 16]
                           ; LHS
                              ; Member Accessor Assignment
                                 ; LHS
                                    ; This keyword
                                       push qword [rbp - 8] ; __this
                                 ; RHS
                                    push qword [.__field____main__block__87____Vector__float____data] ; 
                                 pop rdi ; rhs
                                 pop rbx ; lhs
                           pop rdx ; rhs value
                           mov qword [rbx + 8*rdi], rdx
                           push rdx
                        ; Statement results can be ignored
                        pop rdx
            ;------------------------------------------------------------
                  jmp .__endif__102 ; jump to end of condition chain
                  ; End of if
.__endif__102:
      ;------------------------------------------------------------------
               ; Assignment - '='
                  ; RHS
                     ; Identifier - float val
                        push qword [rbp - -24]
                  ; LHS
                     ; Subscript assignment
                        ; LHS
                           ; Member Accessor
                              ; LHS
                                 ; This keyword
                                    push qword [rbp - 8] ; __this
                              ; RHS
                                 push qword [.__field____main__block__87____Vector__float____data] ; stored index associated with field that is being accessed
                              pop rdx ; rhs
                              pop rax ; lhs
                              push qword [rax + 8*rdx] ; lhs.rhs
                        ; OFFSET
                           ; Member Accessor
                              ; LHS
                                 ; This keyword
                                    push qword [rbp - 8] ; __this
                              ; RHS
                                 push qword [.__field____main__block__87____Vector__float____size] ; stored index associated with field that is being accessed
                              pop rdx ; rhs
                              pop rax ; lhs
                              push qword [rax + 8*rdx] ; lhs.rhs
                        pop rdi ; __offset
                        pop rbx ; __pointer
                  pop rdx ; rhs value
                  mov qword [rbx + 8*rdi], rdx
                  push rdx
               ; Statement results can be ignored
               pop rdx
               ; Pre-Increment - int
                  ; RHS
                     ; Member Accessor
                        ; LHS
                           ; This keyword
                              push qword [rbp - 8] ; __this
                        ; RHS
                           push qword [.__field____main__block__87____Vector__float____size] ; stored index associated with field that is being accessed
                        pop rdx ; rhs
                        pop rax ; lhs
                        push qword [rax + 8*rdx] ; lhs.rhs
                  pop rdx
                  ; LHS
                     ; Member Accessor Assignment
                        ; LHS
                           ; This keyword
                              push qword [rbp - 8] ; __this
                        ; RHS
                           push qword [.__field____main__block__87____Vector__float____size] ; size
                        pop rdi ; rhs
                        pop rbx ; lhs
                        mov rax, qword [rbx + 8*rdi]
                        add rax, 1
                        mov qword [rbx + 8*rdi], rax
                  push rax ; push result
               ; Statement results can be ignored
               pop rdx
   ;---------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
         .__end__method____main__block__87____Vector__float____pushBack__float:
         ; End Method Declaration - .__method____main__block__87____Vector__float____pushBack__float
;---------------------------------------------------------------------------

;---------------------------------------------------------------------------
         ; Method Declaration - Vector<:float:>::popBack() -> float
         jmp .__end__method____main__block__87____Vector__float____popBack
         .__method____main__block__87____Vector__float____popBack:
         ; Function Header:
         ; Setup stack frame
            push rbp
            mov rbp, rsp
            ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
               sub rsp, 16 ; space for local variables (16-byte aligned)
               ; [rbp - 8] - this - Reference to 'this' object instance
               mov rdx, qword [rbp + 16] ; param passed 'this'
               mov qword [rbp - 8], rdx ; save this to a local
         ; Parameters
         ; Body
   ;---------------------------------------------------------------------
            ; Code Block
               ; Return
                  ; Subscript
                     ; LHS
                        ; Member Accessor
                           ; LHS
                              ; This keyword
                                 push qword [rbp - 8] ; __this
                           ; RHS
                              push qword [.__field____main__block__87____Vector__float____data] ; stored index associated with field that is being accessed
                           pop rdx ; rhs
                           pop rax ; lhs
                           push qword [rax + 8*rdx] ; lhs.rhs
                     ; OFFSET
                        ; Pre-Decrement - int
                           ; RHS
                              ; Member Accessor
                                 ; LHS
                                    ; This keyword
                                       push qword [rbp - 8] ; __this
                                 ; RHS
                                    push qword [.__field____main__block__87____Vector__float____size] ; stored index associated with field that is being accessed
                                 pop rdx ; rhs
                                 pop rax ; lhs
                                 push qword [rax + 8*rdx] ; lhs.rhs
                           pop rdx
                           ; LHS
                              ; Member Accessor Assignment
                                 ; LHS
                                    ; This keyword
                                       push qword [rbp - 8] ; __this
                                 ; RHS
                                    push qword [.__field____main__block__87____Vector__float____size] ; size
                                 pop rdi ; rhs
                                 pop rbx ; lhs
                                 mov rax, qword [rbx + 8*rdi]
                                 sub rax, 1
                                 mov qword [rbx + 8*rdi], rax
                           push rax ; push result
                     pop rdx ; __offset
                     pop rax ; __pointer
                     push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                  pop rax
                  ; Clean up stack and return
                  mov rsp, rbp ; remove local vars + unpopped pushes
                  pop rbp
                  ret
   ;---------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
         .__end__method____main__block__87____Vector__float____popBack:
         ; End Method Declaration - .__method____main__block__87____Vector__float____popBack
;---------------------------------------------------------------------------

;---------------------------------------------------------------------------
         ; Method Declaration - Vector<:float:>::get(int) -> float
         jmp .__end__method____main__block__87____Vector__float____get__int
         .__method____main__block__87____Vector__float____get__int:
         ; Function Header:
         ; Setup stack frame
            push rbp
            mov rbp, rsp
            ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
               sub rsp, 16 ; space for local variables (16-byte aligned)
               ; [rbp - 8] - this - Reference to 'this' object instance
               mov rdx, qword [rbp + 16] ; param passed 'this'
               mov qword [rbp - 8], rdx ; save this to a local
         ; Parameters
            ; Param: index [rbp + 24] (__main__block__87____Vector__float__get__index)
         ; Body
   ;---------------------------------------------------------------------
            ; Code Block
               ; Return
                  ; Subscript
                     ; LHS
                        ; Member Accessor
                           ; LHS
                              ; This keyword
                                 push qword [rbp - 8] ; __this
                           ; RHS
                              push qword [.__field____main__block__87____Vector__float____data] ; stored index associated with field that is being accessed
                           pop rdx ; rhs
                           pop rax ; lhs
                           push qword [rax + 8*rdx] ; lhs.rhs
                     ; OFFSET
                        ; Identifier - int index
                           push qword [rbp - -24]
                     pop rdx ; __offset
                     pop rax ; __pointer
                     push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                  pop rax
                  ; Clean up stack and return
                  mov rsp, rbp ; remove local vars + unpopped pushes
                  pop rbp
                  ret
   ;---------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
         .__end__method____main__block__87____Vector__float____get__int:
         ; End Method Declaration - .__method____main__block__87____Vector__float____get__int
;---------------------------------------------------------------------------

;---------------------------------------------------------------------------
         ; Method Declaration - Vector<:float:>::toString() -> char[]
         jmp .__end__method____main__block__87____Vector__float____toString
         .__method____main__block__87____Vector__float____toString:
         ; Function Header:
         ; Setup stack frame
            push rbp
            mov rbp, rsp
            ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
               sub rsp, 16 ; space for local variables (16-byte aligned)
               ; [rbp - 8] - this - Reference to 'this' object instance
               mov rdx, qword [rbp + 16] ; param passed 'this'
               mov qword [rbp - 8], rdx ; save this to a local
         ; Parameters
         ; Body
   ;---------------------------------------------------------------------
            ; Code Block
               ; Return
                  ; String Literal
                     ; "<Vector>"
                     mov rax, .str184
                     push rax
                  pop rax
                  ; Clean up stack and return
                  mov rsp, rbp ; remove local vars + unpopped pushes
                  pop rbp
                  ret
   ;---------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
         .__end__method____main__block__87____Vector__float____toString:
         ; End Method Declaration - .__method____main__block__87____Vector__float____toString
;---------------------------------------------------------------------------

.__endclass____main__block__87____Vector__float:
         ; End Class Declaration - __main__block__87____Vector__float
; ==============================================================================

         ; End Class Template - 
; ====================================================================================

; ====================================================================================
         ; Function Declaration - print(Printable) -> void
         ; Skip over function declaration
         jmp .__end____main__block__87____print__Printable
.__main__block__87____print__Printable:
         ; Function Header:
         ; Setup stack frame
         push rbp
         mov rbp, rsp
         sub rsp, 0
         ; Parameters
         ; Param: o [rbp + 16]
         ; Local Variables - Each variable is currently 64-bit (sorry not sorry)

         ; Body
;------------------------------------------------------------------------------
         ; Code Block
         ; Function Call - print(char[]) -> void
         ; Make space for 1 arg(s)
         sub rsp, 8
         ; Arguments
            ; Eval arg0
               ; Virtual Method Call - toString() -> char[]
                  ; Make space for 0 arg(s) and object parameter
                  sub rsp, 8
                  ; LHS
                     ; Identifier - Printable o
                        push qword [rbp - -16]
                     pop rax ; object parameter
                     mov qword [rsp + 0], rax ; place as first parameter
                  ; RHS
                  ; Arguments
                  ; Virtual Function Dispatch
                  mov rdx, qword [rsp + 0] ;  rdx = object
                  mov rdi, qword [rdx + 0] ;  rdi = object[0] ; dtable
                  call qword [rdi + 0] ; dtable[0] ; __method____main__block__87____Printable____toString
                  ; Remove args
                  add rsp, 8
                  ; Push return value
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
;------------------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
.__end____main__block__87____print__Printable:
         ; End Function Declaration - print(Printable) -> void
; ====================================================================================

; ====================================================================================
         ; Function Declaration - println(Printable) -> void
         ; Skip over function declaration
         jmp .__end____main__block__87____println__Printable
.__main__block__87____println__Printable:
         ; Function Header:
         ; Setup stack frame
         push rbp
         mov rbp, rsp
         sub rsp, 0
         ; Parameters
         ; Param: o [rbp + 16]
         ; Local Variables - Each variable is currently 64-bit (sorry not sorry)

         ; Body
;------------------------------------------------------------------------------
         ; Code Block
         ; Function Call - println(char[]) -> void
         ; Make space for 1 arg(s)
         sub rsp, 8
         ; Arguments
            ; Eval arg0
               ; Virtual Method Call - toString() -> char[]
                  ; Make space for 0 arg(s) and object parameter
                  sub rsp, 8
                  ; LHS
                     ; Identifier - Printable o
                        push qword [rbp - -16]
                     pop rax ; object parameter
                     mov qword [rsp + 0], rax ; place as first parameter
                  ; RHS
                  ; Arguments
                  ; Virtual Function Dispatch
                  mov rdx, qword [rsp + 0] ;  rdx = object
                  mov rdi, qword [rdx + 0] ;  rdi = object[0] ; dtable
                  call qword [rdi + 0] ; dtable[0] ; __method____main__block__87____Printable____toString
                  ; Remove args
                  add rsp, 8
                  ; Push return value
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
;------------------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
.__end____main__block__87____println__Printable:
         ; End Function Declaration - println(Printable) -> void
; ====================================================================================

         ; Assignment - '='
         ; RHS
         ; Constructor Call - Vector<:int:>::Vector() -> Vector<:int:>
         ; Make space for 0 arg(s)
         sub rsp, 0
         ; Arguments
         ; Call Vector<:int:>::Vector()
         call .__ctor____main__block__87____Vector__int____Vector
         ; Remove args
         add rsp, 0
         ; Push return value
         push rax
         ; LHS
         ; Variable Declaration - myArray
         mov rax, qword [rbp - 384]  ; __main__block__87__myArray
         pop rdx ; rhs value
         mov qword [rbp - 384], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
         ; Method Call - Vector<:int:>::pushBack(int) -> void
         ; Make space for 1 arg(s) and object parameter
         sub rsp, 16
         ; LHS
         ; Identifier - Vector<:int:> myArray
         push qword [rbp - 384]
         pop rax ; object parameter
         mov qword [rsp + 0], rax ; place as first parameter
         ; RHS
         ; Arguments
         ; Eval arg0
         ; Int Literal
         mov rax, 42
         push rax
         ; Move arg0's result to reverse order position on stack
         pop rax
         mov qword [rsp + 8], rax
         call .__method____main__block__87____Vector__int____pushBack__int
         ; Remove args
         add rsp, 16
         ; Push return value
         push rax
         ; Statement results can be ignored
         pop rdx
         ; Method Call - Vector<:int:>::pushBack(int) -> void
         ; Make space for 1 arg(s) and object parameter
         sub rsp, 16
         ; LHS
         ; Identifier - Vector<:int:> myArray
         push qword [rbp - 384]
         pop rax ; object parameter
         mov qword [rsp + 0], rax ; place as first parameter
         ; RHS
         ; Arguments
         ; Eval arg0
         ; Int Literal
         mov rax, 7
         push rax
         ; Move arg0's result to reverse order position on stack
         pop rax
         mov qword [rsp + 8], rax
         call .__method____main__block__87____Vector__int____pushBack__int
         ; Remove args
         add rsp, 16
         ; Push return value
         push rax
         ; Statement results can be ignored
         pop rdx
         ; Method Call - Vector<:int:>::popBack() -> int
         ; Make space for 0 arg(s) and object parameter
         sub rsp, 8
         ; LHS
         ; Identifier - Vector<:int:> myArray
         push qword [rbp - 384]
         pop rax ; object parameter
         mov qword [rsp + 0], rax ; place as first parameter
         ; RHS
         ; Arguments
         call .__method____main__block__87____Vector__int____popBack
         ; Remove args
         add rsp, 8
         ; Push return value
         push rax
         ; Statement results can be ignored
         pop rdx
         ; Method Call - Vector<:int:>::pushBack(int) -> void
         ; Make space for 1 arg(s) and object parameter
         sub rsp, 16
         ; LHS
         ; Identifier - Vector<:int:> myArray
         push qword [rbp - 384]
         pop rax ; object parameter
         mov qword [rsp + 0], rax ; place as first parameter
         ; RHS
         ; Arguments
         ; Eval arg0
         ; Int Literal
         mov rax, 19
         push rax
         ; Move arg0's result to reverse order position on stack
         pop rax
         mov qword [rsp + 8], rax
         call .__method____main__block__87____Vector__int____pushBack__int
         ; Remove args
         add rsp, 16
         ; Push return value
         push rax
         ; Statement results can be ignored
         pop rdx
         ; Method Call - Vector<:int:>::pushBack(int) -> void
         ; Make space for 1 arg(s) and object parameter
         sub rsp, 16
         ; LHS
         ; Identifier - Vector<:int:> myArray
         push qword [rbp - 384]
         pop rax ; object parameter
         mov qword [rsp + 0], rax ; place as first parameter
         ; RHS
         ; Arguments
         ; Eval arg0
         ; Int Literal
         mov rax, 25
         push rax
         ; Move arg0's result to reverse order position on stack
         pop rax
         mov qword [rsp + 8], rax
         call .__method____main__block__87____Vector__int____pushBack__int
         ; Remove args
         add rsp, 16
         ; Push return value
         push rax
         ; Statement results can be ignored
         pop rdx
         ; Method Call - Vector<:int:>::popBack() -> int
         ; Make space for 0 arg(s) and object parameter
         sub rsp, 8
         ; LHS
         ; Identifier - Vector<:int:> myArray
         push qword [rbp - 384]
         pop rax ; object parameter
         mov qword [rsp + 0], rax ; place as first parameter
         ; RHS
         ; Arguments
         call .__method____main__block__87____Vector__int____popBack
         ; Remove args
         add rsp, 8
         ; Push return value
         push rax
         ; Statement results can be ignored
         pop rdx
;------------------------------------------------------------------------------------
         ; For-Loop
         ; Init
         ; Assignment - '='
         ; RHS
         ; Int Literal
         mov rax, 0
         push rax
         ; LHS
         ; Variable Declaration - i
         mov rax, qword [rbp - 392]  ; __main__block__87__for__111__i
         pop rdx ; rhs value
         mov qword [rbp - 392], rdx
         push rdx
         ; Loop init result can be discarded
         pop rax
         jmp .__forcond__111
.__for__111:
         ; Update
         ; Pre-Increment - int
         ; RHS
         ; Identifier - int i
            push qword [rbp - 392]
         pop rdx
         add qword [rbp - 392], 1
         mov rax, qword [rbp - 392]
         push rax ; push result
         ; Loop update result can be discarded
         pop rax
.__forcond__111:
         ; Condition
         ; Less Than
         ; LHS
         ; Identifier - int i
            push qword [rbp - 392]
         ; RHS
         ; Member Accessor
            ; LHS
               ; Identifier - Vector<:int:> myArray
                  push qword [rbp - 384]
            ; RHS
               push qword [.__field____main__block__87____Vector__int____size] ; stored index associated with field that is being accessed
            pop rdx ; rhs
            pop rax ; lhs
            push qword [rax + 8*rdx] ; lhs.rhs
         pop rdx ; rhs
         pop rax ; lhs
         cmp rax, rdx
         setl al
         movzx eax, al
         push rax
         pop rax ; __cond
         cmp rax, 0 ; __cond
         je .__endfor__111
         ; Body
;------------------------------------------------------------------------------
         ; Code Block
         ; Function Call - print(int) -> void
         ; Make space for 1 arg(s)
         sub rsp, 8
         ; Arguments
            ; Eval arg0
               ; Method Call - Vector<:int:>::get(int) -> int
                  ; Make space for 1 arg(s) and object parameter
                  sub rsp, 16
                  ; LHS
                     ; Identifier - Vector<:int:> myArray
                        push qword [rbp - 384]
                     pop rax ; object parameter
                     mov qword [rsp + 0], rax ; place as first parameter
                  ; RHS
                  ; Arguments
                     ; Eval arg0
                        ; Identifier - int i
                           push qword [rbp - 392]
                     ; Move arg0's result to reverse order position on stack
                     pop rax
                     mov qword [rsp + 8], rax
                  call .__method____main__block__87____Vector__int____get__int
                  ; Remove args
                  add rsp, 16
                  ; Push return value
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
         ; Function Call - print(char[]) -> void
         ; Make space for 1 arg(s)
         sub rsp, 8
         ; Arguments
            ; Eval arg0
               ; String Literal
                  ; " "
                  mov rax, .str183
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
;------------------------------------------------------------------------------
         ; Repeat
jmp .__for__111
         ; End of For
.__endfor__111:
;------------------------------------------------------------------------------------
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
         ; Function Call - println(int) -> void
         ; Make space for 1 arg(s)
         sub rsp, 8
         ; Arguments
         ; Eval arg0
         ; Post-Decrement
         ; RHS
            ; Subscript assignment
               ; LHS
                  ; Member Accessor
                     ; LHS
                        ; Identifier - Vector<:int:> myArray
                           push qword [rbp - 384]
                     ; RHS
                        push qword [.__field____main__block__87____Vector__int____data] ; stored index associated with field that is being accessed
                     pop rdx ; rhs
                     pop rax ; lhs
                     push qword [rax + 8*rdx] ; lhs.rhs
               ; OFFSET
                  ; Int Literal
                     mov rax, 0
                     push rax
               pop rdi ; rhs
               pop rbx ; lhs
               mov rax, qword [rbx + 8*rdi] ; save original value
               sub qword [rbx + 8*rdi], 1   ; decrement
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
         ; Function Call - println(int) -> void
         ; Make space for 1 arg(s)
         sub rsp, 8
         ; Arguments
         ; Eval arg0
         ; Subscript
         ; LHS
            ; Member Accessor
               ; LHS
                  ; Identifier - Vector<:int:> myArray
                     push qword [rbp - 384]
               ; RHS
                  push qword [.__field____main__block__87____Vector__int____data] ; stored index associated with field that is being accessed
               pop rdx ; rhs
               pop rax ; lhs
               push qword [rax + 8*rdx] ; lhs.rhs
         ; OFFSET
            ; Int Literal
               mov rax, 0
               push rax
         pop rdx ; __offset
         pop rax ; __pointer
         push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
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
         ; Function Call - println(int) -> void
         ; Make space for 1 arg(s)
         sub rsp, 8
         ; Arguments
         ; Eval arg0
         ; Post-Increment
         ; LHS
            ; Member Accessor Assignment
               ; LHS
                  ; Identifier - Vector<:int:> myArray
                     push qword [rbp - 384]
               ; RHS
                  push qword [.__field____main__block__87____Vector__int____size] ; size
               pop rdi ; rhs
               pop rbx ; lhs
               mov rax, qword [rbx + 8*rdi] ; save original value
               add qword [rbx + 8*rdi], 1   ; increment
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
         ; Function Call - println(int) -> void
         ; Make space for 1 arg(s)
         sub rsp, 8
         ; Arguments
         ; Eval arg0
         ; Member Accessor
         ; LHS
            ; Identifier - Vector<:int:> myArray
               push qword [rbp - 384]
         ; RHS
            push qword [.__field____main__block__87____Vector__int____size] ; stored index associated with field that is being accessed
         pop rdx ; rhs
         pop rax ; lhs
         push qword [rax + 8*rdx] ; lhs.rhs
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
         ; Function Call - println(Printable) -> void
         ; Make space for 1 arg(s)
         sub rsp, 8
         ; Arguments
         ; Eval arg0
         ; Identifier - Vector<:int:> myArray
         push qword [rbp - 384]
         ; Move arg0's result to reverse order position on stack
         pop rax
         mov qword [rsp + 0], rax
         ; Call println(Printable)
         call .__main__block__87____println__Printable
         ; Remove args
         add rsp, 8
         ; Push return value
         push rax
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
         ; RHS
         ; Constructor Call - Vector<:float:>::Vector() -> Vector<:float:>
         ; Make space for 0 arg(s)
         sub rsp, 0
         ; Arguments
         ; Call Vector<:float:>::Vector()
         call .__ctor____main__block__87____Vector__float____Vector
         ; Remove args
         add rsp, 0
         ; Push return value
         push rax
         ; LHS
         ; Variable Declaration - vals
         mov rax, qword [rbp - 400]  ; __main__block__87__vals
         pop rdx ; rhs value
         mov qword [rbp - 400], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
         ; Method Call - Vector<:float:>::pushBack(float) -> void
         ; Make space for 1 arg(s) and object parameter
         sub rsp, 16
         ; LHS
         ; Identifier - Vector<:float:> vals
         push qword [rbp - 400]
         pop rax ; object parameter
         mov qword [rsp + 0], rax ; place as first parameter
         ; RHS
         ; Arguments
         ; Eval arg0
         ; Float Literal
         mov rax, qword [.float62] ; 42.0
         push rax
         ; Move arg0's result to reverse order position on stack
         pop rax
         mov qword [rsp + 8], rax
         call .__method____main__block__87____Vector__float____pushBack__float
         ; Remove args
         add rsp, 16
         ; Push return value
         push rax
         ; Statement results can be ignored
         pop rdx
         ; Method Call - Vector<:float:>::pushBack(float) -> void
         ; Make space for 1 arg(s) and object parameter
         sub rsp, 16
         ; LHS
         ; Identifier - Vector<:float:> vals
         push qword [rbp - 400]
         pop rax ; object parameter
         mov qword [rsp + 0], rax ; place as first parameter
         ; RHS
         ; Arguments
         ; Eval arg0
         ; Float Literal
         mov rax, qword [.float63] ; 12345.6789
         push rax
         ; Move arg0's result to reverse order position on stack
         pop rax
         mov qword [rsp + 8], rax
         call .__method____main__block__87____Vector__float____pushBack__float
         ; Remove args
         add rsp, 16
         ; Push return value
         push rax
         ; Statement results can be ignored
         pop rdx
         ; Function Call - println(float) -> void
         ; Make space for 1 arg(s)
         sub rsp, 8
         ; Arguments
         ; Eval arg0
         ; Method Call - Vector<:float:>::get(int) -> float
         ; Make space for 1 arg(s) and object parameter
         sub rsp, 16
         ; LHS
            ; Identifier - Vector<:float:> vals
               push qword [rbp - 400]
            pop rax ; object parameter
            mov qword [rsp + 0], rax ; place as first parameter
         ; RHS
         ; Arguments
            ; Eval arg0
               ; Int Literal
                  mov rax, 1
                  push rax
            ; Move arg0's result to reverse order position on stack
            pop rax
            mov qword [rsp + 8], rax
         call .__method____main__block__87____Vector__float____get__int
         ; Remove args
         add rsp, 16
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
;------------------------------------------------------------------------------------
         ; For-Loop
         ; Init
         ; Assignment - '='
         ; RHS
         ; Int Literal
         mov rax, 0
         push rax
         ; LHS
         ; Variable Declaration - i
         mov rax, qword [rbp - 408]  ; __main__block__87__for__113__i
         pop rdx ; rhs value
         mov qword [rbp - 408], rdx
         push rdx
         ; Loop init result can be discarded
         pop rax
         jmp .__forcond__113
.__for__113:
         ; Update
         ; Pre-Increment - int
         ; RHS
         ; Identifier - int i
            push qword [rbp - 408]
         pop rdx
         add qword [rbp - 408], 1
         mov rax, qword [rbp - 408]
         push rax ; push result
         ; Loop update result can be discarded
         pop rax
.__forcond__113:
         ; Condition
         ; Less Than
         ; LHS
         ; Identifier - int i
            push qword [rbp - 408]
         ; RHS
         ; Member Accessor
            ; LHS
               ; Identifier - Vector<:float:> vals
                  push qword [rbp - 400]
            ; RHS
               push qword [.__field____main__block__87____Vector__float____size] ; stored index associated with field that is being accessed
            pop rdx ; rhs
            pop rax ; lhs
            push qword [rax + 8*rdx] ; lhs.rhs
         pop rdx ; rhs
         pop rax ; lhs
         cmp rax, rdx
         setl al
         movzx eax, al
         push rax
         pop rax ; __cond
         cmp rax, 0 ; __cond
         je .__endfor__113
         ; Body
;------------------------------------------------------------------------------
         ; Code Block
         ; Function Call - print(float) -> void
         ; Make space for 1 arg(s)
         sub rsp, 8
         ; Arguments
            ; Eval arg0
               ; Method Call - Vector<:float:>::get(int) -> float
                  ; Make space for 1 arg(s) and object parameter
                  sub rsp, 16
                  ; LHS
                     ; Identifier - Vector<:float:> vals
                        push qword [rbp - 400]
                     pop rax ; object parameter
                     mov qword [rsp + 0], rax ; place as first parameter
                  ; RHS
                  ; Arguments
                     ; Eval arg0
                        ; Identifier - int i
                           push qword [rbp - 408]
                     ; Move arg0's result to reverse order position on stack
                     pop rax
                     mov qword [rsp + 8], rax
                  call .__method____main__block__87____Vector__float____get__int
                  ; Remove args
                  add rsp, 16
                  ; Push return value
                  movq rax, xmm0
                  push rax
            ; Move arg0's result to reverse order position on stack
            pop rax
            mov qword [rsp + 0], rax
         ; Call print(float)
         call print__float
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
                  ; " "
                  mov rax, .str185
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
;------------------------------------------------------------------------------
         ; Repeat
jmp .__for__113
         ; End of For
.__endfor__113:
;------------------------------------------------------------------------------------
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
;---------------------------------------------------------------------------------------
         ; Function Call - exit(int) -> void
         ; Make space for 1 arg(s)
         sub rsp, 8
         ; Arguments
         ; Eval arg0
         ; Int Literal
         mov rax, 0
         push rax
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
;---------------------------------------------------------------------------------------
         ; Code Block
         ; Function Call - print(char[]) -> void
         ; Make space for 1 arg(s)
         sub rsp, 8
         ; Arguments
         ; Eval arg0
         ; String Literal
         ; "Enter a phrase => "
         mov rax, .str186
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
         mov rax, qword [rbp - 416]  ; __main__block__115__line
         pop rdx ; rhs value
         mov qword [rbp - 416], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
         ; Function Call - print(char[]) -> void
         ; Make space for 1 arg(s)
         sub rsp, 8
         ; Arguments
         ; Eval arg0
         ; Identifier - char[] line
         push qword [rbp - 416]
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
         mov rax, .str187
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
         pop rdx ; rhs value
         mov qword [rbp - 416], rdx
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
            ; Identifier - char[] line
               push qword [rbp - 416]
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
         mov rax, qword [rbp - 424]  ; __main__block__115__x
         pop rdx ; rhs value
         mov qword [rbp - 424], rdx
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
         mov rax, .str188
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
            ; Identifier - int x
               push qword [rbp - 424]
         ; RHS
            ; Identifier - int x
               push qword [rbp - 424]
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
         mov rax, .str189
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
         pop rdx ; rhs value
         mov qword [rbp - 416], rdx
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
            ; Identifier - char[] line
               push qword [rbp - 416]
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
         mov rax, qword [rbp - 432]  ; __main__block__115__y
         pop rdx ; rhs value
         mov qword [rbp - 432], rdx
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
         mov rax, .str190
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
         ; Identifier - float y
         push qword [rbp - 432]
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
;---------------------------------------------------------------------------------------
         ; Function Call - exit(int) -> void
         ; Make space for 1 arg(s)
         sub rsp, 8
         ; Arguments
         ; Eval arg0
         ; Int Literal
         mov rax, 0
         push rax
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
; =======================================================================================
; ### END OF CODE #######################################################################
; =======================================================================================

         push 0
         call exit__int
; =======================================================================================
; ### DATA SECTION ######################################################################
; =======================================================================================

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
.str55: db '=', '=', '=', ' ', 'T', 'e', 's', 't', 'i', 'n', 'g', ' ', 'A', 's', 's', 'i', 'g', 'n', 'm', 'e', 'n', 't', ' ', 'A', 'r', 'i', 't', 'h', 'm', 'e', 't', 'i', 'c', ' ', '=', '=', '=', 0
.str56: db 'i', 'n', 't', ' ', 'x', ' ', '=', ' ', '2', '1', ';', ' ', '=', '>', ' ', 0
.str57: db 'f', 'l', 'o', 'a', 't', ' ', 'y', ' ', '=', ' ', '3', '.', '1', '4', ';', ' ', '=', '>', ' ', 0
.str58: db 'y', ' ', '=', ' ', '0', '.', '0', '0', '2', '1', ';', ' ', '=', '>', ' ', 0
.str59: db 'c', 'h', 'a', 'r', ' ', 'c', ' ', '=', ' ', 39, 'A', 39, ';', ' ', '=', '>', ' ', 0
.str60: db 'c', ' ', '=', ' ', 39, 'm', 39, ';', ' ', '=', '>', ' ', 0
.str61: db 'p', 'r', 'i', 'n', 't', '(', 'c', ' ', '=', ' ', 39, 'y', 39, ')', ' ', '=', '>', ' ', 0
.str62: db 'a', ' ', '=', ' ', '1', '6', ';', ' ', '+', '+', 'a', ' ', '=', '>', ' ', 0
.str63: db 'a', ' ', '=', '>', ' ', 0
.str64: db 'b', ' ', '=', ' ', '3', '.', '1', '4', ';', ' ', '+', '+', 'b', ' ', '=', '>', ' ', 0
.str65: db 'b', ' ', '=', '>', ' ', 0
.str66: db 'a', ' ', '=', ' ', '4', '2', ';', ' ', 'a', '+', '+', ' ', '=', '>', ' ', 0
.str67: db 'a', ' ', '=', '>', ' ', 0
.str68: db 'b', ' ', '=', ' ', '6', '.', '2', '8', ';', ' ', 'b', '+', '+', ' ', '=', '>', ' ', 0
.str69: db 'b', ' ', '=', '>', ' ', 0
.str70: db 'a', ' ', '=', ' ', '1', '6', ';', ' ', '-', '-', 'a', ' ', '=', '>', ' ', 0
.str71: db 'a', ' ', '=', '>', ' ', 0
.str72: db 'b', ' ', '=', ' ', '3', '.', '1', '4', ';', ' ', '-', '-', 'b', ' ', '=', '>', ' ', 0
.str73: db 'b', ' ', '=', '>', ' ', 0
.str74: db 'a', ' ', '=', ' ', '4', '2', ';', ' ', 'a', '-', '-', ' ', '=', '>', ' ', 0
.str75: db 'a', ' ', '=', '>', ' ', 0
.str76: db 'b', ' ', '=', ' ', '-', '6', '.', '2', '8', ';', ' ', 'b', '-', '-', ' ', '=', '>', ' ', 0
.str77: db 'b', ' ', '=', '>', ' ', 0
.str78: db 'a', ' ', '=', ' ', '3', '2', ';', ' ', 'a', ' ', '+', '=', ' ', '6', '3', ' ', '=', '>', ' ', 0
.str79: db 'b', ' ', '=', ' ', '3', '.', '1', '4', ';', ' ', 'b', ' ', '+', '=', ' ', '0', '.', '2', '5', ' ', '=', '>', ' ', 0
.str80: db 'a', ' ', '=', ' ', '3', '2', ';', ' ', 'a', ' ', '-', '=', ' ', '4', '7', ' ', '=', '>', ' ', 0
.str81: db 'b', ' ', '=', ' ', '-', '3', '.', '1', '4', ';', ' ', 'b', ' ', '-', '=', ' ', '1', '.', '2', '1', ' ', '=', '>', ' ', 0
.str82: db 'a', ' ', '=', ' ', '2', ';', ' ', 'a', ' ', '*', '=', ' ', '1', '6', ' ', '=', '>', ' ', 0
.str83: db 'b', ' ', '=', ' ', '0', '.', '5', ';', ' ', 'b', ' ', '*', '=', ' ', '5', '7', '.', '0', ' ', '=', '>', ' ', 0
.str84: db 'a', ' ', '=', ' ', '2', '5', '6', ';', ' ', 'a', ' ', '/', '=', ' ', '6', '4', ' ', '=', '>', ' ', 0
.str85: db 'a', ' ', '=', ' ', '2', '5', '6', ';', ' ', 'a', ' ', '/', '=', ' ', '6', '5', ' ', '=', '>', ' ', 0
.str86: db 'b', ' ', '=', ' ', '2', '5', '.', '0', ';', ' ', 'b', ' ', '/', '=', ' ', '3', '.', '0', ' ', '=', '>', ' ', 0
.str87: db 'b', ' ', '=', ' ', '0', '.', '4', '3', '5', ';', ' ', 'b', ' ', '/', '=', ' ', '4', '3', '5', '.', '0', ' ', '=', '>', ' ', 0
.str88: db 'a', ' ', '=', ' ', '2', '3', '5', '2', ';', ' ', 'a', ' ', '%', '=', ' ', '2', ' ', '=', '>', ' ', 0
.str89: db 'a', ' ', '=', ' ', '1', '3', '7', ';', ' ', 'a', ' ', '%', '=', ' ', '3', ' ', '=', '>', ' ', 0
.str90: db 'a', ' ', '=', ' ', '2', '3', '5', '3', ';', ' ', 'a', ' ', '%', '=', ' ', '5', ' ', '=', '>', ' ', 0
.str91: db 'a', ' ', '=', ' ', '-', '7', ';', ' ', 'a', ' ', '%', '=', ' ', '2', ' ', '=', '>', ' ', 0
.str92: db '=', '=', '=', ' ', 'T', 'e', 's', 't', 'i', 'n', 'g', ' ', 'E', 'q', 'u', 'a', 'l', 'i', 't', 'y', ' ', '=', '=', '=', 0
.str93: db '=', '=', '=', ' ', 'T', 'e', 's', 't', 'i', 'n', 'g', ' ', 'I', 'n', 'e', 'q', 'u', 'a', 'l', 'i', 't', 'y', ' ', '=', '=', '=', 0
.str94: db '=', '=', '=', ' ', 'T', 'e', 's', 't', 'i', 'n', 'g', ' ', 'A', 'r', 'r', 'a', 'y', 's', ' ', '=', '=', '=', 0
.str95: db 'i', 'n', 't', '[', ']', ' ', 'n', 'u', 'm', 's', ' ', '=', ' ', '[', '7', ',', ' ', '3', ',', ' ', '1', '9', ',', ' ', '-', '4', '2', ']', ';', 0
.str96: db 'f', 'l', 'o', 'a', 't', '[', ']', ' ', 'f', 'l', 'o', 'a', 't', 's', ' ', '=', ' ', '[', '3', '.', '1', '4', ',', ' ', '0', '.', '2', '5', ',', ' ', '2', '.', '0', ',', ' ', '6', '.', '2', '8', ']', ';', 0
.str97: db 'c', 'h', 'a', 'r', '[', ']', ' ', 's', 't', 'r', ' ', '=', ' ', '[', 39, 'H', 39, ',', ' ', 39, 'e', 39, ',', ' ', 39, 'l', 39, ',', ' ', 39, 'l', 39, ',', ' ', 39, 'o', 39, ']', ';', 0
.str98: db 'i', 'n', 't', '[', ']', ' ', 'i', 'n', 't', 's', ' ', '=', ' ', 'n', 'e', 'w', ' ', 'i', 'n', 't', '[', '3', ']', ';', 0
.str99: db 'n', 'u', 'm', 's', '[', '0', ']', ' ', '=', '>', ' ', 0
.str100: db 'n', 'u', 'm', 's', '[', '1', ']', ' ', '=', '>', ' ', 0
.str101: db 'n', 'u', 'm', 's', '[', '2', ']', ' ', '=', '>', ' ', 0
.str102: db 'n', 'u', 'm', 's', '[', '3', ']', ' ', '=', '>', ' ', 0
.str103: db 'f', 'l', 'o', 'a', 't', 's', '[', '0', ']', ' ', '=', '>', ' ', 0
.str104: db 'f', 'l', 'o', 'a', 't', 's', '[', '1', ']', ' ', '=', '>', ' ', 0
.str105: db 'f', 'l', 'o', 'a', 't', 's', '[', '2', ']', ' ', '=', '>', ' ', 0
.str106: db 'f', 'l', 'o', 'a', 't', 's', '[', '3', ']', ' ', '=', '>', ' ', 0
.str107: db 's', 't', 'r', '[', '0', ']', ' ', '=', '>', ' ', 0
.str108: db 's', 't', 'r', '[', '1', ']', ' ', '=', '>', ' ', 0
.str109: db 's', 't', 'r', '[', '2', ']', ' ', '=', '>', ' ', 0
.str110: db 's', 't', 'r', '[', '3', ']', ' ', '=', '>', ' ', 0
.str111: db 's', 't', 'r', '[', '4', ']', ' ', '=', '>', ' ', 0
.str112: db 'p', 'r', 'i', 'n', 't', 'l', 'n', ' ', '(', 's', 't', 'r', ')', ';', ' ', '=', '>', ' ', 0
.str113: db 'i', 'n', 't', 's', '[', '0', ']', ' ', '=', '>', ' ', 0
.str114: db 'i', 'n', 't', 's', '[', '1', ']', ' ', '=', '>', ' ', 0
.str115: db 'i', 'n', 't', 's', '[', '2', ']', ' ', '=', '>', ' ', 0
.str116: db 'n', 'u', 'm', 's', '[', '2', ']', ' ', '=', ' ', '-', '1', '7', ';', ' ', '=', '>', ' ', 0
.str117: db 'n', 'u', 'm', 's', '[', '2', ']', ' ', '=', '>', ' ', 0
.str118: db 'f', 'l', 'o', 'a', 't', 's', '[', '1', ']', ' ', '=', ' ', '1', '2', '3', '.', '4', '5', '6', ';', ' ', '=', '>', ' ', 0
.str119: db 'f', 'l', 'o', 'a', 't', 's', '[', '1', ']', ' ', '=', '>', ' ', 0
.str120: db 's', 't', 'r', '[', '0', ']', ' ', '=', ' ', 39, 'A', 39, ' ', '=', '>', ' ', 0
.str121: db 's', 't', 'r', '[', '0', ']', ' ', '=', '>', ' ', 0
.str122: db 's', 't', 'r', '[', '1', ']', ' ', '=', ' ', 39, 'm', 39, ' ', '=', '>', ' ', 0
.str123: db 's', 't', 'r', '[', '1', ']', ' ', '=', '>', ' ', 0
.str124: db 's', 't', 'r', '[', '2', ']', ' ', '=', ' ', 39, 'y', 39, ' ', '=', '>', ' ', 0
.str125: db 's', 't', 'r', '[', '2', ']', ' ', '=', '>', ' ', 0
.str126: db 's', 't', 'r', '[', '3', ']', ' ', '=', ' ', 39, 92, '0', 39, ' ', '=', '>', ' ', 0
.str127: db 's', 't', 'r', '[', '3', ']', ' ', '=', '>', ' ', 0
.str128: db 's', 't', 'r', '[', '4', ']', ' ', '=', '>', ' ', 0
.str129: db 'p', 'r', 'i', 'n', 't', 'l', 'n', ' ', '(', 's', 't', 'r', ')', ';', ' ', '=', '>', ' ', 0
.str130: db 'i', 'n', 't', 's', '[', '0', ']', ' ', '=', ' ', 'n', 'u', 'm', 's', '[', '0', ']', ' ', '=', '>', ' ', 0
.str131: db 'i', 'n', 't', 's', '[', '1', ']', ' ', '=', ' ', 'n', 'u', 'm', 's', '[', '1', ']', ' ', '=', '>', ' ', 0
.str132: db 'i', 'n', 't', 's', '[', '2', ']', ' ', '=', ' ', 'n', 'u', 'm', 's', '[', '2', ']', ' ', '=', '>', ' ', 0
.str133: db '=', '=', '=', ' ', 'T', 'e', 's', 't', 'i', 'n', 'g', ' ', 'A', 'r', 'r', 'a', 'y', ' ', 'C', 'o', 'n', 't', ' ', '=', '=', '=', 0
.str134: db ',', ' ', 0
.str135: db ',', ' ', 0
.str136: db ',', ' ', 0
.str137: db 'H', 'e', 'l', 'l', 'o', ',', ' ', 'w', 'o', 'r', 'l', 'd', '!', 0
.str138: db 'a', ' ', '=', ' ', 0
.str139: db 'b', ' ', '=', ' ', 0
.str140: db 'c', ' ', '=', ' ', 0
.str141: db 'c', ' ', '=', ' ', 'a', ' ', '+', ' ', 'b', 0
.str142: db 'c', ' ', '=', ' ', 0
.str143: db '=', '=', '=', ' ', 'T', 'e', 's', 't', 'i', 'n', 'g', ' ', 'M', 'u', 'l', 't', 'i', 'd', 'i', 'm', 'e', 'n', 's', 'i', 'o', 'n', 'a', 'l', ' ', 'A', 'r', 'r', 'a', 'y', 's', ' ', '=', '=', '=', 0
.str144: db 'A', ' ', '=', ' ', 0
.str145: db 'B', ' ', '=', ' ', 0
.str146: db 'C', ' ', '=', ' ', 0
.str147: db 'C', ' ', '=', ' ', 'A', ' ', '(', 'd', 'o', 't', ')', ' ', 'B', 0
.str148: db 'C', ' ', '=', ' ', 0
.str149: db 'D', ' ', '=', ' ', 'A', ' ', '+', ' ', 'B', 0
.str150: db 'D', ' ', '=', ' ', 0
.str151: db '=', '=', '=', ' ', 'T', 'e', 's', 't', 'i', 'n', 'g', ' ', 'C', 'l', 'a', 's', 's', 'e', 's', ' ', '=', '=', '=', 0
.str152: db 'v', '.', 'x', ' ', '=', ' ', 0
.str153: db 'v', '.', 'y', ' ', '=', ' ', 0
.str154: db 'v', '.', 's', 'e', 't', ' ', '(', '4', '2', '.', '0', ',', ' ', '0', '.', '0', '0', '4', '3', ')', ';', 0
.str155: db 'v', '.', 'x', ' ', '=', ' ', 0
.str156: db 'v', '.', 'y', ' ', '=', ' ', 0
.str157: db 'v', '2', '.', 'x', ' ', '=', ' ', 0
.str158: db 'v', '2', '.', 'y', ' ', '=', ' ', 0
.str159: db 'v', '2', '.', 's', 'e', 't', ' ', '(', 'v', ')', ';', 0
.str160: db 'v', '2', '.', 'x', ' ', '=', ' ', 0
.str161: db 'v', '2', '.', 'y', ' ', '=', ' ', 0
.str162: db 'v', '2', '.', 'a', 'd', 'd', ' ', '(', 'v', ')', ';', 0
.str163: db 'v', '2', '.', 'x', ' ', '=', ' ', 0
.str164: db 'v', '2', '.', 'y', ' ', '=', ' ', 0
.str165: db 'v', '2', '.', 'a', 'd', 'd', ' ', '(', 'v', ')', ';', 0
.str166: db 'v', '2', '.', 'x', ' ', '=', ' ', 0
.str167: db 'v', '2', '.', 'y', ' ', '=', ' ', 0
.str168: db 'v', '2', '.', 'a', 'd', 'd', ' ', '(', 'v', ')', ';', 0
.str169: db 'v', '2', '.', 'x', ' ', '=', ' ', 0
.str170: db 'v', '2', '.', 'y', ' ', '=', ' ', 0
.str171: db ',', ' ', 0
.str172: db ',', ' ', 0
.str173: db ',', ' ', 0
.str174: db ',', ' ', 0
.str175: db 'V', 'e', 'c', 't', 'o', 'r', '3', 'D', ' ', 'v', '3', ' ', '=', ' ', 'n', 'e', 'w', ' ', 'V', 'e', 'c', 't', 'o', 'r', '3', 'D', ' ', '(', '1', '.', '0', ',', ' ', '2', '.', '0', ',', ' ', '3', '.', '0', ')', ';', 0
.str176: db 'V', 'e', 'c', 't', 'o', 'r', '3', 'D', ' ', 'v', '4', ' ', '=', ' ', 'n', 'e', 'w', ' ', 'V', 'e', 'c', 't', 'o', 'r', '3', 'D', ' ', '(', '5', '.', '5', ',', ' ', '6', '.', '2', '5', ',', ' ', '7', '.', '7', '5', ')', ';', 0
.str177: db 'v', '3', '.', 's', 'e', 't', ' ', '(', 'v', '2', ')', ';', ' ', '/', '/', ' ', 'i', 'n', 'h', 'e', 'r', 'i', 't', 'e', 'd', ' ', 'f', 'r', 'o', 'm', ' ', 'V', 'e', 'c', 't', 'o', 'r', '2', 'D', 0
.str178: db 'v', '3', '.', 's', 'e', 't', ' ', '(', '0', '.', '0', ',', ' ', '0', '.', '0', ',', ' ', '0', '.', '0', ')', ';', 0
.str179: db 'v', '3', '.', 's', 'e', 't', ' ', '(', 'v', '4', ')', ';', 0
.str180: db '=', '=', '=', ' ', 'T', 'e', 's', 't', 'i', 'n', 'g', ' ', 'A', 'r', 'r', 'a', 'y', 'L', 'i', 's', 't', ' ', '=', '=', '=', 0
.str181: db '<', 'O', 'b', 'j', 'e', 'c', 't', '>', 0
.str182: db '<', 'V', 'e', 'c', 't', 'o', 'r', '>', 0
.str183: db ' ', 0
.str184: db '<', 'V', 'e', 'c', 't', 'o', 'r', '>', 0
.str185: db ' ', 0
.str186: db 'E', 'n', 't', 'e', 'r', ' ', 'a', ' ', 'p', 'h', 'r', 'a', 's', 'e', ' ', '=', '>', ' ', 0
.str187: db 'E', 'n', 't', 'e', 'r', ' ', 'i', 'n', 't', 'e', 'g', 'e', 'r', ' ', '=', '=', '>', ' ', 0
.str188: db 'x', ' ', '*', ' ', 'x', ' ', '=', '>', ' ', 0
.str189: db 'E', 'n', 't', 'e', 'r', ' ', 'f', 'l', 'o', 'a', 't', ' ', '=', '=', '>', ' ', 0
.str190: db 'y', ' ', '=', '>', ' ', 0
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
.float16: dq 3.14
.float17: dq 0.0021
.float18: dq 3.14
.float19: dq 6.28
.float20: dq 3.14
.float21: dq -6.28
.float22: dq 3.14
.float23: dq 0.25
.float24: dq -3.14
.float25: dq 1.21
.float26: dq 0.5
.float27: dq 57.0
.float28: dq 25.0
.float29: dq 3.0
.float30: dq 0.435
.float31: dq 435.0
.float32: dq 3.14
.float33: dq 0.25
.float34: dq 2.0
.float35: dq 6.28
.float36: dq 123.456
.float37: dq 3.25
.float38: dq 1.0
.float39: dq 0.0
.float40: dq 0.0
.float41: dq 0.0
.float42: dq 1.0
.float43: dq 0.0
.float44: dq 0.0
.float45: dq 0.0
.float46: dq 1.0
.float47: dq 0.5
.float48: dq 3.1415
.float49: dq 42.0
.float50: dq 0.0043
.float51: dq 0.5
.float52: dq 3.1415
.float53: dq 1.0
.float54: dq 2.0
.float55: dq 3.0
.float56: dq 5.5
.float57: dq 6.25
.float58: dq 7.75
.float59: dq 0.0
.float60: dq 0.0
.float61: dq 0.0
.float62: dq 42.0
.float63: dq 12345.6789
.floatNegOne: dq -1.0
.floatZero: dq 0.0
.floatOne: dq 1.0
