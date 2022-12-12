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
         sub rsp, 272
         ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
         ; [rbp - 8] - char[] line (<unset-scope-name>)
         ; [rbp - 16] - Vector<:char[]:> lines (<unset-scope-name>)
         ; [rbp - 24] - int OP_MUL (<unset-scope-name>)
         ; [rbp - 32] - int OP_ADD (<unset-scope-name>)
         ; [rbp - 40] - int OP_SQUARE (<unset-scope-name>)
         ; [rbp - 48] - Vector<:Monkey:> monkeys (<unset-scope-name>)
         ; [rbp - 56] - int l (<unset-scope-name>)
         ; [rbp - 64] - Monkey monkey (<unset-scope-name>)
         ; [rbp - 72] - char[] items_str (<unset-scope-name>)
         ; [rbp - 80] - Vector<:char[]:> tokens0 (<unset-scope-name>)
         ; [rbp - 88] - int i (<unset-scope-name>)
         ; [rbp - 96] - char[] item_str (<unset-scope-name>)
         ; [rbp - 104] - int item (<unset-scope-name>)
         ; [rbp - 112] - int i (<unset-scope-name>)
         ; [rbp - 120] - Vector<:char[]:> tokens1 (<unset-scope-name>)
         ; [rbp - 128] - int j (<unset-scope-name>)
         ; [rbp - 136] - Vector<:char[]:> tokens1 (<unset-scope-name>)
         ; [rbp - 144] - int j (<unset-scope-name>)
         ; [rbp - 152] - Vector<:char[]:> tokens2 (<unset-scope-name>)
         ; [rbp - 160] - int j (<unset-scope-name>)
         ; [rbp - 168] - Vector<:char[]:> tokens3 (<unset-scope-name>)
         ; [rbp - 176] - int j (<unset-scope-name>)
         ; [rbp - 184] - Vector<:char[]:> tokens4 (<unset-scope-name>)
         ; [rbp - 192] - int j (<unset-scope-name>)
         ; [rbp - 200] - int r (<unset-scope-name>)
         ; [rbp - 208] - int m (<unset-scope-name>)
         ; [rbp - 216] - Monkey monkey (<unset-scope-name>)
         ; [rbp - 224] - Vector<:int:> monkey_items (<unset-scope-name>)
         ; [rbp - 232] - int i (<unset-scope-name>)
         ; [rbp - 240] - int worry_level (<unset-scope-name>)
         ; [rbp - 248] - int firstmax (<unset-scope-name>)
         ; [rbp - 256] - int secondmax (<unset-scope-name>)
         ; [rbp - 264] - int i (<unset-scope-name>)
         ; [rbp - 272] - int i (<unset-scope-name>)

         ; Body
; ========================================================================
         ; Class Template - 
            ; Instances:
      ; ==================================================================
               ; Class Declaration - __main____Vector__char__1 inherits __builtin____main__Object
                  ; Class data
                  section .data
                     ; Dispatch Table - this might need to be a malloc**
                     .__dtable____main____Vector__char__1:
                     ; Dispatch Table Entries
                     dq .__method____main____Vector__char__1____pushBack__char__1 ; 0
                     dq .__method____main____Vector__char__1____popBack ; 1
                     dq .__method____main____Vector__char__1____clear ; 2
                     dq .__method____main____Vector__char__1____get__int ; 3
                     dq .__method____main____Vector__char__1____set__int__char__1 ; 4
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
               ; Constructor Declaration - Vector<:char[]:>::Vector(int) -> Vector<:char[]:>
               jmp .__end__ctor____main____Vector__char__1____Vector__int
               .__ctor____main____Vector__char__1____Vector__int:
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
                     ; Param: size [rbp + 16]
               ; Body
         ;---------------------------------------------------------------
                  ; Code Block
                     ; Assignment - '='
                        ; RHS
                           ; Addition - int, int
                              ; LHS
                                 ; Identifier - int size
                                    push qword [rbp - -16]
                              ; RHS
                                 ; Int Literal
                                    mov rax, 10
                                    push rax
                              pop rdx ; rhs
                              pop rax ; lhs
                              add rax, rdx
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
                           ; Identifier - int size
                              push qword [rbp - -16]
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
         ;---------------------------------------------------------------
               mov rax, qword [rbp - 8] ; __this
               ; Function Epilogue
               mov rsp, rbp ; remove local vars + unpopped pushes
               pop rbp
               ret
            .__end__ctor____main____Vector__char__1____Vector__int:
            ; End Constructor Declaration - __ctor____main____Vector__char__1____Vector__int
   ;---------------------------------------------------------------------

   ;---------------------------------------------------------------------
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
         ;---------------------------------------------------------------
                  ; Code Block
            ;------------------------------------------------------------
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
                           je .__endif__3 ; jump to end
                        ; Body
                  ;------------------------------------------------------
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
                                       mov rax, qword [rbp - 16]  ; __main____Vector__char__1__pushBack__block__2__if__3__block__4__nData
                                 pop rdx ; rhs value
                                 mov qword [rbp - 16], rdx
                                 push rdx
                              ; Statement results can be ignored
                              pop rdx
                     ;---------------------------------------------------
                              ; For-Loop
                              ; Init
                                 ; Assignment - '='
                                    ; RHS
                                       ; Int Literal
                                          mov rax, 0
                                          push rax
                                    ; LHS
                                       ; Variable Declaration - i
                                          mov rax, qword [rbp - 24]  ; __main____Vector__char__1__pushBack__block__2__if__3__block__4__for__5__i
                                    pop rdx ; rhs value
                                    mov qword [rbp - 24], rdx
                                    push rdx
                                 ; Loop init result can be discarded
                                 pop rax
                              jmp .__forcond__5
.__for__5:
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
.__forcond__5:
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
                                    je .__endfor__5
                                 ; Body
                           ;---------------------------------------------
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
                           ;---------------------------------------------
                                 ; Repeat
jmp .__for__5
                                 ; End of For
.__endfor__5:
                     ;---------------------------------------------------
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
                  ;------------------------------------------------------
                        jmp .__endif__3 ; jump to end of condition chain
                        ; End of if
.__endif__3:
            ;------------------------------------------------------------
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
         ;---------------------------------------------------------------
               ; Function Epilogue
               mov rsp, rbp ; remove local vars + unpopped pushes
               pop rbp
               ret
            .__end__method____main____Vector__char__1____pushBack__char__1:
            ; End Method Declaration - .__method____main____Vector__char__1____pushBack__char__1
   ;---------------------------------------------------------------------

   ;---------------------------------------------------------------------
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
         ;---------------------------------------------------------------
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
         ;---------------------------------------------------------------
               ; Function Epilogue
               mov rsp, rbp ; remove local vars + unpopped pushes
               pop rbp
               ret
            .__end__method____main____Vector__char__1____popBack:
            ; End Method Declaration - .__method____main____Vector__char__1____popBack
   ;---------------------------------------------------------------------

   ;---------------------------------------------------------------------
            ; Method Declaration - Vector<:char[]:>::clear() -> void
            jmp .__end__method____main____Vector__char__1____clear
            .__method____main____Vector__char__1____clear:
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
         ;---------------------------------------------------------------
                  ; Code Block
            ;------------------------------------------------------------
                     ; While-Loop
.__while__9:
                        ; Condition
                           ; Greater Than
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
                                    mov rax, 0
                                    push rax
                              pop rdx ; rhs
                              pop rax ; lhs
                              cmp rax, rdx
                              setg al
                              movzx eax, al
                              push rax
                           pop rax ; __cond
                           cmp rax, 0 ; __cond
                           je .__endwhile__9
                        ; Body
                           ; Method Call - Vector<:char[]:>::popBack() -> char[]
                              ; Make space for 0 arg(s) and object parameter
                              sub rsp, 8
                              ; LHS
                                 ; This keyword
                                    push qword [rbp - 8] ; __this
                                 pop rax ; object parameter
                                 mov qword [rsp + 0], rax ; place as first parameter
                              ; RHS
                              ; Arguments
                              call .__method____main____Vector__char__1____popBack
                              ; Remove args
                              add rsp, 8
                              ; Push return value
                              push rax
                           ; Statement results can be ignored
                           pop rdx
                        jmp .__while__9
                        ; End of While
.__endwhile__9:
            ;------------------------------------------------------------
         ;---------------------------------------------------------------
               ; Function Epilogue
               mov rsp, rbp ; remove local vars + unpopped pushes
               pop rbp
               ret
            .__end__method____main____Vector__char__1____clear:
            ; End Method Declaration - .__method____main____Vector__char__1____clear
   ;---------------------------------------------------------------------

   ;---------------------------------------------------------------------
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
         ;---------------------------------------------------------------
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
         ;---------------------------------------------------------------
               ; Function Epilogue
               mov rsp, rbp ; remove local vars + unpopped pushes
               pop rbp
               ret
            .__end__method____main____Vector__char__1____get__int:
            ; End Method Declaration - .__method____main____Vector__char__1____get__int
   ;---------------------------------------------------------------------

   ;---------------------------------------------------------------------
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
         ;---------------------------------------------------------------
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
         ;---------------------------------------------------------------
               ; Function Epilogue
               mov rsp, rbp ; remove local vars + unpopped pushes
               pop rbp
               ret
            .__end__method____main____Vector__char__1____set__int__char__1:
            ; End Method Declaration - .__method____main____Vector__char__1____set__int__char__1
   ;---------------------------------------------------------------------

.__endclass____main____Vector__char__1:
         ; End Class Declaration - __main____Vector__char__1
; ========================================================================

; ========================================================================
         ; Class Declaration - __main____Vector__int inherits __builtin____main__Object
            ; Class data
            section .data
               ; Dispatch Table - this might need to be a malloc**
               .__dtable____main____Vector__int:
               ; Dispatch Table Entries
               dq .__method____main____Vector__int____pushBack__int ; 0
               dq .__method____main____Vector__int____popBack ; 1
               dq .__method____main____Vector__int____clear ; 2
               dq .__method____main____Vector__int____get__int ; 3
               dq .__method____main____Vector__int____set__int__int ; 4
            section .text
   ;---------------------------------------------------------------------
            ; Field - int[] Vector<:int:>::data
            section .data
            .__field____main____Vector__int____data: dq 1
            section .text
   ;---------------------------------------------------------------------
   ;---------------------------------------------------------------------
            ; Field - int Vector<:int:>::size
            section .data
            .__field____main____Vector__int____size: dq 2
            section .text
   ;---------------------------------------------------------------------
   ;---------------------------------------------------------------------
            ; Field - int Vector<:int:>::capacity
            section .data
            .__field____main____Vector__int____capacity: dq 3
            section .text
   ;---------------------------------------------------------------------
         ; skip over class methods
         jmp .__endclass____main____Vector__int
   ;---------------------------------------------------------------------
            ; Constructor Declaration - Vector<:int:>::Vector() -> Vector<:int:>
            jmp .__end__ctor____main____Vector__int____Vector
            .__ctor____main____Vector__int____Vector:
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
                  mov qword [rax + 0], .__dtable____main____Vector__int ; this[0] = &dtable
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
                              push qword [.__field____main____Vector__int____capacity] ; 
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
                              push qword [.__field____main____Vector__int____size] ; 
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
                                 push qword [.__field____main____Vector__int____capacity] ; stored index associated with field that is being accessed
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
                              push qword [.__field____main____Vector__int____data] ; 
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
         .__end__ctor____main____Vector__int____Vector:
         ; End Constructor Declaration - __ctor____main____Vector__int____Vector
;------------------------------------------------------------------------

;------------------------------------------------------------------------
         ; Constructor Declaration - Vector<:int:>::Vector(int) -> Vector<:int:>
         jmp .__end__ctor____main____Vector__int____Vector__int
         .__ctor____main____Vector__int____Vector__int:
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
               mov qword [rax + 0], .__dtable____main____Vector__int ; this[0] = &dtable
            ; Parameters
               ; Param: size [rbp + 16]
         ; Body
   ;---------------------------------------------------------------------
            ; Code Block
               ; Assignment - '='
                  ; RHS
                     ; Addition - int, int
                        ; LHS
                           ; Identifier - int size
                              push qword [rbp - -16]
                        ; RHS
                           ; Int Literal
                              mov rax, 10
                              push rax
                        pop rdx ; rhs
                        pop rax ; lhs
                        add rax, rdx
                        push rax
                  ; LHS
                     ; Member Accessor Assignment
                        ; LHS
                           ; This keyword
                              push qword [rbp - 8] ; __this
                        ; RHS
                           push qword [.__field____main____Vector__int____capacity] ; 
                        pop rdi ; rhs
                        pop rbx ; lhs
                  pop rdx ; rhs value
                  mov qword [rbx + 8*rdi], rdx
                  push rdx
               ; Statement results can be ignored
               pop rdx
               ; Assignment - '='
                  ; RHS
                     ; Identifier - int size
                        push qword [rbp - -16]
                  ; LHS
                     ; Member Accessor Assignment
                        ; LHS
                           ; This keyword
                              push qword [rbp - 8] ; __this
                        ; RHS
                           push qword [.__field____main____Vector__int____size] ; 
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
                              push qword [.__field____main____Vector__int____capacity] ; stored index associated with field that is being accessed
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
                           push qword [.__field____main____Vector__int____data] ; 
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
         .__end__ctor____main____Vector__int____Vector__int:
         ; End Constructor Declaration - __ctor____main____Vector__int____Vector__int
;---------------------------------------------------------------------------

;---------------------------------------------------------------------------
         ; Method Declaration - Vector<:int:>::pushBack(int) -> void
         jmp .__end__method____main____Vector__int____pushBack__int
         .__method____main____Vector__int____pushBack__int:
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
            ; Param: val [rbp + 24] (__main____Vector__int__pushBack__val)
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
                                       push qword [.__field____main____Vector__int____size] ; stored index associated with field that is being accessed
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
                                 push qword [.__field____main____Vector__int____capacity] ; stored index associated with field that is being accessed
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
                     je .__endif__15 ; jump to end
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
                                          push qword [.__field____main____Vector__int____capacity] ; stored index associated with field that is being accessed
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
                                    push qword [.__field____main____Vector__int____capacity] ; 
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
                                       push qword [.__field____main____Vector__int____capacity] ; stored index associated with field that is being accessed
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
                                 mov rax, qword [rbp - 16]  ; __main____Vector__int__pushBack__block__14__if__15__block__16__nData
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
                                    mov rax, qword [rbp - 24]  ; __main____Vector__int__pushBack__block__14__if__15__block__16__for__17__i
                              pop rdx ; rhs value
                              mov qword [rbp - 24], rdx
                              push rdx
                           ; Loop init result can be discarded
                           pop rax
                        jmp .__forcond__17
.__for__17:
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
.__forcond__17:
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
                                          push qword [.__field____main____Vector__int____size] ; stored index associated with field that is being accessed
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
                              je .__endfor__17
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
                                                   push qword [.__field____main____Vector__int____data] ; stored index associated with field that is being accessed
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
                     ;---------------------------------------------------
                           ; Repeat
jmp .__for__17
                           ; End of For
.__endfor__17:
               ;---------------------------------------------------------
                        ; Free Operator
                           ; RHS
                              ; Member Accessor
                                 ; LHS
                                    ; This keyword
                                       push qword [rbp - 8] ; __this
                                 ; RHS
                                    push qword [.__field____main____Vector__int____data] ; stored index associated with field that is being accessed
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
                                    push qword [.__field____main____Vector__int____data] ; 
                                 pop rdi ; rhs
                                 pop rbx ; lhs
                           pop rdx ; rhs value
                           mov qword [rbx + 8*rdi], rdx
                           push rdx
                        ; Statement results can be ignored
                        pop rdx
            ;------------------------------------------------------------
                  jmp .__endif__15 ; jump to end of condition chain
                  ; End of if
.__endif__15:
      ;------------------------------------------------------------------
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
                                 push qword [.__field____main____Vector__int____data] ; stored index associated with field that is being accessed
                              pop rdx ; rhs
                              pop rax ; lhs
                              push qword [rax + 8*rdx] ; lhs.rhs
                        ; OFFSET
                           ; Member Accessor
                              ; LHS
                                 ; This keyword
                                    push qword [rbp - 8] ; __this
                              ; RHS
                                 push qword [.__field____main____Vector__int____size] ; stored index associated with field that is being accessed
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
                           push qword [.__field____main____Vector__int____size] ; stored index associated with field that is being accessed
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
                           push qword [.__field____main____Vector__int____size] ; size
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
         .__end__method____main____Vector__int____pushBack__int:
         ; End Method Declaration - .__method____main____Vector__int____pushBack__int
;---------------------------------------------------------------------------

;---------------------------------------------------------------------------
         ; Method Declaration - Vector<:int:>::popBack() -> int
         jmp .__end__method____main____Vector__int____popBack
         .__method____main____Vector__int____popBack:
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
                              push qword [.__field____main____Vector__int____data] ; stored index associated with field that is being accessed
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
                                    push qword [.__field____main____Vector__int____size] ; stored index associated with field that is being accessed
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
                                    push qword [.__field____main____Vector__int____size] ; size
                                 pop rdi ; rhs
                                 pop rbx ; lhs
                                 mov rax, qword [rbx + 8*rdi]
                                 sub rax, 1
                                 mov qword [rbx + 8*rdi], rax
                           push rax ; push result
                     pop rdx ; __offset
                     pop rax ; __pointer
                     push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                  pop rax ; return value (int)
                  ; Clean up stack and return
                  mov rsp, rbp ; remove local vars + unpopped pushes
                  pop rbp
                  ret
   ;---------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
         .__end__method____main____Vector__int____popBack:
         ; End Method Declaration - .__method____main____Vector__int____popBack
;---------------------------------------------------------------------------

;---------------------------------------------------------------------------
         ; Method Declaration - Vector<:int:>::clear() -> void
         jmp .__end__method____main____Vector__int____clear
         .__method____main____Vector__int____clear:
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
      ;------------------------------------------------------------------
               ; While-Loop
.__while__21:
                  ; Condition
                     ; Greater Than
                        ; LHS
                           ; Member Accessor
                              ; LHS
                                 ; This keyword
                                    push qword [rbp - 8] ; __this
                              ; RHS
                                 push qword [.__field____main____Vector__int____size] ; stored index associated with field that is being accessed
                              pop rdx ; rhs
                              pop rax ; lhs
                              push qword [rax + 8*rdx] ; lhs.rhs
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
                     pop rax ; __cond
                     cmp rax, 0 ; __cond
                     je .__endwhile__21
                  ; Body
                     ; Method Call - Vector<:int:>::popBack() -> int
                        ; Make space for 0 arg(s) and object parameter
                        sub rsp, 8
                        ; LHS
                           ; This keyword
                              push qword [rbp - 8] ; __this
                           pop rax ; object parameter
                           mov qword [rsp + 0], rax ; place as first parameter
                        ; RHS
                        ; Arguments
                        call .__method____main____Vector__int____popBack
                        ; Remove args
                        add rsp, 8
                        ; Push return value
                        push rax
                     ; Statement results can be ignored
                     pop rdx
                  jmp .__while__21
                  ; End of While
.__endwhile__21:
      ;------------------------------------------------------------------
   ;---------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
         .__end__method____main____Vector__int____clear:
         ; End Method Declaration - .__method____main____Vector__int____clear
;---------------------------------------------------------------------------

;---------------------------------------------------------------------------
         ; Method Declaration - Vector<:int:>::get(int) -> int
         jmp .__end__method____main____Vector__int____get__int
         .__method____main____Vector__int____get__int:
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
            ; Param: index [rbp + 24] (__main____Vector__int__get__index)
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
                              push qword [.__field____main____Vector__int____data] ; stored index associated with field that is being accessed
                           pop rdx ; rhs
                           pop rax ; lhs
                           push qword [rax + 8*rdx] ; lhs.rhs
                     ; OFFSET
                        ; Identifier - int index
                           push qword [rbp - -24]
                     pop rdx ; __offset
                     pop rax ; __pointer
                     push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                  pop rax ; return value (int)
                  ; Clean up stack and return
                  mov rsp, rbp ; remove local vars + unpopped pushes
                  pop rbp
                  ret
   ;---------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
         .__end__method____main____Vector__int____get__int:
         ; End Method Declaration - .__method____main____Vector__int____get__int
;---------------------------------------------------------------------------

;---------------------------------------------------------------------------
         ; Method Declaration - Vector<:int:>::set(int, int) -> void
         jmp .__end__method____main____Vector__int____set__int__int
         .__method____main____Vector__int____set__int__int:
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
            ; Param: index [rbp + 24] (__main____Vector__int__set__index)
            ; Param: value [rbp + 32] (__main____Vector__int__set__value)
         ; Body
   ;---------------------------------------------------------------------
            ; Code Block
               ; Assignment - '='
                  ; RHS
                     ; Identifier - int value
                        push qword [rbp - -32]
                  ; LHS
                     ; Subscript assignment
                        ; LHS
                           ; Member Accessor
                              ; LHS
                                 ; This keyword
                                    push qword [rbp - 8] ; __this
                              ; RHS
                                 push qword [.__field____main____Vector__int____data] ; stored index associated with field that is being accessed
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
   ;---------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
         .__end__method____main____Vector__int____set__int__int:
         ; End Method Declaration - .__method____main____Vector__int____set__int__int
