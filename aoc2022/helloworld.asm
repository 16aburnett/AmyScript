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
         sub rsp, 208
         ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
         ; [rbp - 8] - char[] line (<unset-scope-name>)
         ; [rbp - 16] - int total (<unset-scope-name>)
         ; [rbp - 24] - Vector<:char[]:> lines (<unset-scope-name>)
         ; [rbp - 32] - int l (<unset-scope-name>)
         ; [rbp - 40] - char[] line (<unset-scope-name>)
         ; [rbp - 48] - int indexcomma (<unset-scope-name>)
         ; [rbp - 56] - int indexdash0 (<unset-scope-name>)
         ; [rbp - 64] - int indexdash1 (<unset-scope-name>)
         ; [rbp - 72] - int i (<unset-scope-name>)
         ; [rbp - 80] - int begin (<unset-scope-name>)
         ; [rbp - 88] - int end (<unset-scope-name>)
         ; [rbp - 96] - int iter (<unset-scope-name>)
         ; [rbp - 104] - char[] a_ (<unset-scope-name>)
         ; [rbp - 112] - int i (<unset-scope-name>)
         ; [rbp - 120] - char[] b_ (<unset-scope-name>)
         ; [rbp - 128] - int i (<unset-scope-name>)
         ; [rbp - 136] - char[] c_ (<unset-scope-name>)
         ; [rbp - 144] - int i (<unset-scope-name>)
         ; [rbp - 152] - char[] d_ (<unset-scope-name>)
         ; [rbp - 160] - int i (<unset-scope-name>)
         ; [rbp - 168] - int begin0 (<unset-scope-name>)
         ; [rbp - 176] - int end0 (<unset-scope-name>)
         ; [rbp - 184] - int begin1 (<unset-scope-name>)
         ; [rbp - 192] - int end1 (<unset-scope-name>)
         ; [rbp - 200] - int isAInB (<unset-scope-name>)
         ; [rbp - 208] - int isBInA (<unset-scope-name>)

         ; Body
; ========================================================================
         ; Class Template - 
            ; Instances:
      ; ==================================================================
               ; Class Declaration - __main____Vector__char__1 inherits __main__Object
                  ; Class data
                  section .data
                     ; Dispatch Table - this might need to be a malloc**
                     .__dtable____main____Vector__char__1:
                     ; Dispatch Table Entries
                     dq .__method____main____Vector__char__1____pushBack__char__1 ; 0
                     dq .__method____main____Vector__char__1____popBack ; 1
                     dq .__method____main____Vector__char__1____get__int ; 2
                     dq .__method____main____Vector__char__1____set__int__char__1 ; 3
                  section .text
         ;---------------------------------------------------------------
                  ; Field - char[][] Vector<:char[]:>::data
                  section .data
                  .__field____main____Vector__char__1____data: dq 1
                  section .text
         ;---------------------------------------------------------------
         ;---------------------------------------------------------------
                  ; Field - int Vector<:char[]:>::size
                  section .data
                  .__field____main____Vector__char__1____size: dq 2
                  section .text
         ;---------------------------------------------------------------
         ;---------------------------------------------------------------
                  ; Field - int Vector<:char[]:>::capacity
                  section .data
                  .__field____main____Vector__char__1____capacity: dq 3
                  section .text
         ;---------------------------------------------------------------
               ; skip over class methods
               jmp .__endclass____main____Vector__char__1
         ;---------------------------------------------------------------
                  ; Constructor Declaration - Vector<:char[]:>::Vector() -> Vector<:char[]:>
                  jmp .__end__ctor____main____Vector__char__1____Vector
                  .__ctor____main____Vector__char__1____Vector:
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
                        mov qword [rax + 0], .__dtable____main____Vector__char__1 ; this[0] = &dtable
                     ; Parameters
                  ; Body
            ;------------------------------------------------------------
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
                                    push qword [.__field____main____Vector__char__1____capacity] ; 
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
                                    push qword [.__field____main____Vector__char__1____size] ; 
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
                                       push qword [.__field____main____Vector__char__1____capacity] ; stored index associated with field that is being accessed
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
                                    push qword [.__field____main____Vector__char__1____data] ; 
                                 pop rdi ; rhs
                                 pop rbx ; lhs
                           pop rdx ; rhs value
                           mov qword [rbx + 8*rdi], rdx
                           push rdx
                        ; Statement results can be ignored
                        pop rdx
            ;------------------------------------------------------------
                  mov rax, qword [rbp - 8] ; __this
                  ; Function Epilogue
                  mov rsp, rbp ; remove local vars + unpopped pushes
                  pop rbp
                  ret
               .__end__ctor____main____Vector__char__1____Vector:
               ; End Constructor Declaration - __ctor____main____Vector__char__1____Vector
      ;------------------------------------------------------------------

      ;------------------------------------------------------------------
               ; Method Declaration - Vector<:char[]:>::pushBack(char[]) -> void
               jmp .__end__method____main____Vector__char__1____pushBack__char__1
               .__method____main____Vector__char__1____pushBack__char__1:
                  ; Function Header:
                  ; Setup stack frame
                     push rbp
                     mov rbp, rsp
                     ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
                        sub rsp, 32 ; space for local variables (16-byte aligned)
                        ; [rbp - 8] - this - Reference to 'this' object instance
                        mov rdx, qword [rbp + 16] ; param passed 'this'
                        mov qword [rbp - 8], rdx ; save this to a local
                        ; [rbp - 16] - char[][] nData (<unset-scope-name>)
                        ; [rbp - 24] - int i (<unset-scope-name>)
                  ; Parameters
                     ; Param: val [rbp + 24] (__main____Vector__char__1__pushBack__val)
                  ; Body
            ;------------------------------------------------------------
                     ; Code Block
               ;---------------------------------------------------------
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
                                                push qword [.__field____main____Vector__char__1____size] ; stored index associated with field that is being accessed
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
                                          push qword [.__field____main____Vector__char__1____capacity] ; stored index associated with field that is being accessed
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
                              je .__endif__2 ; jump to end
                           ; Body
                     ;---------------------------------------------------
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
                                                   push qword [.__field____main____Vector__char__1____capacity] ; stored index associated with field that is being accessed
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
                                             push qword [.__field____main____Vector__char__1____capacity] ; 
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
                                                push qword [.__field____main____Vector__char__1____capacity] ; stored index associated with field that is being accessed
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
                                          mov rax, qword [rbp - 16]  ; __main____Vector__char__1__pushBack__block__1__if__2__block__3__nData
                                    pop rdx ; rhs value
                                    mov qword [rbp - 16], rdx
                                    push rdx
                                 ; Statement results can be ignored
                                 pop rdx
                        ;------------------------------------------------
                                 ; For-Loop
                                 ; Init
                                    ; Assignment - '='
                                       ; RHS
                                          ; Int Literal
                                             mov rax, 0
                                             push rax
                                       ; LHS
                                          ; Variable Declaration - i
                                             mov rax, qword [rbp - 24]  ; __main____Vector__char__1__pushBack__block__1__if__2__block__3__for__4__i
                                       pop rdx ; rhs value
                                       mov qword [rbp - 24], rdx
                                       push rdx
                                    ; Loop init result can be discarded
                                    pop rax
                                 jmp .__forcond__4
.__for__4:
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
.__forcond__4:
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
                                                   push qword [.__field____main____Vector__char__1____size] ; stored index associated with field that is being accessed
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
                                       je .__endfor__4
                                    ; Body
                              ;------------------------------------------
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
                                                            push qword [.__field____main____Vector__char__1____data] ; stored index associated with field that is being accessed
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
                                                      ; Identifier - char[][] nData
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
                              ;------------------------------------------
                                    ; Repeat
jmp .__for__4
                                    ; End of For
.__endfor__4:
                        ;------------------------------------------------
                                 ; Free Operator
                                    ; RHS
                                       ; Member Accessor
                                          ; LHS
                                             ; This keyword
                                                push qword [rbp - 8] ; __this
                                          ; RHS
                                             push qword [.__field____main____Vector__char__1____data] ; stored index associated with field that is being accessed
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
                                       ; Identifier - char[][] nData
                                          push qword [rbp - 16]
                                    ; LHS
                                       ; Member Accessor Assignment
                                          ; LHS
                                             ; This keyword
                                                push qword [rbp - 8] ; __this
                                          ; RHS
                                             push qword [.__field____main____Vector__char__1____data] ; 
                                          pop rdi ; rhs
                                          pop rbx ; lhs
                                    pop rdx ; rhs value
                                    mov qword [rbx + 8*rdi], rdx
                                    push rdx
                                 ; Statement results can be ignored
                                 pop rdx
                     ;---------------------------------------------------
                           jmp .__endif__2 ; jump to end of condition chain
                           ; End of if
.__endif__2:
               ;---------------------------------------------------------
                        ; Assignment - '='
                           ; RHS
                              ; Identifier - char[] val
                                 push qword [rbp - -24]
                           ; LHS
                              ; Subscript assignment
                                 ; LHS
                                    ; Member Accessor
                                       ; LHS
                                          ; This keyword
                                             push qword [rbp - 8] ; __this
                                       ; RHS
                                          push qword [.__field____main____Vector__char__1____data] ; stored index associated with field that is being accessed
                                       pop rdx ; rhs
                                       pop rax ; lhs
                                       push qword [rax + 8*rdx] ; lhs.rhs
                                 ; OFFSET
                                    ; Member Accessor
                                       ; LHS
                                          ; This keyword
                                             push qword [rbp - 8] ; __this
                                       ; RHS
                                          push qword [.__field____main____Vector__char__1____size] ; stored index associated with field that is being accessed
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
                                    push qword [.__field____main____Vector__char__1____size] ; stored index associated with field that is being accessed
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
                                    push qword [.__field____main____Vector__char__1____size] ; size
                                 pop rdi ; rhs
                                 pop rbx ; lhs
                                 mov rax, qword [rbx + 8*rdi]
                                 add rax, 1
                                 mov qword [rbx + 8*rdi], rax
                           push rax ; push result
                        ; Statement results can be ignored
                        pop rdx
            ;------------------------------------------------------------
                  ; Function Epilogue
                  mov rsp, rbp ; remove local vars + unpopped pushes
                  pop rbp
                  ret
               .__end__method____main____Vector__char__1____pushBack__char__1:
               ; End Method Declaration - .__method____main____Vector__char__1____pushBack__char__1
      ;------------------------------------------------------------------

      ;------------------------------------------------------------------
               ; Method Declaration - Vector<:char[]:>::popBack() -> char[]
               jmp .__end__method____main____Vector__char__1____popBack
               .__method____main____Vector__char__1____popBack:
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
            ;------------------------------------------------------------
                     ; Code Block
                        ; Return
                           ; Subscript
                              ; LHS
                                 ; Member Accessor
                                    ; LHS
                                       ; This keyword
                                          push qword [rbp - 8] ; __this
                                    ; RHS
                                       push qword [.__field____main____Vector__char__1____data] ; stored index associated with field that is being accessed
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
                                             push qword [.__field____main____Vector__char__1____size] ; stored index associated with field that is being accessed
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
                                             push qword [.__field____main____Vector__char__1____size] ; size
                                          pop rdi ; rhs
                                          pop rbx ; lhs
                                          mov rax, qword [rbx + 8*rdi]
                                          sub rax, 1
                                          mov qword [rbx + 8*rdi], rax
                                    push rax ; push result
                              pop rdx ; __offset
                              pop rax ; __pointer
                              push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                           pop rax ; return value (char[])
                           ; Clean up stack and return
                           mov rsp, rbp ; remove local vars + unpopped pushes
                           pop rbp
                           ret
            ;------------------------------------------------------------
                  ; Function Epilogue
                  mov rsp, rbp ; remove local vars + unpopped pushes
                  pop rbp
                  ret
               .__end__method____main____Vector__char__1____popBack:
               ; End Method Declaration - .__method____main____Vector__char__1____popBack
      ;------------------------------------------------------------------

      ;------------------------------------------------------------------
               ; Method Declaration - Vector<:char[]:>::get(int) -> char[]
               jmp .__end__method____main____Vector__char__1____get__int
               .__method____main____Vector__char__1____get__int:
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
                     ; Param: index [rbp + 24] (__main____Vector__char__1__get__index)
                  ; Body
            ;------------------------------------------------------------
                     ; Code Block
                        ; Return
                           ; Subscript
                              ; LHS
                                 ; Member Accessor
                                    ; LHS
                                       ; This keyword
                                          push qword [rbp - 8] ; __this
                                    ; RHS
                                       push qword [.__field____main____Vector__char__1____data] ; stored index associated with field that is being accessed
                                    pop rdx ; rhs
                                    pop rax ; lhs
                                    push qword [rax + 8*rdx] ; lhs.rhs
                              ; OFFSET
                                 ; Identifier - int index
                                    push qword [rbp - -24]
                              pop rdx ; __offset
                              pop rax ; __pointer
                              push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                           pop rax ; return value (char[])
                           ; Clean up stack and return
                           mov rsp, rbp ; remove local vars + unpopped pushes
                           pop rbp
                           ret
            ;------------------------------------------------------------
                  ; Function Epilogue
                  mov rsp, rbp ; remove local vars + unpopped pushes
                  pop rbp
                  ret
               .__end__method____main____Vector__char__1____get__int:
               ; End Method Declaration - .__method____main____Vector__char__1____get__int
      ;------------------------------------------------------------------

      ;------------------------------------------------------------------
               ; Method Declaration - Vector<:char[]:>::set(int, char[]) -> void
               jmp .__end__method____main____Vector__char__1____set__int__char__1
               .__method____main____Vector__char__1____set__int__char__1:
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
                     ; Param: index [rbp + 24] (__main____Vector__char__1__set__index)
                     ; Param: value [rbp + 32] (__main____Vector__char__1__set__value)
                  ; Body
            ;------------------------------------------------------------
                     ; Code Block
                        ; Assignment - '='
                           ; RHS
                              ; Identifier - char[] value
                                 push qword [rbp - -32]
                           ; LHS
                              ; Subscript assignment
                                 ; LHS
                                    ; Member Accessor
                                       ; LHS
                                          ; This keyword
                                             push qword [rbp - 8] ; __this
                                       ; RHS
                                          push qword [.__field____main____Vector__char__1____data] ; stored index associated with field that is being accessed
                                       pop rdx ; rhs
                                       pop rax ; lhs
                                       push qword [rax + 8*rdx] ; lhs.rhs
                                 ; OFFSET
                                    ; Identifier - int index
                                       push qword [rbp - -24]
                                 pop rdi ; __offset
                                 pop rbx ; __pointer
                           pop rdx ; rhs value
                           mov qword [rbx + 8*rdi], rdx
                           push rdx
                        ; Statement results can be ignored
                        pop rdx
            ;------------------------------------------------------------
                  ; Function Epilogue
                  mov rsp, rbp ; remove local vars + unpopped pushes
                  pop rbp
                  ret
               .__end__method____main____Vector__char__1____set__int__char__1:
               ; End Method Declaration - .__method____main____Vector__char__1____set__int__char__1
      ;------------------------------------------------------------------