;---------------------------------------------------------------------------

.__endclass____main____Vector__int:
         ; End Class Declaration - __main____Vector__int
; ==============================================================================

; ==============================================================================
         ; Class Declaration - __main____Vector__Monkey inherits __builtin____main__Object
         ; Class data
         section .data
         ; Dispatch Table - this might need to be a malloc**
         .__dtable____main____Vector__Monkey:
         ; Dispatch Table Entries
         dq .__method____main____Vector__Monkey____pushBack__Monkey ; 0
         dq .__method____main____Vector__Monkey____popBack ; 1
         dq .__method____main____Vector__Monkey____clear ; 2
         dq .__method____main____Vector__Monkey____get__int ; 3
         dq .__method____main____Vector__Monkey____set__int__Monkey ; 4
         section .text
;---------------------------------------------------------------------------
         ; Field - Monkey[] Vector<:Monkey:>::data
         section .data
         .__field____main____Vector__Monkey____data: dq 1
         section .text
;---------------------------------------------------------------------------
;---------------------------------------------------------------------------
         ; Field - int Vector<:Monkey:>::size
         section .data
         .__field____main____Vector__Monkey____size: dq 2
         section .text
;---------------------------------------------------------------------------
;---------------------------------------------------------------------------
         ; Field - int Vector<:Monkey:>::capacity
         section .data
         .__field____main____Vector__Monkey____capacity: dq 3
         section .text
;---------------------------------------------------------------------------
         ; skip over class methods
         jmp .__endclass____main____Vector__Monkey
;---------------------------------------------------------------------------
         ; Constructor Declaration - Vector<:Monkey:>::Vector() -> Vector<:Monkey:>
         jmp .__end__ctor____main____Vector__Monkey____Vector
         .__ctor____main____Vector__Monkey____Vector:
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
            mov qword [rax + 0], .__dtable____main____Vector__Monkey ; this[0] = &dtable
         ; Parameters
         ; Body
;------------------------------------------------------------------------
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
                        push qword [.__field____main____Vector__Monkey____capacity] ; 
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
                        push qword [.__field____main____Vector__Monkey____size] ; 
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
                           push qword [.__field____main____Vector__Monkey____capacity] ; stored index associated with field that is being accessed
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
                        push qword [.__field____main____Vector__Monkey____data] ; 
                     pop rdi ; rhs
                     pop rbx ; lhs
               pop rdx ; rhs value
               mov qword [rbx + 8*rdi], rdx
               push rdx
            ; Statement results can be ignored
            pop rdx
;------------------------------------------------------------------------
         mov rax, qword [rbp - 8] ; __this
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
         .__end__ctor____main____Vector__Monkey____Vector:
         ; End Constructor Declaration - __ctor____main____Vector__Monkey____Vector
;------------------------------------------------------------------------------

;------------------------------------------------------------------------------
         ; Constructor Declaration - Vector<:Monkey:>::Vector(int) -> Vector<:Monkey:>
         jmp .__end__ctor____main____Vector__Monkey____Vector__int
         .__ctor____main____Vector__Monkey____Vector__int:
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
         mov qword [rax + 0], .__dtable____main____Vector__Monkey ; this[0] = &dtable
         ; Parameters
         ; Param: size [rbp + 16]
         ; Body
;---------------------------------------------------------------------------
         ; Code Block
         ; Assignment - '='
            ; RHS
               ; Addition - int, int
                  ; LHS
                     ; Identifier - int size
                        push qword [rbp - -16]
                  ; RHS
                     ; Int Literal
                        mov rax, 10
                        push rax
                  pop rdx ; rhs
                  pop rax ; lhs
                  add rax, rdx
                  push rax
            ; LHS
               ; Member Accessor Assignment
                  ; LHS
                     ; This keyword
                        push qword [rbp - 8] ; __this
                  ; RHS
                     push qword [.__field____main____Vector__Monkey____capacity] ; 
                  pop rdi ; rhs
                  pop rbx ; lhs
            pop rdx ; rhs value
            mov qword [rbx + 8*rdi], rdx
            push rdx
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
            ; RHS
               ; Identifier - int size
                  push qword [rbp - -16]
            ; LHS
               ; Member Accessor Assignment
                  ; LHS
                     ; This keyword
                        push qword [rbp - 8] ; __this
                  ; RHS
                     push qword [.__field____main____Vector__Monkey____size] ; 
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
                        push qword [.__field____main____Vector__Monkey____capacity] ; stored index associated with field that is being accessed
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
                     push qword [.__field____main____Vector__Monkey____data] ; 
                  pop rdi ; rhs
                  pop rbx ; lhs
            pop rdx ; rhs value
            mov qword [rbx + 8*rdi], rdx
            push rdx
         ; Statement results can be ignored
         pop rdx
;---------------------------------------------------------------------------
         mov rax, qword [rbp - 8] ; __this
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
         .__end__ctor____main____Vector__Monkey____Vector__int:
         ; End Constructor Declaration - __ctor____main____Vector__Monkey____Vector__int
;---------------------------------------------------------------------------------

;---------------------------------------------------------------------------------
         ; Method Declaration - Vector<:Monkey:>::pushBack(Monkey) -> void
         jmp .__end__method____main____Vector__Monkey____pushBack__Monkey
         .__method____main____Vector__Monkey____pushBack__Monkey:
         ; Function Header:
         ; Setup stack frame
         push rbp
         mov rbp, rsp
         ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
         sub rsp, 32 ; space for local variables (16-byte aligned)
         ; [rbp - 8] - this - Reference to 'this' object instance
         mov rdx, qword [rbp + 16] ; param passed 'this'
         mov qword [rbp - 8], rdx ; save this to a local
         ; [rbp - 16] - Monkey[] nData (<unset-scope-name>)
         ; [rbp - 24] - int i (<unset-scope-name>)
         ; Parameters
         ; Param: val [rbp + 24] (__main____Vector__Monkey__pushBack__val)
         ; Body
;---------------------------------------------------------------------------
         ; Code Block
;------------------------------------------------------------------------
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
                                 push qword [.__field____main____Vector__Monkey____size] ; stored index associated with field that is being accessed
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
                           push qword [.__field____main____Vector__Monkey____capacity] ; stored index associated with field that is being accessed
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
               je .__endif__27 ; jump to end
            ; Body
      ;------------------------------------------------------------------
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
                                    push qword [.__field____main____Vector__Monkey____capacity] ; stored index associated with field that is being accessed
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
                              push qword [.__field____main____Vector__Monkey____capacity] ; 
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
                                 push qword [.__field____main____Vector__Monkey____capacity] ; stored index associated with field that is being accessed
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
                           mov rax, qword [rbp - 16]  ; __main____Vector__Monkey__pushBack__block__26__if__27__block__28__nData
                     pop rdx ; rhs value
                     mov qword [rbp - 16], rdx
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
                              mov rax, qword [rbp - 24]  ; __main____Vector__Monkey__pushBack__block__26__if__27__block__28__for__29__i
                        pop rdx ; rhs value
                        mov qword [rbp - 24], rdx
                        push rdx
                     ; Loop init result can be discarded
                     pop rax
                  jmp .__forcond__29
.__for__29:
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
.__forcond__29:
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
                                    push qword [.__field____main____Vector__Monkey____size] ; stored index associated with field that is being accessed
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
                        je .__endfor__29
                     ; Body
               ;---------------------------------------------------------
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
                                             push qword [.__field____main____Vector__Monkey____data] ; stored index associated with field that is being accessed
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
                                       ; Identifier - Monkey[] nData
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
               ;---------------------------------------------------------
                     ; Repeat
jmp .__for__29
                     ; End of For
.__endfor__29:
         ;---------------------------------------------------------------
                  ; Free Operator
                     ; RHS
                        ; Member Accessor
                           ; LHS
                              ; This keyword
                                 push qword [rbp - 8] ; __this
                           ; RHS
                              push qword [.__field____main____Vector__Monkey____data] ; stored index associated with field that is being accessed
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
                        ; Identifier - Monkey[] nData
                           push qword [rbp - 16]
                     ; LHS
                        ; Member Accessor Assignment
                           ; LHS
                              ; This keyword
                                 push qword [rbp - 8] ; __this
                           ; RHS
                              push qword [.__field____main____Vector__Monkey____data] ; 
                           pop rdi ; rhs
                           pop rbx ; lhs
                     pop rdx ; rhs value
                     mov qword [rbx + 8*rdi], rdx
                     push rdx
                  ; Statement results can be ignored
                  pop rdx
      ;------------------------------------------------------------------
            jmp .__endif__27 ; jump to end of condition chain
            ; End of if
.__endif__27:
;------------------------------------------------------------------------
         ; Assignment - '='
            ; RHS
               ; Identifier - Monkey val
                  push qword [rbp - -24]
            ; LHS
               ; Subscript assignment
                  ; LHS
                     ; Member Accessor
                        ; LHS
                           ; This keyword
                              push qword [rbp - 8] ; __this
                        ; RHS
                           push qword [.__field____main____Vector__Monkey____data] ; stored index associated with field that is being accessed
                        pop rdx ; rhs
                        pop rax ; lhs
                        push qword [rax + 8*rdx] ; lhs.rhs
                  ; OFFSET
                     ; Member Accessor
                        ; LHS
                           ; This keyword
                              push qword [rbp - 8] ; __this
                        ; RHS
                           push qword [.__field____main____Vector__Monkey____size] ; stored index associated with field that is being accessed
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
                     push qword [.__field____main____Vector__Monkey____size] ; stored index associated with field that is being accessed
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
                     push qword [.__field____main____Vector__Monkey____size] ; size
                  pop rdi ; rhs
                  pop rbx ; lhs
                  mov rax, qword [rbx + 8*rdi]
                  add rax, 1
                  mov qword [rbx + 8*rdi], rax
            push rax ; push result
         ; Statement results can be ignored
         pop rdx
;---------------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
         .__end__method____main____Vector__Monkey____pushBack__Monkey:
         ; End Method Declaration - .__method____main____Vector__Monkey____pushBack__Monkey
;---------------------------------------------------------------------------------

;---------------------------------------------------------------------------------
         ; Method Declaration - Vector<:Monkey:>::popBack() -> Monkey
         jmp .__end__method____main____Vector__Monkey____popBack
         .__method____main____Vector__Monkey____popBack:
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
;---------------------------------------------------------------------------
         ; Code Block
         ; Return
            ; Subscript
               ; LHS
                  ; Member Accessor
                     ; LHS
                        ; This keyword
                           push qword [rbp - 8] ; __this
                     ; RHS
                        push qword [.__field____main____Vector__Monkey____data] ; stored index associated with field that is being accessed
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
                              push qword [.__field____main____Vector__Monkey____size] ; stored index associated with field that is being accessed
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
                              push qword [.__field____main____Vector__Monkey____size] ; size
                           pop rdi ; rhs
                           pop rbx ; lhs
                           mov rax, qword [rbx + 8*rdi]
                           sub rax, 1
                           mov qword [rbx + 8*rdi], rax
                     push rax ; push result
               pop rdx ; __offset
               pop rax ; __pointer
               push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
            pop rax ; return value (Monkey)
            ; Clean up stack and return
            mov rsp, rbp ; remove local vars + unpopped pushes
            pop rbp
            ret
;---------------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
         .__end__method____main____Vector__Monkey____popBack:
         ; End Method Declaration - .__method____main____Vector__Monkey____popBack
;---------------------------------------------------------------------------------

;---------------------------------------------------------------------------------
         ; Method Declaration - Vector<:Monkey:>::clear() -> void
         jmp .__end__method____main____Vector__Monkey____clear
         .__method____main____Vector__Monkey____clear:
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
;---------------------------------------------------------------------------
         ; Code Block
;------------------------------------------------------------------------
         ; While-Loop
.__while__33:
            ; Condition
               ; Greater Than
                  ; LHS
                     ; Member Accessor
                        ; LHS
                           ; This keyword
                              push qword [rbp - 8] ; __this
                        ; RHS
                           push qword [.__field____main____Vector__Monkey____size] ; stored index associated with field that is being accessed
                        pop rdx ; rhs
                        pop rax ; lhs
                        push qword [rax + 8*rdx] ; lhs.rhs
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
               pop rax ; __cond
               cmp rax, 0 ; __cond
               je .__endwhile__33
            ; Body
               ; Method Call - Vector<:Monkey:>::popBack() -> Monkey
                  ; Make space for 0 arg(s) and object parameter
                  sub rsp, 8
                  ; LHS
                     ; This keyword
                        push qword [rbp - 8] ; __this
                     pop rax ; object parameter
                     mov qword [rsp + 0], rax ; place as first parameter
                  ; RHS
                  ; Arguments
                  call .__method____main____Vector__Monkey____popBack
                  ; Remove args
                  add rsp, 8
                  ; Push return value
                  push rax
               ; Statement results can be ignored
               pop rdx
            jmp .__while__33
            ; End of While
.__endwhile__33:
;------------------------------------------------------------------------
;---------------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
         .__end__method____main____Vector__Monkey____clear:
         ; End Method Declaration - .__method____main____Vector__Monkey____clear
;---------------------------------------------------------------------------------

;---------------------------------------------------------------------------------
         ; Method Declaration - Vector<:Monkey:>::get(int) -> Monkey
         jmp .__end__method____main____Vector__Monkey____get__int
         .__method____main____Vector__Monkey____get__int:
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
         ; Param: index [rbp + 24] (__main____Vector__Monkey__get__index)
         ; Body
;---------------------------------------------------------------------------
         ; Code Block
         ; Return
            ; Subscript
               ; LHS
                  ; Member Accessor
                     ; LHS
                        ; This keyword
                           push qword [rbp - 8] ; __this
                     ; RHS
                        push qword [.__field____main____Vector__Monkey____data] ; stored index associated with field that is being accessed
                     pop rdx ; rhs
                     pop rax ; lhs
                     push qword [rax + 8*rdx] ; lhs.rhs
               ; OFFSET
                  ; Identifier - int index
                     push qword [rbp - -24]
               pop rdx ; __offset
               pop rax ; __pointer
               push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
            pop rax ; return value (Monkey)
            ; Clean up stack and return
            mov rsp, rbp ; remove local vars + unpopped pushes
            pop rbp
            ret
;---------------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
         .__end__method____main____Vector__Monkey____get__int:
         ; End Method Declaration - .__method____main____Vector__Monkey____get__int
;---------------------------------------------------------------------------------

;---------------------------------------------------------------------------------
         ; Method Declaration - Vector<:Monkey:>::set(int, Monkey) -> void
         jmp .__end__method____main____Vector__Monkey____set__int__Monkey
         .__method____main____Vector__Monkey____set__int__Monkey:
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
         ; Param: index [rbp + 24] (__main____Vector__Monkey__set__index)
         ; Param: value [rbp + 32] (__main____Vector__Monkey__set__value)
         ; Body
;---------------------------------------------------------------------------
         ; Code Block
         ; Assignment - '='
            ; RHS
               ; Identifier - Monkey value
                  push qword [rbp - -32]
            ; LHS
               ; Subscript assignment
                  ; LHS
                     ; Member Accessor
                        ; LHS
                           ; This keyword
                              push qword [rbp - 8] ; __this
                        ; RHS
                           push qword [.__field____main____Vector__Monkey____data] ; stored index associated with field that is being accessed
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
;---------------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
         .__end__method____main____Vector__Monkey____set__int__Monkey:
         ; End Method Declaration - .__method____main____Vector__Monkey____set__int__Monkey
;---------------------------------------------------------------------------------

.__endclass____main____Vector__Monkey:
         ; End Class Declaration - __main____Vector__Monkey
; ====================================================================================

         ; End Class Template - 
; ==========================================================================================

; ==========================================================================================
         ; Function Template - 
         ; Instances:
; ====================================================================================
         ; Function Declaration - print<:int:>(Vector<:int:>) -> void
         ; Skip over function declaration
         jmp .__end____main____print__int____Vector__tparam0__int
.__main____print__int____Vector__tparam0__int:
         ; Function Header:
         ; Setup stack frame
         push rbp
         mov rbp, rsp
         sub rsp, 16
         ; Parameters
         ; Param: v [rbp + 16]
         ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
         ; [rbp - 8] - int i (<unset-scope-name>)

         ; Body
;------------------------------------------------------------------------------
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
         call __builtin__print__char
         ; Remove args
         add rsp, 8
         ; Push return value
         push rax
         ; Statement results can be ignored
         pop rdx
;---------------------------------------------------------------------------
         ; If-Statement
         ; Condition
            ; Not Equal
               ; LHS
                  ; Member Accessor
                     ; LHS
                        ; Identifier - Vector<:int:> v
                           push qword [rbp - -16]
                     ; RHS
                        push qword [.__field____main____Vector__int____size] ; stored index associated with field that is being accessed
                     pop rdx ; rhs
                     pop rax ; lhs
                     push qword [rax + 8*rdx] ; lhs.rhs
               ; RHS
                  ; Int Literal
                     mov rax, 0
                     push rax
               pop rdx ; rhs
               pop rax ; lhs
               cmp rax, rdx
               setne al
               movzx eax, al
               push rax
            pop rdx ; __cond
            cmp rdx, 0 ; ensure condition is true
            je .__endif__37 ; jump to end
         ; Body
            ; Function Call - print(int) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; Subscript
                        ; LHS
                           ; Member Accessor
                              ; LHS
                                 ; Identifier - Vector<:int:> v
                                    push qword [rbp - -16]
                              ; RHS
                                 push qword [.__field____main____Vector__int____data] ; stored index associated with field that is being accessed
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
               ; Call print(int)
               call __builtin__print__int
               ; Remove args
               add rsp, 8
               ; Push return value
               push rax
            ; Statement results can be ignored
            pop rdx
         jmp .__endif__37 ; jump to end of condition chain
         ; End of if
.__endif__37:
;---------------------------------------------------------------------------
;---------------------------------------------------------------------------
         ; For-Loop
         ; Init
         ; Assignment - '='
            ; RHS
               ; Int Literal
                  mov rax, 1
                  push rax
            ; LHS
               ; Variable Declaration - i
                  mov rax, qword [rbp - 8]  ; __main__print__block__36__for__38__i
            pop rdx ; rhs value
            mov qword [rbp - 8], rdx
            push rdx
         ; Loop init result can be discarded
         pop rax
         jmp .__forcond__38
.__for__38:
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
.__forcond__38:
         ; Condition
            ; Less Than
               ; LHS
                  ; Identifier - int i
                     push qword [rbp - 8]
               ; RHS
                  ; Member Accessor
                     ; LHS
                        ; Identifier - Vector<:int:> v
                           push qword [rbp - -16]
                     ; RHS
                        push qword [.__field____main____Vector__int____size] ; stored index associated with field that is being accessed
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
            je .__endfor__38
         ; Body
   ;---------------------------------------------------------------------
            ; Code Block
               ; Function Call - print(char) -> void
                  ; Make space for 1 arg(s)
                  sub rsp, 8
                  ; Arguments
                     ; Eval arg0
                        ; Char Literal
                           push ','
                     ; Move arg0's result to reverse order position on stack
                     pop rax
                     mov qword [rsp + 0], rax
                  ; Call print(char)
                  call __builtin__print__char
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
                  call __builtin__print__char
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
                              ; Member Accessor
                                 ; LHS
                                    ; Identifier - Vector<:int:> v
                                       push qword [rbp - -16]
                                 ; RHS
                                    push qword [.__field____main____Vector__int____data] ; stored index associated with field that is being accessed
                                 pop rdx ; rhs
                                 pop rax ; lhs
                                 push qword [rax + 8*rdx] ; lhs.rhs
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
                  call __builtin__print__int
                  ; Remove args
                  add rsp, 8
                  ; Push return value
                  push rax
               ; Statement results can be ignored
               pop rdx
   ;---------------------------------------------------------------------
         ; Repeat
jmp .__for__38
         ; End of For
.__endfor__38:
;---------------------------------------------------------------------------
         ; Function Call - print(char) -> void
         ; Make space for 1 arg(s)
         sub rsp, 8
         ; Arguments
            ; Eval arg0
               ; Char Literal
                  push ']'
            ; Move arg0's result to reverse order position on stack
            pop rax
            mov qword [rsp + 0], rax
         ; Call print(char)
         call __builtin__print__char
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
.__end____main____print__int____Vector__tparam0__int:
         ; End Function Declaration - print<:int:>(Vector<:int:>) -> void
; ====================================================================================

         ; End Function Template - 
; ==========================================================================================

; ==========================================================================================
         ; Function Template - 
         ; Instances:
; ====================================================================================
         ; Function Declaration - println<:int:>(Vector<:int:>) -> void
         ; Skip over function declaration
         jmp .__end____main____println__int____Vector__tparam0__int