.__endclass____main____Vector__char__1:
            ; End Class Declaration - __main____Vector__char__1
   ; =====================================================================

         ; End Class Template - 
; ===========================================================================

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
            ; Int Literal
               mov rax, 0
               push rax
         ; LHS
            ; Variable Declaration - total
               mov rax, qword [rbp - 16]  ; __main__total
         pop rdx ; rhs value
         mov qword [rbp - 16], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
         ; RHS
            ; Constructor Call - Vector<:char[]:>::Vector() -> Vector<:char[]:>
               ; Make space for 0 arg(s)
               sub rsp, 0
               ; Arguments
               ; Call Vector<:char[]:>::Vector()
               call .__ctor____main____Vector__char__1____Vector
               ; Remove args
               add rsp, 0
               ; Push return value
               push rax
         ; LHS
            ; Variable Declaration - lines
               mov rax, qword [rbp - 24]  ; __main__lines
         pop rdx ; rhs value
         mov qword [rbp - 24], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
;---------------------------------------------------------------------------
         ; While-Loop
.__while__9:
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
            je .__endwhile__9
         ; Body
   ;---------------------------------------------------------------------
            ; Code Block
               ; Method Call - Vector<:char[]:>::pushBack(char[]) -> void
                  ; Make space for 1 arg(s) and object parameter
                  sub rsp, 16
                  ; LHS
                     ; Identifier - Vector<:char[]:> lines
                        push qword [rbp - 24]
                     pop rax ; object parameter
                     mov qword [rsp + 0], rax ; place as first parameter
                  ; RHS
                  ; Arguments
                     ; Eval arg0
                        ; Identifier - char[] line
                           push qword [rbp - 8]
                     ; Move arg0's result to reverse order position on stack
                     pop rax
                     mov qword [rsp + 8], rax
                  call .__method____main____Vector__char__1____pushBack__char__1
                  ; Remove args
                  add rsp, 16
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
                  mov qword [rbp - 8], rdx
                  push rdx
               ; Statement results can be ignored
               pop rdx
   ;---------------------------------------------------------------------
         jmp .__while__9
         ; End of While
.__endwhile__9:
;---------------------------------------------------------------------------
;---------------------------------------------------------------------------
         ; For-Loop
         ; Init
         ; Assignment - '='
            ; RHS
               ; Int Literal
                  mov rax, 0
                  push rax
            ; LHS
               ; Variable Declaration - l
                  mov rax, qword [rbp - 32]  ; __main__for__11__l
            pop rdx ; rhs value
            mov qword [rbp - 32], rdx
            push rdx
         ; Loop init result can be discarded
         pop rax
         jmp .__forcond__11
.__for__11:
         ; Update
            ; Pre-Increment - int
               ; RHS
                  ; Identifier - int l
                     push qword [rbp - 32]
               pop rdx
               add qword [rbp - 32], 1
               mov rax, qword [rbp - 32]
               push rax ; push result
            ; Loop update result can be discarded
            pop rax
.__forcond__11:
         ; Condition
            ; Less Than
               ; LHS
                  ; Identifier - int l
                     push qword [rbp - 32]
               ; RHS
                  ; Member Accessor
                     ; LHS
                        ; Identifier - Vector<:char[]:> lines
                           push qword [rbp - 24]
                     ; RHS
                        push qword [.__field____main____Vector__char__1____size] ; stored index associated with field that is being accessed
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
            je .__endfor__11
         ; Body
   ;---------------------------------------------------------------------
            ; Code Block
               ; Assignment - '='
                  ; RHS
                     ; Subscript
                        ; LHS
                           ; Member Accessor
                              ; LHS
                                 ; Identifier - Vector<:char[]:> lines
                                    push qword [rbp - 24]
                              ; RHS
                                 push qword [.__field____main____Vector__char__1____data] ; stored index associated with field that is being accessed
                              pop rdx ; rhs
                              pop rax ; lhs
                              push qword [rax + 8*rdx] ; lhs.rhs
                        ; OFFSET
                           ; Identifier - int l
                              push qword [rbp - 32]
                        pop rdx ; __offset
                        pop rax ; __pointer
                        push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                  ; LHS
                     ; Variable Declaration - line
                        mov rax, qword [rbp - 40]  ; __main__for__11__block__12__line
                  pop rdx ; rhs value
                  mov qword [rbp - 40], rdx
                  push rdx
               ; Statement results can be ignored
               pop rdx
               ; Assignment - '='
                  ; RHS
                     ; Int Literal
                        mov rax, 0
                        push rax
                  ; LHS
                     ; Variable Declaration - indexcomma
                        mov rax, qword [rbp - 48]  ; __main__for__11__block__12__indexcomma
                  pop rdx ; rhs value
                  mov qword [rbp - 48], rdx
                  push rdx
               ; Statement results can be ignored
               pop rdx
               ; Assignment - '='
                  ; RHS
                     ; Int Literal
                        mov rax, 0
                        push rax
                  ; LHS
                     ; Variable Declaration - indexdash0
                        mov rax, qword [rbp - 56]  ; __main__for__11__block__12__indexdash0
                  pop rdx ; rhs value
                  mov qword [rbp - 56], rdx
                  push rdx
               ; Statement results can be ignored
               pop rdx
               ; Assignment - '='
                  ; RHS
                     ; Int Literal
                        mov rax, 0
                        push rax
                  ; LHS
                     ; Variable Declaration - indexdash1
                        mov rax, qword [rbp - 64]  ; __main__for__11__block__12__indexdash1
                  pop rdx ; rhs value
                  mov qword [rbp - 64], rdx
                  push rdx
               ; Statement results can be ignored
               pop rdx
      ;------------------------------------------------------------------
               ; For-Loop
               ; Init
                  ; Assignment - '='
                     ; RHS
                        ; Int Literal
                           mov rax, 0
                           push rax
                     ; LHS
                        ; Variable Declaration - i
                           mov rax, qword [rbp - 72]  ; __main__for__11__block__12__for__13__i
                     pop rdx ; rhs value
                     mov qword [rbp - 72], rdx
                     push rdx
                  ; Loop init result can be discarded
                  pop rax
               jmp .__forcond__13
.__for__13:
                  ; Update
                     ; Pre-Increment - int
                        ; RHS
                           ; Identifier - int i
                              push qword [rbp - 72]
                        pop rdx
                        add qword [rbp - 72], 1
                        mov rax, qword [rbp - 72]
                        push rax ; push result
                     ; Loop update result can be discarded
                     pop rax
.__forcond__13:
                  ; Condition
                     ; Less Than
                        ; LHS
                           ; Identifier - int i
                              push qword [rbp - 72]
                        ; RHS
                           ; Sizeof Operator
                              ; RHS
                                 ; Identifier - char[] line
                                    push qword [rbp - 40]
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
               ;---------------------------------------------------------
                        ; Code Block
                  ;------------------------------------------------------
                           ; If-Statement
                              ; Condition
                                 ; AND
                                    ; Eval LHS
                                       ; Equal
                                          ; LHS
                                             ; Subscript
                                                ; LHS
                                                   ; Identifier - char[] line
                                                      push qword [rbp - 40]
                                                ; OFFSET
                                                   ; Identifier - int i
                                                      push qword [rbp - 72]
                                                pop rdx ; __offset
                                                pop rax ; __pointer
                                                push qword [rax + rdx] ; pointer + sizeof(data_t) * offset
                                          ; RHS
                                             ; Char Literal
                                                push '-'
                                          pop rdx ; rhs
                                          pop rax ; lhs
                                          cmp rax, rdx
                                          sete al
                                          movzx eax, al
                                          push rax
                                    ; Check if we need to short-circuit
                                       pop rax ; __lhs
                                       test rax, rax
                                       je .AND_SHORT_CIRCUIT16
                                    ; Eval RHS
                                       ; Equal
                                          ; LHS
                                             ; Identifier - int indexcomma
                                                push qword [rbp - 48]
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
                                    ; Check RHS
                                       pop rax ; __rhs
                                       test rax, rax
                                       je .AND_SHORT_CIRCUIT16
                                    ; Success state
                                    mov rax, 1 ; result = True
                                    jmp .AND_END16
.AND_SHORT_CIRCUIT16:
                                    mov rax, 0 ; result = False
.AND_END16:
                                    movzx eax, al
                                    push rax ; result
                                 pop rdx ; __cond
                                 cmp rdx, 0 ; ensure condition is true
                                 je .__elif__15x0 ; jump to first elif
                              ; Body
                                 ; Assignment - '='
                                    ; RHS
                                       ; Identifier - int i
                                          push qword [rbp - 72]
                                    pop rdx ; rhs value
                                    mov qword [rbp - 56], rdx
                                    push rdx
                                 ; Statement results can be ignored
                                 pop rdx
                              jmp .__endif__15 ; jump to end of condition chain
                     ;---------------------------------------------------
                              ; Elif-Statement
.__elif__15x0:
                                 ; Condition
                                 ; Equal
                                    ; LHS
                                       ; Subscript
                                          ; LHS
                                             ; Identifier - char[] line
                                                push qword [rbp - 40]
                                          ; OFFSET
                                             ; Identifier - int i
                                                push qword [rbp - 72]
                                          pop rdx ; __offset
                                          pop rax ; __pointer
                                          push qword [rax + rdx] ; pointer + sizeof(data_t) * offset
                                    ; RHS
                                       ; Char Literal
                                          push '-'
                                    pop rdx ; rhs
                                    pop rax ; lhs
                                    cmp rax, rdx
                                    sete al
                                    movzx eax, al
                                    push rax
                                 pop rdx ; __cond
                                 cmp rdx, 0 ; ensure condition is true
                                 je .__endif__15
                                 ; Body
                                 ; Assignment - '='
                                    ; RHS
                                       ; Identifier - int i
                                          push qword [rbp - 72]
                                    pop rdx ; rhs value
                                    mov qword [rbp - 64], rdx
                                    push rdx
                                 ; Statement results can be ignored
                                 pop rdx
                                 jmp .__endif__15
                     ;---------------------------------------------------
                              ; End of if
.__endif__15:
                  ;------------------------------------------------------
                  ;------------------------------------------------------
                           ; If-Statement
                              ; Condition
                                 ; Equal
                                    ; LHS
                                       ; Subscript
                                          ; LHS
                                             ; Identifier - char[] line
                                                push qword [rbp - 40]
                                          ; OFFSET
                                             ; Identifier - int i
                                                push qword [rbp - 72]
                                          pop rdx ; __offset
                                          pop rax ; __pointer
                                          push qword [rax + rdx] ; pointer + sizeof(data_t) * offset
                                    ; RHS
                                       ; Char Literal
                                          push ','
                                    pop rdx ; rhs
                                    pop rax ; lhs
                                    cmp rax, rdx
                                    sete al
                                    movzx eax, al
                                    push rax
                                 pop rdx ; __cond
                                 cmp rdx, 0 ; ensure condition is true
                                 je .__endif__17 ; jump to end
                              ; Body
                                 ; Assignment - '='
                                    ; RHS
                                       ; Identifier - int i
                                          push qword [rbp - 72]
                                    pop rdx ; rhs value
                                    mov qword [rbp - 48], rdx
                                    push rdx
                                 ; Statement results can be ignored
                                 pop rdx
                              jmp .__endif__17 ; jump to end of condition chain
                              ; End of if
.__endif__17:
                  ;------------------------------------------------------
               ;---------------------------------------------------------
                     ; Repeat
jmp .__for__13
                     ; End of For