.__main____println__int____Vector__tparam0__int:
         ; Function Header:
         ; Setup stack frame
         push rbp
         mov rbp, rsp
         sub rsp, 0
         ; Parameters
         ; Param: v [rbp + 16]
         ; Local Variables - Each variable is currently 64-bit (sorry not sorry)

         ; Body
;------------------------------------------------------------------------------
         ; Code Block
         ; Function Call - print<:int:>(Vector<:int:>) -> void
         ; Make space for 1 arg(s)
         sub rsp, 8
         ; Arguments
            ; Eval arg0
               ; Identifier - Vector<:int:> v
                  push qword [rbp - -16]
            ; Move arg0's result to reverse order position on stack
            pop rax
            mov qword [rsp + 0], rax
         ; Call print<:int:>(Vector<:int:>)
         call .__main____print__int____Vector__tparam0__int
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
         call __builtin__println
         ; Remove args
         add rsp, 0
         ; Push return value
         push rax
         ; Statement results can be ignored
         pop rdx
;------------------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
.__end____main____println__int____Vector__tparam0__int:
         ; End Function Declaration - println<:int:>(Vector<:int:>) -> void
; ====================================================================================

         ; End Function Template - 
; ==========================================================================================

; ==========================================================================================
         ; Function Declaration - strlen(char[]) -> int
         ; Skip over function declaration
         jmp .__end____main____strlen__char__1
.__main____strlen__char__1:
         ; Function Header:
         ; Setup stack frame
         push rbp
         mov rbp, rsp
         sub rsp, 16
         ; Parameters
         ; Param: str [rbp + 16]
         ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
         ; [rbp - 8] - int size (<unset-scope-name>)

         ; Body
;------------------------------------------------------------------------------------
         ; Code Block
;---------------------------------------------------------------------------------
         ; If-Statement
         ; Condition
         ; Equal
         ; LHS
            ; Identifier - char[] str
               push qword [rbp - -16]
         ; RHS
            ; Null Literal
               push 0
         pop rdx ; rhs
         pop rax ; lhs
         cmp rax, rdx
         sete al
         movzx eax, al
         push rax
         pop rdx ; __cond
         cmp rdx, 0 ; ensure condition is true
         je .__endif__42 ; jump to end
         ; Body
         ; Return
         ; Negative - int
            ; RHS
               ; Int Literal
                  mov rax, 1
                  push rax
            pop rdx
            ; val = 0 - val
            mov rax, 0
            sub rax, rdx
            push rax ; push result
         pop rax ; return value (int)
         ; Clean up stack and return
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
         jmp .__endif__42 ; jump to end of condition chain
         ; End of if
.__endif__42:
;---------------------------------------------------------------------------------
         ; Assignment - '='
         ; RHS
         ; Int Literal
         mov rax, 0
         push rax
         ; LHS
         ; Variable Declaration - size
         mov rax, qword [rbp - 8]  ; __main__strlen__block__41__size
         pop rdx ; rhs value
         mov qword [rbp - 8], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
;---------------------------------------------------------------------------------
         ; While-Loop
.__while__43:
         ; Condition
         ; Not Equal
         ; LHS
            ; Subscript
               ; LHS
                  ; Identifier - char[] str
                     push qword [rbp - -16]
               ; OFFSET
                  ; Post-Increment
                     mov rax, qword [rbp - 8]
                     add qword [rbp - 8], 1
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
         je .__endwhile__43
         ; Body
         jmp .__while__43
         ; End of While
.__endwhile__43:
;---------------------------------------------------------------------------------
         ; Return
         ; Subtraction - int, int
         ; LHS
         ; Identifier - int size
            push qword [rbp - 8]
         ; RHS
         ; Int Literal
            mov rax, 1
            push rax
         pop rdx ; rhs
         pop rax ; lhs
         sub rax, rdx
         push rax
         pop rax ; return value (int)
         ; Clean up stack and return
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
;------------------------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
.__end____main____strlen__char__1:
         ; End Function Declaration - strlen(char[]) -> int
; ==========================================================================================

; ==========================================================================================
         ; Function Declaration - strcmp(char[], char[]) -> int
         ; Skip over function declaration
         jmp .__end____main____strcmp__char__1__char__1
.__main____strcmp__char__1__char__1:
         ; Function Header:
         ; Setup stack frame
         push rbp
         mov rbp, rsp
         sub rsp, 32
         ; Parameters
         ; Param: a [rbp + 16]
         ; Param: b [rbp + 24]
         ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
         ; [rbp - 8] - int asize (<unset-scope-name>)
         ; [rbp - 16] - int bsize (<unset-scope-name>)
         ; [rbp - 24] - int i (<unset-scope-name>)

         ; Body
;------------------------------------------------------------------------------------
         ; Code Block
         ; Assignment - '='
         ; RHS
         ; Function Call - strlen(char[]) -> int
         ; Make space for 1 arg(s)
         sub rsp, 8
         ; Arguments
            ; Eval arg0
               ; Identifier - char[] a
                  push qword [rbp - -16]
            ; Move arg0's result to reverse order position on stack
            pop rax
            mov qword [rsp + 0], rax
         ; Call strlen(char[])
         call .__main____strlen__char__1
         ; Remove args
         add rsp, 8
         ; Push return value
         push rax
         ; LHS
         ; Variable Declaration - asize
         mov rax, qword [rbp - 8]  ; __main__strcmp__block__44__asize
         pop rdx ; rhs value
         mov qword [rbp - 8], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
         ; RHS
         ; Function Call - strlen(char[]) -> int
         ; Make space for 1 arg(s)
         sub rsp, 8
         ; Arguments
            ; Eval arg0
               ; Identifier - char[] b
                  push qword [rbp - -24]
            ; Move arg0's result to reverse order position on stack
            pop rax
            mov qword [rsp + 0], rax
         ; Call strlen(char[])
         call .__main____strlen__char__1
         ; Remove args
         add rsp, 8
         ; Push return value
         push rax
         ; LHS
         ; Variable Declaration - bsize
         mov rax, qword [rbp - 16]  ; __main__strcmp__block__44__bsize
         pop rdx ; rhs value
         mov qword [rbp - 16], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
;---------------------------------------------------------------------------------
         ; If-Statement
         ; Condition
         ; Not Equal
         ; LHS
            ; Identifier - int asize
               push qword [rbp - 8]
         ; RHS
            ; Identifier - int bsize
               push qword [rbp - 16]
         pop rdx ; rhs
         pop rax ; lhs
         cmp rax, rdx
         setne al
         movzx eax, al
         push rax
         pop rdx ; __cond
         cmp rdx, 0 ; ensure condition is true
         je .__endif__45 ; jump to end
         ; Body
         ; Return
         ; Int Literal
            mov rax, 0
            push rax
         pop rax ; return value (int)
         ; Clean up stack and return
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
         jmp .__endif__45 ; jump to end of condition chain
         ; End of if
.__endif__45:
;---------------------------------------------------------------------------------
;---------------------------------------------------------------------------------
         ; For-Loop
         ; Init
         ; Assignment - '='
         ; RHS
         ; Int Literal
            mov rax, 0
            push rax
         ; LHS
         ; Variable Declaration - i
            mov rax, qword [rbp - 24]  ; __main__strcmp__block__44__for__46__i
         pop rdx ; rhs value
         mov qword [rbp - 24], rdx
         push rdx
         ; Loop init result can be discarded
         pop rax
         jmp .__forcond__46
.__for__46:
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
.__forcond__46:
         ; Condition
         ; Less Than
         ; LHS
            ; Identifier - int i
               push qword [rbp - 24]
         ; RHS
            ; Identifier - int asize
               push qword [rbp - 8]
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
;---------------------------------------------------------------------------
         ; Code Block
;------------------------------------------------------------------------
         ; If-Statement
            ; Condition
               ; Not Equal
                  ; LHS
                     ; Subscript
                        ; LHS
                           ; Identifier - char[] a
                              push qword [rbp - -16]
                        ; OFFSET
                           ; Identifier - int i
                              push qword [rbp - 24]
                        pop rdx ; __offset
                        pop rax ; __pointer
                        mov al, byte [rax + rdx] ; pointer + sizeof(data_t) * offset
                        movzx rax, al ; zero extend because we need to push 64bit to stack
                        push rax ; push char onto stack
                  ; RHS
                     ; Subscript
                        ; LHS
                           ; Identifier - char[] b
                              push qword [rbp - -24]
                        ; OFFSET
                           ; Identifier - int i
                              push qword [rbp - 24]
                        pop rdx ; __offset
                        pop rax ; __pointer
                        mov al, byte [rax + rdx] ; pointer + sizeof(data_t) * offset
                        movzx rax, al ; zero extend because we need to push 64bit to stack
                        push rax ; push char onto stack
                  pop rdx ; rhs
                  pop rax ; lhs
                  cmp rax, rdx
                  setne al
                  movzx eax, al
                  push rax
               pop rdx ; __cond
               cmp rdx, 0 ; ensure condition is true
               je .__endif__48 ; jump to end
            ; Body
      ;------------------------------------------------------------------
               ; Code Block
                  ; Return
                     ; Int Literal
                        mov rax, 0
                        push rax
                     pop rax ; return value (int)
                     ; Clean up stack and return
                     mov rsp, rbp ; remove local vars + unpopped pushes
                     pop rbp
                     ret
      ;------------------------------------------------------------------
            jmp .__endif__48 ; jump to end of condition chain
            ; End of if
.__endif__48:
;------------------------------------------------------------------------
;---------------------------------------------------------------------------
         ; Repeat
jmp .__for__46
         ; End of For
.__endfor__46:
;---------------------------------------------------------------------------------
         ; Return
         ; Int Literal
         mov rax, 1
         push rax
         pop rax ; return value (int)
         ; Clean up stack and return
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
;------------------------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
.__end____main____strcmp__char__1__char__1:
         ; End Function Declaration - strcmp(char[], char[]) -> int
; ==========================================================================================

; ==========================================================================================
         ; Function Declaration - substr(char[], int, int) -> char[]
         ; Skip over function declaration
         jmp .__end____main____substr__char__1__int__int
.__main____substr__char__1__int__int:
         ; Function Header:
         ; Setup stack frame
         push rbp
         mov rbp, rsp
         sub rsp, 16
         ; Parameters
         ; Param: a [rbp + 16]
         ; Param: start [rbp + 24]
         ; Param: end [rbp + 32]
         ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
         ; [rbp - 8] - char[] res (<unset-scope-name>)
         ; [rbp - 16] - int i (<unset-scope-name>)

         ; Body
;------------------------------------------------------------------------------------
         ; Code Block
         ; Assignment - '='
         ; RHS
         ; Array Allocator
         ; Addition - int, int
            ; LHS
               ; Subtraction - int, int
                  ; LHS
                     ; Identifier - int end
                        push qword [rbp - -32]
                  ; RHS
                     ; Identifier - int start
                        push qword [rbp - -24]
                  pop rdx ; rhs
                  pop rax ; lhs
                  sub rax, rdx
                  push rax
            ; RHS
               ; Int Literal
                  mov rax, 1
                  push rax
            pop rdx ; rhs
            pop rax ; lhs
            add rax, rdx
            push rax
         pop rdx ; num elements for dimension[0]
         mov rdi, rdx ; num bytes to allocate (1 byte per element)
         call malloc ; allocates edi bytes on heap and stores pointer in rax
         push rax ; __ptr
         ; LHS
         ; Variable Declaration - res
         mov rax, qword [rbp - 8]  ; __main__substr__block__50__res
         pop rdx ; rhs value
         mov qword [rbp - 8], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
;---------------------------------------------------------------------------------
         ; For-Loop
         ; Init
         ; Assignment - '='
         ; RHS
         ; Int Literal
            mov rax, 0
            push rax
         ; LHS
         ; Variable Declaration - i
            mov rax, qword [rbp - 16]  ; __main__substr__block__50__for__51__i
         pop rdx ; rhs value
         mov qword [rbp - 16], rdx
         push rdx
         ; Loop init result can be discarded
         pop rax
         jmp .__forcond__51
.__for__51:
         ; Update
         ; Pre-Increment - int
         ; RHS
            ; Identifier - int i
               push qword [rbp - 16]
         pop rdx
         add qword [rbp - 16], 1
         mov rax, qword [rbp - 16]
         push rax ; push result
         ; Loop update result can be discarded
         pop rax
.__forcond__51:
         ; Condition
         ; Less Than
         ; LHS
            ; Identifier - int i
               push qword [rbp - 16]
         ; RHS
            ; Subtraction - int, int
               ; LHS
                  ; Identifier - int end
                     push qword [rbp - -32]
               ; RHS
                  ; Identifier - int start
                     push qword [rbp - -24]
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
         je .__endfor__51
         ; Body
;---------------------------------------------------------------------------
         ; Code Block
         ; Assignment - '='
            ; RHS
               ; Subscript
                  ; LHS
                     ; Identifier - char[] a
                        push qword [rbp - -16]
                  ; OFFSET
                     ; Addition - int, int
                        ; LHS
                           ; Identifier - int i
                              push qword [rbp - 16]
                        ; RHS
                           ; Identifier - int start
                              push qword [rbp - -24]
                        pop rdx ; rhs
                        pop rax ; lhs
                        add rax, rdx
                        push rax
                  pop rdx ; __offset
                  pop rax ; __pointer
                  mov al, byte [rax + rdx] ; pointer + sizeof(data_t) * offset
                  movzx rax, al ; zero extend because we need to push 64bit to stack
                  push rax ; push char onto stack
            ; LHS
               ; Subscript assignment
                  ; LHS
                     ; Identifier - char[] res
                        push qword [rbp - 8]
                  ; OFFSET
                     ; Identifier - int i
                        push qword [rbp - 16]
                  pop rdi ; __offset
                  pop rbx ; __pointer
            pop rdx ; rhs value
            mov byte [rbx + rdi], dl
            push rdx
         ; Statement results can be ignored
         pop rdx
;---------------------------------------------------------------------------
         ; Repeat
jmp .__for__51
         ; End of For
.__endfor__51:
;---------------------------------------------------------------------------------
         ; Assignment - '='
         ; RHS
         ; Char Literal
         push 0 ; \0
         ; LHS
         ; Subscript assignment
         ; LHS
            ; Identifier - char[] res
               push qword [rbp - 8]
         ; OFFSET
            ; Subtraction - int, int
               ; LHS
                  ; Identifier - int end
                     push qword [rbp - -32]
               ; RHS
                  ; Identifier - int start
                     push qword [rbp - -24]
               pop rdx ; rhs
               pop rax ; lhs
               sub rax, rdx
               push rax
         pop rdi ; __offset
         pop rbx ; __pointer
         pop rdx ; rhs value
         mov byte [rbx + rdi], dl
         push rdx
         ; Statement results can be ignored
         pop rdx
         ; Return
         ; Identifier - char[] res
         push qword [rbp - 8]
         pop rax ; return value (char[])
         ; Clean up stack and return
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
;------------------------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
.__end____main____substr__char__1__int__int:
         ; End Function Declaration - substr(char[], int, int) -> char[]
; ==========================================================================================

; ==========================================================================================
         ; Function Declaration - first_index_of(char[], char) -> int
         ; Skip over function declaration
         jmp .__end____main____first_index_of__char__1__char
.__main____first_index_of__char__1__char:
         ; Function Header:
         ; Setup stack frame
         push rbp
         mov rbp, rsp
         sub rsp, 16
         ; Parameters
         ; Param: arr [rbp + 16]
         ; Param: c [rbp + 24]
         ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
         ; [rbp - 8] - int size (<unset-scope-name>)
         ; [rbp - 16] - int i (<unset-scope-name>)

         ; Body
;------------------------------------------------------------------------------------
         ; Code Block
         ; Assignment - '='
         ; RHS
         ; Function Call - strlen(char[]) -> int
         ; Make space for 1 arg(s)
         sub rsp, 8
         ; Arguments
            ; Eval arg0
               ; Identifier - char[] arr
                  push qword [rbp - -16]
            ; Move arg0's result to reverse order position on stack
            pop rax
            mov qword [rsp + 0], rax
         ; Call strlen(char[])
         call .__main____strlen__char__1
         ; Remove args
         add rsp, 8
         ; Push return value
         push rax
         ; LHS
         ; Variable Declaration - size
         mov rax, qword [rbp - 8]  ; __main__first_index_of__block__53__size
         pop rdx ; rhs value
         mov qword [rbp - 8], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
;---------------------------------------------------------------------------------
         ; For-Loop
         ; Init
         ; Assignment - '='
         ; RHS
         ; Int Literal
            mov rax, 0
            push rax
         ; LHS
         ; Variable Declaration - i
            mov rax, qword [rbp - 16]  ; __main__first_index_of__block__53__for__54__i
         pop rdx ; rhs value
         mov qword [rbp - 16], rdx
         push rdx
         ; Loop init result can be discarded
         pop rax
         jmp .__forcond__54
.__for__54:
         ; Update
         ; Pre-Increment - int
         ; RHS
            ; Identifier - int i
               push qword [rbp - 16]
         pop rdx
         add qword [rbp - 16], 1
         mov rax, qword [rbp - 16]
         push rax ; push result
         ; Loop update result can be discarded
         pop rax
.__forcond__54:
         ; Condition
         ; Less Than
         ; LHS
            ; Identifier - int i
               push qword [rbp - 16]
         ; RHS
            ; Identifier - int size
               push qword [rbp - 8]
         pop rdx ; rhs
         pop rax ; lhs
         cmp rax, rdx
         setl al
         movzx eax, al
         push rax
         pop rax ; __cond
         cmp rax, 0 ; __cond
         je .__endfor__54
         ; Body
;---------------------------------------------------------------------------
         ; Code Block
;------------------------------------------------------------------------
         ; If-Statement
            ; Condition
               ; Equal
                  ; LHS
                     ; Subscript
                        ; LHS
                           ; Identifier - char[] arr
                              push qword [rbp - -16]
                        ; OFFSET
                           ; Identifier - int i
                              push qword [rbp - 16]
                        pop rdx ; __offset
                        pop rax ; __pointer
                        mov al, byte [rax + rdx] ; pointer + sizeof(data_t) * offset
                        movzx rax, al ; zero extend because we need to push 64bit to stack
                        push rax ; push char onto stack
                  ; RHS
                     ; Identifier - char c
                        mov al, byte [rbp - -24]
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
               je .__endif__56 ; jump to end
            ; Body
               ; Return
                  ; Identifier - int i
                     push qword [rbp - 16]
                  pop rax ; return value (int)
                  ; Clean up stack and return
                  mov rsp, rbp ; remove local vars + unpopped pushes
                  pop rbp
                  ret
            jmp .__endif__56 ; jump to end of condition chain
            ; End of if
.__endif__56:
;------------------------------------------------------------------------
;---------------------------------------------------------------------------
         ; Repeat
jmp .__for__54
         ; End of For
.__endfor__54:
;---------------------------------------------------------------------------------
         ; Return
         ; Negative - int
         ; RHS
         ; Int Literal
            mov rax, 1
            push rax
         pop rdx
         ; val = 0 - val
         mov rax, 0
         sub rax, rdx
         push rax ; push result
         pop rax ; return value (int)
         ; Clean up stack and return
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
;------------------------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
.__end____main____first_index_of__char__1__char:
         ; End Function Declaration - first_index_of(char[], char) -> int
; ==========================================================================================

; ==========================================================================================
         ; Function Declaration - split(char[], char) -> Vector<:char[]:>
         ; Skip over function declaration
         jmp .__end____main____split__char__1__char
.__main____split__char__1__char:
         ; Function Header:
         ; Setup stack frame
         push rbp
         mov rbp, rsp
         sub rsp, 64
         ; Parameters
         ; Param: str [rbp + 16]
         ; Param: delim [rbp + 24]
         ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
         ; [rbp - 8] - Vector<:char[]:> tokens (<unset-scope-name>)
         ; [rbp - 16] - int size (<unset-scope-name>)
         ; [rbp - 24] - int i (<unset-scope-name>)
         ; [rbp - 32] - int j (<unset-scope-name>)
         ; [rbp - 40] - int count (<unset-scope-name>)
         ; [rbp - 48] - int k (<unset-scope-name>)
         ; [rbp - 56] - int k (<unset-scope-name>)

         ; Body
;------------------------------------------------------------------------------------
         ; Code Block
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
         ; Variable Declaration - tokens
         mov rax, qword [rbp - 8]  ; __main__split__block__57__tokens
         pop rdx ; rhs value
         mov qword [rbp - 8], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
         ; RHS
         ; Function Call - strlen(char[]) -> int
         ; Make space for 1 arg(s)
         sub rsp, 8
         ; Arguments
            ; Eval arg0
               ; Identifier - char[] str
                  push qword [rbp - -16]
            ; Move arg0's result to reverse order position on stack
            pop rax
            mov qword [rsp + 0], rax
         ; Call strlen(char[])
         call .__main____strlen__char__1
         ; Remove args
         add rsp, 8
         ; Push return value
         push rax
         ; LHS
         ; Variable Declaration - size
         mov rax, qword [rbp - 16]  ; __main__split__block__57__size
         pop rdx ; rhs value
         mov qword [rbp - 16], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
         ; RHS
         ; Int Literal
         mov rax, 0
         push rax
         ; LHS
         ; Variable Declaration - i
         mov rax, qword [rbp - 24]  ; __main__split__block__57__i
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
         ; Variable Declaration - j
         mov rax, qword [rbp - 32]  ; __main__split__block__57__j
         pop rdx ; rhs value
         mov qword [rbp - 32], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