.__endfor__13:
         ;---------------------------------------------------------------
                  ; Assignment - '='
                     ; RHS
                        ; Int Literal
                           mov rax, 0
                           push rax
                     ; LHS
                        ; Variable Declaration - begin
                           mov rax, qword [rbp - 80]  ; __main__for__11__block__12__begin
                     pop rdx ; rhs value
                     mov qword [rbp - 80], rdx
                     push rdx
                  ; Statement results can be ignored
                  pop rdx
                  ; Assignment - '='
                     ; RHS
                        ; Identifier - int indexdash0
                           push qword [rbp - 56]
                     ; LHS
                        ; Variable Declaration - end
                           mov rax, qword [rbp - 88]  ; __main__for__11__block__12__end
                     pop rdx ; rhs value
                     mov qword [rbp - 88], rdx
                     push rdx
                  ; Statement results can be ignored
                  pop rdx
                  ; Assignment - '='
                     ; RHS
                        ; Int Literal
                           mov rax, 0
                           push rax
                     ; LHS
                        ; Variable Declaration - iter
                           mov rax, qword [rbp - 96]  ; __main__for__11__block__12__iter
                     pop rdx ; rhs value
                     mov qword [rbp - 96], rdx
                     push rdx
                  ; Statement results can be ignored
                  pop rdx
                  ; Assignment - '='
                     ; RHS
                        ; Array Allocator
                           ; Subtraction - int, int
                              ; LHS
                                 ; Identifier - int end
                                    push qword [rbp - 88]
                              ; RHS
                                 ; Identifier - int begin
                                    push qword [rbp - 80]
                              pop rdx ; rhs
                              pop rax ; lhs
                              sub rax, rdx
                              push rax
                           pop rdx ; num elements for dimension[0]
                           mov rdi, rdx ; num bytes to allocate (1 byte per element)
                           call malloc ; allocates edi bytes on heap and stores pointer in rax
                           push rax ; __ptr
                     ; LHS
                        ; Variable Declaration - a_
                           mov rax, qword [rbp - 104]  ; __main__for__11__block__12__a_
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
                           ; Identifier - int begin
                              push qword [rbp - 80]
                        ; LHS
                           ; Variable Declaration - i
                              mov rax, qword [rbp - 112]  ; __main__for__11__block__12__for__18__i
                        pop rdx ; rhs value
                        mov qword [rbp - 112], rdx
                        push rdx
                     ; Loop init result can be discarded
                     pop rax
                  jmp .__forcond__18
.__for__18:
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
.__forcond__18:
                     ; Condition
                        ; Less Than
                           ; LHS
                              ; Identifier - int i
                                 push qword [rbp - 112]
                           ; RHS
                              ; Identifier - int end
                                 push qword [rbp - 88]
                           pop rdx ; rhs
                           pop rax ; lhs
                           cmp rax, rdx
                           setl al
                           movzx eax, al
                           push rax
                        pop rax ; __cond
                        cmp rax, 0 ; __cond
                        je .__endfor__18
                     ; Body
                        ; Assignment - '='
                           ; RHS
                              ; Subscript
                                 ; LHS
                                    ; Identifier - char[] line
                                       push qword [rbp - 40]
                                 ; OFFSET
                                    ; Identifier - int i
                                       push qword [rbp - 112]
                                 pop rdx ; __offset
                                 pop rax ; __pointer
                                 push qword [rax + rdx] ; pointer + sizeof(data_t) * offset
                           ; LHS
                              ; Subscript assignment
                                 ; LHS
                                    ; Identifier - char[] a_
                                       push qword [rbp - 104]
                                 ; OFFSET
                                    ; Post-Increment
                                       mov rax, qword [rbp - 96]
                                       add qword [rbp - 96], 1
                                       push rax
                                 pop rdi ; __offset
                                 pop rbx ; __pointer
                           pop rdx ; rhs value
                           mov byte [rbx + rdi], dl
                           push rdx
                        ; Statement results can be ignored
                        pop rdx
                     ; Repeat
jmp .__for__18
                     ; End of For
.__endfor__18:
         ;---------------------------------------------------------------
                  ; Assignment - '='
                     ; RHS
                        ; Addition - int, int
                           ; LHS
                              ; Identifier - int indexdash0
                                 push qword [rbp - 56]
                           ; RHS
                              ; Int Literal
                                 mov rax, 1
                                 push rax
                           pop rdx ; rhs
                           pop rax ; lhs
                           add rax, rdx
                           push rax
                     pop rdx ; rhs value
                     mov qword [rbp - 80], rdx
                     push rdx
                  ; Statement results can be ignored
                  pop rdx
                  ; Assignment - '='
                     ; RHS
                        ; Identifier - int indexcomma
                           push qword [rbp - 48]
                     pop rdx ; rhs value
                     mov qword [rbp - 88], rdx
                     push rdx
                  ; Statement results can be ignored
                  pop rdx
                  ; Assignment - '='
                     ; RHS
                        ; Int Literal
                           mov rax, 0
                           push rax
                     pop rdx ; rhs value
                     mov qword [rbp - 96], rdx
                     push rdx
                  ; Statement results can be ignored
                  pop rdx
                  ; Assignment - '='
                     ; RHS
                        ; Array Allocator
                           ; Subtraction - int, int
                              ; LHS
                                 ; Identifier - int end
                                    push qword [rbp - 88]
                              ; RHS
                                 ; Identifier - int begin
                                    push qword [rbp - 80]
                              pop rdx ; rhs
                              pop rax ; lhs
                              sub rax, rdx
                              push rax
                           pop rdx ; num elements for dimension[0]
                           mov rdi, rdx ; num bytes to allocate (1 byte per element)
                           call malloc ; allocates edi bytes on heap and stores pointer in rax
                           push rax ; __ptr
                     ; LHS
                        ; Variable Declaration - b_
                           mov rax, qword [rbp - 120]  ; __main__for__11__block__12__b_
                     pop rdx ; rhs value
                     mov qword [rbp - 120], rdx
                     push rdx
                  ; Statement results can be ignored
                  pop rdx
         ;---------------------------------------------------------------
                  ; For-Loop
                  ; Init
                     ; Assignment - '='
                        ; RHS
                           ; Identifier - int begin
                              push qword [rbp - 80]
                        ; LHS
                           ; Variable Declaration - i
                              mov rax, qword [rbp - 128]  ; __main__for__11__block__12__for__19__i
                        pop rdx ; rhs value
                        mov qword [rbp - 128], rdx
                        push rdx
                     ; Loop init result can be discarded
                     pop rax
                  jmp .__forcond__19
.__for__19:
                     ; Update
                        ; Pre-Increment - int
                           ; RHS
                              ; Identifier - int i
                                 push qword [rbp - 128]
                           pop rdx
                           add qword [rbp - 128], 1
                           mov rax, qword [rbp - 128]
                           push rax ; push result
                        ; Loop update result can be discarded
                        pop rax