;---------------------------------------------------------------------------------
         ; While-Loop
.__while__58:
         ; Condition
         ; Less Than
         ; LHS
            ; Identifier - int i
               push qword [rbp - 24]
         ; RHS
            ; Identifier - int size
               push qword [rbp - 16]
         pop rdx ; rhs
         pop rax ; lhs
         cmp rax, rdx
         setl al
         movzx eax, al
         push rax
         pop rax ; __cond
         cmp rax, 0 ; __cond
         je .__endwhile__58
         ; Body
;---------------------------------------------------------------------------
         ; Code Block
;------------------------------------------------------------------------
         ; If-Statement
            ; Condition
               ; Not Equal
                  ; LHS
                     ; Subscript
                        ; LHS
                           ; Identifier - char[] str
                              push qword [rbp - -16]
                        ; OFFSET
                           ; Identifier - int i
                              push qword [rbp - 24]
                        pop rdx ; __offset
                        pop rax ; __pointer
                        mov al, byte [rax + rdx] ; pointer + sizeof(data_t) * offset
                        movzx rax, al ; zero extend because we need to push 64bit to stack
                        push rax ; push char onto stack
                  ; RHS
                     ; Identifier - char delim
                        mov al, byte [rbp - -24]
                        movzx rax, al
                        push rax
                  pop rdx ; rhs
                  pop rax ; lhs
                  cmp rax, rdx
                  setne al
                  movzx eax, al
                  push rax
               pop rdx ; __cond
               cmp rdx, 0 ; ensure condition is true
               je .__endif__60 ; jump to end
            ; Body
      ;------------------------------------------------------------------
               ; Code Block
                  ; Assignment - '='
                     ; RHS
                        ; Int Literal
                           mov rax, 0
                           push rax
                     ; LHS
                        ; Variable Declaration - count
                           mov rax, qword [rbp - 40]  ; __main__split__block__57__while__58__block__59__if__60__block__61__count
                     pop rdx ; rhs value
                     mov qword [rbp - 40], rdx
                     push rdx
                  ; Statement results can be ignored
                  pop rdx
                  ; Assignment - '='
                     ; RHS
                        ; Identifier - int i
                           push qword [rbp - 24]
                     ; LHS
                        ; Variable Declaration - k
                           mov rax, qword [rbp - 48]  ; __main__split__block__57__while__58__block__59__if__60__block__61__k
                     pop rdx ; rhs value
                     mov qword [rbp - 48], rdx
                     push rdx
                  ; Statement results can be ignored
                  pop rdx
         ;---------------------------------------------------------------
                  ; While-Loop
.__while__62:
                     ; Condition
                        ; Less Than
                           ; LHS
                              ; Identifier - int k
                                 push qword [rbp - 48]
                           ; RHS
                              ; Identifier - int size
                                 push qword [rbp - 16]
                           pop rdx ; rhs
                           pop rax ; lhs
                           cmp rax, rdx
                           setl al
                           movzx eax, al
                           push rax
                        pop rax ; __cond
                        cmp rax, 0 ; __cond
                        je .__endwhile__62
                     ; Body
               ;---------------------------------------------------------
                        ; If-Statement
                           ; Condition
                              ; Not Equal
                                 ; LHS
                                    ; Subscript
                                       ; LHS
                                          ; Identifier - char[] str
                                             push qword [rbp - -16]
                                       ; OFFSET
                                          ; Post-Increment
                                             mov rax, qword [rbp - 48]
                                             add qword [rbp - 48], 1
                                             push rax
                                       pop rdx ; __offset
                                       pop rax ; __pointer
                                       mov al, byte [rax + rdx] ; pointer + sizeof(data_t) * offset
                                       movzx rax, al ; zero extend because we need to push 64bit to stack
                                       push rax ; push char onto stack
                                 ; RHS
                                    ; Identifier - char delim
                                       mov al, byte [rbp - -24]
                                       movzx rax, al
                                       push rax
                                 pop rdx ; rhs
                                 pop rax ; lhs
                                 cmp rax, rdx
                                 setne al
                                 movzx eax, al
                                 push rax
                              pop rdx ; __cond
                              cmp rdx, 0 ; ensure condition is true
                              je .__else__63 ; jump to else
                           ; Body
                              ; Pre-Increment - int
                                 ; RHS
                                    ; Identifier - int count
                                       push qword [rbp - 40]
                                 pop rdx
                                 add qword [rbp - 40], 1
                                 mov rax, qword [rbp - 40]
                                 push rax ; push result
                              ; Statement results can be ignored
                              pop rdx
                           jmp .__endif__63 ; jump to end of condition chain
                  ;------------------------------------------------------
                           ; Else-Statement
.__else__63:
                           ; Break out of __while__62
                           jmp .__endwhile__62
                  ;------------------------------------------------------
                           ; End of if
.__endif__63:
               ;---------------------------------------------------------
                     jmp .__while__62
                     ; End of While
.__endwhile__62:
         ;---------------------------------------------------------------
                  ; Method Call - Vector<:char[]:>::pushBack(char[]) -> void
                     ; Make space for 1 arg(s) and object parameter
                     sub rsp, 16
                     ; LHS
                        ; Identifier - Vector<:char[]:> tokens
                           push qword [rbp - 8]
                        pop rax ; object parameter
                        mov qword [rsp + 0], rax ; place as first parameter
                     ; RHS
                     ; Arguments
                        ; Eval arg0
                           ; Array Allocator
                              ; Addition - int, int
                                 ; LHS
                                    ; Identifier - int count
                                       push qword [rbp - 40]
                                 ; RHS
                                    ; Int Literal
                                       mov rax, 1
                                       push rax
                                 pop rdx ; rhs
                                 pop rax ; lhs
                                 add rax, rdx
                                 push rax
                              pop rdx ; num elements for dimension[0]
                              mov rdi, rdx ; num bytes to allocate (1 byte per element)
                              call malloc ; allocates edi bytes on heap and stores pointer in rax
                              push rax ; __ptr
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
         ;---------------------------------------------------------------
                  ; For-Loop
                  ; Init
                     ; Assignment - '='
                        ; RHS
                           ; Int Literal
                              mov rax, 0
                              push rax
                        ; LHS
                           ; Variable Declaration - k
                              mov rax, qword [rbp - 56]  ; __main__split__block__57__while__58__block__59__if__60__block__61__for__64__k
                        pop rdx ; rhs value
                        mov qword [rbp - 56], rdx
                        push rdx
                     ; Loop init result can be discarded
                     pop rax
                  jmp .__forcond__64
.__for__64:
                     ; Update
                        ; Pre-Increment - int
                           ; RHS
                              ; Identifier - int k
                                 push qword [rbp - 56]
                           pop rdx
                           add qword [rbp - 56], 1
                           mov rax, qword [rbp - 56]
                           push rax ; push result
                        ; Loop update result can be discarded
                        pop rax
.__forcond__64:
                     ; Condition
                        ; Less Than
                           ; LHS
                              ; Identifier - int k
                                 push qword [rbp - 56]
                           ; RHS
                              ; Identifier - int count
                                 push qword [rbp - 40]
                           pop rdx ; rhs
                           pop rax ; lhs
                           cmp rax, rdx
                           setl al
                           movzx eax, al
                           push rax
                        pop rax ; __cond
                        cmp rax, 0 ; __cond
                        je .__endfor__64
                     ; Body
               ;---------------------------------------------------------
                        ; Code Block
                           ; Assignment - '='
                              ; RHS
                                 ; Subscript
                                    ; LHS
                                       ; Identifier - char[] str
                                          push qword [rbp - -16]
                                    ; OFFSET
                                       ; Post-Increment
                                          mov rax, qword [rbp - 24]
                                          add qword [rbp - 24], 1
                                          push rax
                                    pop rdx ; __offset
                                    pop rax ; __pointer
                                    mov al, byte [rax + rdx] ; pointer + sizeof(data_t) * offset
                                    movzx rax, al ; zero extend because we need to push 64bit to stack
                                    push rax ; push char onto stack
                              ; LHS
                                 ; Subscript assignment
                                    ; LHS
                                       ; Subscript
                                          ; LHS
                                             ; Member Accessor
                                                ; LHS
                                                   ; Identifier - Vector<:char[]:> tokens
                                                      push qword [rbp - 8]
                                                ; RHS
                                                   push qword [.__field____main____Vector__char__1____data] ; stored index associated with field that is being accessed
                                                pop rdx ; rhs
                                                pop rax ; lhs
                                                push qword [rax + 8*rdx] ; lhs.rhs
                                          ; OFFSET
                                             ; Identifier - int j
                                                push qword [rbp - 32]
                                          pop rdx ; __offset
                                          pop rax ; __pointer
                                          push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                                    ; OFFSET
                                       ; Identifier - int k
                                          push qword [rbp - 56]
                                    pop rdi ; __offset
                                    pop rbx ; __pointer
                              pop rdx ; rhs value
                              mov byte [rbx + rdi], dl
                              push rdx
                           ; Statement results can be ignored
                           pop rdx
               ;---------------------------------------------------------
                     ; Repeat
jmp .__for__64
                     ; End of For
.__endfor__64:
         ;---------------------------------------------------------------
                  ; Assignment - '='
                     ; RHS
                        ; Char Literal
                           push 0 ; \0
                     ; LHS
                        ; Subscript assignment
                           ; LHS
                              ; Subscript
                                 ; LHS
                                    ; Member Accessor
                                       ; LHS
                                          ; Identifier - Vector<:char[]:> tokens
                                             push qword [rbp - 8]
                                       ; RHS
                                          push qword [.__field____main____Vector__char__1____data] ; stored index associated with field that is being accessed
                                       pop rdx ; rhs
                                       pop rax ; lhs
                                       push qword [rax + 8*rdx] ; lhs.rhs
                                 ; OFFSET
                                    ; Identifier - int j
                                       push qword [rbp - 32]
                                 pop rdx ; __offset
                                 pop rax ; __pointer
                                 push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                           ; OFFSET
                              ; Identifier - int count
                                 push qword [rbp - 40]
                           pop rdi ; __offset
                           pop rbx ; __pointer
                     pop rdx ; rhs value
                     mov byte [rbx + rdi], dl
                     push rdx
                  ; Statement results can be ignored
                  pop rdx
                  ; Pre-Increment - int
                     ; RHS
                        ; Identifier - int j
                           push qword [rbp - 32]
                     pop rdx
                     add qword [rbp - 32], 1
                     mov rax, qword [rbp - 32]
                     push rax ; push result
                  ; Statement results can be ignored
                  pop rdx
      ;------------------------------------------------------------------
            jmp .__endif__60 ; jump to end of condition chain
            ; End of if
.__endif__60:
;------------------------------------------------------------------------
         ; Pre-Increment - int
            ; RHS
               ; Identifier - int i
                  push qword [rbp - 24]
            pop rdx
            add qword [rbp - 24], 1
            mov rax, qword [rbp - 24]
            push rax ; push result
         ; Statement results can be ignored
         pop rdx
;---------------------------------------------------------------------------
         jmp .__while__58
         ; End of While
.__endwhile__58:
;---------------------------------------------------------------------------------
         ; Return
         ; Identifier - Vector<:char[]:> tokens
         push qword [rbp - 8]
         pop rax ; return value (Vector<:char[]:>)
         ; Clean up stack and return
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
;------------------------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
.__end____main____split__char__1__char:
         ; End Function Declaration - split(char[], char) -> Vector<:char[]:>
; ==========================================================================================

; ==========================================================================================
         ; Function Declaration - max(int, int) -> int
         ; Skip over function declaration
         jmp .__end____main____max__int__int
.__main____max__int__int:
         ; Function Header:
         ; Setup stack frame
         push rbp
         mov rbp, rsp
         sub rsp, 0
         ; Parameters
         ; Param: a [rbp + 16]
         ; Param: b [rbp + 24]
         ; Local Variables - Each variable is currently 64-bit (sorry not sorry)

         ; Body
;------------------------------------------------------------------------------------
         ; Code Block
;---------------------------------------------------------------------------------
         ; If-Statement
         ; Condition
         ; Greater Than or Equal to
         ; LHS
            ; Identifier - int a
               push qword [rbp - -16]
         ; RHS
            ; Identifier - int b
               push qword [rbp - -24]
         pop rdx ; rhs
         pop rax ; lhs
         cmp rax, rdx
         setge al
         movzx eax, al
         push rax
         pop rdx ; __cond
         cmp rdx, 0 ; ensure condition is true
         je .__endif__67 ; jump to end
         ; Body
         ; Return
         ; Identifier - int a
            push qword [rbp - -16]
         pop rax ; return value (int)
         ; Clean up stack and return
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
         jmp .__endif__67 ; jump to end of condition chain
         ; End of if
.__endif__67:
;---------------------------------------------------------------------------------
         ; Return
         ; Identifier - int b
         push qword [rbp - -24]
         pop rax ; return value (int)
         ; Clean up stack and return
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
;------------------------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
.__end____main____max__int__int:
         ; End Function Declaration - max(int, int) -> int
; ==========================================================================================

; ==========================================================================================
         ; Function Declaration - max(float, float) -> float
         ; Skip over function declaration
         jmp .__end____main____max__float__float
.__main____max__float__float:
         ; Function Header:
         ; Setup stack frame
         push rbp
         mov rbp, rsp
         sub rsp, 0
         ; Parameters
         ; Param: a [rbp + 16]
         ; Param: b [rbp + 24]
         ; Local Variables - Each variable is currently 64-bit (sorry not sorry)

         ; Body
;------------------------------------------------------------------------------------
         ; Code Block
;---------------------------------------------------------------------------------
         ; If-Statement
         ; Condition
         ; Greater Than or Equal to
         ; LHS
            ; Identifier - float a
               push qword [rbp - -16]
         ; RHS
            ; Identifier - float b
               push qword [rbp - -24]
         pop rdx ; rhs
         pop rax ; lhs
         cmp rax, rdx
         setge al
         movzx eax, al
         push rax
         pop rdx ; __cond
         cmp rdx, 0 ; ensure condition is true
         je .__endif__69 ; jump to end
         ; Body
         ; Return
         ; Identifier - float a
            push qword [rbp - -16]
         pop rax ; return value (float)
         movq xmm0, rax ; xmm0 is used for float return values
         ; Clean up stack and return
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
         jmp .__endif__69 ; jump to end of condition chain
         ; End of if
.__endif__69:
;---------------------------------------------------------------------------------
         ; Return
         ; Identifier - float b
         push qword [rbp - -24]
         pop rax ; return value (float)
         movq xmm0, rax ; xmm0 is used for float return values
         ; Clean up stack and return
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
;------------------------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
.__end____main____max__float__float:
         ; End Function Declaration - max(float, float) -> float
; ==========================================================================================

; ==========================================================================================
         ; Function Declaration - min(int, int) -> int
         ; Skip over function declaration
         jmp .__end____main____min__int__int
.__main____min__int__int:
         ; Function Header:
         ; Setup stack frame
         push rbp
         mov rbp, rsp
         sub rsp, 0
         ; Parameters
         ; Param: a [rbp + 16]
         ; Param: b [rbp + 24]
         ; Local Variables - Each variable is currently 64-bit (sorry not sorry)

         ; Body
;------------------------------------------------------------------------------------
         ; Code Block
;---------------------------------------------------------------------------------
         ; If-Statement
         ; Condition
         ; Less Than or Equal to
         ; LHS
            ; Identifier - int a
               push qword [rbp - -16]
         ; RHS
            ; Identifier - int b
               push qword [rbp - -24]
         pop rdx ; rhs
         pop rax ; lhs
         cmp rax, rdx
         setle al
         movzx eax, al
         push rax
         pop rdx ; __cond
         cmp rdx, 0 ; ensure condition is true
         je .__endif__71 ; jump to end
         ; Body
         ; Return
         ; Identifier - int a
            push qword [rbp - -16]
         pop rax ; return value (int)
         ; Clean up stack and return
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
         jmp .__endif__71 ; jump to end of condition chain
         ; End of if
.__endif__71:
;---------------------------------------------------------------------------------
         ; Return
         ; Identifier - int b
         push qword [rbp - -24]
         pop rax ; return value (int)
         ; Clean up stack and return
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
;------------------------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
.__end____main____min__int__int:
         ; End Function Declaration - min(int, int) -> int
; ==========================================================================================

; ==========================================================================================
         ; Function Declaration - min(float, float) -> float
         ; Skip over function declaration
         jmp .__end____main____min__float__float
.__main____min__float__float:
         ; Function Header:
         ; Setup stack frame
         push rbp
         mov rbp, rsp
         sub rsp, 0
         ; Parameters
         ; Param: a [rbp + 16]
         ; Param: b [rbp + 24]
         ; Local Variables - Each variable is currently 64-bit (sorry not sorry)

         ; Body
;------------------------------------------------------------------------------------
         ; Code Block
;---------------------------------------------------------------------------------
         ; If-Statement
         ; Condition
         ; Less Than or Equal to
         ; LHS
            ; Identifier - float a
               push qword [rbp - -16]
         ; RHS
            ; Identifier - float b
               push qword [rbp - -24]
         pop rdx ; rhs
         pop rax ; lhs
         cmp rax, rdx
         setle al
         movzx eax, al
         push rax
         pop rdx ; __cond
         cmp rdx, 0 ; ensure condition is true
         je .__endif__73 ; jump to end
         ; Body
         ; Return
         ; Identifier - float a
            push qword [rbp - -16]
         pop rax ; return value (float)
         movq xmm0, rax ; xmm0 is used for float return values
         ; Clean up stack and return
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
         jmp .__endif__73 ; jump to end of condition chain
         ; End of if
.__endif__73:
;---------------------------------------------------------------------------------
         ; Return
         ; Identifier - float b
         push qword [rbp - -24]
         pop rax ; return value (float)
         movq xmm0, rax ; xmm0 is used for float return values
         ; Clean up stack and return
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
;------------------------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
.__end____main____min__float__float:
         ; End Function Declaration - min(float, float) -> float
; ==========================================================================================

; ==========================================================================================
         ; Function Declaration - abs(int) -> int
         ; Skip over function declaration
         jmp .__end____main____abs__int
.__main____abs__int:
         ; Function Header:
         ; Setup stack frame
         push rbp
         mov rbp, rsp
         sub rsp, 0
         ; Parameters
         ; Param: v [rbp + 16]
         ; Local Variables - Each variable is currently 64-bit (sorry not sorry)

         ; Body
;------------------------------------------------------------------------------------
         ; Code Block
;---------------------------------------------------------------------------------
         ; If-Statement
         ; Condition
         ; Less Than
         ; LHS
            ; Identifier - int v
               push qword [rbp - -16]
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
         je .__endif__75 ; jump to end
         ; Body
         ; Return
         ; Negative - int
            ; RHS
               ; Identifier - int v
                  push qword [rbp - -16]
            pop rdx
            ; val = 0 - val
            mov rax, 0
            sub rax, rdx
            push rax ; push result
         pop rax ; return value (int)
         ; Clean up stack and return
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
         jmp .__endif__75 ; jump to end of condition chain
         ; End of if
.__endif__75:
;---------------------------------------------------------------------------------
         ; Return
         ; Identifier - int v
         push qword [rbp - -16]
         pop rax ; return value (int)
         ; Clean up stack and return
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
;------------------------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
.__end____main____abs__int:
         ; End Function Declaration - abs(int) -> int
; ==========================================================================================

; ==========================================================================================
         ; Function Declaration - abs(float) -> float
         ; Skip over function declaration
         jmp .__end____main____abs__float
.__main____abs__float:
         ; Function Header:
         ; Setup stack frame
         push rbp
         mov rbp, rsp
         sub rsp, 0
         ; Parameters
         ; Param: v [rbp + 16]
         ; Local Variables - Each variable is currently 64-bit (sorry not sorry)

         ; Body
;------------------------------------------------------------------------------------
         ; Code Block
;---------------------------------------------------------------------------------
         ; If-Statement
         ; Condition
         ; Less Than
         ; LHS
            ; Identifier - float v
               push qword [rbp - -16]
         ; RHS
            ; Float Literal
               mov rax, qword [.float0] ; 0.0
               push rax
         pop rdx ; rhs
         pop rax ; lhs
         cmp rax, rdx
         setl al
         movzx eax, al
         push rax
         pop rdx ; __cond
         cmp rdx, 0 ; ensure condition is true
         je .__endif__77 ; jump to end
         ; Body
         ; Return
         ; Negative - float
            ; RHS
               ; Identifier - float v
                  push qword [rbp - -16]
            pop rdx
            ; Implemented as multiplying by -1.0
            movsd xmm1, qword [__builtin__neg] ; -1.0
            movq xmm0, rdx
            mulsd xmm0, xmm1 ; v = v * -1.0
            movq rax, xmm0
            push rax ; push result
         pop rax ; return value (float)
         movq xmm0, rax ; xmm0 is used for float return values
         ; Clean up stack and return
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
         jmp .__endif__77 ; jump to end of condition chain
         ; End of if
.__endif__77:
;---------------------------------------------------------------------------------
         ; Return
         ; Identifier - float v
         push qword [rbp - -16]
         pop rax ; return value (float)
         movq xmm0, rax ; xmm0 is used for float return values
         ; Clean up stack and return
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
;------------------------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
.__end____main____abs__float:
         ; End Function Declaration - abs(float) -> float
; ==========================================================================================

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
         mov rax, qword [rbp - 16]  ; __main__lines
         pop rdx ; rhs value
         mov qword [rbp - 16], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
;------------------------------------------------------------------------------------------
         ; While-Loop
.__while__78:
         ; Condition
         ; Not Equal
         ; LHS
         ; Identifier - char[] line
         push qword [rbp - 8]
         ; RHS
         ; Null Literal
         push 0
         pop rdx ; rhs
         pop rax ; lhs
         cmp rax, rdx
         setne al
         movzx eax, al
         push rax
         pop rax ; __cond
         cmp rax, 0 ; __cond
         je .__endwhile__78
         ; Body
;------------------------------------------------------------------------------------
         ; Code Block
         ; Method Call - Vector<:char[]:>::pushBack(char[]) -> void
         ; Make space for 1 arg(s) and object parameter
         sub rsp, 16
         ; LHS
         ; Identifier - Vector<:char[]:> lines
         push qword [rbp - 16]
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
         call __builtin__input
         ; Remove args
         add rsp, 0
         ; Push return value
         push rax
         pop rdx ; rhs value
         mov qword [rbp - 8], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
;------------------------------------------------------------------------------------
         jmp .__while__78
         ; End of While
.__endwhile__78:
;------------------------------------------------------------------------------------------
         ; Assignment - '='
         ; RHS
         ; Int Literal
         mov rax, 0
         push rax
         ; LHS
         ; Variable Declaration - OP_MUL
         mov rax, qword [rbp - 24]  ; __main__OP_MUL
         pop rdx ; rhs value
         mov qword [rbp - 24], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
         ; RHS
         ; Int Literal
         mov rax, 1
         push rax
         ; LHS
         ; Variable Declaration - OP_ADD
         mov rax, qword [rbp - 32]  ; __main__OP_ADD
         pop rdx ; rhs value
         mov qword [rbp - 32], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
         ; RHS
         ; Int Literal
         mov rax, 2
         push rax
         ; LHS
         ; Variable Declaration - OP_SQUARE
         mov rax, qword [rbp - 40]  ; __main__OP_SQUARE
         pop rdx ; rhs value
         mov qword [rbp - 40], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
; ==========================================================================================
         ; Class Declaration - __main____Monkey inherits __builtin____main__Object
         ; Class data
         section .data
         ; Dispatch Table - this might need to be a malloc**
         .__dtable____main____Monkey:
         ; Dispatch Table Entries
         section .text
;---------------------------------------------------------------------------------------
         ; Field - Vector<:int:> Monkey::items
         section .data
         .__field____main____Monkey____items: dq 1
         section .text
;---------------------------------------------------------------------------------------
;---------------------------------------------------------------------------------------
         ; Field - int Monkey::op
         section .data
         .__field____main____Monkey____op: dq 2
         section .text
;---------------------------------------------------------------------------------------
;---------------------------------------------------------------------------------------
         ; Field - int Monkey::operand
         section .data
         .__field____main____Monkey____operand: dq 3
         section .text
;---------------------------------------------------------------------------------------
;---------------------------------------------------------------------------------------
         ; Field - int Monkey::divisible_by
         section .data
         .__field____main____Monkey____divisible_by: dq 4
         section .text
;---------------------------------------------------------------------------------------
;---------------------------------------------------------------------------------------
         ; Field - int Monkey::true_monkey_id
         section .data
         .__field____main____Monkey____true_monkey_id: dq 5
         section .text
;---------------------------------------------------------------------------------------
;---------------------------------------------------------------------------------------
         ; Field - int Monkey::false_monkey_id
         section .data
         .__field____main____Monkey____false_monkey_id: dq 6
         section .text
;---------------------------------------------------------------------------------------
;---------------------------------------------------------------------------------------
         ; Field - int Monkey::inspected_items
         section .data
         .__field____main____Monkey____inspected_items: dq 7
         section .text
;---------------------------------------------------------------------------------------
         ; skip over class methods
         jmp .__endclass____main____Monkey
;---------------------------------------------------------------------------------------
         ; Constructor Declaration - Monkey::Monkey() -> Monkey
         jmp .__end__ctor____main____Monkey____Monkey
         .__ctor____main____Monkey____Monkey:
         ; Function Header:
         ; Setup stack frame
         push rbp
         mov rbp, rsp
         ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
         sub rsp, 16 ; space for local variables (16-byte aligned)
         ; [rbp - 8] - this - Reference to 'this' object instance
         ; Creating Class Instance
         mov rdi, 64 ; [dtable, field0, field1, ..., fieldN] each 8 bytes
         call malloc
         mov qword [rbp - 8], rax ; save class instance as 'this'
         ; Add Dispatch Table
         mov rax, qword [rbp - 8] ; this
         mov qword [rax + 0], .__dtable____main____Monkey ; this[0] = &dtable
         ; Parameters
         ; Body
;------------------------------------------------------------------------------------
         ; Code Block
         ; Assignment - '='
         ; RHS
         ; Constructor Call - Vector<:int:>::Vector() -> Vector<:int:>
         ; Make space for 0 arg(s)
         sub rsp, 0
         ; Arguments
         ; Call Vector<:int:>::Vector()
         call .__ctor____main____Vector__int____Vector
         ; Remove args
         add rsp, 0
         ; Push return value
         push rax
         ; LHS
         ; Member Accessor Assignment
         ; LHS
            ; This keyword
               push qword [rbp - 8] ; __this
         ; RHS
            push qword [.__field____main____Monkey____items] ; 
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
            push qword [.__field____main____Monkey____op] ; 
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
            push qword [.__field____main____Monkey____operand] ; 
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
            push qword [.__field____main____Monkey____divisible_by] ; 
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
            push qword [.__field____main____Monkey____true_monkey_id] ; 
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
            push qword [.__field____main____Monkey____false_monkey_id] ; 
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
            push qword [.__field____main____Monkey____inspected_items] ; 
         pop rdi ; rhs
         pop rbx ; lhs
         pop rdx ; rhs value
         mov qword [rbx + 8*rdi], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
;------------------------------------------------------------------------------------
         mov rax, qword [rbp - 8] ; __this
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
         .__end__ctor____main____Monkey____Monkey:
         ; End Constructor Declaration - __ctor____main____Monkey____Monkey
;------------------------------------------------------------------------------------------

.__endclass____main____Monkey:
         ; End Class Declaration - __main____Monkey
; =============================================================================================

         ; Assignment - '='
         ; RHS
         ; Constructor Call - Vector<:Monkey:>::Vector() -> Vector<:Monkey:>
         ; Make space for 0 arg(s)
         sub rsp, 0
         ; Arguments
         ; Call Vector<:Monkey:>::Vector()
         call .__ctor____main____Vector__Monkey____Vector
         ; Remove args
         add rsp, 0
         ; Push return value
         push rax
         ; LHS
         ; Variable Declaration - monkeys
         mov rax, qword [rbp - 48]  ; __main__monkeys
         pop rdx ; rhs value
         mov qword [rbp - 48], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
;---------------------------------------------------------------------------------------------
         ; For-Loop
         ; Init
         ; Assignment - '='
         ; RHS
         ; Int Literal
         mov rax, 0
         push rax
         ; LHS
         ; Variable Declaration - l
         mov rax, qword [rbp - 56]  ; __main__for__81__l
         pop rdx ; rhs value
         mov qword [rbp - 56], rdx
         push rdx
         ; Loop init result can be discarded
         pop rax
         jmp .__forcond__81
.__for__81:
         ; Update
         ; Assignment - '+='
         ; RHS
         ; Int Literal
         mov rax, 7
         push rax
         pop rdx ; rhs value
         mov rax, qword [rbp - 56] ; read lhs value
         add rax, rdx      ; add lhs and rhs
         mov qword [rbp - 56], rax ; write back to lhs
         push rax          ; push result for other expressions
         ; Loop update result can be discarded
         pop rax
.__forcond__81:
         ; Condition
         ; Less Than
         ; LHS
         ; Identifier - int l
         push qword [rbp - 56]
         ; RHS
         ; Member Accessor
         ; LHS
         ; Identifier - Vector<:char[]:> lines
         push qword [rbp - 16]
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
         je .__endfor__81
         ; Body
;---------------------------------------------------------------------------------------
         ; Code Block
         ; Assignment - '='
         ; RHS
         ; Constructor Call - Monkey::Monkey() -> Monkey
         ; Make space for 0 arg(s)
         sub rsp, 0
         ; Arguments
         ; Call Monkey::Monkey()
         call .__ctor____main____Monkey____Monkey
         ; Remove args
         add rsp, 0
         ; Push return value
         push rax
         ; LHS
         ; Variable Declaration - monkey
         mov rax, qword [rbp - 64]  ; __main__for__81__block__82__monkey
         pop rdx ; rhs value
         mov qword [rbp - 64], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
         ; RHS
         ; Function Call - substr(char[], int, int) -> char[]
         ; Make space for 3 arg(s)
         sub rsp, 24
         ; Arguments
         ; Eval arg0
            ; Subscript
               ; LHS
                  ; Member Accessor
                     ; LHS
                        ; Identifier - Vector<:char[]:> lines
                           push qword [rbp - 16]
                     ; RHS
                        push qword [.__field____main____Vector__char__1____data] ; stored index associated with field that is being accessed
                     pop rdx ; rhs
                     pop rax ; lhs
                     push qword [rax + 8*rdx] ; lhs.rhs
               ; OFFSET
                  ; Addition - int, int
                     ; LHS
                        ; Identifier - int l
                           push qword [rbp - 56]
                     ; RHS
                        ; Int Literal
                           mov rax, 1
                           push rax
                     pop rdx ; rhs
                     pop rax ; lhs
                     add rax, rdx
                     push rax
               pop rdx ; __offset
               pop rax ; __pointer
               push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
         ; Move arg0's result to reverse order position on stack
         pop rax
         mov qword [rsp + 0], rax
         ; Eval arg1
            ; Int Literal
               mov rax, 17
               push rax
         ; Move arg1's result to reverse order position on stack
         pop rax
         mov qword [rsp + 8], rax
         ; Eval arg2
            ; Function Call - strlen(char[]) -> int
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; Subscript
                        ; LHS
                           ; Member Accessor
                              ; LHS
                                 ; Identifier - Vector<:char[]:> lines
                                    push qword [rbp - 16]
                              ; RHS
                                 push qword [.__field____main____Vector__char__1____data] ; stored index associated with field that is being accessed
                              pop rdx ; rhs
                              pop rax ; lhs
                              push qword [rax + 8*rdx] ; lhs.rhs
                        ; OFFSET
                           ; Addition - int, int
                              ; LHS
                                 ; Identifier - int l
                                    push qword [rbp - 56]
                              ; RHS
                                 ; Int Literal
                                    mov rax, 1
                                    push rax
                              pop rdx ; rhs
                              pop rax ; lhs
                              add rax, rdx
                              push rax
                        pop rdx ; __offset
                        pop rax ; __pointer
                        push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                  ; Move arg0's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 0], rax
               ; Call strlen(char[])
               call .__main____strlen__char__1
               ; Remove args
               add rsp, 8
               ; Push return value
               push rax
         ; Move arg2's result to reverse order position on stack
         pop rax
         mov qword [rsp + 16], rax
         ; Call substr(char[], int, int)
         call .__main____substr__char__1__int__int
         ; Remove args
         add rsp, 24
         ; Push return value
         push rax
         ; LHS
         ; Variable Declaration - items_str
         mov rax, qword [rbp - 72]  ; __main__for__81__block__82__items_str
         pop rdx ; rhs value
         mov qword [rbp - 72], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
         ; RHS
         ; Function Call - split(char[], char) -> Vector<:char[]:>
         ; Make space for 2 arg(s)
         sub rsp, 16
         ; Arguments
         ; Eval arg0
            ; Identifier - char[] items_str
               push qword [rbp - 72]
         ; Move arg0's result to reverse order position on stack
         pop rax
         mov qword [rsp + 0], rax
         ; Eval arg1
            ; Char Literal
               push ' '
         ; Move arg1's result to reverse order position on stack
         pop rax
         mov qword [rsp + 8], rax
         ; Call split(char[], char)
         call .__main____split__char__1__char
         ; Remove args
         add rsp, 16
         ; Push return value
         push rax
         ; LHS
         ; Variable Declaration - tokens0
         mov rax, qword [rbp - 80]  ; __main__for__81__block__82__tokens0
         pop rdx ; rhs value
         mov qword [rbp - 80], rdx
         push rdx
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
         mov rax, qword [rbp - 88]  ; __main__for__81__block__82__for__83__i
         pop rdx ; rhs value
         mov qword [rbp - 88], rdx
         push rdx
         ; Loop init result can be discarded
         pop rax
         jmp .__forcond__83
.__for__83:
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
.__forcond__83:
         ; Condition
         ; Less Than
         ; LHS
         ; Identifier - int i
            push qword [rbp - 88]
         ; RHS
         ; Member Accessor
            ; LHS
               ; Identifier - Vector<:char[]:> tokens0
                  push qword [rbp - 80]
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
         je .__endfor__83
         ; Body
;------------------------------------------------------------------------------
         ; Code Block
         ; Assignment - '='
         ; RHS
            ; Function Call - substr(char[], int, int) -> char[]
               ; Make space for 3 arg(s)
               sub rsp, 24
               ; Arguments
                  ; Eval arg0
                     ; Subscript
                        ; LHS
                           ; Member Accessor
                              ; LHS
                                 ; Identifier - Vector<:char[]:> tokens0
                                    push qword [rbp - 80]
                              ; RHS
                                 push qword [.__field____main____Vector__char__1____data] ; stored index associated with field that is being accessed
                              pop rdx ; rhs
                              pop rax ; lhs
                              push qword [rax + 8*rdx] ; lhs.rhs
                        ; OFFSET
                           ; Identifier - int i
                              push qword [rbp - 88]
                        pop rdx ; __offset
                        pop rax ; __pointer
                        push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                  ; Move arg0's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 0], rax
                  ; Eval arg1
                     ; Int Literal
                        mov rax, 0
                        push rax
                  ; Move arg1's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 8], rax
                  ; Eval arg2
                     ; Subtraction - int, int
                        ; LHS
                           ; Function Call - strlen(char[]) -> int
                              ; Make space for 1 arg(s)
                              sub rsp, 8
                              ; Arguments
                                 ; Eval arg0
                                    ; Subscript
                                       ; LHS
                                          ; Member Accessor
                                             ; LHS
                                                ; Identifier - Vector<:char[]:> tokens0
                                                   push qword [rbp - 80]
                                             ; RHS
                                                push qword [.__field____main____Vector__char__1____data] ; stored index associated with field that is being accessed
                                             pop rdx ; rhs
                                             pop rax ; lhs
                                             push qword [rax + 8*rdx] ; lhs.rhs
                                       ; OFFSET
                                          ; Identifier - int i
                                             push qword [rbp - 88]
                                       pop rdx ; __offset
                                       pop rax ; __pointer
                                       push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                                 ; Move arg0's result to reverse order position on stack
                                 pop rax
                                 mov qword [rsp + 0], rax
                              ; Call strlen(char[])
                              call .__main____strlen__char__1
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
                        sub rax, rdx
                        push rax
                  ; Move arg2's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 16], rax
               ; Call substr(char[], int, int)
               call .__main____substr__char__1__int__int
               ; Remove args
               add rsp, 24
               ; Push return value
               push rax
         ; LHS
            ; Variable Declaration - item_str
               mov rax, qword [rbp - 96]  ; __main__for__81__block__82__for__83__block__84__item_str
         pop rdx ; rhs value
         mov qword [rbp - 96], rdx
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
                     ; Identifier - char[] item_str
                        push qword [rbp - 96]
                  ; Move arg0's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 0], rax
               ; Call stringToInt(char[])
               call __builtin__stringToInt__char__1
               ; Remove args
               add rsp, 8
               ; Push return value
               push rax
         ; LHS
            ; Variable Declaration - item
               mov rax, qword [rbp - 104]  ; __main__for__81__block__82__for__83__block__84__item
         pop rdx ; rhs value
         mov qword [rbp - 104], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
         ; Method Call - Vector<:int:>::pushBack(int) -> void
         ; Make space for 1 arg(s) and object parameter
         sub rsp, 16
         ; LHS
            ; Member Accessor
               ; LHS
                  ; Identifier - Monkey monkey
                     push qword [rbp - 64]
               ; RHS
                  push qword [.__field____main____Monkey____items] ; stored index associated with field that is being accessed
               pop rdx ; rhs
               pop rax ; lhs
               push qword [rax + 8*rdx] ; lhs.rhs
            pop rax ; object parameter
            mov qword [rsp + 0], rax ; place as first parameter
         ; RHS
         ; Arguments
            ; Eval arg0
               ; Identifier - int item
                  push qword [rbp - 104]
            ; Move arg0's result to reverse order position on stack
            pop rax
            mov qword [rsp + 8], rax
         call .__method____main____Vector__int____pushBack__int
         ; Remove args
         add rsp, 16
         ; Push return value
         push rax
         ; Statement results can be ignored
         pop rdx
         ; Free Operator
         ; RHS
            ; Identifier - char[] item_str
               push qword [rbp - 96]
         ; Free pointer
         pop rdi   ; pointer
         call free ; free the pointer
         push rax  ; undefined return value
         ; Statement results can be ignored
         pop rdx
;------------------------------------------------------------------------------
         ; Repeat
jmp .__for__83
         ; End of For
.__endfor__83:
;------------------------------------------------------------------------------------
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
         mov rax, qword [rbp - 112]  ; __main__for__81__block__82__for__85__i
         pop rdx ; rhs value
         mov qword [rbp - 112], rdx
         push rdx
         ; Loop init result can be discarded
         pop rax
         jmp .__forcond__85
.__for__85:
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
.__forcond__85:
         ; Condition
         ; Less Than
         ; LHS
         ; Identifier - int i
            push qword [rbp - 112]
         ; RHS
         ; Member Accessor
            ; LHS
               ; Identifier - Vector<:char[]:> tokens0
                  push qword [rbp - 80]
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
         je .__endfor__85
         ; Body
         ; Free Operator
         ; RHS
         ; Subscript
            ; LHS
               ; Member Accessor
                  ; LHS
                     ; Identifier - Vector<:char[]:> tokens0
                        push qword [rbp - 80]
                  ; RHS
                     push qword [.__field____main____Vector__char__1____data] ; stored index associated with field that is being accessed
                  pop rdx ; rhs
                  pop rax ; lhs
                  push qword [rax + 8*rdx] ; lhs.rhs
            ; OFFSET
               ; Identifier - int i
                  push qword [rbp - 112]
            pop rdx ; __offset
            pop rax ; __pointer
            push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
         ; Free pointer
         pop rdi   ; pointer
         call free ; free the pointer
         push rax  ; undefined return value
         ; Statement results can be ignored
         pop rdx
         ; Repeat
jmp .__for__85
         ; End of For
.__endfor__85:
;------------------------------------------------------------------------------------
         ; Free Operator
         ; RHS
         ; Identifier - Vector<:char[]:> tokens0
         push qword [rbp - 80]
         ; Free pointer
         pop rdi   ; pointer
         call free ; free the pointer
         push rax  ; undefined return value
         ; Statement results can be ignored
         pop rdx
         ; Free Operator
         ; RHS
         ; Identifier - char[] items_str
         push qword [rbp - 72]
         ; Free pointer
         pop rdi   ; pointer
         call free ; free the pointer
         push rax  ; undefined return value
         ; Statement results can be ignored
         pop rdx