.__forcond__19:
                     ; Condition
                        ; Less Than
                           ; LHS
                              ; Identifier - int i
                                 push qword [rbp - 128]
                           ; RHS
                              ; Identifier - int end
                                 push qword [rbp - 88]
                           pop rdx ; rhs
                           pop rax ; lhs
                           cmp rax, rdx
                           setl al
                           movzx eax, al
                           push rax
                        pop rax ; __cond
                        cmp rax, 0 ; __cond
                        je .__endfor__19
                     ; Body
                        ; Assignment - '='
                           ; RHS
                              ; Subscript
                                 ; LHS
                                    ; Identifier - char[] line
                                       push qword [rbp - 40]
                                 ; OFFSET
                                    ; Identifier - int i
                                       push qword [rbp - 128]
                                 pop rdx ; __offset
                                 pop rax ; __pointer
                                 push qword [rax + rdx] ; pointer + sizeof(data_t) * offset
                           ; LHS
                              ; Subscript assignment
                                 ; LHS
                                    ; Identifier - char[] b_
                                       push qword [rbp - 120]
                                 ; OFFSET
                                    ; Post-Increment
                                       mov rax, qword [rbp - 96]
                                       add qword [rbp - 96], 1
                                       push rax
                                 pop rdi ; __offset
                                 pop rbx ; __pointer
                           pop rdx ; rhs value
                           mov byte [rbx + rdi], dl
                           push rdx
                        ; Statement results can be ignored
                        pop rdx
                     ; Repeat
jmp .__for__19
                     ; End of For
.__endfor__19:
         ;---------------------------------------------------------------
                  ; Assignment - '='
                     ; RHS
                        ; Addition - int, int
                           ; LHS
                              ; Identifier - int indexcomma
                                 push qword [rbp - 48]
                           ; RHS
                              ; Int Literal
                                 mov rax, 1
                                 push rax
                           pop rdx ; rhs
                           pop rax ; lhs
                           add rax, rdx
                           push rax
                     pop rdx ; rhs value
                     mov qword [rbp - 80], rdx
                     push rdx
                  ; Statement results can be ignored
                  pop rdx
                  ; Assignment - '='
                     ; RHS
                        ; Identifier - int indexdash1
                           push qword [rbp - 64]
                     pop rdx ; rhs value
                     mov qword [rbp - 88], rdx
                     push rdx
                  ; Statement results can be ignored
                  pop rdx
                  ; Assignment - '='
                     ; RHS
                        ; Int Literal
                           mov rax, 0
                           push rax
                     pop rdx ; rhs value
                     mov qword [rbp - 96], rdx
                     push rdx
                  ; Statement results can be ignored
                  pop rdx
                  ; Assignment - '='
                     ; RHS
                        ; Array Allocator
                           ; Subtraction - int, int
                              ; LHS
                                 ; Identifier - int end
                                    push qword [rbp - 88]
                              ; RHS
                                 ; Identifier - int begin
                                    push qword [rbp - 80]
                              pop rdx ; rhs
                              pop rax ; lhs
                              sub rax, rdx
                              push rax
                           pop rdx ; num elements for dimension[0]
                           mov rdi, rdx ; num bytes to allocate (1 byte per element)
                           call malloc ; allocates edi bytes on heap and stores pointer in rax
                           push rax ; __ptr
                     ; LHS
                        ; Variable Declaration - c_
                           mov rax, qword [rbp - 136]  ; __main__for__11__block__12__c_
                     pop rdx ; rhs value
                     mov qword [rbp - 136], rdx
                     push rdx
                  ; Statement results can be ignored
                  pop rdx
         ;---------------------------------------------------------------
                  ; For-Loop
                  ; Init
                     ; Assignment - '='
                        ; RHS
                           ; Identifier - int begin
                              push qword [rbp - 80]
                        ; LHS
                           ; Variable Declaration - i
                              mov rax, qword [rbp - 144]  ; __main__for__11__block__12__for__20__i
                        pop rdx ; rhs value
                        mov qword [rbp - 144], rdx
                        push rdx
                     ; Loop init result can be discarded
                     pop rax
                  jmp .__forcond__20
.__for__20:
                     ; Update
                        ; Pre-Increment - int
                           ; RHS
                              ; Identifier - int i
                                 push qword [rbp - 144]
                           pop rdx
                           add qword [rbp - 144], 1
                           mov rax, qword [rbp - 144]
                           push rax ; push result
                        ; Loop update result can be discarded
                        pop rax
.__forcond__20:
                     ; Condition
                        ; Less Than
                           ; LHS
                              ; Identifier - int i
                                 push qword [rbp - 144]
                           ; RHS
                              ; Identifier - int end
                                 push qword [rbp - 88]
                           pop rdx ; rhs
                           pop rax ; lhs
                           cmp rax, rdx
                           setl al
                           movzx eax, al
                           push rax
                        pop rax ; __cond
                        cmp rax, 0 ; __cond
                        je .__endfor__20
                     ; Body
                        ; Assignment - '='
                           ; RHS
                              ; Subscript
                                 ; LHS
                                    ; Identifier - char[] line
                                       push qword [rbp - 40]
                                 ; OFFSET
                                    ; Identifier - int i
                                       push qword [rbp - 144]
                                 pop rdx ; __offset
                                 pop rax ; __pointer
                                 push qword [rax + rdx] ; pointer + sizeof(data_t) * offset
                           ; LHS
                              ; Subscript assignment
                                 ; LHS
                                    ; Identifier - char[] c_
                                       push qword [rbp - 136]
                                 ; OFFSET
                                    ; Post-Increment
                                       mov rax, qword [rbp - 96]
                                       add qword [rbp - 96], 1
                                       push rax
                                 pop rdi ; __offset
                                 pop rbx ; __pointer
                           pop rdx ; rhs value
                           mov byte [rbx + rdi], dl
                           push rdx
                        ; Statement results can be ignored
                        pop rdx
                     ; Repeat
jmp .__for__20
                     ; End of For
.__endfor__20:
         ;---------------------------------------------------------------
                  ; Assignment - '='
                     ; RHS
                        ; Addition - int, int
                           ; LHS
                              ; Identifier - int indexdash1
                                 push qword [rbp - 64]
                           ; RHS
                              ; Int Literal
                                 mov rax, 1
                                 push rax
                           pop rdx ; rhs
                           pop rax ; lhs
                           add rax, rdx
                           push rax
                     pop rdx ; rhs value
                     mov qword [rbp - 80], rdx
                     push rdx
                  ; Statement results can be ignored
                  pop rdx
                  ; Assignment - '='
                     ; RHS
                        ; Subtraction - int, int
                           ; LHS
                              ; Sizeof Operator
                                 ; RHS
                                    ; Identifier - char[] line
                                       push qword [rbp - 40]
                              ; RHS
                                 ; Int Literal
                                    mov rax, 1
                                    push rax
                              pop rdx ; rhs
                              pop rax ; lhs
                              sub rax, rdx
                              push rax
                        pop rdx ; rhs value
                        mov qword [rbp - 88], rdx
                        push rdx
                     ; Statement results can be ignored
                     pop rdx
                     ; Assignment - '='
                        ; RHS
                           ; Int Literal
                              mov rax, 0
                              push rax
                        pop rdx ; rhs value
                        mov qword [rbp - 96], rdx
                        push rdx
                     ; Statement results can be ignored
                     pop rdx
                     ; Assignment - '='
                        ; RHS
                           ; Array Allocator
                              ; Subtraction - int, int
                                 ; LHS
                                    ; Identifier - int end
                                       push qword [rbp - 88]
                                 ; RHS
                                    ; Identifier - int begin
                                       push qword [rbp - 80]
                                 pop rdx ; rhs
                                 pop rax ; lhs
                                 sub rax, rdx
                                 push rax
                              pop rdx ; num elements for dimension[0]
                              mov rdi, rdx ; num bytes to allocate (1 byte per element)
                              call malloc ; allocates edi bytes on heap and stores pointer in rax
                              push rax ; __ptr
                        ; LHS
                           ; Variable Declaration - d_
                              mov rax, qword [rbp - 152]  ; __main__for__11__block__12__d_
                        pop rdx ; rhs value
                        mov qword [rbp - 152], rdx
                        push rdx
                     ; Statement results can be ignored
                     pop rdx
            ;------------------------------------------------------------
                     ; For-Loop
                     ; Init
                        ; Assignment - '='
                           ; RHS
                              ; Identifier - int begin
                                 push qword [rbp - 80]
                           ; LHS
                              ; Variable Declaration - i
                                 mov rax, qword [rbp - 160]  ; __main__for__11__block__12__for__21__i
                           pop rdx ; rhs value
                           mov qword [rbp - 160], rdx
                           push rdx
                        ; Loop init result can be discarded
                        pop rax
                     jmp .__forcond__21
.__for__21:
                        ; Update
                           ; Pre-Increment - int
                              ; RHS
                                 ; Identifier - int i
                                    push qword [rbp - 160]
                              pop rdx
                              add qword [rbp - 160], 1
                              mov rax, qword [rbp - 160]
                              push rax ; push result
                           ; Loop update result can be discarded
                           pop rax
.__forcond__21:
                        ; Condition
                           ; Less Than
                              ; LHS
                                 ; Identifier - int i
                                    push qword [rbp - 160]
                              ; RHS
                                 ; Identifier - int end
                                    push qword [rbp - 88]
                              pop rdx ; rhs
                              pop rax ; lhs
                              cmp rax, rdx
                              setl al
                              movzx eax, al
                              push rax
                           pop rax ; __cond
                           cmp rax, 0 ; __cond
                           je .__endfor__21
                        ; Body
                           ; Assignment - '='
                              ; RHS
                                 ; Subscript
                                    ; LHS
                                       ; Identifier - char[] line
                                          push qword [rbp - 40]
                                    ; OFFSET
                                       ; Identifier - int i
                                          push qword [rbp - 160]
                                    pop rdx ; __offset
                                    pop rax ; __pointer
                                    push qword [rax + rdx] ; pointer + sizeof(data_t) * offset
                              ; LHS
                                 ; Subscript assignment
                                    ; LHS
                                       ; Identifier - char[] d_
                                          push qword [rbp - 152]
                                    ; OFFSET
                                       ; Post-Increment
                                          mov rax, qword [rbp - 96]
                                          add qword [rbp - 96], 1
                                          push rax
                                    pop rdi ; __offset
                                    pop rbx ; __pointer
                              pop rdx ; rhs value
                              mov byte [rbx + rdi], dl
                              push rdx
                           ; Statement results can be ignored
                           pop rdx
                        ; Repeat
jmp .__for__21
                        ; End of For
.__endfor__21:
            ;------------------------------------------------------------
                     ; Assignment - '='
                        ; RHS
                           ; Function Call - stringToInt(char[]) -> int
                              ; Make space for 1 arg(s)
                              sub rsp, 8
                              ; Arguments
                                 ; Eval arg0
                                    ; Identifier - char[] a_
                                       push qword [rbp - 104]
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
                           ; Variable Declaration - begin0
                              mov rax, qword [rbp - 168]  ; __main__for__11__block__12__begin0
                        pop rdx ; rhs value
                        mov qword [rbp - 168], rdx
                        push rdx
                     ; Statement results can be ignored
                     pop rdx
                     ; Assignment - '='
                        ; RHS
                           ; Addition - int, int
                              ; LHS
                                 ; Function Call - stringToInt(char[]) -> int
                                    ; Make space for 1 arg(s)
                                    sub rsp, 8
                                    ; Arguments
                                       ; Eval arg0
                                          ; Identifier - char[] b_
                                             push qword [rbp - 120]
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
                                    mov rax, 1
                                    push rax
                              pop rdx ; rhs
                              pop rax ; lhs
                              add rax, rdx
                              push rax
                        ; LHS
                           ; Variable Declaration - end0
                              mov rax, qword [rbp - 176]  ; __main__for__11__block__12__end0
                        pop rdx ; rhs value
                        mov qword [rbp - 176], rdx
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
                                    ; Identifier - char[] c_
                                       push qword [rbp - 136]
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
                           ; Variable Declaration - begin1
                              mov rax, qword [rbp - 184]  ; __main__for__11__block__12__begin1
                        pop rdx ; rhs value
                        mov qword [rbp - 184], rdx
                        push rdx
                     ; Statement results can be ignored
                     pop rdx
                     ; Assignment - '='
                        ; RHS
                           ; Addition - int, int
                              ; LHS
                                 ; Function Call - stringToInt(char[]) -> int
                                    ; Make space for 1 arg(s)
                                    sub rsp, 8
                                    ; Arguments
                                       ; Eval arg0
                                          ; Identifier - char[] d_
                                             push qword [rbp - 152]
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
                                    mov rax, 1
                                    push rax
                              pop rdx ; rhs
                              pop rax ; lhs
                              add rax, rdx
                              push rax
                        ; LHS
                           ; Variable Declaration - end1
                              mov rax, qword [rbp - 192]  ; __main__for__11__block__12__end1
                        pop rdx ; rhs value
                        mov qword [rbp - 192], rdx
                        push rdx
                     ; Statement results can be ignored
                     pop rdx
                     ; Assignment - '='
                        ; RHS
                           ; Int Literal
                              mov rax, 0
                              push rax
                        ; LHS
                           ; Variable Declaration - isAInB
                              mov rax, qword [rbp - 200]  ; __main__for__11__block__12__isAInB
                        pop rdx ; rhs value
                        mov qword [rbp - 200], rdx
                        push rdx
                     ; Statement results can be ignored
                     pop rdx
                     ; Assignment - '='
                        ; RHS
                           ; Int Literal
                              mov rax, 0
                              push rax
                        ; LHS
                           ; Variable Declaration - isBInA
                              mov rax, qword [rbp - 208]  ; __main__for__11__block__12__isBInA
                        pop rdx ; rhs value
                        mov qword [rbp - 208], rdx
                        push rdx
                     ; Statement results can be ignored
                     pop rdx
            ;------------------------------------------------------------
                     ; If-Statement
                        ; Condition
                           ; AND
                              ; Eval LHS
                                 ; Greater Than or Equal to
                                    ; LHS
                                       ; Identifier - int begin0
                                          push qword [rbp - 168]
                                    ; RHS
                                       ; Identifier - int begin1
                                          push qword [rbp - 184]
                                    pop rdx ; rhs
                                    pop rax ; lhs
                                    cmp rax, rdx
                                    setge al
                                    movzx eax, al
                                    push rax
                              ; Check if we need to short-circuit
                                 pop rax ; __lhs
                                 test rax, rax
                                 je .AND_SHORT_CIRCUIT23
                              ; Eval RHS
                                 ; Less Than or Equal to
                                    ; LHS
                                       ; Identifier - int end0
                                          push qword [rbp - 176]
                                    ; RHS
                                       ; Identifier - int end1
                                          push qword [rbp - 192]
                                    pop rdx ; rhs
                                    pop rax ; lhs
                                    cmp rax, rdx
                                    setle al
                                    movzx eax, al
                                    push rax
                              ; Check RHS
                                 pop rax ; __rhs
                                 test rax, rax
                                 je .AND_SHORT_CIRCUIT23
                              ; Success state
                              mov rax, 1 ; result = True
                              jmp .AND_END23