;------------------------------------------------------------------------------------
         ; If-Statement
         ; Condition
         ; Not Equal
         ; LHS
         ; Function Call - first_index_of(char[], char) -> int
            ; Make space for 2 arg(s)
            sub rsp, 16
            ; Arguments
               ; Eval arg0
                  ; Subscript
                     ; LHS
                        ; Member Accessor
                           ; LHS
                              ; Identifier - Vector<:char[]:> lines
                                 push qword [rbp - 16]
                           ; RHS
                              push qword [.__field____main____Vector__char__1____data] ; stored index associated with field that is being accessed
                           pop rdx ; rhs
                           pop rax ; lhs
                           push qword [rax + 8*rdx] ; lhs.rhs
                     ; OFFSET
                        ; Addition - int, int
                           ; LHS
                              ; Identifier - int l
                                 push qword [rbp - 56]
                           ; RHS
                              ; Int Literal
                                 mov rax, 2
                                 push rax
                           pop rdx ; rhs
                           pop rax ; lhs
                           add rax, rdx
                           push rax
                     pop rdx ; __offset
                     pop rax ; __pointer
                     push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
               ; Move arg0's result to reverse order position on stack
               pop rax
               mov qword [rsp + 0], rax
               ; Eval arg1
                  ; Char Literal
                     push '*'
               ; Move arg1's result to reverse order position on stack
               pop rax
               mov qword [rsp + 8], rax
            ; Call first_index_of(char[], char)
            call .__main____first_index_of__char__1__char
            ; Remove args
            add rsp, 16
            ; Push return value
            push rax
         ; RHS
         ; Negative - int
            ; RHS
               ; Int Literal
                  mov rax, 1
                  push rax
            pop rdx
            ; val = 0 - val
            mov rax, 0
            sub rax, rdx
            push rax ; push result
         pop rdx ; rhs
         pop rax ; lhs
         cmp rax, rdx
         setne al
         movzx eax, al
         push rax
         pop rdx ; __cond
         cmp rdx, 0 ; ensure condition is true
         je .__else__86 ; jump to else
         ; Body
;------------------------------------------------------------------------------
         ; Code Block
         ; Assignment - '='
         ; RHS
            ; Function Call - split(char[], char) -> Vector<:char[]:>
               ; Make space for 2 arg(s)
               sub rsp, 16
               ; Arguments
                  ; Eval arg0
                     ; Subscript
                        ; LHS
                           ; Member Accessor
                              ; LHS
                                 ; Identifier - Vector<:char[]:> lines
                                    push qword [rbp - 16]
                              ; RHS
                                 push qword [.__field____main____Vector__char__1____data] ; stored index associated with field that is being accessed
                              pop rdx ; rhs
                              pop rax ; lhs
                              push qword [rax + 8*rdx] ; lhs.rhs
                        ; OFFSET
                           ; Addition - int, int
                              ; LHS
                                 ; Identifier - int l
                                    push qword [rbp - 56]
                              ; RHS
                                 ; Int Literal
                                    mov rax, 2
                                    push rax
                              pop rdx ; rhs
                              pop rax ; lhs
                              add rax, rdx
                              push rax
                        pop rdx ; __offset
                        pop rax ; __pointer
                        push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                  ; Move arg0's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 0], rax
                  ; Eval arg1
                     ; Char Literal
                        push ' '
                  ; Move arg1's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 8], rax
               ; Call split(char[], char)
               call .__main____split__char__1__char
               ; Remove args
               add rsp, 16
               ; Push return value
               push rax
         ; LHS
            ; Variable Declaration - tokens1
               mov rax, qword [rbp - 120]  ; __main__for__81__block__82__if__86__block__87__tokens1
         pop rdx ; rhs value
         mov qword [rbp - 120], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
;---------------------------------------------------------------------------
         ; If-Statement
         ; Condition
            ; Equal
               ; LHS
                  ; Subscript
                     ; LHS
                        ; Subscript
                           ; LHS
                              ; Member Accessor
                                 ; LHS
                                    ; Identifier - Vector<:char[]:> tokens1
                                       push qword [rbp - 120]
                                 ; RHS
                                    push qword [.__field____main____Vector__char__1____data] ; stored index associated with field that is being accessed
                                 pop rdx ; rhs
                                 pop rax ; lhs
                                 push qword [rax + 8*rdx] ; lhs.rhs
                           ; OFFSET
                              ; Subtraction - int, int
                                 ; LHS
                                    ; Member Accessor
                                       ; LHS
                                          ; Identifier - Vector<:char[]:> tokens1
                                             push qword [rbp - 120]
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
                                 sub rax, rdx
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
                     mov al, byte [rax + rdx] ; pointer + sizeof(data_t) * offset
                     movzx rax, al ; zero extend because we need to push 64bit to stack
                     push rax ; push char onto stack
               ; RHS
                  ; Char Literal
                     push 'o'
               pop rdx ; rhs
               pop rax ; lhs
               cmp rax, rdx
               sete al
               movzx eax, al
               push rax
            pop rdx ; __cond
            cmp rdx, 0 ; ensure condition is true
            je .__else__88 ; jump to else
         ; Body
   ;---------------------------------------------------------------------
            ; Code Block
               ; Assignment - '='
                  ; RHS
                     ; Identifier - int OP_SQUARE
                        push qword [rbp - 40]
                  ; LHS
                     ; Member Accessor Assignment
                        ; LHS
                           ; Identifier - Monkey monkey
                              push qword [rbp - 64]
                        ; RHS
                           push qword [.__field____main____Monkey____op] ; 
                        pop rdi ; rhs
                        pop rbx ; lhs
                  pop rdx ; rhs value
                  mov qword [rbx + 8*rdi], rdx
                  push rdx
               ; Statement results can be ignored
               pop rdx
   ;---------------------------------------------------------------------
         jmp .__endif__88 ; jump to end of condition chain
;------------------------------------------------------------------------
         ; Else-Statement
.__else__88:
;------------------------------------------------------------------------
         ; Code Block
            ; Assignment - '='
               ; RHS
                  ; Identifier - int OP_MUL
                     push qword [rbp - 24]
               ; LHS
                  ; Member Accessor Assignment
                     ; LHS
                        ; Identifier - Monkey monkey
                           push qword [rbp - 64]
                     ; RHS
                        push qword [.__field____main____Monkey____op] ; 
                     pop rdi ; rhs
                     pop rbx ; lhs
               pop rdx ; rhs value
               mov qword [rbx + 8*rdi], rdx
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
                           ; Subscript
                              ; LHS
                                 ; Member Accessor
                                    ; LHS
                                       ; Identifier - Vector<:char[]:> tokens1
                                          push qword [rbp - 120]
                                    ; RHS
                                       push qword [.__field____main____Vector__char__1____data] ; stored index associated with field that is being accessed
                                    pop rdx ; rhs
                                    pop rax ; lhs
                                    push qword [rax + 8*rdx] ; lhs.rhs
                              ; OFFSET
                                 ; Subtraction - int, int
                                    ; LHS
                                       ; Member Accessor
                                          ; LHS
                                             ; Identifier - Vector<:char[]:> tokens1
                                                push qword [rbp - 120]
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
                                    sub rax, rdx
                                    push rax
                              pop rdx ; __offset
                              pop rax ; __pointer
                              push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                        ; Move arg0's result to reverse order position on stack
                        pop rax
                        mov qword [rsp + 0], rax
                     ; Call stringToInt(char[])
                     call __builtin__stringToInt__char__1
                     ; Remove args
                     add rsp, 8
                     ; Push return value
                     push rax
               ; LHS
                  ; Member Accessor Assignment
                     ; LHS
                        ; Identifier - Monkey monkey
                           push qword [rbp - 64]
                     ; RHS
                        push qword [.__field____main____Monkey____operand] ; 
                     pop rdi ; rhs
                     pop rbx ; lhs
               pop rdx ; rhs value
               mov qword [rbx + 8*rdi], rdx
               push rdx
            ; Statement results can be ignored
            pop rdx
;------------------------------------------------------------------------
;------------------------------------------------------------------------
         ; End of if
.__endif__88:
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
               ; Variable Declaration - j
                  mov rax, qword [rbp - 128]  ; __main__for__81__block__82__if__86__block__87__for__91__j
            pop rdx ; rhs value
            mov qword [rbp - 128], rdx
            push rdx
         ; Loop init result can be discarded
         pop rax
         jmp .__forcond__91
.__for__91:
         ; Update
            ; Pre-Increment - int
               ; RHS
                  ; Identifier - int j
                     push qword [rbp - 128]
               pop rdx
               add qword [rbp - 128], 1
               mov rax, qword [rbp - 128]
               push rax ; push result
            ; Loop update result can be discarded
            pop rax
.__forcond__91:
         ; Condition
            ; Less Than
               ; LHS
                  ; Identifier - int j
                     push qword [rbp - 128]
               ; RHS
                  ; Member Accessor
                     ; LHS
                        ; Identifier - Vector<:char[]:> tokens1
                           push qword [rbp - 120]
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
            je .__endfor__91
         ; Body
            ; Free Operator
               ; RHS
                  ; Subscript
                     ; LHS
                        ; Member Accessor
                           ; LHS
                              ; Identifier - Vector<:char[]:> tokens1
                                 push qword [rbp - 120]
                           ; RHS
                              push qword [.__field____main____Vector__char__1____data] ; stored index associated with field that is being accessed
                           pop rdx ; rhs
                           pop rax ; lhs
                           push qword [rax + 8*rdx] ; lhs.rhs
                     ; OFFSET
                        ; Identifier - int j
                           push qword [rbp - 128]
                     pop rdx ; __offset
                     pop rax ; __pointer
                     push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
               ; Free pointer
               pop rdi   ; pointer
               call free ; free the pointer
               push rax  ; undefined return value
            ; Statement results can be ignored
            pop rdx
         ; Repeat
jmp .__for__91
         ; End of For
.__endfor__91:
;---------------------------------------------------------------------------
         ; Free Operator
         ; RHS
            ; Identifier - Vector<:char[]:> tokens1
               push qword [rbp - 120]
         ; Free pointer
         pop rdi   ; pointer
         call free ; free the pointer
         push rax  ; undefined return value
         ; Statement results can be ignored
         pop rdx
;------------------------------------------------------------------------------
         jmp .__endif__86 ; jump to end of condition chain
;---------------------------------------------------------------------------------
         ; Else-Statement
.__else__86:
;---------------------------------------------------------------------------------
         ; Code Block
         ; Assignment - '='
         ; RHS
         ; Function Call - split(char[], char) -> Vector<:char[]:>
            ; Make space for 2 arg(s)
            sub rsp, 16
            ; Arguments
               ; Eval arg0
                  ; Subscript
                     ; LHS
                        ; Member Accessor
                           ; LHS
                              ; Identifier - Vector<:char[]:> lines
                                 push qword [rbp - 16]
                           ; RHS
                              push qword [.__field____main____Vector__char__1____data] ; stored index associated with field that is being accessed
                           pop rdx ; rhs
                           pop rax ; lhs
                           push qword [rax + 8*rdx] ; lhs.rhs
                     ; OFFSET
                        ; Addition - int, int
                           ; LHS
                              ; Identifier - int l
                                 push qword [rbp - 56]
                           ; RHS
                              ; Int Literal
                                 mov rax, 2
                                 push rax
                           pop rdx ; rhs
                           pop rax ; lhs
                           add rax, rdx
                           push rax
                     pop rdx ; __offset
                     pop rax ; __pointer
                     push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
               ; Move arg0's result to reverse order position on stack
               pop rax
               mov qword [rsp + 0], rax
               ; Eval arg1
                  ; Char Literal
                     push ' '
               ; Move arg1's result to reverse order position on stack
               pop rax
               mov qword [rsp + 8], rax
            ; Call split(char[], char)
            call .__main____split__char__1__char
            ; Remove args
            add rsp, 16
            ; Push return value
            push rax
         ; LHS
         ; Variable Declaration - tokens1
            mov rax, qword [rbp - 136]  ; __main__for__81__block__82.__else__86__block__92__tokens1
         pop rdx ; rhs value
         mov qword [rbp - 136], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
;------------------------------------------------------------------------------
         ; If-Statement
         ; Condition
         ; Equal
            ; LHS
               ; Subscript
                  ; LHS
                     ; Subscript
                        ; LHS
                           ; Member Accessor
                              ; LHS
                                 ; Identifier - Vector<:char[]:> tokens1
                                    push qword [rbp - 136]
                              ; RHS
                                 push qword [.__field____main____Vector__char__1____data] ; stored index associated with field that is being accessed
                              pop rdx ; rhs
                              pop rax ; lhs
                              push qword [rax + 8*rdx] ; lhs.rhs
                        ; OFFSET
                           ; Subtraction - int, int
                              ; LHS
                                 ; Member Accessor
                                    ; LHS
                                       ; Identifier - Vector<:char[]:> tokens1
                                          push qword [rbp - 136]
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
                              sub rax, rdx
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
                  mov al, byte [rax + rdx] ; pointer + sizeof(data_t) * offset
                  movzx rax, al ; zero extend because we need to push 64bit to stack
                  push rax ; push char onto stack
            ; RHS
               ; Char Literal
                  push 'o'
            pop rdx ; rhs
            pop rax ; lhs
            cmp rax, rdx
            sete al
            movzx eax, al
            push rax
         pop rdx ; __cond
         cmp rdx, 0 ; ensure condition is true
         je .__else__93 ; jump to else
         ; Body
;------------------------------------------------------------------------
         ; Code Block
            ; Assignment - '='
               ; RHS
                  ; Identifier - int OP_SQUARE
                     push qword [rbp - 40]
               ; LHS
                  ; Member Accessor Assignment
                     ; LHS
                        ; Identifier - Monkey monkey
                           push qword [rbp - 64]
                     ; RHS
                        push qword [.__field____main____Monkey____op] ; 
                     pop rdi ; rhs
                     pop rbx ; lhs
               pop rdx ; rhs value
               mov qword [rbx + 8*rdi], rdx
               push rdx
            ; Statement results can be ignored
            pop rdx
;------------------------------------------------------------------------
         jmp .__endif__93 ; jump to end of condition chain
;---------------------------------------------------------------------------
         ; Else-Statement
.__else__93:
;---------------------------------------------------------------------------
         ; Code Block
         ; Assignment - '='
            ; RHS
               ; Identifier - int OP_ADD
                  push qword [rbp - 32]
            ; LHS
               ; Member Accessor Assignment
                  ; LHS
                     ; Identifier - Monkey monkey
                        push qword [rbp - 64]
                  ; RHS
                     push qword [.__field____main____Monkey____op] ; 
                  pop rdi ; rhs
                  pop rbx ; lhs
            pop rdx ; rhs value
            mov qword [rbx + 8*rdi], rdx
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
                        ; Subscript
                           ; LHS
                              ; Member Accessor
                                 ; LHS
                                    ; Identifier - Vector<:char[]:> tokens1
                                       push qword [rbp - 136]
                                 ; RHS
                                    push qword [.__field____main____Vector__char__1____data] ; stored index associated with field that is being accessed
                                 pop rdx ; rhs
                                 pop rax ; lhs
                                 push qword [rax + 8*rdx] ; lhs.rhs
                           ; OFFSET
                              ; Subtraction - int, int
                                 ; LHS
                                    ; Member Accessor
                                       ; LHS
                                          ; Identifier - Vector<:char[]:> tokens1
                                             push qword [rbp - 136]
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
                                 sub rax, rdx
                                 push rax
                           pop rdx ; __offset
                           pop rax ; __pointer
                           push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                     ; Move arg0's result to reverse order position on stack
                     pop rax
                     mov qword [rsp + 0], rax
                  ; Call stringToInt(char[])
                  call __builtin__stringToInt__char__1
                  ; Remove args
                  add rsp, 8
                  ; Push return value
                  push rax
            ; LHS
               ; Member Accessor Assignment
                  ; LHS
                     ; Identifier - Monkey monkey
                        push qword [rbp - 64]
                  ; RHS
                     push qword [.__field____main____Monkey____operand] ; 
                  pop rdi ; rhs
                  pop rbx ; lhs
            pop rdx ; rhs value
            mov qword [rbx + 8*rdi], rdx
            push rdx
         ; Statement results can be ignored
         pop rdx
;---------------------------------------------------------------------------
;---------------------------------------------------------------------------
         ; End of if
.__endif__93:
;------------------------------------------------------------------------------
;------------------------------------------------------------------------------
         ; For-Loop
         ; Init
         ; Assignment - '='
         ; RHS
            ; Int Literal
               mov rax, 0
               push rax
         ; LHS
            ; Variable Declaration - j
               mov rax, qword [rbp - 144]  ; __main__for__81__block__82.__else__86__block__92__for__96__j
         pop rdx ; rhs value
         mov qword [rbp - 144], rdx
         push rdx
         ; Loop init result can be discarded
         pop rax
         jmp .__forcond__96
.__for__96:
         ; Update
         ; Pre-Increment - int
            ; RHS
               ; Identifier - int j
                  push qword [rbp - 144]
            pop rdx
            add qword [rbp - 144], 1
            mov rax, qword [rbp - 144]
            push rax ; push result
         ; Loop update result can be discarded
         pop rax
.__forcond__96:
         ; Condition
         ; Less Than
            ; LHS
               ; Identifier - int j
                  push qword [rbp - 144]
            ; RHS
               ; Member Accessor
                  ; LHS
                     ; Identifier - Vector<:char[]:> tokens1
                        push qword [rbp - 136]
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
         je .__endfor__96
         ; Body
         ; Free Operator
            ; RHS
               ; Subscript
                  ; LHS
                     ; Member Accessor
                        ; LHS
                           ; Identifier - Vector<:char[]:> tokens1
                              push qword [rbp - 136]
                        ; RHS
                           push qword [.__field____main____Vector__char__1____data] ; stored index associated with field that is being accessed
                        pop rdx ; rhs
                        pop rax ; lhs
                        push qword [rax + 8*rdx] ; lhs.rhs
                  ; OFFSET
                     ; Identifier - int j
                        push qword [rbp - 144]
                  pop rdx ; __offset
                  pop rax ; __pointer
                  push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
            ; Free pointer
            pop rdi   ; pointer
            call free ; free the pointer
            push rax  ; undefined return value
         ; Statement results can be ignored
         pop rdx
         ; Repeat
jmp .__for__96
         ; End of For
.__endfor__96:
;------------------------------------------------------------------------------
         ; Free Operator
         ; RHS
         ; Identifier - Vector<:char[]:> tokens1
            push qword [rbp - 136]
         ; Free pointer
         pop rdi   ; pointer
         call free ; free the pointer
         push rax  ; undefined return value
         ; Statement results can be ignored
         pop rdx
;---------------------------------------------------------------------------------
;---------------------------------------------------------------------------------
         ; End of if
.__endif__86:
;------------------------------------------------------------------------------------
         ; Assignment - '='
         ; RHS
         ; Function Call - split(char[], char) -> Vector<:char[]:>
         ; Make space for 2 arg(s)
         sub rsp, 16
         ; Arguments
         ; Eval arg0
            ; Subscript
               ; LHS
                  ; Member Accessor
                     ; LHS
                        ; Identifier - Vector<:char[]:> lines
                           push qword [rbp - 16]
                     ; RHS
                        push qword [.__field____main____Vector__char__1____data] ; stored index associated with field that is being accessed
                     pop rdx ; rhs
                     pop rax ; lhs
                     push qword [rax + 8*rdx] ; lhs.rhs
               ; OFFSET
                  ; Addition - int, int
                     ; LHS
                        ; Identifier - int l
                           push qword [rbp - 56]
                     ; RHS
                        ; Int Literal
                           mov rax, 3
                           push rax
                     pop rdx ; rhs
                     pop rax ; lhs
                     add rax, rdx
                     push rax
               pop rdx ; __offset
               pop rax ; __pointer
               push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
         ; Move arg0's result to reverse order position on stack
         pop rax
         mov qword [rsp + 0], rax
         ; Eval arg1
            ; Char Literal
               push ' '
         ; Move arg1's result to reverse order position on stack
         pop rax
         mov qword [rsp + 8], rax
         ; Call split(char[], char)
         call .__main____split__char__1__char
         ; Remove args
         add rsp, 16
         ; Push return value
         push rax
         ; LHS
         ; Variable Declaration - tokens2
         mov rax, qword [rbp - 152]  ; __main__for__81__block__82__tokens2
         pop rdx ; rhs value
         mov qword [rbp - 152], rdx
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
            ; Subscript
               ; LHS
                  ; Member Accessor
                     ; LHS
                        ; Identifier - Vector<:char[]:> tokens2
                           push qword [rbp - 152]
                     ; RHS
                        push qword [.__field____main____Vector__char__1____data] ; stored index associated with field that is being accessed
                     pop rdx ; rhs
                     pop rax ; lhs
                     push qword [rax + 8*rdx] ; lhs.rhs
               ; OFFSET
                  ; Subtraction - int, int
                     ; LHS
                        ; Member Accessor
                           ; LHS
                              ; Identifier - Vector<:char[]:> tokens2
                                 push qword [rbp - 152]
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
                     sub rax, rdx
                     push rax
               pop rdx ; __offset
               pop rax ; __pointer
               push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
         ; Move arg0's result to reverse order position on stack
         pop rax
         mov qword [rsp + 0], rax
         ; Call stringToInt(char[])
         call __builtin__stringToInt__char__1
         ; Remove args
         add rsp, 8
         ; Push return value
         push rax
         ; LHS
         ; Member Accessor Assignment
         ; LHS
         ; Identifier - Monkey monkey
            push qword [rbp - 64]
         ; RHS
         push qword [.__field____main____Monkey____divisible_by] ; 
         pop rdi ; rhs
         pop rbx ; lhs
         pop rdx ; rhs value
         mov qword [rbx + 8*rdi], rdx
         push rdx
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
         ; Variable Declaration - j
         mov rax, qword [rbp - 160]  ; __main__for__81__block__82__for__97__j
         pop rdx ; rhs value
         mov qword [rbp - 160], rdx
         push rdx
         ; Loop init result can be discarded
         pop rax
         jmp .__forcond__97