.AND_SHORT_CIRCUIT23:
                              mov rax, 0 ; result = False
.AND_END23:
                              movzx eax, al
                              push rax ; result
                           pop rdx ; __cond
                           cmp rdx, 0 ; ensure condition is true
                           je .__endif__22 ; jump to end
                        ; Body
                           ; Assignment - '='
                              ; RHS
                                 ; Int Literal
                                    mov rax, 1
                                    push rax
                              pop rdx ; rhs value
                              mov qword [rbp - 200], rdx
                              push rdx
                           ; Statement results can be ignored
                           pop rdx
                        jmp .__endif__22 ; jump to end of condition chain
                        ; End of if
.__endif__22:
            ;------------------------------------------------------------
            ;------------------------------------------------------------
                     ; If-Statement
                        ; Condition
                           ; AND
                              ; Eval LHS
                                 ; Greater Than or Equal to
                                    ; LHS
                                       ; Identifier - int begin1
                                          push qword [rbp - 184]
                                    ; RHS
                                       ; Identifier - int begin0
                                          push qword [rbp - 168]
                                    pop rdx ; rhs
                                    pop rax ; lhs
                                    cmp rax, rdx
                                    setge al
                                    movzx eax, al
                                    push rax
                              ; Check if we need to short-circuit
                                 pop rax ; __lhs
                                 test rax, rax
                                 je .AND_SHORT_CIRCUIT25
                              ; Eval RHS
                                 ; Less Than or Equal to
                                    ; LHS
                                       ; Identifier - int end1
                                          push qword [rbp - 192]
                                    ; RHS
                                       ; Identifier - int end0
                                          push qword [rbp - 176]
                                    pop rdx ; rhs
                                    pop rax ; lhs
                                    cmp rax, rdx
                                    setle al
                                    movzx eax, al
                                    push rax
                              ; Check RHS
                                 pop rax ; __rhs
                                 test rax, rax
                                 je .AND_SHORT_CIRCUIT25
                              ; Success state
                              mov rax, 1 ; result = True
                              jmp .AND_END25
.AND_SHORT_CIRCUIT25:
                              mov rax, 0 ; result = False
.AND_END25:
                              movzx eax, al
                              push rax ; result
                           pop rdx ; __cond
                           cmp rdx, 0 ; ensure condition is true
                           je .__endif__24 ; jump to end
                        ; Body
                           ; Assignment - '='
                              ; RHS
                                 ; Int Literal
                                    mov rax, 1
                                    push rax
                              pop rdx ; rhs value
                              mov qword [rbp - 208], rdx
                              push rdx
                           ; Statement results can be ignored
                           pop rdx
                        jmp .__endif__24 ; jump to end of condition chain
                        ; End of if
.__endif__24:
            ;------------------------------------------------------------
            ;------------------------------------------------------------
                     ; If-Statement
                        ; Condition
                           ; OR
                              ; Eval LHS
                                 ; Identifier - int isAInB
                                    push qword [rbp - 200]
                              ; Check if we need to short-circuit
                                 pop rax ; __lhs
                                 test rax, rax
                                 jne .OR_SHORT_CIRCUIT27
                              ; Eval RHS
                                 ; Identifier - int isBInA
                                    push qword [rbp - 208]
                              ; Check rhs
                                 pop rax ; __rhs
                                 test rax, rax
                                 je .OR_FALSE27 ; skip true state if false (rax == 0)
.OR_SHORT_CIRCUIT27:
                              mov rax, 1 ; result = True
                              jmp .OR_END27 ; skip false state
                              ; False state
.OR_FALSE27:
                              mov rax, 0 ; result = False
.OR_END27:
                              movzx eax, al
                              push rax ; result
                           pop rdx ; __cond
                           cmp rdx, 0 ; ensure condition is true
                           je .__endif__26 ; jump to end
                        ; Body
                  ;------------------------------------------------------
                           ; Code Block
                              ; Post-Increment
                                 mov rax, qword [rbp - 16]
                                 add qword [rbp - 16], 1
                                 push rax
                              ; Statement results can be ignored
                              pop rdx
                  ;------------------------------------------------------
                        jmp .__endif__26 ; jump to end of condition chain
                        ; End of if
.__endif__26:
            ;------------------------------------------------------------
         ;---------------------------------------------------------------
               ; Repeat
jmp .__for__11
               ; End of For
.__endfor__11:
   ;---------------------------------------------------------------------
            ; Function Call - println(int) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; Identifier - int total
                        push qword [rbp - 16]
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
   ; ### END OF CODE #####################################################
   ; =====================================================================

            push 0
            call exit__int
   ; =====================================================================
   ; ### DATA SECTION ####################################################
   ; =====================================================================

            section .data
.floatNegOne: dq -1.0
.floatZero: dq 0.0
.floatOne: dq 1.0