.__for__97:
         ; Update
         ; Pre-Increment - int
         ; RHS
         ; Identifier - int j
            push qword [rbp - 160]
         pop rdx
         add qword [rbp - 160], 1
         mov rax, qword [rbp - 160]
         push rax ; push result
         ; Loop update result can be discarded
         pop rax
.__forcond__97:
         ; Condition
         ; Less Than
         ; LHS
         ; Identifier - int j
            push qword [rbp - 160]
         ; RHS
         ; Member Accessor
            ; LHS
               ; Identifier - Vector<:char[]:> tokens2
                  push qword [rbp - 152]
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
         je .__endfor__97
         ; Body
         ; Free Operator
         ; RHS
         ; Subscript
            ; LHS
               ; Member Accessor
                  ; LHS
                     ; Identifier - Vector<:char[]:> tokens2
                        push qword [rbp - 152]
                  ; RHS
                     push qword [.__field____main____Vector__char__1____data] ; stored index associated with field that is being accessed
                  pop rdx ; rhs
                  pop rax ; lhs
                  push qword [rax + 8*rdx] ; lhs.rhs
            ; OFFSET
               ; Identifier - int j
                  push qword [rbp - 160]
            pop rdx ; __offset
            pop rax ; __pointer
            push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
         ; Free pointer
         pop rdi   ; pointer
         call free ; free the pointer
         push rax  ; undefined return value
         ; Statement results can be ignored
         pop rdx
         ; Repeat
jmp .__for__97
         ; End of For
.__endfor__97:
;------------------------------------------------------------------------------------
         ; Free Operator
         ; RHS
         ; Identifier - Vector<:char[]:> tokens2
         push qword [rbp - 152]
         ; Free pointer
         pop rdi   ; pointer
         call free ; free the pointer
         push rax  ; undefined return value
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
         ; RHS
         ; Function Call - split(char[], char) -> Vector<:char[]:>
         ; Make space for 2 arg(s)
         sub rsp, 16
         ; Arguments
         ; Eval arg0
            ; Subscript
               ; LHS
                  ; Member Accessor
                     ; LHS
                        ; Identifier - Vector<:char[]:> lines
                           push qword [rbp - 16]
                     ; RHS
                        push qword [.__field____main____Vector__char__1____data] ; stored index associated with field that is being accessed
                     pop rdx ; rhs
                     pop rax ; lhs
                     push qword [rax + 8*rdx] ; lhs.rhs
               ; OFFSET
                  ; Addition - int, int
                     ; LHS
                        ; Identifier - int l
                           push qword [rbp - 56]
                     ; RHS
                        ; Int Literal
                           mov rax, 4
                           push rax
                     pop rdx ; rhs
                     pop rax ; lhs
                     add rax, rdx
                     push rax
               pop rdx ; __offset
               pop rax ; __pointer
               push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
         ; Move arg0's result to reverse order position on stack
         pop rax
         mov qword [rsp + 0], rax
         ; Eval arg1
            ; Char Literal
               push ' '
         ; Move arg1's result to reverse order position on stack
         pop rax
         mov qword [rsp + 8], rax
         ; Call split(char[], char)
         call .__main____split__char__1__char
         ; Remove args
         add rsp, 16
         ; Push return value
         push rax
         ; LHS
         ; Variable Declaration - tokens3
         mov rax, qword [rbp - 168]  ; __main__for__81__block__82__tokens3
         pop rdx ; rhs value
         mov qword [rbp - 168], rdx
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
            ; Subscript
               ; LHS
                  ; Member Accessor
                     ; LHS
                        ; Identifier - Vector<:char[]:> tokens3
                           push qword [rbp - 168]
                     ; RHS
                        push qword [.__field____main____Vector__char__1____data] ; stored index associated with field that is being accessed
                     pop rdx ; rhs
                     pop rax ; lhs
                     push qword [rax + 8*rdx] ; lhs.rhs
               ; OFFSET
                  ; Subtraction - int, int
                     ; LHS
                        ; Member Accessor
                           ; LHS
                              ; Identifier - Vector<:char[]:> tokens3
                                 push qword [rbp - 168]
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
                     sub rax, rdx
                     push rax
               pop rdx ; __offset
               pop rax ; __pointer
               push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
         ; Move arg0's result to reverse order position on stack
         pop rax
         mov qword [rsp + 0], rax
         ; Call stringToInt(char[])
         call __builtin__stringToInt__char__1
         ; Remove args
         add rsp, 8
         ; Push return value
         push rax
         ; LHS
         ; Member Accessor Assignment
         ; LHS
         ; Identifier - Monkey monkey
            push qword [rbp - 64]
         ; RHS
         push qword [.__field____main____Monkey____true_monkey_id] ; 
         pop rdi ; rhs
         pop rbx ; lhs
         pop rdx ; rhs value
         mov qword [rbx + 8*rdi], rdx
         push rdx
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
         ; Variable Declaration - j
         mov rax, qword [rbp - 176]  ; __main__for__81__block__82__for__98__j
         pop rdx ; rhs value
         mov qword [rbp - 176], rdx
         push rdx
         ; Loop init result can be discarded
         pop rax
         jmp .__forcond__98
.__for__98:
         ; Update
         ; Pre-Increment - int
         ; RHS
         ; Identifier - int j
            push qword [rbp - 176]
         pop rdx
         add qword [rbp - 176], 1
         mov rax, qword [rbp - 176]
         push rax ; push result
         ; Loop update result can be discarded
         pop rax
.__forcond__98:
         ; Condition
         ; Less Than
         ; LHS
         ; Identifier - int j
            push qword [rbp - 176]
         ; RHS
         ; Member Accessor
            ; LHS
               ; Identifier - Vector<:char[]:> tokens3
                  push qword [rbp - 168]
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
         je .__endfor__98
         ; Body
         ; Free Operator
         ; RHS
         ; Subscript
            ; LHS
               ; Member Accessor
                  ; LHS
                     ; Identifier - Vector<:char[]:> tokens3
                        push qword [rbp - 168]
                  ; RHS
                     push qword [.__field____main____Vector__char__1____data] ; stored index associated with field that is being accessed
                  pop rdx ; rhs
                  pop rax ; lhs
                  push qword [rax + 8*rdx] ; lhs.rhs
            ; OFFSET
               ; Identifier - int j
                  push qword [rbp - 176]
            pop rdx ; __offset
            pop rax ; __pointer
            push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
         ; Free pointer
         pop rdi   ; pointer
         call free ; free the pointer
         push rax  ; undefined return value
         ; Statement results can be ignored
         pop rdx
         ; Repeat
jmp .__for__98
         ; End of For
.__endfor__98:
;------------------------------------------------------------------------------------
         ; Free Operator
         ; RHS
         ; Identifier - Vector<:char[]:> tokens3
         push qword [rbp - 168]
         ; Free pointer
         pop rdi   ; pointer
         call free ; free the pointer
         push rax  ; undefined return value
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
         ; RHS
         ; Function Call - split(char[], char) -> Vector<:char[]:>
         ; Make space for 2 arg(s)
         sub rsp, 16
         ; Arguments
         ; Eval arg0
            ; Subscript
               ; LHS
                  ; Member Accessor
                     ; LHS
                        ; Identifier - Vector<:char[]:> lines
                           push qword [rbp - 16]
                     ; RHS
                        push qword [.__field____main____Vector__char__1____data] ; stored index associated with field that is being accessed
                     pop rdx ; rhs
                     pop rax ; lhs
                     push qword [rax + 8*rdx] ; lhs.rhs
               ; OFFSET
                  ; Addition - int, int
                     ; LHS
                        ; Identifier - int l
                           push qword [rbp - 56]
                     ; RHS
                        ; Int Literal
                           mov rax, 5
                           push rax
                     pop rdx ; rhs
                     pop rax ; lhs
                     add rax, rdx
                     push rax
               pop rdx ; __offset
               pop rax ; __pointer
               push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
         ; Move arg0's result to reverse order position on stack
         pop rax
         mov qword [rsp + 0], rax
         ; Eval arg1
            ; Char Literal
               push ' '
         ; Move arg1's result to reverse order position on stack
         pop rax
         mov qword [rsp + 8], rax
         ; Call split(char[], char)
         call .__main____split__char__1__char
         ; Remove args
         add rsp, 16
         ; Push return value
         push rax
         ; LHS
         ; Variable Declaration - tokens4
         mov rax, qword [rbp - 184]  ; __main__for__81__block__82__tokens4
         pop rdx ; rhs value
         mov qword [rbp - 184], rdx
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
            ; Subscript
               ; LHS
                  ; Member Accessor
                     ; LHS
                        ; Identifier - Vector<:char[]:> tokens4
                           push qword [rbp - 184]
                     ; RHS
                        push qword [.__field____main____Vector__char__1____data] ; stored index associated with field that is being accessed
                     pop rdx ; rhs
                     pop rax ; lhs
                     push qword [rax + 8*rdx] ; lhs.rhs
               ; OFFSET
                  ; Subtraction - int, int
                     ; LHS
                        ; Member Accessor
                           ; LHS
                              ; Identifier - Vector<:char[]:> tokens4
                                 push qword [rbp - 184]
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
                     sub rax, rdx
                     push rax
               pop rdx ; __offset
               pop rax ; __pointer
               push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
         ; Move arg0's result to reverse order position on stack
         pop rax
         mov qword [rsp + 0], rax
         ; Call stringToInt(char[])
         call __builtin__stringToInt__char__1
         ; Remove args
         add rsp, 8
         ; Push return value
         push rax
         ; LHS
         ; Member Accessor Assignment
         ; LHS
         ; Identifier - Monkey monkey
            push qword [rbp - 64]
         ; RHS
         push qword [.__field____main____Monkey____false_monkey_id] ; 
         pop rdi ; rhs
         pop rbx ; lhs
         pop rdx ; rhs value
         mov qword [rbx + 8*rdi], rdx
         push rdx
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
         ; Variable Declaration - j
         mov rax, qword [rbp - 192]  ; __main__for__81__block__82__for__99__j
         pop rdx ; rhs value
         mov qword [rbp - 192], rdx
         push rdx
         ; Loop init result can be discarded
         pop rax
         jmp .__forcond__99
.__for__99:
         ; Update
         ; Pre-Increment - int
         ; RHS
         ; Identifier - int j
            push qword [rbp - 192]
         pop rdx
         add qword [rbp - 192], 1
         mov rax, qword [rbp - 192]
         push rax ; push result
         ; Loop update result can be discarded
         pop rax
.__forcond__99:
         ; Condition
         ; Less Than
         ; LHS
         ; Identifier - int j
            push qword [rbp - 192]
         ; RHS
         ; Member Accessor
            ; LHS
               ; Identifier - Vector<:char[]:> tokens4
                  push qword [rbp - 184]
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
         je .__endfor__99
         ; Body
         ; Free Operator
         ; RHS
         ; Subscript
            ; LHS
               ; Member Accessor
                  ; LHS
                     ; Identifier - Vector<:char[]:> tokens4
                        push qword [rbp - 184]
                  ; RHS
                     push qword [.__field____main____Vector__char__1____data] ; stored index associated with field that is being accessed
                  pop rdx ; rhs
                  pop rax ; lhs
                  push qword [rax + 8*rdx] ; lhs.rhs
            ; OFFSET
               ; Identifier - int j
                  push qword [rbp - 192]
            pop rdx ; __offset
            pop rax ; __pointer
            push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
         ; Free pointer
         pop rdi   ; pointer
         call free ; free the pointer
         push rax  ; undefined return value
         ; Statement results can be ignored
         pop rdx
         ; Repeat
jmp .__for__99
         ; End of For
.__endfor__99:
;------------------------------------------------------------------------------------
         ; Free Operator
         ; RHS
         ; Identifier - Vector<:char[]:> tokens4
         push qword [rbp - 184]
         ; Free pointer
         pop rdi   ; pointer
         call free ; free the pointer
         push rax  ; undefined return value
         ; Statement results can be ignored
         pop rdx
         ; Method Call - Vector<:Monkey:>::pushBack(Monkey) -> void
         ; Make space for 1 arg(s) and object parameter
         sub rsp, 16
         ; LHS
         ; Identifier - Vector<:Monkey:> monkeys
         push qword [rbp - 48]
         pop rax ; object parameter
         mov qword [rsp + 0], rax ; place as first parameter
         ; RHS
         ; Arguments
         ; Eval arg0
         ; Identifier - Monkey monkey
         push qword [rbp - 64]
         ; Move arg0's result to reverse order position on stack
         pop rax
         mov qword [rsp + 8], rax
         call .__method____main____Vector__Monkey____pushBack__Monkey
         ; Remove args
         add rsp, 16
         ; Push return value
         push rax
         ; Statement results can be ignored
         pop rdx
;---------------------------------------------------------------------------------------
         ; Repeat
jmp .__for__81
         ; End of For
.__endfor__81:
;---------------------------------------------------------------------------------------------
; =============================================================================================
         ; Function Declaration - println(Vector<:Monkey:>) -> void
         ; Skip over function declaration
         jmp .__end____main____println__Vector__tparam0__Monkey
.__main____println__Vector__tparam0__Monkey:
         ; Function Header:
         ; Setup stack frame
         push rbp
         mov rbp, rsp
         sub rsp, 16
         ; Parameters
         ; Param: monkeys [rbp + 16]
         ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
         ; [rbp - 8] - int i (<unset-scope-name>)

         ; Body
;---------------------------------------------------------------------------------------
         ; Code Block
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
         mov rax, qword [rbp - 8]  ; __main__println__block__100__for__101__i
         pop rdx ; rhs value
         mov qword [rbp - 8], rdx
         push rdx
         ; Loop init result can be discarded
         pop rax
         jmp .__forcond__101
.__for__101:
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
.__forcond__101:
         ; Condition
         ; Less Than
         ; LHS
         ; Identifier - int i
            push qword [rbp - 8]
         ; RHS
         ; Member Accessor
            ; LHS
               ; Identifier - Vector<:Monkey:> monkeys
                  push qword [rbp - -16]
            ; RHS
               push qword [.__field____main____Vector__Monkey____size] ; stored index associated with field that is being accessed
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
         je .__endfor__101
         ; Body
;------------------------------------------------------------------------------
         ; Code Block
         ; Function Call - print(int) -> void
         ; Make space for 1 arg(s)
         sub rsp, 8
         ; Arguments
            ; Eval arg0
               ; Identifier - int i
                  push qword [rbp - 8]
            ; Move arg0's result to reverse order position on stack
            pop rax
            mov qword [rsp + 0], rax
         ; Call print(int)
         call __builtin__print__int
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
                  push ':'
            ; Move arg0's result to reverse order position on stack
            pop rax
            mov qword [rsp + 0], rax
         ; Call print(char)
         call __builtin__print__char
         ; Remove args
         add rsp, 8
         ; Push return value
         push rax
         ; Statement results can be ignored
         pop rdx
         ; Function Call - println<:int:>(Vector<:int:>) -> void
         ; Make space for 1 arg(s)
         sub rsp, 8
         ; Arguments
            ; Eval arg0
               ; Member Accessor
                  ; LHS
                     ; Subscript
                        ; LHS
                           ; Member Accessor
                              ; LHS
                                 ; Identifier - Vector<:Monkey:> monkeys
                                    push qword [rbp - -16]
                              ; RHS
                                 push qword [.__field____main____Vector__Monkey____data] ; stored index associated with field that is being accessed
                              pop rdx ; rhs
                              pop rax ; lhs
                              push qword [rax + 8*rdx] ; lhs.rhs
                        ; OFFSET
                           ; Identifier - int i
                              push qword [rbp - 8]
                        pop rdx ; __offset
                        pop rax ; __pointer
                        push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                  ; RHS
                     push qword [.__field____main____Monkey____items] ; stored index associated with field that is being accessed
                  pop rdx ; rhs
                  pop rax ; lhs
                  push qword [rax + 8*rdx] ; lhs.rhs
            ; Move arg0's result to reverse order position on stack
            pop rax
            mov qword [rsp + 0], rax
         ; Call println<:int:>(Vector<:int:>)
         call .__main____println__int____Vector__tparam0__int
         ; Remove args
         add rsp, 8
         ; Push return value
         push rax
         ; Statement results can be ignored
         pop rdx
;------------------------------------------------------------------------------
         ; Repeat
jmp .__for__101
         ; End of For
.__endfor__101:
;------------------------------------------------------------------------------------
;---------------------------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
.__end____main____println__Vector__tparam0__Monkey:
         ; End Function Declaration - println(Vector<:Monkey:>) -> void
; =============================================================================================

;---------------------------------------------------------------------------------------------
         ; For-Loop
         ; Init
         ; Assignment - '='
         ; RHS
         ; Int Literal
         mov rax, 0
         push rax
         ; LHS
         ; Variable Declaration - r
         mov rax, qword [rbp - 200]  ; __main__for__103__r
         pop rdx ; rhs value
         mov qword [rbp - 200], rdx
         push rdx
         ; Loop init result can be discarded
         pop rax
         jmp .__forcond__103
.__for__103:
         ; Update
         ; Pre-Increment - int
         ; RHS
         ; Identifier - int r
         push qword [rbp - 200]
         pop rdx
         add qword [rbp - 200], 1
         mov rax, qword [rbp - 200]
         push rax ; push result
         ; Loop update result can be discarded
         pop rax
.__forcond__103:
         ; Condition
         ; Less Than
         ; LHS
         ; Identifier - int r
         push qword [rbp - 200]
         ; RHS
         ; Int Literal
         mov rax, 20
         push rax
         pop rdx ; rhs
         pop rax ; lhs
         cmp rax, rdx
         setl al
         movzx eax, al
         push rax
         pop rax ; __cond
         cmp rax, 0 ; __cond
         je .__endfor__103
         ; Body
;---------------------------------------------------------------------------------------
         ; Code Block
;------------------------------------------------------------------------------------
         ; For-Loop
         ; Init
         ; Assignment - '='
         ; RHS
         ; Int Literal
         mov rax, 0
         push rax
         ; LHS
         ; Variable Declaration - m
         mov rax, qword [rbp - 208]  ; __main__for__103__block__104__for__105__m
         pop rdx ; rhs value
         mov qword [rbp - 208], rdx
         push rdx
         ; Loop init result can be discarded
         pop rax
         jmp .__forcond__105
.__for__105:
         ; Update
         ; Pre-Increment - int
         ; RHS
         ; Identifier - int m
            push qword [rbp - 208]
         pop rdx
         add qword [rbp - 208], 1
         mov rax, qword [rbp - 208]
         push rax ; push result
         ; Loop update result can be discarded
         pop rax
.__forcond__105:
         ; Condition
         ; Less Than
         ; LHS
         ; Identifier - int m
            push qword [rbp - 208]
         ; RHS
         ; Member Accessor
            ; LHS
               ; Identifier - Vector<:Monkey:> monkeys
                  push qword [rbp - 48]
            ; RHS
               push qword [.__field____main____Vector__Monkey____size] ; stored index associated with field that is being accessed
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
         je .__endfor__105
         ; Body
;------------------------------------------------------------------------------
         ; Code Block
         ; Assignment - '='
         ; RHS
            ; Subscript
               ; LHS
                  ; Member Accessor
                     ; LHS
                        ; Identifier - Vector<:Monkey:> monkeys
                           push qword [rbp - 48]
                     ; RHS
                        push qword [.__field____main____Vector__Monkey____data] ; stored index associated with field that is being accessed
                     pop rdx ; rhs
                     pop rax ; lhs
                     push qword [rax + 8*rdx] ; lhs.rhs
               ; OFFSET
                  ; Identifier - int m
                     push qword [rbp - 208]
               pop rdx ; __offset
               pop rax ; __pointer
               push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
         ; LHS
            ; Variable Declaration - monkey
               mov rax, qword [rbp - 216]  ; __main__for__103__block__104__for__105__block__106__monkey
         pop rdx ; rhs value
         mov qword [rbp - 216], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
         ; RHS
            ; Member Accessor
               ; LHS
                  ; Identifier - Monkey monkey
                     push qword [rbp - 216]
               ; RHS
                  push qword [.__field____main____Monkey____items] ; stored index associated with field that is being accessed
               pop rdx ; rhs
               pop rax ; lhs
               push qword [rax + 8*rdx] ; lhs.rhs
         ; LHS
            ; Variable Declaration - monkey_items
               mov rax, qword [rbp - 224]  ; __main__for__103__block__104__for__105__block__106__monkey_items
         pop rdx ; rhs value
         mov qword [rbp - 224], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
;---------------------------------------------------------------------------
         ; For-Loop
         ; Init
         ; Assignment - '='
            ; RHS
               ; Int Literal
                  mov rax, 0
                  push rax
            ; LHS
               ; Variable Declaration - i
                  mov rax, qword [rbp - 232]  ; __main__for__103__block__104__for__105__block__106__for__107__i
            pop rdx ; rhs value
            mov qword [rbp - 232], rdx
            push rdx
         ; Loop init result can be discarded
         pop rax
         jmp .__forcond__107
.__for__107:
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
.__forcond__107:
         ; Condition
            ; Less Than
               ; LHS
                  ; Identifier - int i
                     push qword [rbp - 232]
               ; RHS
                  ; Member Accessor
                     ; LHS
                        ; Identifier - Vector<:int:> monkey_items
                           push qword [rbp - 224]
                     ; RHS
                        push qword [.__field____main____Vector__int____size] ; stored index associated with field that is being accessed
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
            je .__endfor__107
         ; Body
   ;---------------------------------------------------------------------
            ; Code Block
               ; Assignment - '='
                  ; RHS
                     ; Subscript
                        ; LHS
                           ; Member Accessor
                              ; LHS
                                 ; Identifier - Vector<:int:> monkey_items
                                    push qword [rbp - 224]
                              ; RHS
                                 push qword [.__field____main____Vector__int____data] ; stored index associated with field that is being accessed
                              pop rdx ; rhs
                              pop rax ; lhs
                              push qword [rax + 8*rdx] ; lhs.rhs
                        ; OFFSET
                           ; Identifier - int i
                              push qword [rbp - 232]
                        pop rdx ; __offset
                        pop rax ; __pointer
                        push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                  ; LHS
                     ; Variable Declaration - worry_level
                        mov rax, qword [rbp - 240]  ; __main__for__103__block__104__for__105__block__106__for__107__block__108__worry_level
                  pop rdx ; rhs value
                  mov qword [rbp - 240], rdx
                  push rdx
               ; Statement results can be ignored
               pop rdx
      ;------------------------------------------------------------------
               ; If-Statement
                  ; Condition
                     ; Equal
                        ; LHS
                           ; Member Accessor
                              ; LHS
                                 ; Identifier - Monkey monkey
                                    push qword [rbp - 216]
                              ; RHS
                                 push qword [.__field____main____Monkey____op] ; stored index associated with field that is being accessed
                              pop rdx ; rhs
                              pop rax ; lhs
                              push qword [rax + 8*rdx] ; lhs.rhs
                        ; RHS
                           ; Identifier - int OP_ADD
                              push qword [rbp - 32]
                        pop rdx ; rhs
                        pop rax ; lhs
                        cmp rax, rdx
                        sete al
                        movzx eax, al
                        push rax
                     pop rdx ; __cond
                     cmp rdx, 0 ; ensure condition is true
                     je .__elif__109x0 ; jump to first elif
                  ; Body
                     ; Assignment - '+='
                        ; RHS
                           ; Member Accessor
                              ; LHS
                                 ; Identifier - Monkey monkey
                                    push qword [rbp - 216]
                              ; RHS
                                 push qword [.__field____main____Monkey____operand] ; stored index associated with field that is being accessed
                              pop rdx ; rhs
                              pop rax ; lhs
                              push qword [rax + 8*rdx] ; lhs.rhs
                        pop rdx ; rhs value
                        mov rax, qword [rbp - 240] ; read lhs value
                        add rax, rdx      ; add lhs and rhs
                        mov qword [rbp - 240], rax ; write back to lhs
                        push rax          ; push result for other expressions
                     ; Statement results can be ignored
                     pop rdx
                  jmp .__endif__109 ; jump to end of condition chain
         ;---------------------------------------------------------------
                  ; Elif-Statement
.__elif__109x0:
                     ; Condition
                     ; Equal
                        ; LHS
                           ; Member Accessor
                              ; LHS
                                 ; Identifier - Monkey monkey
                                    push qword [rbp - 216]
                              ; RHS
                                 push qword [.__field____main____Monkey____op] ; stored index associated with field that is being accessed
                              pop rdx ; rhs
                              pop rax ; lhs
                              push qword [rax + 8*rdx] ; lhs.rhs
                        ; RHS
                           ; Identifier - int OP_MUL
                              push qword [rbp - 24]
                        pop rdx ; rhs
                        pop rax ; lhs
                        cmp rax, rdx
                        sete al
                        movzx eax, al
                        push rax
                     pop rdx ; __cond
                     cmp rdx, 0 ; ensure condition is true
                     je .__else__109
                     ; Body
                     ; Assignment - '*='
                        ; RHS
                           ; Member Accessor
                              ; LHS
                                 ; Identifier - Monkey monkey
                                    push qword [rbp - 216]
                              ; RHS
                                 push qword [.__field____main____Monkey____operand] ; stored index associated with field that is being accessed
                              pop rdx ; rhs
                              pop rax ; lhs
                              push qword [rax + 8*rdx] ; lhs.rhs
                        pop rdx ; rhs value
                        mov rax, qword [rbp - 240] ; read lhs value
                        imul rax, rdx      ; lhs = lhs * rhs
                        mov qword [rbp - 240], rax ; write back to lhs
                        push rax          ; push result for other expressions
                     ; Statement results can be ignored
                     pop rdx
                     jmp .__endif__109
         ;---------------------------------------------------------------
         ;---------------------------------------------------------------
                  ; Else-Statement
.__else__109:
                  ; Assignment - '*='
                     ; RHS
                        ; Identifier - int worry_level
                           push qword [rbp - 240]
                     pop rdx ; rhs value
                     mov rax, qword [rbp - 240] ; read lhs value
                     imul rax, rdx      ; lhs = lhs * rhs
                     mov qword [rbp - 240], rax ; write back to lhs
                     push rax          ; push result for other expressions
                  ; Statement results can be ignored
                  pop rdx
         ;---------------------------------------------------------------
                  ; End of if
.__endif__109:
      ;------------------------------------------------------------------
               ; Assignment - '='
                  ; RHS
                     ; Division - int, int
                        ; LHS
                           ; Identifier - int worry_level
                              push qword [rbp - 240]
                        ; RHS
                           ; Int Literal
                              mov rax, 3
                              push rax
                        pop rdx
                        pop rax
                        mov rsi, rdx
                        xor rdx, rdx
                        cqo ; sign extend rax into rdx (specifically for 64bit -> 128bit)
                        idiv rsi ; perform rdx:rax (128bit) / rsi (64bit) = rax
                        push rax
                  pop rdx ; rhs value
                  mov qword [rbp - 240], rdx
                  push rdx
               ; Statement results can be ignored
               pop rdx
      ;------------------------------------------------------------------
               ; If-Statement
                  ; Condition
                     ; Equal
                        ; LHS
                           ; Mod - int, int
                              ; LHS
                                 ; Identifier - int worry_level
                                    push qword [rbp - 240]
                              ; RHS
                                 ; Member Accessor
                                    ; LHS
                                       ; Identifier - Monkey monkey
                                          push qword [rbp - 216]
                                    ; RHS
                                       push qword [.__field____main____Monkey____divisible_by] ; stored index associated with field that is being accessed
                                    pop rdx ; rhs
                                    pop rax ; lhs
                                    push qword [rax + 8*rdx] ; lhs.rhs
                              pop rdx
                              pop rax
                              mov rsi, rdx
                              xor rdx, rdx
                              cqo ; sign extend rax into rdx (specifically for 64bit -> 128bit)
                              idiv rsi ; perform rdx:rax (128bit) / rsi (64bit)
                              mov rax, rdx ; move remainder to rax
                              push rax
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
                     je .__else__110 ; jump to else
                  ; Body
                     ; Method Call - Vector<:int:>::pushBack(int) -> void
                        ; Make space for 1 arg(s) and object parameter
                        sub rsp, 16
                        ; LHS
                           ; Member Accessor
                              ; LHS
                                 ; Subscript
                                    ; LHS
                                       ; Member Accessor
                                          ; LHS
                                             ; Identifier - Vector<:Monkey:> monkeys
                                                push qword [rbp - 48]
                                          ; RHS
                                             push qword [.__field____main____Vector__Monkey____data] ; stored index associated with field that is being accessed
                                          pop rdx ; rhs
                                          pop rax ; lhs
                                          push qword [rax + 8*rdx] ; lhs.rhs
                                    ; OFFSET
                                       ; Member Accessor
                                          ; LHS
                                             ; Identifier - Monkey monkey
                                                push qword [rbp - 216]
                                          ; RHS
                                             push qword [.__field____main____Monkey____true_monkey_id] ; stored index associated with field that is being accessed
                                          pop rdx ; rhs
                                          pop rax ; lhs
                                          push qword [rax + 8*rdx] ; lhs.rhs
                                    pop rdx ; __offset
                                    pop rax ; __pointer
                                    push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                              ; RHS
                                 push qword [.__field____main____Monkey____items] ; stored index associated with field that is being accessed
                              pop rdx ; rhs
                              pop rax ; lhs
                              push qword [rax + 8*rdx] ; lhs.rhs
                           pop rax ; object parameter
                           mov qword [rsp + 0], rax ; place as first parameter
                        ; RHS
                        ; Arguments
                           ; Eval arg0
                              ; Identifier - int worry_level
                                 push qword [rbp - 240]
                           ; Move arg0's result to reverse order position on stack
                           pop rax
                           mov qword [rsp + 8], rax
                        call .__method____main____Vector__int____pushBack__int
                        ; Remove args
                        add rsp, 16
                        ; Push return value
                        push rax
                     ; Statement results can be ignored
                     pop rdx
                  jmp .__endif__110 ; jump to end of condition chain
         ;---------------------------------------------------------------
                  ; Else-Statement
.__else__110:
                  ; Method Call - Vector<:int:>::pushBack(int) -> void
                     ; Make space for 1 arg(s) and object parameter
                     sub rsp, 16
                     ; LHS
                        ; Member Accessor
                           ; LHS
                              ; Subscript
                                 ; LHS
                                    ; Member Accessor
                                       ; LHS
                                          ; Identifier - Vector<:Monkey:> monkeys
                                             push qword [rbp - 48]
                                       ; RHS
                                          push qword [.__field____main____Vector__Monkey____data] ; stored index associated with field that is being accessed
                                       pop rdx ; rhs
                                       pop rax ; lhs
                                       push qword [rax + 8*rdx] ; lhs.rhs
                                 ; OFFSET
                                    ; Member Accessor
                                       ; LHS
                                          ; Identifier - Monkey monkey
                                             push qword [rbp - 216]
                                       ; RHS
                                          push qword [.__field____main____Monkey____false_monkey_id] ; stored index associated with field that is being accessed
                                       pop rdx ; rhs
                                       pop rax ; lhs
                                       push qword [rax + 8*rdx] ; lhs.rhs
                                 pop rdx ; __offset
                                 pop rax ; __pointer
                                 push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                           ; RHS
                              push qword [.__field____main____Monkey____items] ; stored index associated with field that is being accessed
                           pop rdx ; rhs
                           pop rax ; lhs
                           push qword [rax + 8*rdx] ; lhs.rhs
                        pop rax ; object parameter
                        mov qword [rsp + 0], rax ; place as first parameter
                     ; RHS
                     ; Arguments
                        ; Eval arg0
                           ; Identifier - int worry_level
                              push qword [rbp - 240]
                        ; Move arg0's result to reverse order position on stack
                        pop rax
                        mov qword [rsp + 8], rax
                     call .__method____main____Vector__int____pushBack__int
                     ; Remove args
                     add rsp, 16
                     ; Push return value
                     push rax
                  ; Statement results can be ignored
                  pop rdx
         ;---------------------------------------------------------------
                  ; End of if
.__endif__110:
      ;------------------------------------------------------------------
               ; Assignment - '+='
                  ; RHS
                     ; Int Literal
                        mov rax, 1
                        push rax
                  ; LHS
                     ; Member Accessor Assignment
                        ; LHS
                           ; Identifier - Monkey monkey
                              push qword [rbp - 216]
                        ; RHS
                           push qword [.__field____main____Monkey____inspected_items] ; 
                        pop rdi ; rhs
                        pop rbx ; lhs
                  pop rdx ; rhs value
                  mov rax, qword [rbx + 8*rdi] ; read lhs value
                  add rax, rdx      ; add lhs and rhs
                  mov qword [rbx + 8*rdi], rax ; write back to lhs
                  push rax          ; push result for other expressions
               ; Statement results can be ignored
               pop rdx
   ;---------------------------------------------------------------------
         ; Repeat
jmp .__for__107
         ; End of For
.__endfor__107:
;---------------------------------------------------------------------------
         ; Method Call - Vector<:int:>::clear() -> void
         ; Make space for 0 arg(s) and object parameter
         sub rsp, 8
         ; LHS
            ; Identifier - Vector<:int:> monkey_items
               push qword [rbp - 224]
            pop rax ; object parameter
            mov qword [rsp + 0], rax ; place as first parameter
         ; RHS
         ; Arguments
         call .__method____main____Vector__int____clear
         ; Remove args
         add rsp, 8
         ; Push return value
         push rax
         ; Statement results can be ignored
         pop rdx
;------------------------------------------------------------------------------
         ; Repeat
jmp .__for__105
         ; End of For
.__endfor__105:
;------------------------------------------------------------------------------------
;---------------------------------------------------------------------------------------
         ; Repeat
jmp .__for__103
         ; End of For
.__endfor__103:
;---------------------------------------------------------------------------------------------
         ; Assignment - '='
         ; RHS
         ; Int Literal
         mov rax, 0
         push rax
         ; LHS
         ; Variable Declaration - firstmax
         mov rax, qword [rbp - 248]  ; __main__firstmax
         pop rdx ; rhs value
         mov qword [rbp - 248], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
         ; RHS
         ; Int Literal
         mov rax, 0
         push rax
         ; LHS
         ; Variable Declaration - secondmax
         mov rax, qword [rbp - 256]  ; __main__secondmax
         pop rdx ; rhs value
         mov qword [rbp - 256], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
;---------------------------------------------------------------------------------------------
         ; For-Loop
         ; Init
         ; Assignment - '='
         ; RHS
         ; Int Literal
         mov rax, 0
         push rax
         ; LHS
         ; Variable Declaration - i
         mov rax, qword [rbp - 264]  ; __main__for__111__i
         pop rdx ; rhs value
         mov qword [rbp - 264], rdx
         push rdx
         ; Loop init result can be discarded
         pop rax
         jmp .__forcond__111
.__for__111:
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
.__forcond__111:
         ; Condition
         ; Less Than
         ; LHS
         ; Identifier - int i
         push qword [rbp - 264]
         ; RHS
         ; Member Accessor
         ; LHS
         ; Identifier - Vector<:Monkey:> monkeys
         push qword [rbp - 48]
         ; RHS
         push qword [.__field____main____Vector__Monkey____size] ; stored index associated with field that is being accessed
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
         ; Assignment - '='
         ; RHS
         ; Function Call - max(int, int) -> int
         ; Make space for 2 arg(s)
         sub rsp, 16
         ; Arguments
         ; Eval arg0
         ; Member Accessor
            ; LHS
               ; Subscript
                  ; LHS
                     ; Member Accessor
                        ; LHS
                           ; Identifier - Vector<:Monkey:> monkeys
                              push qword [rbp - 48]
                        ; RHS
                           push qword [.__field____main____Vector__Monkey____data] ; stored index associated with field that is being accessed
                        pop rdx ; rhs
                        pop rax ; lhs
                        push qword [rax + 8*rdx] ; lhs.rhs
                  ; OFFSET
                     ; Identifier - int i
                        push qword [rbp - 264]
                  pop rdx ; __offset
                  pop rax ; __pointer
                  push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
            ; RHS
               push qword [.__field____main____Monkey____inspected_items] ; stored index associated with field that is being accessed
            pop rdx ; rhs
            pop rax ; lhs
            push qword [rax + 8*rdx] ; lhs.rhs
         ; Move arg0's result to reverse order position on stack
         pop rax
         mov qword [rsp + 0], rax
         ; Eval arg1
         ; Identifier - int firstmax
            push qword [rbp - 248]
         ; Move arg1's result to reverse order position on stack
         pop rax
         mov qword [rsp + 8], rax
         ; Call max(int, int)
         call .__main____max__int__int
         ; Remove args
         add rsp, 16
         ; Push return value
         push rax
         pop rdx ; rhs value
         mov qword [rbp - 248], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
         ; Repeat
jmp .__for__111
         ; End of For
.__endfor__111:
;---------------------------------------------------------------------------------------------
;---------------------------------------------------------------------------------------------
         ; For-Loop
         ; Init
         ; Assignment - '='
         ; RHS
         ; Int Literal
         mov rax, 0
         push rax
         ; LHS
         ; Variable Declaration - i
         mov rax, qword [rbp - 272]  ; __main__for__112__i
         pop rdx ; rhs value
         mov qword [rbp - 272], rdx
         push rdx
         ; Loop init result can be discarded
         pop rax
         jmp .__forcond__112
.__for__112:
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
.__forcond__112:
         ; Condition
         ; Less Than
         ; LHS
         ; Identifier - int i
         push qword [rbp - 272]
         ; RHS
         ; Member Accessor
         ; LHS
         ; Identifier - Vector<:Monkey:> monkeys
         push qword [rbp - 48]
         ; RHS
         push qword [.__field____main____Vector__Monkey____size] ; stored index associated with field that is being accessed
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
         je .__endfor__112
         ; Body
;---------------------------------------------------------------------------------------
         ; If-Statement
         ; Condition
         ; Not Equal
         ; LHS
         ; Member Accessor
         ; LHS
            ; Subscript
               ; LHS
                  ; Member Accessor
                     ; LHS
                        ; Identifier - Vector<:Monkey:> monkeys
                           push qword [rbp - 48]
                     ; RHS
                        push qword [.__field____main____Vector__Monkey____data] ; stored index associated with field that is being accessed
                     pop rdx ; rhs
                     pop rax ; lhs
                     push qword [rax + 8*rdx] ; lhs.rhs
               ; OFFSET
                  ; Identifier - int i
                     push qword [rbp - 272]
               pop rdx ; __offset
               pop rax ; __pointer
               push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
         ; RHS
            push qword [.__field____main____Monkey____inspected_items] ; stored index associated with field that is being accessed
         pop rdx ; rhs
         pop rax ; lhs
         push qword [rax + 8*rdx] ; lhs.rhs
         ; RHS
         ; Identifier - int firstmax
         push qword [rbp - 248]
         pop rdx ; rhs
         pop rax ; lhs
         cmp rax, rdx
         setne al
         movzx eax, al
         push rax
         pop rdx ; __cond
         cmp rdx, 0 ; ensure condition is true
         je .__endif__113 ; jump to end
         ; Body
         ; Assignment - '='
         ; RHS
         ; Function Call - max(int, int) -> int
         ; Make space for 2 arg(s)
         sub rsp, 16
         ; Arguments
            ; Eval arg0
               ; Member Accessor
                  ; LHS
                     ; Subscript
                        ; LHS
                           ; Member Accessor
                              ; LHS
                                 ; Identifier - Vector<:Monkey:> monkeys
                                    push qword [rbp - 48]
                              ; RHS
                                 push qword [.__field____main____Vector__Monkey____data] ; stored index associated with field that is being accessed
                              pop rdx ; rhs
                              pop rax ; lhs
                              push qword [rax + 8*rdx] ; lhs.rhs
                        ; OFFSET
                           ; Identifier - int i
                              push qword [rbp - 272]
                        pop rdx ; __offset
                        pop rax ; __pointer
                        push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                  ; RHS
                     push qword [.__field____main____Monkey____inspected_items] ; stored index associated with field that is being accessed
                  pop rdx ; rhs
                  pop rax ; lhs
                  push qword [rax + 8*rdx] ; lhs.rhs
            ; Move arg0's result to reverse order position on stack
            pop rax
            mov qword [rsp + 0], rax
            ; Eval arg1
               ; Identifier - int secondmax
                  push qword [rbp - 256]
            ; Move arg1's result to reverse order position on stack
            pop rax
            mov qword [rsp + 8], rax
         ; Call max(int, int)
         call .__main____max__int__int
         ; Remove args
         add rsp, 16
         ; Push return value
         push rax
         pop rdx ; rhs value
         mov qword [rbp - 256], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
         jmp .__endif__113 ; jump to end of condition chain
         ; End of if
.__endif__113:
;---------------------------------------------------------------------------------------
         ; Repeat
jmp .__for__112
         ; End of For
.__endfor__112:
;---------------------------------------------------------------------------------------------
         ; Function Call - println(int) -> void
         ; Make space for 1 arg(s)
         sub rsp, 8
         ; Arguments
         ; Eval arg0
         ; Multiplication - int, int
         ; LHS
         ; Identifier - int firstmax
         push qword [rbp - 248]
         ; RHS
         ; Identifier - int secondmax
         push qword [rbp - 256]
         pop rdx
         pop rax
         imul rax, rdx
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
; =============================================================================================
; ### END OF CODE #############################################################################
; =============================================================================================

         push 0
         call __builtin__exit__int
; =============================================================================================
; ### DATA SECTION ############################################################################
; =============================================================================================

         section .data
.float0: dq 0.0
.floatNegOne: dq -1.0
.floatZero: dq 0.0
.floatOne: dq 1.0
