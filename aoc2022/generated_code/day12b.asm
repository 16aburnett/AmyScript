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
         sub rsp, 144
         ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
         ; [rbp - 8] - char[] line (<unset-scope-name>)
         ; [rbp - 16] - Vector<:char[]:> lines (<unset-scope-name>)
         ; [rbp - 24] - Vector<:Vector<:int:>:> elevations (<unset-scope-name>)
         ; [rbp - 32] - Vector<:Vector<:int:>:> was_visited (<unset-scope-name>)
         ; [rbp - 40] - char[] alphabet (<unset-scope-name>)
         ; [rbp - 48] - Vec start_pos (<unset-scope-name>)
         ; [rbp - 56] - Vec end_pos (<unset-scope-name>)
         ; [rbp - 64] - LinkedList<:Vec:> starting_positions (<unset-scope-name>)
         ; [rbp - 72] - int l (<unset-scope-name>)
         ; [rbp - 80] - int size (<unset-scope-name>)
         ; [rbp - 88] - int c (<unset-scope-name>)
         ; [rbp - 96] - int val (<unset-scope-name>)
         ; [rbp - 104] - int min_moves (<unset-scope-name>)
         ; [rbp - 112] - Vec starting_pos (<unset-scope-name>)
         ; [rbp - 120] - int i (<unset-scope-name>)
         ; [rbp - 128] - int j (<unset-scope-name>)
         ; [rbp - 136] - int res (<unset-scope-name>)

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
         ; Class Declaration - __main____Vector__Vector inherits __builtin____main__Object
            ; Class data
            section .data
               ; Dispatch Table - this might need to be a malloc**
               .__dtable____main____Vector__Vector:
               ; Dispatch Table Entries
               dq .__method____main____Vector__Vector____pushBack__Vector ; 0
               dq .__method____main____Vector__Vector____popBack ; 1
               dq .__method____main____Vector__Vector____clear ; 2
               dq .__method____main____Vector__Vector____get__int ; 3
               dq .__method____main____Vector__Vector____set__int__Vector ; 4
            section .text
   ;---------------------------------------------------------------------
            ; Field - Vector<:int:>[] Vector<:Vector<:int:>:>::data
            section .data
            .__field____main____Vector__Vector____data: dq 1
            section .text
   ;---------------------------------------------------------------------
   ;---------------------------------------------------------------------
            ; Field - int Vector<:Vector<:int:>:>::size
            section .data
            .__field____main____Vector__Vector____size: dq 2
            section .text
   ;---------------------------------------------------------------------
   ;---------------------------------------------------------------------
            ; Field - int Vector<:Vector<:int:>:>::capacity
            section .data
            .__field____main____Vector__Vector____capacity: dq 3
            section .text
   ;---------------------------------------------------------------------
         ; skip over class methods
         jmp .__endclass____main____Vector__Vector
   ;---------------------------------------------------------------------
            ; Constructor Declaration - Vector<:Vector<:int:>:>::Vector() -> Vector<:Vector<:int:>:>
            jmp .__end__ctor____main____Vector__Vector____Vector
            .__ctor____main____Vector__Vector____Vector:
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
                  mov qword [rax + 0], .__dtable____main____Vector__Vector ; this[0] = &dtable
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
                              push qword [.__field____main____Vector__Vector____capacity] ; 
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
                              push qword [.__field____main____Vector__Vector____size] ; 
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
                                 push qword [.__field____main____Vector__Vector____capacity] ; stored index associated with field that is being accessed
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
                              push qword [.__field____main____Vector__Vector____data] ; 
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
         .__end__ctor____main____Vector__Vector____Vector:
         ; End Constructor Declaration - __ctor____main____Vector__Vector____Vector
;------------------------------------------------------------------------

;------------------------------------------------------------------------
         ; Constructor Declaration - Vector<:Vector<:int:>:>::Vector(int) -> Vector<:Vector<:int:>:>
         jmp .__end__ctor____main____Vector__Vector____Vector__int
         .__ctor____main____Vector__Vector____Vector__int:
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
               mov qword [rax + 0], .__dtable____main____Vector__Vector ; this[0] = &dtable
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
                           push qword [.__field____main____Vector__Vector____capacity] ; 
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
                           push qword [.__field____main____Vector__Vector____size] ; 
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
                              push qword [.__field____main____Vector__Vector____capacity] ; stored index associated with field that is being accessed
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
                           push qword [.__field____main____Vector__Vector____data] ; 
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
         .__end__ctor____main____Vector__Vector____Vector__int:
         ; End Constructor Declaration - __ctor____main____Vector__Vector____Vector__int
;---------------------------------------------------------------------------

;---------------------------------------------------------------------------
         ; Method Declaration - Vector<:Vector<:int:>:>::pushBack(Vector<:int:>) -> void
         jmp .__end__method____main____Vector__Vector____pushBack__Vector
         .__method____main____Vector__Vector____pushBack__Vector:
         ; Function Header:
         ; Setup stack frame
            push rbp
            mov rbp, rsp
            ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
               sub rsp, 32 ; space for local variables (16-byte aligned)
               ; [rbp - 8] - this - Reference to 'this' object instance
               mov rdx, qword [rbp + 16] ; param passed 'this'
               mov qword [rbp - 8], rdx ; save this to a local
               ; [rbp - 16] - Vector<:int:>[] nData (<unset-scope-name>)
               ; [rbp - 24] - int i (<unset-scope-name>)
         ; Parameters
            ; Param: val [rbp + 24] (__main____Vector__Vector__pushBack__val)
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
                                       push qword [.__field____main____Vector__Vector____size] ; stored index associated with field that is being accessed
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
                                 push qword [.__field____main____Vector__Vector____capacity] ; stored index associated with field that is being accessed
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
                                          push qword [.__field____main____Vector__Vector____capacity] ; stored index associated with field that is being accessed
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
                                    push qword [.__field____main____Vector__Vector____capacity] ; 
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
                                       push qword [.__field____main____Vector__Vector____capacity] ; stored index associated with field that is being accessed
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
                                 mov rax, qword [rbp - 16]  ; __main____Vector__Vector__pushBack__block__14__if__15__block__16__nData
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
                                    mov rax, qword [rbp - 24]  ; __main____Vector__Vector__pushBack__block__14__if__15__block__16__for__17__i
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
                                          push qword [.__field____main____Vector__Vector____size] ; stored index associated with field that is being accessed
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
                                                   push qword [.__field____main____Vector__Vector____data] ; stored index associated with field that is being accessed
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
                                             ; Identifier - Vector<:int:>[] nData
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
                                    push qword [.__field____main____Vector__Vector____data] ; stored index associated with field that is being accessed
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
                              ; Identifier - Vector<:int:>[] nData
                                 push qword [rbp - 16]
                           ; LHS
                              ; Member Accessor Assignment
                                 ; LHS
                                    ; This keyword
                                       push qword [rbp - 8] ; __this
                                 ; RHS
                                    push qword [.__field____main____Vector__Vector____data] ; 
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
                     ; Identifier - Vector<:int:> val
                        push qword [rbp - -24]
                  ; LHS
                     ; Subscript assignment
                        ; LHS
                           ; Member Accessor
                              ; LHS
                                 ; This keyword
                                    push qword [rbp - 8] ; __this
                              ; RHS
                                 push qword [.__field____main____Vector__Vector____data] ; stored index associated with field that is being accessed
                              pop rdx ; rhs
                              pop rax ; lhs
                              push qword [rax + 8*rdx] ; lhs.rhs
                        ; OFFSET
                           ; Member Accessor
                              ; LHS
                                 ; This keyword
                                    push qword [rbp - 8] ; __this
                              ; RHS
                                 push qword [.__field____main____Vector__Vector____size] ; stored index associated with field that is being accessed
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
                           push qword [.__field____main____Vector__Vector____size] ; stored index associated with field that is being accessed
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
                           push qword [.__field____main____Vector__Vector____size] ; size
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
         .__end__method____main____Vector__Vector____pushBack__Vector:
         ; End Method Declaration - .__method____main____Vector__Vector____pushBack__Vector
;---------------------------------------------------------------------------

;---------------------------------------------------------------------------
         ; Method Declaration - Vector<:Vector<:int:>:>::popBack() -> Vector<:int:>
         jmp .__end__method____main____Vector__Vector____popBack
         .__method____main____Vector__Vector____popBack:
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
                              push qword [.__field____main____Vector__Vector____data] ; stored index associated with field that is being accessed
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
                                    push qword [.__field____main____Vector__Vector____size] ; stored index associated with field that is being accessed
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
                                    push qword [.__field____main____Vector__Vector____size] ; size
                                 pop rdi ; rhs
                                 pop rbx ; lhs
                                 mov rax, qword [rbx + 8*rdi]
                                 sub rax, 1
                                 mov qword [rbx + 8*rdi], rax
                           push rax ; push result
                     pop rdx ; __offset
                     pop rax ; __pointer
                     push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                  pop rax ; return value (Vector<:int:>)
                  ; Clean up stack and return
                  mov rsp, rbp ; remove local vars + unpopped pushes
                  pop rbp
                  ret
   ;---------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
         .__end__method____main____Vector__Vector____popBack:
         ; End Method Declaration - .__method____main____Vector__Vector____popBack
;---------------------------------------------------------------------------

;---------------------------------------------------------------------------
         ; Method Declaration - Vector<:Vector<:int:>:>::clear() -> void
         jmp .__end__method____main____Vector__Vector____clear
         .__method____main____Vector__Vector____clear:
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
                                 push qword [.__field____main____Vector__Vector____size] ; stored index associated with field that is being accessed
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
                     ; Method Call - Vector<:Vector<:int:>:>::popBack() -> Vector<:int:>
                        ; Make space for 0 arg(s) and object parameter
                        sub rsp, 8
                        ; LHS
                           ; This keyword
                              push qword [rbp - 8] ; __this
                           pop rax ; object parameter
                           mov qword [rsp + 0], rax ; place as first parameter
                        ; RHS
                        ; Arguments
                        call .__method____main____Vector__Vector____popBack
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
         .__end__method____main____Vector__Vector____clear:
         ; End Method Declaration - .__method____main____Vector__Vector____clear
;---------------------------------------------------------------------------

;---------------------------------------------------------------------------
         ; Method Declaration - Vector<:Vector<:int:>:>::get(int) -> Vector<:int:>
         jmp .__end__method____main____Vector__Vector____get__int
         .__method____main____Vector__Vector____get__int:
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
            ; Param: index [rbp + 24] (__main____Vector__Vector__get__index)
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
                              push qword [.__field____main____Vector__Vector____data] ; stored index associated with field that is being accessed
                           pop rdx ; rhs
                           pop rax ; lhs
                           push qword [rax + 8*rdx] ; lhs.rhs
                     ; OFFSET
                        ; Identifier - int index
                           push qword [rbp - -24]
                     pop rdx ; __offset
                     pop rax ; __pointer
                     push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                  pop rax ; return value (Vector<:int:>)
                  ; Clean up stack and return
                  mov rsp, rbp ; remove local vars + unpopped pushes
                  pop rbp
                  ret
   ;---------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
         .__end__method____main____Vector__Vector____get__int:
         ; End Method Declaration - .__method____main____Vector__Vector____get__int
;---------------------------------------------------------------------------

;---------------------------------------------------------------------------
         ; Method Declaration - Vector<:Vector<:int:>:>::set(int, Vector<:int:>) -> void
         jmp .__end__method____main____Vector__Vector____set__int__Vector
         .__method____main____Vector__Vector____set__int__Vector:
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
            ; Param: index [rbp + 24] (__main____Vector__Vector__set__index)
            ; Param: value [rbp + 32] (__main____Vector__Vector__set__value)
         ; Body
   ;---------------------------------------------------------------------
            ; Code Block
               ; Assignment - '='
                  ; RHS
                     ; Identifier - Vector<:int:> value
                        push qword [rbp - -32]
                  ; LHS
                     ; Subscript assignment
                        ; LHS
                           ; Member Accessor
                              ; LHS
                                 ; This keyword
                                    push qword [rbp - 8] ; __this
                              ; RHS
                                 push qword [.__field____main____Vector__Vector____data] ; stored index associated with field that is being accessed
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
         .__end__method____main____Vector__Vector____set__int__Vector:
         ; End Method Declaration - .__method____main____Vector__Vector____set__int__Vector
;---------------------------------------------------------------------------

.__endclass____main____Vector__Vector:
         ; End Class Declaration - __main____Vector__Vector
; ==============================================================================

; ==============================================================================
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
;---------------------------------------------------------------------------
         ; Field - int[] Vector<:int:>::data
         section .data
         .__field____main____Vector__int____data: dq 1
         section .text
;---------------------------------------------------------------------------
;---------------------------------------------------------------------------
         ; Field - int Vector<:int:>::size
         section .data
         .__field____main____Vector__int____size: dq 2
         section .text
;---------------------------------------------------------------------------
;---------------------------------------------------------------------------
         ; Field - int Vector<:int:>::capacity
         section .data
         .__field____main____Vector__int____capacity: dq 3
         section .text
;---------------------------------------------------------------------------
         ; skip over class methods
         jmp .__endclass____main____Vector__int
;---------------------------------------------------------------------------
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
;------------------------------------------------------------------------
         mov rax, qword [rbp - 8] ; __this
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
         .__end__ctor____main____Vector__int____Vector:
         ; End Constructor Declaration - __ctor____main____Vector__int____Vector
;------------------------------------------------------------------------------

;------------------------------------------------------------------------------
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
;---------------------------------------------------------------------------
         mov rax, qword [rbp - 8] ; __this
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
         .__end__ctor____main____Vector__int____Vector__int:
         ; End Constructor Declaration - __ctor____main____Vector__int____Vector__int
;---------------------------------------------------------------------------------

;---------------------------------------------------------------------------------
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
                           mov rax, qword [rbp - 16]  ; __main____Vector__int__pushBack__block__26__if__27__block__28__nData
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
                              mov rax, qword [rbp - 24]  ; __main____Vector__int__pushBack__block__26__if__27__block__28__for__29__i
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
      ;------------------------------------------------------------------
            jmp .__endif__27 ; jump to end of condition chain
            ; End of if
.__endif__27:
;------------------------------------------------------------------------
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
;---------------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
         .__end__method____main____Vector__int____pushBack__int:
         ; End Method Declaration - .__method____main____Vector__int____pushBack__int
;---------------------------------------------------------------------------------

;---------------------------------------------------------------------------------
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
;---------------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
         .__end__method____main____Vector__int____popBack:
         ; End Method Declaration - .__method____main____Vector__int____popBack
;---------------------------------------------------------------------------------

;---------------------------------------------------------------------------------
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
               je .__endwhile__33
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
            jmp .__while__33
            ; End of While
.__endwhile__33:
;------------------------------------------------------------------------
;---------------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
         .__end__method____main____Vector__int____clear:
         ; End Method Declaration - .__method____main____Vector__int____clear
;---------------------------------------------------------------------------------

;---------------------------------------------------------------------------------
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
;---------------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
         .__end__method____main____Vector__int____get__int:
         ; End Method Declaration - .__method____main____Vector__int____get__int
;---------------------------------------------------------------------------------

;---------------------------------------------------------------------------------
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
;---------------------------------------------------------------------------
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
;---------------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
         .__end__method____main____Vector__int____set__int__int:
         ; End Method Declaration - .__method____main____Vector__int____set__int__int
;---------------------------------------------------------------------------------

.__endclass____main____Vector__int:
         ; End Class Declaration - __main____Vector__int
; ====================================================================================

         ; End Class Template - 
; ==========================================================================================

; ==========================================================================================
         ; Function Template - 
         ; Instances:
         ; End Function Template - 
; ==========================================================================================

; ==========================================================================================
         ; Function Template - 
         ; Instances:
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
         je .__endif__37 ; jump to end
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
         jmp .__endif__37 ; jump to end of condition chain
         ; End of if
.__endif__37:
;---------------------------------------------------------------------------------
         ; Assignment - '='
         ; RHS
         ; Int Literal
         mov rax, 0
         push rax
         ; LHS
         ; Variable Declaration - size
         mov rax, qword [rbp - 8]  ; __main__strlen__block__36__size
         pop rdx ; rhs value
         mov qword [rbp - 8], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
;---------------------------------------------------------------------------------
         ; While-Loop
.__while__38:
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
         je .__endwhile__38
         ; Body
         jmp .__while__38
         ; End of While
.__endwhile__38:
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
         mov rax, qword [rbp - 8]  ; __main__strcmp__block__39__asize
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
         mov rax, qword [rbp - 16]  ; __main__strcmp__block__39__bsize
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
         je .__endif__40 ; jump to end
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
         jmp .__endif__40 ; jump to end of condition chain
         ; End of if
.__endif__40:
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
            mov rax, qword [rbp - 24]  ; __main__strcmp__block__39__for__41__i
         pop rdx ; rhs value
         mov qword [rbp - 24], rdx
         push rdx
         ; Loop init result can be discarded
         pop rax
         jmp .__forcond__41
.__for__41:
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
.__forcond__41:
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
         je .__endfor__41
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
               je .__endif__43 ; jump to end
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
            jmp .__endif__43 ; jump to end of condition chain
            ; End of if
.__endif__43:
;------------------------------------------------------------------------
;---------------------------------------------------------------------------
         ; Repeat
jmp .__for__41
         ; End of For
.__endfor__41:
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
         mov rax, qword [rbp - 8]  ; __main__substr__block__45__res
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
            mov rax, qword [rbp - 16]  ; __main__substr__block__45__for__46__i
         pop rdx ; rhs value
         mov qword [rbp - 16], rdx
         push rdx
         ; Loop init result can be discarded
         pop rax
         jmp .__forcond__46
.__for__46:
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
.__forcond__46:
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
         je .__endfor__46
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
jmp .__for__46
         ; End of For
.__endfor__46:
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
         mov rax, qword [rbp - 8]  ; __main__first_index_of__block__48__size
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
            mov rax, qword [rbp - 16]  ; __main__first_index_of__block__48__for__49__i
         pop rdx ; rhs value
         mov qword [rbp - 16], rdx
         push rdx
         ; Loop init result can be discarded
         pop rax
         jmp .__forcond__49
.__for__49:
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
.__forcond__49:
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
         je .__endfor__49
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
               je .__endif__51 ; jump to end
            ; Body
               ; Return
                  ; Identifier - int i
                     push qword [rbp - 16]
                  pop rax ; return value (int)
                  ; Clean up stack and return
                  mov rsp, rbp ; remove local vars + unpopped pushes
                  pop rbp
                  ret
            jmp .__endif__51 ; jump to end of condition chain
            ; End of if
.__endif__51:
;------------------------------------------------------------------------
;---------------------------------------------------------------------------
         ; Repeat
jmp .__for__49
         ; End of For
.__endfor__49:
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
         mov rax, qword [rbp - 8]  ; __main__split__block__52__tokens
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
         mov rax, qword [rbp - 16]  ; __main__split__block__52__size
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
         mov rax, qword [rbp - 24]  ; __main__split__block__52__i
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
         mov rax, qword [rbp - 32]  ; __main__split__block__52__j
         pop rdx ; rhs value
         mov qword [rbp - 32], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
;---------------------------------------------------------------------------------
         ; While-Loop
.__while__53:
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
         je .__endwhile__53
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
               je .__endif__55 ; jump to end
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
                           mov rax, qword [rbp - 40]  ; __main__split__block__52__while__53__block__54__if__55__block__56__count
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
                           mov rax, qword [rbp - 48]  ; __main__split__block__52__while__53__block__54__if__55__block__56__k
                     pop rdx ; rhs value
                     mov qword [rbp - 48], rdx
                     push rdx
                  ; Statement results can be ignored
                  pop rdx
         ;---------------------------------------------------------------
                  ; While-Loop
.__while__57:
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
                        je .__endwhile__57
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
                              je .__else__58 ; jump to else
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
                           jmp .__endif__58 ; jump to end of condition chain
                  ;------------------------------------------------------
                           ; Else-Statement
.__else__58:
                           ; Break out of __while__57
                           jmp .__endwhile__57
                  ;------------------------------------------------------
                           ; End of if
.__endif__58:
               ;---------------------------------------------------------
                     jmp .__while__57
                     ; End of While
.__endwhile__57:
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
                              mov rax, qword [rbp - 56]  ; __main__split__block__52__while__53__block__54__if__55__block__56__for__59__k
                        pop rdx ; rhs value
                        mov qword [rbp - 56], rdx
                        push rdx
                     ; Loop init result can be discarded
                     pop rax
                  jmp .__forcond__59
.__for__59:
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
.__forcond__59:
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
                        je .__endfor__59
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
jmp .__for__59
                     ; End of For
.__endfor__59:
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
            jmp .__endif__55 ; jump to end of condition chain
            ; End of if
.__endif__55:
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
         jmp .__while__53
         ; End of While
.__endwhile__53:
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
         je .__endif__62 ; jump to end
         ; Body
         ; Return
         ; Identifier - int a
            push qword [rbp - -16]
         pop rax ; return value (int)
         ; Clean up stack and return
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
         jmp .__endif__62 ; jump to end of condition chain
         ; End of if
.__endif__62:
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
         je .__endif__64 ; jump to end
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
         jmp .__endif__64 ; jump to end of condition chain
         ; End of if
.__endif__64:
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
         je .__endif__66 ; jump to end
         ; Body
         ; Return
         ; Identifier - int a
            push qword [rbp - -16]
         pop rax ; return value (int)
         ; Clean up stack and return
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
         jmp .__endif__66 ; jump to end of condition chain
         ; End of if
.__endif__66:
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
         je .__endif__68 ; jump to end
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
         jmp .__endif__68 ; jump to end of condition chain
         ; End of if
.__endif__68:
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
         je .__endif__70 ; jump to end
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
         jmp .__endif__70 ; jump to end of condition chain
         ; End of if
.__endif__70:
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
         je .__endif__72 ; jump to end
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
         jmp .__endif__72 ; jump to end of condition chain
         ; End of if
.__endif__72:
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
.__while__73:
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
         je .__endwhile__73
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
         jmp .__while__73
         ; End of While
.__endwhile__73:
;------------------------------------------------------------------------------------------
; ==========================================================================================
         ; Class Declaration - __main____Vec inherits __builtin____main__Object
         ; Class data
         section .data
         ; Dispatch Table - this might need to be a malloc**
         .__dtable____main____Vec:
         ; Dispatch Table Entries
         section .text
;---------------------------------------------------------------------------------------
         ; Field - int Vec::i
         section .data
         .__field____main____Vec____i: dq 1
         section .text
;---------------------------------------------------------------------------------------
;---------------------------------------------------------------------------------------
         ; Field - int Vec::j
         section .data
         .__field____main____Vec____j: dq 2
         section .text
;---------------------------------------------------------------------------------------
;---------------------------------------------------------------------------------------
         ; Field - int Vec::time
         section .data
         .__field____main____Vec____time: dq 3
         section .text
;---------------------------------------------------------------------------------------
         ; skip over class methods
         jmp .__endclass____main____Vec
;---------------------------------------------------------------------------------------
         ; Constructor Declaration - Vec::Vec() -> Vec
         jmp .__end__ctor____main____Vec____Vec
         .__ctor____main____Vec____Vec:
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
         mov qword [rax + 0], .__dtable____main____Vec ; this[0] = &dtable
         ; Parameters
         ; Body
;------------------------------------------------------------------------------------
         ; Code Block
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
            push qword [.__field____main____Vec____i] ; 
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
            push qword [.__field____main____Vec____j] ; 
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
            push qword [.__field____main____Vec____time] ; 
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
         .__end__ctor____main____Vec____Vec:
         ; End Constructor Declaration - __ctor____main____Vec____Vec
;------------------------------------------------------------------------------------------

;------------------------------------------------------------------------------------------
         ; Constructor Declaration - Vec::Vec(int, int) -> Vec
         jmp .__end__ctor____main____Vec____Vec__int__int
         .__ctor____main____Vec____Vec__int__int:
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
         mov qword [rax + 0], .__dtable____main____Vec ; this[0] = &dtable
         ; Parameters
         ; Param: i [rbp + 16]
         ; Param: j [rbp + 24]
         ; Body
;---------------------------------------------------------------------------------------
         ; Code Block
         ; Assignment - '='
         ; RHS
         ; Identifier - int i
         push qword [rbp - -16]
         ; LHS
         ; Member Accessor Assignment
         ; LHS
         ; This keyword
            push qword [rbp - 8] ; __this
         ; RHS
         push qword [.__field____main____Vec____i] ; 
         pop rdi ; rhs
         pop rbx ; lhs
         pop rdx ; rhs value
         mov qword [rbx + 8*rdi], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
         ; RHS
         ; Identifier - int j
         push qword [rbp - -24]
         ; LHS
         ; Member Accessor Assignment
         ; LHS
         ; This keyword
            push qword [rbp - 8] ; __this
         ; RHS
         push qword [.__field____main____Vec____j] ; 
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
         push qword [.__field____main____Vec____time] ; 
         pop rdi ; rhs
         pop rbx ; lhs
         pop rdx ; rhs value
         mov qword [rbx + 8*rdi], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
;---------------------------------------------------------------------------------------
         mov rax, qword [rbp - 8] ; __this
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
         .__end__ctor____main____Vec____Vec__int__int:
         ; End Constructor Declaration - __ctor____main____Vec____Vec__int__int
;---------------------------------------------------------------------------------------------

;---------------------------------------------------------------------------------------------
         ; Constructor Declaration - Vec::Vec(int, int, int) -> Vec
         jmp .__end__ctor____main____Vec____Vec__int__int__int
         .__ctor____main____Vec____Vec__int__int__int:
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
         mov qword [rax + 0], .__dtable____main____Vec ; this[0] = &dtable
         ; Parameters
         ; Param: i [rbp + 16]
         ; Param: j [rbp + 24]
         ; Param: time [rbp + 32]
         ; Body
;------------------------------------------------------------------------------------------
         ; Code Block
         ; Assignment - '='
         ; RHS
         ; Identifier - int i
         push qword [rbp - -16]
         ; LHS
         ; Member Accessor Assignment
         ; LHS
         ; This keyword
         push qword [rbp - 8] ; __this
         ; RHS
         push qword [.__field____main____Vec____i] ; 
         pop rdi ; rhs
         pop rbx ; lhs
         pop rdx ; rhs value
         mov qword [rbx + 8*rdi], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
         ; RHS
         ; Identifier - int j
         push qword [rbp - -24]
         ; LHS
         ; Member Accessor Assignment
         ; LHS
         ; This keyword
         push qword [rbp - 8] ; __this
         ; RHS
         push qword [.__field____main____Vec____j] ; 
         pop rdi ; rhs
         pop rbx ; lhs
         pop rdx ; rhs value
         mov qword [rbx + 8*rdi], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
         ; RHS
         ; Identifier - int time
         push qword [rbp - -32]
         ; LHS
         ; Member Accessor Assignment
         ; LHS
         ; This keyword
         push qword [rbp - 8] ; __this
         ; RHS
         push qword [.__field____main____Vec____time] ; 
         pop rdi ; rhs
         pop rbx ; lhs
         pop rdx ; rhs value
         mov qword [rbx + 8*rdi], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
;------------------------------------------------------------------------------------------
         mov rax, qword [rbp - 8] ; __this
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
         .__end__ctor____main____Vec____Vec__int__int__int:
         ; End Constructor Declaration - __ctor____main____Vec____Vec__int__int__int
;------------------------------------------------------------------------------------------------

.__endclass____main____Vec:
         ; End Class Declaration - __main____Vec
; ===================================================================================================

; ===================================================================================================
         ; Function Declaration - print(Vec) -> void
         ; Skip over function declaration
         jmp .__end____main____print__Vec
.__main____print__Vec:
         ; Function Header:
         ; Setup stack frame
         push rbp
         mov rbp, rsp
         sub rsp, 0
         ; Parameters
         ; Param: p [rbp + 16]
         ; Local Variables - Each variable is currently 64-bit (sorry not sorry)

         ; Body
;---------------------------------------------------------------------------------------------
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
         ; Member Accessor
         ; LHS
         ; Identifier - Vec p
         push qword [rbp - -16]
         ; RHS
         push qword [.__field____main____Vec____i] ; stored index associated with field that is being accessed
         pop rdx ; rhs
         pop rax ; lhs
         push qword [rax + 8*rdx] ; lhs.rhs
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
         ; Member Accessor
         ; LHS
         ; Identifier - Vec p
         push qword [rbp - -16]
         ; RHS
         push qword [.__field____main____Vec____j] ; stored index associated with field that is being accessed
         pop rdx ; rhs
         pop rax ; lhs
         push qword [rax + 8*rdx] ; lhs.rhs
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
         push ')'
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
;---------------------------------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
.__end____main____print__Vec:
         ; End Function Declaration - print(Vec) -> void
; ===================================================================================================

; ===================================================================================================
         ; Function Declaration - println(Vec) -> void
         ; Skip over function declaration
         jmp .__end____main____println__Vec
.__main____println__Vec:
         ; Function Header:
         ; Setup stack frame
         push rbp
         mov rbp, rsp
         sub rsp, 0
         ; Parameters
         ; Param: p [rbp + 16]
         ; Local Variables - Each variable is currently 64-bit (sorry not sorry)

         ; Body
;---------------------------------------------------------------------------------------------
         ; Code Block
         ; Function Call - print(Vec) -> void
         ; Make space for 1 arg(s)
         sub rsp, 8
         ; Arguments
         ; Eval arg0
         ; Identifier - Vec p
         push qword [rbp - -16]
         ; Move arg0's result to reverse order position on stack
         pop rax
         mov qword [rsp + 0], rax
         ; Call print(Vec)
         call .__main____print__Vec
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
;---------------------------------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
.__end____main____println__Vec:
         ; End Function Declaration - println(Vec) -> void
; ===================================================================================================

; ===================================================================================================
         ; Function Declaration - manhattan(int, int, int, int) -> int
         ; Skip over function declaration
         jmp .__end____main____manhattan__int__int__int__int
.__main____manhattan__int__int__int__int:
         ; Function Header:
         ; Setup stack frame
         push rbp
         mov rbp, rsp
         sub rsp, 0
         ; Parameters
         ; Param: ax [rbp + 16]
         ; Param: ay [rbp + 24]
         ; Param: bx [rbp + 32]
         ; Param: by [rbp + 40]
         ; Local Variables - Each variable is currently 64-bit (sorry not sorry)

         ; Body
;---------------------------------------------------------------------------------------------
         ; Code Block
         ; Return
         ; Addition - int, int
         ; LHS
         ; Function Call - abs(int) -> int
         ; Make space for 1 arg(s)
         sub rsp, 8
         ; Arguments
         ; Eval arg0
         ; Subtraction - int, int
            ; LHS
               ; Identifier - int ax
                  push qword [rbp - -16]
            ; RHS
               ; Identifier - int bx
                  push qword [rbp - -32]
            pop rdx ; rhs
            pop rax ; lhs
            sub rax, rdx
            push rax
         ; Move arg0's result to reverse order position on stack
         pop rax
         mov qword [rsp + 0], rax
         ; Call abs(int)
         call .__main____abs__int
         ; Remove args
         add rsp, 8
         ; Push return value
         push rax
         ; RHS
         ; Function Call - abs(int) -> int
         ; Make space for 1 arg(s)
         sub rsp, 8
         ; Arguments
         ; Eval arg0
         ; Subtraction - int, int
            ; LHS
               ; Identifier - int ay
                  push qword [rbp - -24]
            ; RHS
               ; Identifier - int by
                  push qword [rbp - -40]
            pop rdx ; rhs
            pop rax ; lhs
            sub rax, rdx
            push rax
         ; Move arg0's result to reverse order position on stack
         pop rax
         mov qword [rsp + 0], rax
         ; Call abs(int)
         call .__main____abs__int
         ; Remove args
         add rsp, 8
         ; Push return value
         push rax
         pop rdx ; rhs
         pop rax ; lhs
         add rax, rdx
         push rax
         pop rax ; return value (int)
         ; Clean up stack and return
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
;---------------------------------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
.__end____main____manhattan__int__int__int__int:
         ; End Function Declaration - manhattan(int, int, int, int) -> int
; ===================================================================================================

; ===================================================================================================
         ; Class Template - 
         ; Instances:
; =============================================================================================
         ; Class Declaration - __main____Node__Vec inherits __builtin____main__Object
         ; Class data
         section .data
         ; Dispatch Table - this might need to be a malloc**
         .__dtable____main____Node__Vec:
         ; Dispatch Table Entries
         section .text
;------------------------------------------------------------------------------------------
         ; Field - Vec Node<:Vec:>::data
         section .data
         .__field____main____Node__Vec____data: dq 1
         section .text
;------------------------------------------------------------------------------------------
;------------------------------------------------------------------------------------------
         ; Field - Node<:Vec:> Node<:Vec:>::prev
         section .data
         .__field____main____Node__Vec____prev: dq 2
         section .text
;------------------------------------------------------------------------------------------
;------------------------------------------------------------------------------------------
         ; Field - Node<:Vec:> Node<:Vec:>::next
         section .data
         .__field____main____Node__Vec____next: dq 3
         section .text
;------------------------------------------------------------------------------------------
         ; skip over class methods
         jmp .__endclass____main____Node__Vec
;------------------------------------------------------------------------------------------
         ; Constructor Declaration - Node<:Vec:>::Node(Vec, Node<:Vec:>, Node<:Vec:>) -> Node<:Vec:>
         jmp .__end__ctor____main____Node__Vec____Node__Vec__Node__Node
         .__ctor____main____Node__Vec____Node__Vec__Node__Node:
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
         mov qword [rax + 0], .__dtable____main____Node__Vec ; this[0] = &dtable
         ; Parameters
         ; Param: data [rbp + 16]
         ; Param: prev [rbp + 24]
         ; Param: next [rbp + 32]
         ; Body
;---------------------------------------------------------------------------------------
         ; Code Block
         ; Assignment - '='
         ; RHS
         ; Identifier - Vec data
         push qword [rbp - -16]
         ; LHS
         ; Member Accessor Assignment
         ; LHS
         ; This keyword
            push qword [rbp - 8] ; __this
         ; RHS
         push qword [.__field____main____Node__Vec____data] ; 
         pop rdi ; rhs
         pop rbx ; lhs
         pop rdx ; rhs value
         mov qword [rbx + 8*rdi], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
         ; RHS
         ; Identifier - Node<:Vec:> prev
         push qword [rbp - -24]
         ; LHS
         ; Member Accessor Assignment
         ; LHS
         ; This keyword
            push qword [rbp - 8] ; __this
         ; RHS
         push qword [.__field____main____Node__Vec____prev] ; 
         pop rdi ; rhs
         pop rbx ; lhs
         pop rdx ; rhs value
         mov qword [rbx + 8*rdi], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
         ; RHS
         ; Identifier - Node<:Vec:> next
         push qword [rbp - -32]
         ; LHS
         ; Member Accessor Assignment
         ; LHS
         ; This keyword
            push qword [rbp - 8] ; __this
         ; RHS
         push qword [.__field____main____Node__Vec____next] ; 
         pop rdi ; rhs
         pop rbx ; lhs
         pop rdx ; rhs value
         mov qword [rbx + 8*rdi], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
;---------------------------------------------------------------------------------------
         mov rax, qword [rbp - 8] ; __this
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
         .__end__ctor____main____Node__Vec____Node__Vec__Node__Node:
         ; End Constructor Declaration - __ctor____main____Node__Vec____Node__Vec__Node__Node
;---------------------------------------------------------------------------------------------

.__endclass____main____Node__Vec:
         ; End Class Declaration - __main____Node__Vec
; ================================================================================================

         ; End Class Template - 
; ======================================================================================================

; ======================================================================================================
         ; Class Template - 
         ; Instances:
; ================================================================================================
         ; Class Declaration - __main____LinkedList__Vec inherits __builtin____main__Object
         ; Class data
         section .data
         ; Dispatch Table - this might need to be a malloc**
         .__dtable____main____LinkedList__Vec:
         ; Dispatch Table Entries
         dq .__method____main____LinkedList__Vec____pushBack__Vec ; 0
         dq .__method____main____LinkedList__Vec____pushFront__Vec ; 1
         dq .__method____main____LinkedList__Vec____popBack ; 2
         dq .__method____main____LinkedList__Vec____popFront ; 3
         dq .__method____main____LinkedList__Vec____begin ; 4
         dq .__method____main____LinkedList__Vec____end ; 5
         dq .__method____main____LinkedList__Vec____rbegin ; 6
         dq .__method____main____LinkedList__Vec____rend ; 7
         dq .__method____main____LinkedList__Vec____isEmpty ; 8
         section .text
;---------------------------------------------------------------------------------------------
         ; Field - Node<:Vec:> LinkedList<:Vec:>::header
         section .data
         .__field____main____LinkedList__Vec____header: dq 1
         section .text
;---------------------------------------------------------------------------------------------
;---------------------------------------------------------------------------------------------
         ; Field - int LinkedList<:Vec:>::size
         section .data
         .__field____main____LinkedList__Vec____size: dq 2
         section .text
;---------------------------------------------------------------------------------------------
         ; skip over class methods
         jmp .__endclass____main____LinkedList__Vec
;---------------------------------------------------------------------------------------------
         ; Constructor Declaration - LinkedList<:Vec:>::LinkedList() -> LinkedList<:Vec:>
         jmp .__end__ctor____main____LinkedList__Vec____LinkedList
         .__ctor____main____LinkedList__Vec____LinkedList:
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
         mov qword [rax + 0], .__dtable____main____LinkedList__Vec ; this[0] = &dtable
         ; Parameters
         ; Body
;------------------------------------------------------------------------------------------
         ; Code Block
         ; Assignment - '='
         ; RHS
         ; Constructor Call - Node<:Vec:>::Node(Vec, Node<:Vec:>, Node<:Vec:>) -> Node<:Vec:>
         ; Make space for 3 arg(s)
         sub rsp, 24
         ; Arguments
         ; Eval arg0
         ; Function Call - Vec::Vec() -> Vec
            ; Make space for 0 arg(s)
            sub rsp, 0
            ; Arguments
            ; Call Vec::Vec()
            call .__ctor____main____Vec____Vec
            ; Remove args
            add rsp, 0
            ; Push return value
            push rax
         ; Move arg0's result to reverse order position on stack
         pop rax
         mov qword [rsp + 0], rax
         ; Eval arg1
         ; Null Literal
            push 0
         ; Move arg1's result to reverse order position on stack
         pop rax
         mov qword [rsp + 8], rax
         ; Eval arg2
         ; Null Literal
            push 0
         ; Move arg2's result to reverse order position on stack
         pop rax
         mov qword [rsp + 16], rax
         ; Call Node<:Vec:>::Node(Vec, Node<:Vec:>, Node<:Vec:>)
         call .__ctor____main____Node__Vec____Node__Vec__Node__Node
         ; Remove args
         add rsp, 24
         ; Push return value
         push rax
         ; LHS
         ; Member Accessor Assignment
         ; LHS
         ; This keyword
         push qword [rbp - 8] ; __this
         ; RHS
         push qword [.__field____main____LinkedList__Vec____header] ; 
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
         ; This keyword
         push qword [rbp - 8] ; __this
         ; RHS
         push qword [.__field____main____LinkedList__Vec____header] ; stored index associated with field that is being accessed
         pop rdx ; rhs
         pop rax ; lhs
         push qword [rax + 8*rdx] ; lhs.rhs
         ; LHS
         ; Member Accessor Assignment
         ; LHS
         ; Member Accessor
         ; LHS
            ; This keyword
               push qword [rbp - 8] ; __this
         ; RHS
            push qword [.__field____main____LinkedList__Vec____header] ; stored index associated with field that is being accessed
         pop rdx ; rhs
         pop rax ; lhs
         push qword [rax + 8*rdx] ; lhs.rhs
         ; RHS
         push qword [.__field____main____Node__Vec____next] ; 
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
         ; This keyword
         push qword [rbp - 8] ; __this
         ; RHS
         push qword [.__field____main____LinkedList__Vec____header] ; stored index associated with field that is being accessed
         pop rdx ; rhs
         pop rax ; lhs
         push qword [rax + 8*rdx] ; lhs.rhs
         ; LHS
         ; Member Accessor Assignment
         ; LHS
         ; Member Accessor
         ; LHS
            ; This keyword
               push qword [rbp - 8] ; __this
         ; RHS
            push qword [.__field____main____LinkedList__Vec____header] ; stored index associated with field that is being accessed
         pop rdx ; rhs
         pop rax ; lhs
         push qword [rax + 8*rdx] ; lhs.rhs
         ; RHS
         push qword [.__field____main____Node__Vec____prev] ; 
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
         push qword [.__field____main____LinkedList__Vec____size] ; 
         pop rdi ; rhs
         pop rbx ; lhs
         pop rdx ; rhs value
         mov qword [rbx + 8*rdi], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
;------------------------------------------------------------------------------------------
         mov rax, qword [rbp - 8] ; __this
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
         .__end__ctor____main____LinkedList__Vec____LinkedList:
         ; End Constructor Declaration - __ctor____main____LinkedList__Vec____LinkedList
;------------------------------------------------------------------------------------------------

;------------------------------------------------------------------------------------------------
         ; Method Declaration - LinkedList<:Vec:>::pushBack(Vec) -> void
         jmp .__end__method____main____LinkedList__Vec____pushBack__Vec
         .__method____main____LinkedList__Vec____pushBack__Vec:
         ; Function Header:
         ; Setup stack frame
         push rbp
         mov rbp, rsp
         ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
         sub rsp, 32 ; space for local variables (16-byte aligned)
         ; [rbp - 8] - this - Reference to 'this' object instance
         mov rdx, qword [rbp + 16] ; param passed 'this'
         mov qword [rbp - 8], rdx ; save this to a local
         ; [rbp - 16] - Node<:Vec:> tail (<unset-scope-name>)
         ; [rbp - 24] - Node<:Vec:> node (<unset-scope-name>)
         ; Parameters
         ; Param: val [rbp + 24] (__main____LinkedList__Vec__pushBack__val)
         ; Body
;------------------------------------------------------------------------------------------
         ; Code Block
         ; Assignment - '='
         ; RHS
         ; Member Accessor
         ; LHS
         ; Member Accessor
         ; LHS
            ; This keyword
               push qword [rbp - 8] ; __this
         ; RHS
            push qword [.__field____main____LinkedList__Vec____header] ; stored index associated with field that is being accessed
         pop rdx ; rhs
         pop rax ; lhs
         push qword [rax + 8*rdx] ; lhs.rhs
         ; RHS
         push qword [.__field____main____Node__Vec____prev] ; stored index associated with field that is being accessed
         pop rdx ; rhs
         pop rax ; lhs
         push qword [rax + 8*rdx] ; lhs.rhs
         ; LHS
         ; Variable Declaration - tail
         mov rax, qword [rbp - 16]  ; __main____LinkedList__Vec__pushBack__block__83__tail
         pop rdx ; rhs value
         mov qword [rbp - 16], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
         ; RHS
         ; Constructor Call - Node<:Vec:>::Node(Vec, Node<:Vec:>, Node<:Vec:>) -> Node<:Vec:>
         ; Make space for 3 arg(s)
         sub rsp, 24
         ; Arguments
         ; Eval arg0
         ; Identifier - Vec val
            push qword [rbp - -24]
         ; Move arg0's result to reverse order position on stack
         pop rax
         mov qword [rsp + 0], rax
         ; Eval arg1
         ; Identifier - Node<:Vec:> tail
            push qword [rbp - 16]
         ; Move arg1's result to reverse order position on stack
         pop rax
         mov qword [rsp + 8], rax
         ; Eval arg2
         ; Member Accessor
            ; LHS
               ; This keyword
                  push qword [rbp - 8] ; __this
            ; RHS
               push qword [.__field____main____LinkedList__Vec____header] ; stored index associated with field that is being accessed
            pop rdx ; rhs
            pop rax ; lhs
            push qword [rax + 8*rdx] ; lhs.rhs
         ; Move arg2's result to reverse order position on stack
         pop rax
         mov qword [rsp + 16], rax
         ; Call Node<:Vec:>::Node(Vec, Node<:Vec:>, Node<:Vec:>)
         call .__ctor____main____Node__Vec____Node__Vec__Node__Node
         ; Remove args
         add rsp, 24
         ; Push return value
         push rax
         ; LHS
         ; Variable Declaration - node
         mov rax, qword [rbp - 24]  ; __main____LinkedList__Vec__pushBack__block__83__node
         pop rdx ; rhs value
         mov qword [rbp - 24], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
         ; RHS
         ; Identifier - Node<:Vec:> node
         push qword [rbp - 24]
         ; LHS
         ; Member Accessor Assignment
         ; LHS
         ; Identifier - Node<:Vec:> tail
         push qword [rbp - 16]
         ; RHS
         push qword [.__field____main____Node__Vec____next] ; 
         pop rdi ; rhs
         pop rbx ; lhs
         pop rdx ; rhs value
         mov qword [rbx + 8*rdi], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
         ; RHS
         ; Identifier - Node<:Vec:> node
         push qword [rbp - 24]
         ; LHS
         ; Member Accessor Assignment
         ; LHS
         ; Member Accessor
         ; LHS
            ; This keyword
               push qword [rbp - 8] ; __this
         ; RHS
            push qword [.__field____main____LinkedList__Vec____header] ; stored index associated with field that is being accessed
         pop rdx ; rhs
         pop rax ; lhs
         push qword [rax + 8*rdx] ; lhs.rhs
         ; RHS
         push qword [.__field____main____Node__Vec____prev] ; 
         pop rdi ; rhs
         pop rbx ; lhs
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
         push qword [.__field____main____LinkedList__Vec____size] ; stored index associated with field that is being accessed
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
         push qword [.__field____main____LinkedList__Vec____size] ; size
         pop rdi ; rhs
         pop rbx ; lhs
         mov rax, qword [rbx + 8*rdi]
         add rax, 1
         mov qword [rbx + 8*rdi], rax
         push rax ; push result
         ; Statement results can be ignored
         pop rdx
;------------------------------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
         .__end__method____main____LinkedList__Vec____pushBack__Vec:
         ; End Method Declaration - .__method____main____LinkedList__Vec____pushBack__Vec
;------------------------------------------------------------------------------------------------

;------------------------------------------------------------------------------------------------
         ; Method Declaration - LinkedList<:Vec:>::pushFront(Vec) -> void
         jmp .__end__method____main____LinkedList__Vec____pushFront__Vec
         .__method____main____LinkedList__Vec____pushFront__Vec:
         ; Function Header:
         ; Setup stack frame
         push rbp
         mov rbp, rsp
         ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
         sub rsp, 32 ; space for local variables (16-byte aligned)
         ; [rbp - 8] - this - Reference to 'this' object instance
         mov rdx, qword [rbp + 16] ; param passed 'this'
         mov qword [rbp - 8], rdx ; save this to a local
         ; [rbp - 16] - Node<:Vec:> head (<unset-scope-name>)
         ; [rbp - 24] - Node<:Vec:> node (<unset-scope-name>)
         ; Parameters
         ; Param: val [rbp + 24] (__main____LinkedList__Vec__pushFront__val)
         ; Body
;------------------------------------------------------------------------------------------
         ; Code Block
         ; Assignment - '='
         ; RHS
         ; Member Accessor
         ; LHS
         ; Member Accessor
         ; LHS
            ; This keyword
               push qword [rbp - 8] ; __this
         ; RHS
            push qword [.__field____main____LinkedList__Vec____header] ; stored index associated with field that is being accessed
         pop rdx ; rhs
         pop rax ; lhs
         push qword [rax + 8*rdx] ; lhs.rhs
         ; RHS
         push qword [.__field____main____Node__Vec____next] ; stored index associated with field that is being accessed
         pop rdx ; rhs
         pop rax ; lhs
         push qword [rax + 8*rdx] ; lhs.rhs
         ; LHS
         ; Variable Declaration - head
         mov rax, qword [rbp - 16]  ; __main____LinkedList__Vec__pushFront__block__84__head
         pop rdx ; rhs value
         mov qword [rbp - 16], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
         ; RHS
         ; Constructor Call - Node<:Vec:>::Node(Vec, Node<:Vec:>, Node<:Vec:>) -> Node<:Vec:>
         ; Make space for 3 arg(s)
         sub rsp, 24
         ; Arguments
         ; Eval arg0
         ; Identifier - Vec val
            push qword [rbp - -24]
         ; Move arg0's result to reverse order position on stack
         pop rax
         mov qword [rsp + 0], rax
         ; Eval arg1
         ; Member Accessor
            ; LHS
               ; This keyword
                  push qword [rbp - 8] ; __this
            ; RHS
               push qword [.__field____main____LinkedList__Vec____header] ; stored index associated with field that is being accessed
            pop rdx ; rhs
            pop rax ; lhs
            push qword [rax + 8*rdx] ; lhs.rhs
         ; Move arg1's result to reverse order position on stack
         pop rax
         mov qword [rsp + 8], rax
         ; Eval arg2
         ; Identifier - Node<:Vec:> head
            push qword [rbp - 16]
         ; Move arg2's result to reverse order position on stack
         pop rax
         mov qword [rsp + 16], rax
         ; Call Node<:Vec:>::Node(Vec, Node<:Vec:>, Node<:Vec:>)
         call .__ctor____main____Node__Vec____Node__Vec__Node__Node
         ; Remove args
         add rsp, 24
         ; Push return value
         push rax
         ; LHS
         ; Variable Declaration - node
         mov rax, qword [rbp - 24]  ; __main____LinkedList__Vec__pushFront__block__84__node
         pop rdx ; rhs value
         mov qword [rbp - 24], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
         ; RHS
         ; Identifier - Node<:Vec:> node
         push qword [rbp - 24]
         ; LHS
         ; Member Accessor Assignment
         ; LHS
         ; Identifier - Node<:Vec:> head
         push qword [rbp - 16]
         ; RHS
         push qword [.__field____main____Node__Vec____prev] ; 
         pop rdi ; rhs
         pop rbx ; lhs
         pop rdx ; rhs value
         mov qword [rbx + 8*rdi], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
         ; RHS
         ; Identifier - Node<:Vec:> node
         push qword [rbp - 24]
         ; LHS
         ; Member Accessor Assignment
         ; LHS
         ; Member Accessor
         ; LHS
            ; This keyword
               push qword [rbp - 8] ; __this
         ; RHS
            push qword [.__field____main____LinkedList__Vec____header] ; stored index associated with field that is being accessed
         pop rdx ; rhs
         pop rax ; lhs
         push qword [rax + 8*rdx] ; lhs.rhs
         ; RHS
         push qword [.__field____main____Node__Vec____next] ; 
         pop rdi ; rhs
         pop rbx ; lhs
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
         push qword [.__field____main____LinkedList__Vec____size] ; stored index associated with field that is being accessed
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
         push qword [.__field____main____LinkedList__Vec____size] ; size
         pop rdi ; rhs
         pop rbx ; lhs
         mov rax, qword [rbx + 8*rdi]
         add rax, 1
         mov qword [rbx + 8*rdi], rax
         push rax ; push result
         ; Statement results can be ignored
         pop rdx
;------------------------------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
         .__end__method____main____LinkedList__Vec____pushFront__Vec:
         ; End Method Declaration - .__method____main____LinkedList__Vec____pushFront__Vec
;------------------------------------------------------------------------------------------------

;------------------------------------------------------------------------------------------------
         ; Method Declaration - LinkedList<:Vec:>::popBack() -> Vec
         jmp .__end__method____main____LinkedList__Vec____popBack
         .__method____main____LinkedList__Vec____popBack:
         ; Function Header:
         ; Setup stack frame
         push rbp
         mov rbp, rsp
         ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
         sub rsp, 16 ; space for local variables (16-byte aligned)
         ; [rbp - 8] - this - Reference to 'this' object instance
         mov rdx, qword [rbp + 16] ; param passed 'this'
         mov qword [rbp - 8], rdx ; save this to a local
         ; [rbp - 16] - Node<:Vec:> tail (<unset-scope-name>)
         ; Parameters
         ; Body
;------------------------------------------------------------------------------------------
         ; Code Block
;---------------------------------------------------------------------------------------
         ; If-Statement
         ; Condition
         ; Less Than or Equal to
         ; LHS
         ; Member Accessor
         ; LHS
            ; This keyword
               push qword [rbp - 8] ; __this
         ; RHS
            push qword [.__field____main____LinkedList__Vec____size] ; stored index associated with field that is being accessed
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
         setle al
         movzx eax, al
         push rax
         pop rdx ; __cond
         cmp rdx, 0 ; ensure condition is true
         je .__endif__86 ; jump to end
         ; Body
         ; Return
         ; Function Call - Vec::Vec() -> Vec
         ; Make space for 0 arg(s)
         sub rsp, 0
         ; Arguments
         ; Call Vec::Vec()
         call .__ctor____main____Vec____Vec
         ; Remove args
         add rsp, 0
         ; Push return value
         push rax
         pop rax ; return value (Vec)
         ; Clean up stack and return
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
         jmp .__endif__86 ; jump to end of condition chain
         ; End of if
.__endif__86:
;---------------------------------------------------------------------------------------
         ; Assignment - '='
         ; RHS
         ; Member Accessor
         ; LHS
         ; Member Accessor
         ; LHS
            ; This keyword
               push qword [rbp - 8] ; __this
         ; RHS
            push qword [.__field____main____LinkedList__Vec____header] ; stored index associated with field that is being accessed
         pop rdx ; rhs
         pop rax ; lhs
         push qword [rax + 8*rdx] ; lhs.rhs
         ; RHS
         push qword [.__field____main____Node__Vec____prev] ; stored index associated with field that is being accessed
         pop rdx ; rhs
         pop rax ; lhs
         push qword [rax + 8*rdx] ; lhs.rhs
         ; LHS
         ; Variable Declaration - tail
         mov rax, qword [rbp - 16]  ; __main____LinkedList__Vec__popBack__block__85__tail
         pop rdx ; rhs value
         mov qword [rbp - 16], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
         ; RHS
         ; Member Accessor
         ; LHS
         ; This keyword
         push qword [rbp - 8] ; __this
         ; RHS
         push qword [.__field____main____LinkedList__Vec____header] ; stored index associated with field that is being accessed
         pop rdx ; rhs
         pop rax ; lhs
         push qword [rax + 8*rdx] ; lhs.rhs
         ; LHS
         ; Member Accessor Assignment
         ; LHS
         ; Member Accessor
         ; LHS
            ; Identifier - Node<:Vec:> tail
               push qword [rbp - 16]
         ; RHS
            push qword [.__field____main____Node__Vec____prev] ; stored index associated with field that is being accessed
         pop rdx ; rhs
         pop rax ; lhs
         push qword [rax + 8*rdx] ; lhs.rhs
         ; RHS
         push qword [.__field____main____Node__Vec____next] ; 
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
         ; Identifier - Node<:Vec:> tail
         push qword [rbp - 16]
         ; RHS
         push qword [.__field____main____Node__Vec____prev] ; stored index associated with field that is being accessed
         pop rdx ; rhs
         pop rax ; lhs
         push qword [rax + 8*rdx] ; lhs.rhs
         ; LHS
         ; Member Accessor Assignment
         ; LHS
         ; Member Accessor
         ; LHS
            ; This keyword
               push qword [rbp - 8] ; __this
         ; RHS
            push qword [.__field____main____LinkedList__Vec____header] ; stored index associated with field that is being accessed
         pop rdx ; rhs
         pop rax ; lhs
         push qword [rax + 8*rdx] ; lhs.rhs
         ; RHS
         push qword [.__field____main____Node__Vec____prev] ; 
         pop rdi ; rhs
         pop rbx ; lhs
         pop rdx ; rhs value
         mov qword [rbx + 8*rdi], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
         ; Pre-Decrement - int
         ; RHS
         ; Member Accessor
         ; LHS
         ; This keyword
         push qword [rbp - 8] ; __this
         ; RHS
         push qword [.__field____main____LinkedList__Vec____size] ; stored index associated with field that is being accessed
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
         push qword [.__field____main____LinkedList__Vec____size] ; size
         pop rdi ; rhs
         pop rbx ; lhs
         mov rax, qword [rbx + 8*rdi]
         sub rax, 1
         mov qword [rbx + 8*rdi], rax
         push rax ; push result
         ; Statement results can be ignored
         pop rdx
         ; Return
         ; Member Accessor
         ; LHS
         ; Identifier - Node<:Vec:> tail
         push qword [rbp - 16]
         ; RHS
         push qword [.__field____main____Node__Vec____data] ; stored index associated with field that is being accessed
         pop rdx ; rhs
         pop rax ; lhs
         push qword [rax + 8*rdx] ; lhs.rhs
         pop rax ; return value (Vec)
         ; Clean up stack and return
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
;------------------------------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
         .__end__method____main____LinkedList__Vec____popBack:
         ; End Method Declaration - .__method____main____LinkedList__Vec____popBack
;------------------------------------------------------------------------------------------------

;------------------------------------------------------------------------------------------------
         ; Method Declaration - LinkedList<:Vec:>::popFront() -> Vec
         jmp .__end__method____main____LinkedList__Vec____popFront
         .__method____main____LinkedList__Vec____popFront:
         ; Function Header:
         ; Setup stack frame
         push rbp
         mov rbp, rsp
         ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
         sub rsp, 16 ; space for local variables (16-byte aligned)
         ; [rbp - 8] - this - Reference to 'this' object instance
         mov rdx, qword [rbp + 16] ; param passed 'this'
         mov qword [rbp - 8], rdx ; save this to a local
         ; [rbp - 16] - Node<:Vec:> head (<unset-scope-name>)
         ; Parameters
         ; Body
;------------------------------------------------------------------------------------------
         ; Code Block
;---------------------------------------------------------------------------------------
         ; If-Statement
         ; Condition
         ; Less Than or Equal to
         ; LHS
         ; Member Accessor
         ; LHS
            ; This keyword
               push qword [rbp - 8] ; __this
         ; RHS
            push qword [.__field____main____LinkedList__Vec____size] ; stored index associated with field that is being accessed
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
         setle al
         movzx eax, al
         push rax
         pop rdx ; __cond
         cmp rdx, 0 ; ensure condition is true
         je .__endif__88 ; jump to end
         ; Body
         ; Return
         ; Function Call - Vec::Vec() -> Vec
         ; Make space for 0 arg(s)
         sub rsp, 0
         ; Arguments
         ; Call Vec::Vec()
         call .__ctor____main____Vec____Vec
         ; Remove args
         add rsp, 0
         ; Push return value
         push rax
         pop rax ; return value (Vec)
         ; Clean up stack and return
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
         jmp .__endif__88 ; jump to end of condition chain
         ; End of if
.__endif__88:
;---------------------------------------------------------------------------------------
         ; Assignment - '='
         ; RHS
         ; Member Accessor
         ; LHS
         ; Member Accessor
         ; LHS
            ; This keyword
               push qword [rbp - 8] ; __this
         ; RHS
            push qword [.__field____main____LinkedList__Vec____header] ; stored index associated with field that is being accessed
         pop rdx ; rhs
         pop rax ; lhs
         push qword [rax + 8*rdx] ; lhs.rhs
         ; RHS
         push qword [.__field____main____Node__Vec____next] ; stored index associated with field that is being accessed
         pop rdx ; rhs
         pop rax ; lhs
         push qword [rax + 8*rdx] ; lhs.rhs
         ; LHS
         ; Variable Declaration - head
         mov rax, qword [rbp - 16]  ; __main____LinkedList__Vec__popFront__block__87__head
         pop rdx ; rhs value
         mov qword [rbp - 16], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
         ; RHS
         ; Member Accessor
         ; LHS
         ; This keyword
         push qword [rbp - 8] ; __this
         ; RHS
         push qword [.__field____main____LinkedList__Vec____header] ; stored index associated with field that is being accessed
         pop rdx ; rhs
         pop rax ; lhs
         push qword [rax + 8*rdx] ; lhs.rhs
         ; LHS
         ; Member Accessor Assignment
         ; LHS
         ; Member Accessor
         ; LHS
            ; Identifier - Node<:Vec:> head
               push qword [rbp - 16]
         ; RHS
            push qword [.__field____main____Node__Vec____next] ; stored index associated with field that is being accessed
         pop rdx ; rhs
         pop rax ; lhs
         push qword [rax + 8*rdx] ; lhs.rhs
         ; RHS
         push qword [.__field____main____Node__Vec____prev] ; 
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
         ; Identifier - Node<:Vec:> head
         push qword [rbp - 16]
         ; RHS
         push qword [.__field____main____Node__Vec____next] ; stored index associated with field that is being accessed
         pop rdx ; rhs
         pop rax ; lhs
         push qword [rax + 8*rdx] ; lhs.rhs
         ; LHS
         ; Member Accessor Assignment
         ; LHS
         ; Member Accessor
         ; LHS
            ; This keyword
               push qword [rbp - 8] ; __this
         ; RHS
            push qword [.__field____main____LinkedList__Vec____header] ; stored index associated with field that is being accessed
         pop rdx ; rhs
         pop rax ; lhs
         push qword [rax + 8*rdx] ; lhs.rhs
         ; RHS
         push qword [.__field____main____Node__Vec____next] ; 
         pop rdi ; rhs
         pop rbx ; lhs
         pop rdx ; rhs value
         mov qword [rbx + 8*rdi], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
         ; Pre-Decrement - int
         ; RHS
         ; Member Accessor
         ; LHS
         ; This keyword
         push qword [rbp - 8] ; __this
         ; RHS
         push qword [.__field____main____LinkedList__Vec____size] ; stored index associated with field that is being accessed
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
         push qword [.__field____main____LinkedList__Vec____size] ; size
         pop rdi ; rhs
         pop rbx ; lhs
         mov rax, qword [rbx + 8*rdi]
         sub rax, 1
         mov qword [rbx + 8*rdi], rax
         push rax ; push result
         ; Statement results can be ignored
         pop rdx
         ; Return
         ; Member Accessor
         ; LHS
         ; Identifier - Node<:Vec:> head
         push qword [rbp - 16]
         ; RHS
         push qword [.__field____main____Node__Vec____data] ; stored index associated with field that is being accessed
         pop rdx ; rhs
         pop rax ; lhs
         push qword [rax + 8*rdx] ; lhs.rhs
         pop rax ; return value (Vec)
         ; Clean up stack and return
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
;------------------------------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
         .__end__method____main____LinkedList__Vec____popFront:
         ; End Method Declaration - .__method____main____LinkedList__Vec____popFront
;------------------------------------------------------------------------------------------------

;------------------------------------------------------------------------------------------------
         ; Method Declaration - LinkedList<:Vec:>::begin() -> Node<:Vec:>
         jmp .__end__method____main____LinkedList__Vec____begin
         .__method____main____LinkedList__Vec____begin:
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
;------------------------------------------------------------------------------------------
         ; Code Block
         ; Return
         ; Member Accessor
         ; LHS
         ; Member Accessor
         ; LHS
         ; This keyword
            push qword [rbp - 8] ; __this
         ; RHS
         push qword [.__field____main____LinkedList__Vec____header] ; stored index associated with field that is being accessed
         pop rdx ; rhs
         pop rax ; lhs
         push qword [rax + 8*rdx] ; lhs.rhs
         ; RHS
         push qword [.__field____main____Node__Vec____next] ; stored index associated with field that is being accessed
         pop rdx ; rhs
         pop rax ; lhs
         push qword [rax + 8*rdx] ; lhs.rhs
         pop rax ; return value (Node<:Vec:>)
         ; Clean up stack and return
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
;------------------------------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
         .__end__method____main____LinkedList__Vec____begin:
         ; End Method Declaration - .__method____main____LinkedList__Vec____begin
;------------------------------------------------------------------------------------------------

;------------------------------------------------------------------------------------------------
         ; Method Declaration - LinkedList<:Vec:>::end() -> Node<:Vec:>
         jmp .__end__method____main____LinkedList__Vec____end
         .__method____main____LinkedList__Vec____end:
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
;------------------------------------------------------------------------------------------
         ; Code Block
         ; Return
         ; Member Accessor
         ; LHS
         ; This keyword
         push qword [rbp - 8] ; __this
         ; RHS
         push qword [.__field____main____LinkedList__Vec____header] ; stored index associated with field that is being accessed
         pop rdx ; rhs
         pop rax ; lhs
         push qword [rax + 8*rdx] ; lhs.rhs
         pop rax ; return value (Node<:Vec:>)
         ; Clean up stack and return
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
;------------------------------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
         .__end__method____main____LinkedList__Vec____end:
         ; End Method Declaration - .__method____main____LinkedList__Vec____end
;------------------------------------------------------------------------------------------------

;------------------------------------------------------------------------------------------------
         ; Method Declaration - LinkedList<:Vec:>::rbegin() -> Node<:Vec:>
         jmp .__end__method____main____LinkedList__Vec____rbegin
         .__method____main____LinkedList__Vec____rbegin:
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
;------------------------------------------------------------------------------------------
         ; Code Block
         ; Return
         ; Member Accessor
         ; LHS
         ; Member Accessor
         ; LHS
         ; This keyword
            push qword [rbp - 8] ; __this
         ; RHS
         push qword [.__field____main____LinkedList__Vec____header] ; stored index associated with field that is being accessed
         pop rdx ; rhs
         pop rax ; lhs
         push qword [rax + 8*rdx] ; lhs.rhs
         ; RHS
         push qword [.__field____main____Node__Vec____prev] ; stored index associated with field that is being accessed
         pop rdx ; rhs
         pop rax ; lhs
         push qword [rax + 8*rdx] ; lhs.rhs
         pop rax ; return value (Node<:Vec:>)
         ; Clean up stack and return
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
;------------------------------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
         .__end__method____main____LinkedList__Vec____rbegin:
         ; End Method Declaration - .__method____main____LinkedList__Vec____rbegin
;------------------------------------------------------------------------------------------------

;------------------------------------------------------------------------------------------------
         ; Method Declaration - LinkedList<:Vec:>::rend() -> Node<:Vec:>
         jmp .__end__method____main____LinkedList__Vec____rend
         .__method____main____LinkedList__Vec____rend:
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
;------------------------------------------------------------------------------------------
         ; Code Block
         ; Return
         ; Member Accessor
         ; LHS
         ; This keyword
         push qword [rbp - 8] ; __this
         ; RHS
         push qword [.__field____main____LinkedList__Vec____header] ; stored index associated with field that is being accessed
         pop rdx ; rhs
         pop rax ; lhs
         push qword [rax + 8*rdx] ; lhs.rhs
         pop rax ; return value (Node<:Vec:>)
         ; Clean up stack and return
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
;------------------------------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
         .__end__method____main____LinkedList__Vec____rend:
         ; End Method Declaration - .__method____main____LinkedList__Vec____rend
;------------------------------------------------------------------------------------------------

;------------------------------------------------------------------------------------------------
         ; Method Declaration - LinkedList<:Vec:>::isEmpty() -> int
         jmp .__end__method____main____LinkedList__Vec____isEmpty
         .__method____main____LinkedList__Vec____isEmpty:
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
;------------------------------------------------------------------------------------------
         ; Code Block
         ; Return
         ; Equal
         ; LHS
         ; Member Accessor
         ; LHS
         ; This keyword
            push qword [rbp - 8] ; __this
         ; RHS
         push qword [.__field____main____LinkedList__Vec____size] ; stored index associated with field that is being accessed
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
         sete al
         movzx eax, al
         push rax
         pop rax ; return value (int)
         ; Clean up stack and return
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
;------------------------------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
         .__end__method____main____LinkedList__Vec____isEmpty:
         ; End Method Declaration - .__method____main____LinkedList__Vec____isEmpty
;------------------------------------------------------------------------------------------------

.__endclass____main____LinkedList__Vec:
         ; End Class Declaration - __main____LinkedList__Vec
; ===================================================================================================

         ; End Class Template - 
; =========================================================================================================

; =========================================================================================================
         ; Function Template - 
         ; Instances:
         ; End Function Template - 
; =========================================================================================================

; =========================================================================================================
         ; Function Template - 
         ; Instances:
         ; End Function Template - 
; =========================================================================================================

         ; Assignment - '='
         ; RHS
         ; Constructor Call - Vector<:Vector<:int:>:>::Vector() -> Vector<:Vector<:int:>:>
         ; Make space for 0 arg(s)
         sub rsp, 0
         ; Arguments
         ; Call Vector<:Vector<:int:>:>::Vector()
         call .__ctor____main____Vector__Vector____Vector
         ; Remove args
         add rsp, 0
         ; Push return value
         push rax
         ; LHS
         ; Variable Declaration - elevations
         mov rax, qword [rbp - 24]  ; __main__elevations
         pop rdx ; rhs value
         mov qword [rbp - 24], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
         ; RHS
         ; Constructor Call - Vector<:Vector<:int:>:>::Vector() -> Vector<:Vector<:int:>:>
         ; Make space for 0 arg(s)
         sub rsp, 0
         ; Arguments
         ; Call Vector<:Vector<:int:>:>::Vector()
         call .__ctor____main____Vector__Vector____Vector
         ; Remove args
         add rsp, 0
         ; Push return value
         push rax
         ; LHS
         ; Variable Declaration - was_visited
         mov rax, qword [rbp - 32]  ; __main__was_visited
         pop rdx ; rhs value
         mov qword [rbp - 32], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
         ; RHS
         ; String Literal
         ; "abcdefghijklmnopqrstuvwxyzSE"
         mov rax, .str0
         push rax
         ; LHS
         ; Variable Declaration - alphabet
         mov rax, qword [rbp - 40]  ; __main__alphabet
         pop rdx ; rhs value
         mov qword [rbp - 40], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
         ; RHS
         ; Constructor Call - Vec::Vec(int, int) -> Vec
         ; Make space for 2 arg(s)
         sub rsp, 16
         ; Arguments
         ; Eval arg0
         ; Int Literal
         mov rax, 0
         push rax
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
         ; Call Vec::Vec(int, int)
         call .__ctor____main____Vec____Vec__int__int
         ; Remove args
         add rsp, 16
         ; Push return value
         push rax
         ; LHS
         ; Variable Declaration - start_pos
         mov rax, qword [rbp - 48]  ; __main__start_pos
         pop rdx ; rhs value
         mov qword [rbp - 48], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
         ; RHS
         ; Constructor Call - Vec::Vec(int, int) -> Vec
         ; Make space for 2 arg(s)
         sub rsp, 16
         ; Arguments
         ; Eval arg0
         ; Int Literal
         mov rax, 0
         push rax
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
         ; Call Vec::Vec(int, int)
         call .__ctor____main____Vec____Vec__int__int
         ; Remove args
         add rsp, 16
         ; Push return value
         push rax
         ; LHS
         ; Variable Declaration - end_pos
         mov rax, qword [rbp - 56]  ; __main__end_pos
         pop rdx ; rhs value
         mov qword [rbp - 56], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
         ; RHS
         ; Constructor Call - LinkedList<:Vec:>::LinkedList() -> LinkedList<:Vec:>
         ; Make space for 0 arg(s)
         sub rsp, 0
         ; Arguments
         ; Call LinkedList<:Vec:>::LinkedList()
         call .__ctor____main____LinkedList__Vec____LinkedList
         ; Remove args
         add rsp, 0
         ; Push return value
         push rax
         ; LHS
         ; Variable Declaration - starting_positions
         mov rax, qword [rbp - 64]  ; __main__starting_positions
         pop rdx ; rhs value
         mov qword [rbp - 64], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
;---------------------------------------------------------------------------------------------------------
         ; For-Loop
         ; Init
         ; Assignment - '='
         ; RHS
         ; Int Literal
         mov rax, 0
         push rax
         ; LHS
         ; Variable Declaration - l
         mov rax, qword [rbp - 72]  ; __main__for__94__l
         pop rdx ; rhs value
         mov qword [rbp - 72], rdx
         push rdx
         ; Loop init result can be discarded
         pop rax
         jmp .__forcond__94
.__for__94:
         ; Update
         ; Assignment - '+='
         ; RHS
         ; Int Literal
         mov rax, 1
         push rax
         pop rdx ; rhs value
         mov rax, qword [rbp - 72] ; read lhs value
         add rax, rdx      ; add lhs and rhs
         mov qword [rbp - 72], rax ; write back to lhs
         push rax          ; push result for other expressions
         ; Loop update result can be discarded
         pop rax
.__forcond__94:
         ; Condition
         ; Less Than
         ; LHS
         ; Identifier - int l
         push qword [rbp - 72]
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
         je .__endfor__94
         ; Body
;---------------------------------------------------------------------------------------------------
         ; Code Block
         ; Method Call - Vector<:Vector<:int:>:>::pushBack(Vector<:int:>) -> void
         ; Make space for 1 arg(s) and object parameter
         sub rsp, 16
         ; LHS
         ; Identifier - Vector<:Vector<:int:>:> elevations
         push qword [rbp - 24]
         pop rax ; object parameter
         mov qword [rsp + 0], rax ; place as first parameter
         ; RHS
         ; Arguments
         ; Eval arg0
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
         ; Move arg0's result to reverse order position on stack
         pop rax
         mov qword [rsp + 8], rax
         call .__method____main____Vector__Vector____pushBack__Vector
         ; Remove args
         add rsp, 16
         ; Push return value
         push rax
         ; Statement results can be ignored
         pop rdx
         ; Method Call - Vector<:Vector<:int:>:>::pushBack(Vector<:int:>) -> void
         ; Make space for 1 arg(s) and object parameter
         sub rsp, 16
         ; LHS
         ; Identifier - Vector<:Vector<:int:>:> was_visited
         push qword [rbp - 32]
         pop rax ; object parameter
         mov qword [rsp + 0], rax ; place as first parameter
         ; RHS
         ; Arguments
         ; Eval arg0
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
         ; Move arg0's result to reverse order position on stack
         pop rax
         mov qword [rsp + 8], rax
         call .__method____main____Vector__Vector____pushBack__Vector
         ; Remove args
         add rsp, 16
         ; Push return value
         push rax
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
         ; RHS
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
                  ; Identifier - Vector<:char[]:> lines
                     push qword [rbp - 16]
               ; RHS
                  push qword [.__field____main____Vector__char__1____data] ; stored index associated with field that is being accessed
               pop rdx ; rhs
               pop rax ; lhs
               push qword [rax + 8*rdx] ; lhs.rhs
         ; OFFSET
            ; Identifier - int l
               push qword [rbp - 72]
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
         ; LHS
         ; Variable Declaration - size
         mov rax, qword [rbp - 80]  ; __main__for__94__block__95__size
         pop rdx ; rhs value
         mov qword [rbp - 80], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
;------------------------------------------------------------------------------------------------
         ; For-Loop
         ; Init
         ; Assignment - '='
         ; RHS
         ; Int Literal
         mov rax, 0
         push rax
         ; LHS
         ; Variable Declaration - c
         mov rax, qword [rbp - 88]  ; __main__for__94__block__95__for__96__c
         pop rdx ; rhs value
         mov qword [rbp - 88], rdx
         push rdx
         ; Loop init result can be discarded
         pop rax
         jmp .__forcond__96
.__for__96:
         ; Update
         ; Pre-Increment - int
         ; RHS
         ; Identifier - int c
         push qword [rbp - 88]
         pop rdx
         add qword [rbp - 88], 1
         mov rax, qword [rbp - 88]
         push rax ; push result
         ; Loop update result can be discarded
         pop rax
.__forcond__96:
         ; Condition
         ; Less Than
         ; LHS
         ; Identifier - int c
         push qword [rbp - 88]
         ; RHS
         ; Identifier - int size
         push qword [rbp - 80]
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
;------------------------------------------------------------------------------------------
         ; Code Block
         ; Assignment - '='
         ; RHS
         ; Function Call - first_index_of(char[], char) -> int
         ; Make space for 2 arg(s)
         sub rsp, 16
         ; Arguments
         ; Eval arg0
         ; Identifier - char[] alphabet
            push qword [rbp - 40]
         ; Move arg0's result to reverse order position on stack
         pop rax
         mov qword [rsp + 0], rax
         ; Eval arg1
         ; Subscript
            ; LHS
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
                     ; Identifier - int l
                        push qword [rbp - 72]
                  pop rdx ; __offset
                  pop rax ; __pointer
                  push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
            ; OFFSET
               ; Identifier - int c
                  push qword [rbp - 88]
            pop rdx ; __offset
            pop rax ; __pointer
            mov al, byte [rax + rdx] ; pointer + sizeof(data_t) * offset
            movzx rax, al ; zero extend because we need to push 64bit to stack
            push rax ; push char onto stack
         ; Move arg1's result to reverse order position on stack
         pop rax
         mov qword [rsp + 8], rax
         ; Call first_index_of(char[], char)
         call .__main____first_index_of__char__1__char
         ; Remove args
         add rsp, 16
         ; Push return value
         push rax
         ; LHS
         ; Variable Declaration - val
         mov rax, qword [rbp - 96]  ; __main__for__94__block__95__for__96__block__97__val
         pop rdx ; rhs value
         mov qword [rbp - 96], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
;---------------------------------------------------------------------------------------
         ; If-Statement
         ; Condition
         ; Equal
         ; LHS
         ; Identifier - int val
         push qword [rbp - 96]
         ; RHS
         ; Int Literal
         mov rax, 26
         push rax
         pop rdx ; rhs
         pop rax ; lhs
         cmp rax, rdx
         sete al
         movzx eax, al
         push rax
         pop rdx ; __cond
         cmp rdx, 0 ; ensure condition is true
         je .__elif__98x0 ; jump to first elif
         ; Body
;---------------------------------------------------------------------------------
         ; Code Block
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
         ; Identifier - int l
            push qword [rbp - 72]
         ; LHS
         ; Member Accessor Assignment
            ; LHS
               ; Identifier - Vec start_pos
                  push qword [rbp - 48]
            ; RHS
               push qword [.__field____main____Vec____i] ; 
            pop rdi ; rhs
            pop rbx ; lhs
         pop rdx ; rhs value
         mov qword [rbx + 8*rdi], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
         ; RHS
         ; Identifier - int c
            push qword [rbp - 88]
         ; LHS
         ; Member Accessor Assignment
            ; LHS
               ; Identifier - Vec start_pos
                  push qword [rbp - 48]
            ; RHS
               push qword [.__field____main____Vec____j] ; 
            pop rdi ; rhs
            pop rbx ; lhs
         pop rdx ; rhs value
         mov qword [rbx + 8*rdi], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
;---------------------------------------------------------------------------------
         jmp .__endif__98 ; jump to end of condition chain
;------------------------------------------------------------------------------------
         ; Elif-Statement
.__elif__98x0:
         ; Condition
         ; Equal
         ; LHS
         ; Identifier - int val
         push qword [rbp - 96]
         ; RHS
         ; Int Literal
         mov rax, 27
         push rax
         pop rdx ; rhs
         pop rax ; lhs
         cmp rax, rdx
         sete al
         movzx eax, al
         push rax
         pop rdx ; __cond
         cmp rdx, 0 ; ensure condition is true
         je .__endif__98
         ; Body
;---------------------------------------------------------------------------------
         ; Code Block
         ; Assignment - '='
         ; RHS
         ; Int Literal
            mov rax, 25
            push rax
         pop rdx ; rhs value
         mov qword [rbp - 96], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
         ; RHS
         ; Identifier - int l
            push qword [rbp - 72]
         ; LHS
         ; Member Accessor Assignment
            ; LHS
               ; Identifier - Vec end_pos
                  push qword [rbp - 56]
            ; RHS
               push qword [.__field____main____Vec____i] ; 
            pop rdi ; rhs
            pop rbx ; lhs
         pop rdx ; rhs value
         mov qword [rbx + 8*rdi], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
         ; RHS
         ; Identifier - int c
            push qword [rbp - 88]
         ; LHS
         ; Member Accessor Assignment
            ; LHS
               ; Identifier - Vec end_pos
                  push qword [rbp - 56]
            ; RHS
               push qword [.__field____main____Vec____j] ; 
            pop rdi ; rhs
            pop rbx ; lhs
         pop rdx ; rhs value
         mov qword [rbx + 8*rdi], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
;---------------------------------------------------------------------------------
         jmp .__endif__98
;------------------------------------------------------------------------------------
         ; End of if
.__endif__98:
;---------------------------------------------------------------------------------------
;---------------------------------------------------------------------------------------
         ; If-Statement
         ; Condition
         ; Equal
         ; LHS
         ; Identifier - int val
         push qword [rbp - 96]
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
         je .__endif__101 ; jump to end
         ; Body
;---------------------------------------------------------------------------------
         ; Code Block
         ; Method Call - LinkedList<:Vec:>::pushBack(Vec) -> void
         ; Make space for 1 arg(s) and object parameter
         sub rsp, 16
         ; LHS
         ; Identifier - LinkedList<:Vec:> starting_positions
            push qword [rbp - 64]
         pop rax ; object parameter
         mov qword [rsp + 0], rax ; place as first parameter
         ; RHS
         ; Arguments
         ; Eval arg0
            ; Constructor Call - Vec::Vec(int, int) -> Vec
               ; Make space for 2 arg(s)
               sub rsp, 16
               ; Arguments
                  ; Eval arg0
                     ; Identifier - int l
                        push qword [rbp - 72]
                  ; Move arg0's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 0], rax
                  ; Eval arg1
                     ; Identifier - int c
                        push qword [rbp - 88]
                  ; Move arg1's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 8], rax
               ; Call Vec::Vec(int, int)
               call .__ctor____main____Vec____Vec__int__int
               ; Remove args
               add rsp, 16
               ; Push return value
               push rax
         ; Move arg0's result to reverse order position on stack
         pop rax
         mov qword [rsp + 8], rax
         call .__method____main____LinkedList__Vec____pushBack__Vec
         ; Remove args
         add rsp, 16
         ; Push return value
         push rax
         ; Statement results can be ignored
         pop rdx
;---------------------------------------------------------------------------------
         jmp .__endif__101 ; jump to end of condition chain
         ; End of if
.__endif__101:
;---------------------------------------------------------------------------------------
         ; Method Call - Vector<:int:>::pushBack(int) -> void
         ; Make space for 1 arg(s) and object parameter
         sub rsp, 16
         ; LHS
         ; Subscript
         ; LHS
         ; Member Accessor
         ; LHS
            ; Identifier - Vector<:Vector<:int:>:> elevations
               push qword [rbp - 24]
         ; RHS
            push qword [.__field____main____Vector__Vector____data] ; stored index associated with field that is being accessed
         pop rdx ; rhs
         pop rax ; lhs
         push qword [rax + 8*rdx] ; lhs.rhs
         ; OFFSET
         ; Identifier - int l
         push qword [rbp - 72]
         pop rdx ; __offset
         pop rax ; __pointer
         push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
         pop rax ; object parameter
         mov qword [rsp + 0], rax ; place as first parameter
         ; RHS
         ; Arguments
         ; Eval arg0
         ; Identifier - int val
         push qword [rbp - 96]
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
         ; Method Call - Vector<:int:>::pushBack(int) -> void
         ; Make space for 1 arg(s) and object parameter
         sub rsp, 16
         ; LHS
         ; Subscript
         ; LHS
         ; Member Accessor
         ; LHS
            ; Identifier - Vector<:Vector<:int:>:> was_visited
               push qword [rbp - 32]
         ; RHS
            push qword [.__field____main____Vector__Vector____data] ; stored index associated with field that is being accessed
         pop rdx ; rhs
         pop rax ; lhs
         push qword [rax + 8*rdx] ; lhs.rhs
         ; OFFSET
         ; Identifier - int l
         push qword [rbp - 72]
         pop rdx ; __offset
         pop rax ; __pointer
         push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
         pop rax ; object parameter
         mov qword [rsp + 0], rax ; place as first parameter
         ; RHS
         ; Arguments
         ; Eval arg0
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
;------------------------------------------------------------------------------------------
         ; Repeat
jmp .__for__96
         ; End of For
.__endfor__96:
;------------------------------------------------------------------------------------------------
;---------------------------------------------------------------------------------------------------
         ; Repeat
jmp .__for__94
         ; End of For
.__endfor__94:
;---------------------------------------------------------------------------------------------------------
; =========================================================================================================
         ; Function Declaration - bfs(Vector<:Vector<:int:>:>, Vector<:Vector<:int:>:>, Vec, Vec) -> int
         ; Skip over function declaration
         jmp .__end____main____bfs__Vector__tparam0__Vector__Vector__tparam0__Vector__Vec__Vec
.__main____bfs__Vector__tparam0__Vector__Vector__tparam0__Vector__Vec__Vec:
         ; Function Header:
         ; Setup stack frame
         push rbp
         mov rbp, rsp
         sub rsp, 16
         ; Parameters
         ; Param: elevations [rbp + 16]
         ; Param: board [rbp + 24]
         ; Param: start_pos [rbp + 32]
         ; Param: end_pos [rbp + 40]
         ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
         ; [rbp - 8] - LinkedList<:Vec:> frontier (<unset-scope-name>)
         ; [rbp - 16] - Vec pos (<unset-scope-name>)

         ; Body
;---------------------------------------------------------------------------------------------------
         ; Code Block
         ; Assignment - '='
         ; RHS
         ; Constructor Call - LinkedList<:Vec:>::LinkedList() -> LinkedList<:Vec:>
         ; Make space for 0 arg(s)
         sub rsp, 0
         ; Arguments
         ; Call LinkedList<:Vec:>::LinkedList()
         call .__ctor____main____LinkedList__Vec____LinkedList
         ; Remove args
         add rsp, 0
         ; Push return value
         push rax
         ; LHS
         ; Variable Declaration - frontier
         mov rax, qword [rbp - 8]  ; __main__bfs__block__103__frontier
         pop rdx ; rhs value
         mov qword [rbp - 8], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
         ; Method Call - LinkedList<:Vec:>::pushBack(Vec) -> void
         ; Make space for 1 arg(s) and object parameter
         sub rsp, 16
         ; LHS
         ; Identifier - LinkedList<:Vec:> frontier
         push qword [rbp - 8]
         pop rax ; object parameter
         mov qword [rsp + 0], rax ; place as first parameter
         ; RHS
         ; Arguments
         ; Eval arg0
         ; Constructor Call - Vec::Vec(int, int, int) -> Vec
         ; Make space for 3 arg(s)
         sub rsp, 24
         ; Arguments
         ; Eval arg0
         ; Member Accessor
         ; LHS
         ; Identifier - Vec start_pos
            push qword [rbp - -32]
         ; RHS
         push qword [.__field____main____Vec____i] ; stored index associated with field that is being accessed
         pop rdx ; rhs
         pop rax ; lhs
         push qword [rax + 8*rdx] ; lhs.rhs
         ; Move arg0's result to reverse order position on stack
         pop rax
         mov qword [rsp + 0], rax
         ; Eval arg1
         ; Member Accessor
         ; LHS
         ; Identifier - Vec start_pos
            push qword [rbp - -32]
         ; RHS
         push qword [.__field____main____Vec____j] ; stored index associated with field that is being accessed
         pop rdx ; rhs
         pop rax ; lhs
         push qword [rax + 8*rdx] ; lhs.rhs
         ; Move arg1's result to reverse order position on stack
         pop rax
         mov qword [rsp + 8], rax
         ; Eval arg2
         ; Int Literal
         mov rax, 0
         push rax
         ; Move arg2's result to reverse order position on stack
         pop rax
         mov qword [rsp + 16], rax
         ; Call Vec::Vec(int, int, int)
         call .__ctor____main____Vec____Vec__int__int__int
         ; Remove args
         add rsp, 24
         ; Push return value
         push rax
         ; Move arg0's result to reverse order position on stack
         pop rax
         mov qword [rsp + 8], rax
         call .__method____main____LinkedList__Vec____pushBack__Vec
         ; Remove args
         add rsp, 16
         ; Push return value
         push rax
         ; Statement results can be ignored
         pop rdx
;------------------------------------------------------------------------------------------------
         ; While-Loop
.__while__104:
         ; Condition
         ; Negate - int
         ; RHS
         ; Method Call - LinkedList<:Vec:>::isEmpty() -> int
         ; Make space for 0 arg(s) and object parameter
         sub rsp, 8
         ; LHS
         ; Identifier - LinkedList<:Vec:> frontier
         push qword [rbp - 8]
         pop rax ; object parameter
         mov qword [rsp + 0], rax ; place as first parameter
         ; RHS
         ; Arguments
         call .__method____main____LinkedList__Vec____isEmpty
         ; Remove args
         add rsp, 8
         ; Push return value
         push rax
         pop rdx
         cmp rdx, 0
         sete al
         movzx eax, al
         push rax ; push result
         pop rax ; __cond
         cmp rax, 0 ; __cond
         je .__endwhile__104
         ; Body
;------------------------------------------------------------------------------------------
         ; Code Block
         ; Assignment - '='
         ; RHS
         ; Method Call - LinkedList<:Vec:>::popFront() -> Vec
         ; Make space for 0 arg(s) and object parameter
         sub rsp, 8
         ; LHS
         ; Identifier - LinkedList<:Vec:> frontier
         push qword [rbp - 8]
         pop rax ; object parameter
         mov qword [rsp + 0], rax ; place as first parameter
         ; RHS
         ; Arguments
         call .__method____main____LinkedList__Vec____popFront
         ; Remove args
         add rsp, 8
         ; Push return value
         push rax
         ; LHS
         ; Variable Declaration - pos
         mov rax, qword [rbp - 16]  ; __main__bfs__block__103__while__104__block__105__pos
         pop rdx ; rhs value
         mov qword [rbp - 16], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
;---------------------------------------------------------------------------------------
         ; If-Statement
         ; Condition
         ; Not Equal
         ; LHS
         ; Subscript
         ; LHS
            ; Member Accessor
               ; LHS
                  ; Subscript
                     ; LHS
                        ; Member Accessor
                           ; LHS
                              ; Identifier - Vector<:Vector<:int:>:> board
                                 push qword [rbp - -24]
                           ; RHS
                              push qword [.__field____main____Vector__Vector____data] ; stored index associated with field that is being accessed
                           pop rdx ; rhs
                           pop rax ; lhs
                           push qword [rax + 8*rdx] ; lhs.rhs
                     ; OFFSET
                        ; Member Accessor
                           ; LHS
                              ; Identifier - Vec pos
                                 push qword [rbp - 16]
                           ; RHS
                              push qword [.__field____main____Vec____i] ; stored index associated with field that is being accessed
                           pop rdx ; rhs
                           pop rax ; lhs
                           push qword [rax + 8*rdx] ; lhs.rhs
                     pop rdx ; __offset
                     pop rax ; __pointer
                     push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
               ; RHS
                  push qword [.__field____main____Vector__int____data] ; stored index associated with field that is being accessed
               pop rdx ; rhs
               pop rax ; lhs
               push qword [rax + 8*rdx] ; lhs.rhs
         ; OFFSET
            ; Member Accessor
               ; LHS
                  ; Identifier - Vec pos
                     push qword [rbp - 16]
               ; RHS
                  push qword [.__field____main____Vec____j] ; stored index associated with field that is being accessed
               pop rdx ; rhs
               pop rax ; lhs
               push qword [rax + 8*rdx] ; lhs.rhs
         pop rdx ; __offset
         pop rax ; __pointer
         push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
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
         je .__endif__106 ; jump to end
         ; Body
;---------------------------------------------------------------------------------
         ; Code Block
         ; Continue in __while__104
         jmp .__while__104
;---------------------------------------------------------------------------------
         jmp .__endif__106 ; jump to end of condition chain
         ; End of if
.__endif__106:
;---------------------------------------------------------------------------------------
         ; Assignment - '='
         ; RHS
         ; Member Accessor
         ; LHS
         ; Identifier - Vec pos
         push qword [rbp - 16]
         ; RHS
         push qword [.__field____main____Vec____time] ; stored index associated with field that is being accessed
         pop rdx ; rhs
         pop rax ; lhs
         push qword [rax + 8*rdx] ; lhs.rhs
         ; LHS
         ; Subscript assignment
         ; LHS
         ; Member Accessor
         ; LHS
            ; Subscript
               ; LHS
                  ; Member Accessor
                     ; LHS
                        ; Identifier - Vector<:Vector<:int:>:> board
                           push qword [rbp - -24]
                     ; RHS
                        push qword [.__field____main____Vector__Vector____data] ; stored index associated with field that is being accessed
                     pop rdx ; rhs
                     pop rax ; lhs
                     push qword [rax + 8*rdx] ; lhs.rhs
               ; OFFSET
                  ; Member Accessor
                     ; LHS
                        ; Identifier - Vec pos
                           push qword [rbp - 16]
                     ; RHS
                        push qword [.__field____main____Vec____i] ; stored index associated with field that is being accessed
                     pop rdx ; rhs
                     pop rax ; lhs
                     push qword [rax + 8*rdx] ; lhs.rhs
               pop rdx ; __offset
               pop rax ; __pointer
               push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
         ; RHS
            push qword [.__field____main____Vector__int____data] ; stored index associated with field that is being accessed
         pop rdx ; rhs
         pop rax ; lhs
         push qword [rax + 8*rdx] ; lhs.rhs
         ; OFFSET
         ; Member Accessor
         ; LHS
            ; Identifier - Vec pos
               push qword [rbp - 16]
         ; RHS
            push qword [.__field____main____Vec____j] ; stored index associated with field that is being accessed
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
;---------------------------------------------------------------------------------------
         ; If-Statement
         ; Condition
         ; Greater Than or Equal to
         ; LHS
         ; Subtraction - int, int
         ; LHS
            ; Member Accessor
               ; LHS
                  ; Identifier - Vec pos
                     push qword [rbp - 16]
               ; RHS
                  push qword [.__field____main____Vec____i] ; stored index associated with field that is being accessed
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
         pop rdx ; __cond
         cmp rdx, 0 ; ensure condition is true
         je .__endif__108 ; jump to end
         ; Body
;---------------------------------------------------------------------------------
         ; If-Statement
         ; Condition
         ; Less Than or Equal to
         ; LHS
            ; Subtraction - int, int
               ; LHS
                  ; Subscript
                     ; LHS
                        ; Member Accessor
                           ; LHS
                              ; Subscript
                                 ; LHS
                                    ; Member Accessor
                                       ; LHS
                                          ; Identifier - Vector<:Vector<:int:>:> elevations
                                             push qword [rbp - -16]
                                       ; RHS
                                          push qword [.__field____main____Vector__Vector____data] ; stored index associated with field that is being accessed
                                       pop rdx ; rhs
                                       pop rax ; lhs
                                       push qword [rax + 8*rdx] ; lhs.rhs
                                 ; OFFSET
                                    ; Subtraction - int, int
                                       ; LHS
                                          ; Member Accessor
                                             ; LHS
                                                ; Identifier - Vec pos
                                                   push qword [rbp - 16]
                                             ; RHS
                                                push qword [.__field____main____Vec____i] ; stored index associated with field that is being accessed
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
                           ; RHS
                              push qword [.__field____main____Vector__int____data] ; stored index associated with field that is being accessed
                           pop rdx ; rhs
                           pop rax ; lhs
                           push qword [rax + 8*rdx] ; lhs.rhs
                     ; OFFSET
                        ; Member Accessor
                           ; LHS
                              ; Identifier - Vec pos
                                 push qword [rbp - 16]
                           ; RHS
                              push qword [.__field____main____Vec____j] ; stored index associated with field that is being accessed
                           pop rdx ; rhs
                           pop rax ; lhs
                           push qword [rax + 8*rdx] ; lhs.rhs
                     pop rdx ; __offset
                     pop rax ; __pointer
                     push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
               ; RHS
                  ; Subscript
                     ; LHS
                        ; Member Accessor
                           ; LHS
                              ; Subscript
                                 ; LHS
                                    ; Member Accessor
                                       ; LHS
                                          ; Identifier - Vector<:Vector<:int:>:> elevations
                                             push qword [rbp - -16]
                                       ; RHS
                                          push qword [.__field____main____Vector__Vector____data] ; stored index associated with field that is being accessed
                                       pop rdx ; rhs
                                       pop rax ; lhs
                                       push qword [rax + 8*rdx] ; lhs.rhs
                                 ; OFFSET
                                    ; Member Accessor
                                       ; LHS
                                          ; Identifier - Vec pos
                                             push qword [rbp - 16]
                                       ; RHS
                                          push qword [.__field____main____Vec____i] ; stored index associated with field that is being accessed
                                       pop rdx ; rhs
                                       pop rax ; lhs
                                       push qword [rax + 8*rdx] ; lhs.rhs
                                 pop rdx ; __offset
                                 pop rax ; __pointer
                                 push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                           ; RHS
                              push qword [.__field____main____Vector__int____data] ; stored index associated with field that is being accessed
                           pop rdx ; rhs
                           pop rax ; lhs
                           push qword [rax + 8*rdx] ; lhs.rhs
                     ; OFFSET
                        ; Member Accessor
                           ; LHS
                              ; Identifier - Vec pos
                                 push qword [rbp - 16]
                           ; RHS
                              push qword [.__field____main____Vec____j] ; stored index associated with field that is being accessed
                           pop rdx ; rhs
                           pop rax ; lhs
                           push qword [rax + 8*rdx] ; lhs.rhs
                     pop rdx ; __offset
                     pop rax ; __pointer
                     push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
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
         cmp rax, rdx
         setle al
         movzx eax, al
         push rax
         pop rdx ; __cond
         cmp rdx, 0 ; ensure condition is true
         je .__endif__109 ; jump to end
         ; Body
         ; Method Call - LinkedList<:Vec:>::pushBack(Vec) -> void
         ; Make space for 1 arg(s) and object parameter
         sub rsp, 16
         ; LHS
            ; Identifier - LinkedList<:Vec:> frontier
               push qword [rbp - 8]
            pop rax ; object parameter
            mov qword [rsp + 0], rax ; place as first parameter
         ; RHS
         ; Arguments
            ; Eval arg0
               ; Constructor Call - Vec::Vec(int, int, int) -> Vec
                  ; Make space for 3 arg(s)
                  sub rsp, 24
                  ; Arguments
                     ; Eval arg0
                        ; Subtraction - int, int
                           ; LHS
                              ; Member Accessor
                                 ; LHS
                                    ; Identifier - Vec pos
                                       push qword [rbp - 16]
                                 ; RHS
                                    push qword [.__field____main____Vec____i] ; stored index associated with field that is being accessed
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
                     ; Move arg0's result to reverse order position on stack
                     pop rax
                     mov qword [rsp + 0], rax
                     ; Eval arg1
                        ; Member Accessor
                           ; LHS
                              ; Identifier - Vec pos
                                 push qword [rbp - 16]
                           ; RHS
                              push qword [.__field____main____Vec____j] ; stored index associated with field that is being accessed
                           pop rdx ; rhs
                           pop rax ; lhs
                           push qword [rax + 8*rdx] ; lhs.rhs
                     ; Move arg1's result to reverse order position on stack
                     pop rax
                     mov qword [rsp + 8], rax
                     ; Eval arg2
                        ; Addition - int, int
                           ; LHS
                              ; Member Accessor
                                 ; LHS
                                    ; Identifier - Vec pos
                                       push qword [rbp - 16]
                                 ; RHS
                                    push qword [.__field____main____Vec____time] ; stored index associated with field that is being accessed
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
                     ; Move arg2's result to reverse order position on stack
                     pop rax
                     mov qword [rsp + 16], rax
                  ; Call Vec::Vec(int, int, int)
                  call .__ctor____main____Vec____Vec__int__int__int
                  ; Remove args
                  add rsp, 24
                  ; Push return value
                  push rax
            ; Move arg0's result to reverse order position on stack
            pop rax
            mov qword [rsp + 8], rax
         call .__method____main____LinkedList__Vec____pushBack__Vec
         ; Remove args
         add rsp, 16
         ; Push return value
         push rax
         ; Statement results can be ignored
         pop rdx
         jmp .__endif__109 ; jump to end of condition chain
         ; End of if
.__endif__109:
;---------------------------------------------------------------------------------
         jmp .__endif__108 ; jump to end of condition chain
         ; End of if
.__endif__108:
;---------------------------------------------------------------------------------------
;---------------------------------------------------------------------------------------
         ; If-Statement
         ; Condition
         ; Less Than
         ; LHS
         ; Addition - int, int
         ; LHS
            ; Member Accessor
               ; LHS
                  ; Identifier - Vec pos
                     push qword [rbp - 16]
               ; RHS
                  push qword [.__field____main____Vec____j] ; stored index associated with field that is being accessed
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
            ; Subscript
               ; LHS
                  ; Member Accessor
                     ; LHS
                        ; Identifier - Vector<:Vector<:int:>:> elevations
                           push qword [rbp - -16]
                     ; RHS
                        push qword [.__field____main____Vector__Vector____data] ; stored index associated with field that is being accessed
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
         pop rdx ; __cond
         cmp rdx, 0 ; ensure condition is true
         je .__endif__110 ; jump to end
         ; Body
;---------------------------------------------------------------------------------
         ; If-Statement
         ; Condition
         ; Less Than or Equal to
         ; LHS
            ; Subtraction - int, int
               ; LHS
                  ; Subscript
                     ; LHS
                        ; Member Accessor
                           ; LHS
                              ; Subscript
                                 ; LHS
                                    ; Member Accessor
                                       ; LHS
                                          ; Identifier - Vector<:Vector<:int:>:> elevations
                                             push qword [rbp - -16]
                                       ; RHS
                                          push qword [.__field____main____Vector__Vector____data] ; stored index associated with field that is being accessed
                                       pop rdx ; rhs
                                       pop rax ; lhs
                                       push qword [rax + 8*rdx] ; lhs.rhs
                                 ; OFFSET
                                    ; Member Accessor
                                       ; LHS
                                          ; Identifier - Vec pos
                                             push qword [rbp - 16]
                                       ; RHS
                                          push qword [.__field____main____Vec____i] ; stored index associated with field that is being accessed
                                       pop rdx ; rhs
                                       pop rax ; lhs
                                       push qword [rax + 8*rdx] ; lhs.rhs
                                 pop rdx ; __offset
                                 pop rax ; __pointer
                                 push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                           ; RHS
                              push qword [.__field____main____Vector__int____data] ; stored index associated with field that is being accessed
                           pop rdx ; rhs
                           pop rax ; lhs
                           push qword [rax + 8*rdx] ; lhs.rhs
                     ; OFFSET
                        ; Addition - int, int
                           ; LHS
                              ; Member Accessor
                                 ; LHS
                                    ; Identifier - Vec pos
                                       push qword [rbp - 16]
                                 ; RHS
                                    push qword [.__field____main____Vec____j] ; stored index associated with field that is being accessed
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
                     pop rdx ; __offset
                     pop rax ; __pointer
                     push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
               ; RHS
                  ; Subscript
                     ; LHS
                        ; Member Accessor
                           ; LHS
                              ; Subscript
                                 ; LHS
                                    ; Member Accessor
                                       ; LHS
                                          ; Identifier - Vector<:Vector<:int:>:> elevations
                                             push qword [rbp - -16]
                                       ; RHS
                                          push qword [.__field____main____Vector__Vector____data] ; stored index associated with field that is being accessed
                                       pop rdx ; rhs
                                       pop rax ; lhs
                                       push qword [rax + 8*rdx] ; lhs.rhs
                                 ; OFFSET
                                    ; Member Accessor
                                       ; LHS
                                          ; Identifier - Vec pos
                                             push qword [rbp - 16]
                                       ; RHS
                                          push qword [.__field____main____Vec____i] ; stored index associated with field that is being accessed
                                       pop rdx ; rhs
                                       pop rax ; lhs
                                       push qword [rax + 8*rdx] ; lhs.rhs
                                 pop rdx ; __offset
                                 pop rax ; __pointer
                                 push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                           ; RHS
                              push qword [.__field____main____Vector__int____data] ; stored index associated with field that is being accessed
                           pop rdx ; rhs
                           pop rax ; lhs
                           push qword [rax + 8*rdx] ; lhs.rhs
                     ; OFFSET
                        ; Member Accessor
                           ; LHS
                              ; Identifier - Vec pos
                                 push qword [rbp - 16]
                           ; RHS
                              push qword [.__field____main____Vec____j] ; stored index associated with field that is being accessed
                           pop rdx ; rhs
                           pop rax ; lhs
                           push qword [rax + 8*rdx] ; lhs.rhs
                     pop rdx ; __offset
                     pop rax ; __pointer
                     push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
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
         cmp rax, rdx
         setle al
         movzx eax, al
         push rax
         pop rdx ; __cond
         cmp rdx, 0 ; ensure condition is true
         je .__endif__111 ; jump to end
         ; Body
         ; Method Call - LinkedList<:Vec:>::pushBack(Vec) -> void
         ; Make space for 1 arg(s) and object parameter
         sub rsp, 16
         ; LHS
            ; Identifier - LinkedList<:Vec:> frontier
               push qword [rbp - 8]
            pop rax ; object parameter
            mov qword [rsp + 0], rax ; place as first parameter
         ; RHS
         ; Arguments
            ; Eval arg0
               ; Constructor Call - Vec::Vec(int, int, int) -> Vec
                  ; Make space for 3 arg(s)
                  sub rsp, 24
                  ; Arguments
                     ; Eval arg0
                        ; Member Accessor
                           ; LHS
                              ; Identifier - Vec pos
                                 push qword [rbp - 16]
                           ; RHS
                              push qword [.__field____main____Vec____i] ; stored index associated with field that is being accessed
                           pop rdx ; rhs
                           pop rax ; lhs
                           push qword [rax + 8*rdx] ; lhs.rhs
                     ; Move arg0's result to reverse order position on stack
                     pop rax
                     mov qword [rsp + 0], rax
                     ; Eval arg1
                        ; Addition - int, int
                           ; LHS
                              ; Member Accessor
                                 ; LHS
                                    ; Identifier - Vec pos
                                       push qword [rbp - 16]
                                 ; RHS
                                    push qword [.__field____main____Vec____j] ; stored index associated with field that is being accessed
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
                     ; Move arg1's result to reverse order position on stack
                     pop rax
                     mov qword [rsp + 8], rax
                     ; Eval arg2
                        ; Addition - int, int
                           ; LHS
                              ; Member Accessor
                                 ; LHS
                                    ; Identifier - Vec pos
                                       push qword [rbp - 16]
                                 ; RHS
                                    push qword [.__field____main____Vec____time] ; stored index associated with field that is being accessed
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
                     ; Move arg2's result to reverse order position on stack
                     pop rax
                     mov qword [rsp + 16], rax
                  ; Call Vec::Vec(int, int, int)
                  call .__ctor____main____Vec____Vec__int__int__int
                  ; Remove args
                  add rsp, 24
                  ; Push return value
                  push rax
            ; Move arg0's result to reverse order position on stack
            pop rax
            mov qword [rsp + 8], rax
         call .__method____main____LinkedList__Vec____pushBack__Vec
         ; Remove args
         add rsp, 16
         ; Push return value
         push rax
         ; Statement results can be ignored
         pop rdx
         jmp .__endif__111 ; jump to end of condition chain
         ; End of if
.__endif__111:
;---------------------------------------------------------------------------------
         jmp .__endif__110 ; jump to end of condition chain
         ; End of if
.__endif__110:
;---------------------------------------------------------------------------------------
;---------------------------------------------------------------------------------------
         ; If-Statement
         ; Condition
         ; Less Than
         ; LHS
         ; Addition - int, int
         ; LHS
            ; Member Accessor
               ; LHS
                  ; Identifier - Vec pos
                     push qword [rbp - 16]
               ; RHS
                  push qword [.__field____main____Vec____i] ; stored index associated with field that is being accessed
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
            ; Identifier - Vector<:Vector<:int:>:> elevations
               push qword [rbp - -16]
         ; RHS
            push qword [.__field____main____Vector__Vector____size] ; stored index associated with field that is being accessed
         pop rdx ; rhs
         pop rax ; lhs
         push qword [rax + 8*rdx] ; lhs.rhs
         pop rdx ; rhs
         pop rax ; lhs
         cmp rax, rdx
         setl al
         movzx eax, al
         push rax
         pop rdx ; __cond
         cmp rdx, 0 ; ensure condition is true
         je .__endif__112 ; jump to end
         ; Body
;---------------------------------------------------------------------------------
         ; If-Statement
         ; Condition
         ; Less Than or Equal to
         ; LHS
            ; Subtraction - int, int
               ; LHS
                  ; Subscript
                     ; LHS
                        ; Member Accessor
                           ; LHS
                              ; Subscript
                                 ; LHS
                                    ; Member Accessor
                                       ; LHS
                                          ; Identifier - Vector<:Vector<:int:>:> elevations
                                             push qword [rbp - -16]
                                       ; RHS
                                          push qword [.__field____main____Vector__Vector____data] ; stored index associated with field that is being accessed
                                       pop rdx ; rhs
                                       pop rax ; lhs
                                       push qword [rax + 8*rdx] ; lhs.rhs
                                 ; OFFSET
                                    ; Addition - int, int
                                       ; LHS
                                          ; Member Accessor
                                             ; LHS
                                                ; Identifier - Vec pos
                                                   push qword [rbp - 16]
                                             ; RHS
                                                push qword [.__field____main____Vec____i] ; stored index associated with field that is being accessed
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
                                 pop rdx ; __offset
                                 pop rax ; __pointer
                                 push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                           ; RHS
                              push qword [.__field____main____Vector__int____data] ; stored index associated with field that is being accessed
                           pop rdx ; rhs
                           pop rax ; lhs
                           push qword [rax + 8*rdx] ; lhs.rhs
                     ; OFFSET
                        ; Member Accessor
                           ; LHS
                              ; Identifier - Vec pos
                                 push qword [rbp - 16]
                           ; RHS
                              push qword [.__field____main____Vec____j] ; stored index associated with field that is being accessed
                           pop rdx ; rhs
                           pop rax ; lhs
                           push qword [rax + 8*rdx] ; lhs.rhs
                     pop rdx ; __offset
                     pop rax ; __pointer
                     push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
               ; RHS
                  ; Subscript
                     ; LHS
                        ; Member Accessor
                           ; LHS
                              ; Subscript
                                 ; LHS
                                    ; Member Accessor
                                       ; LHS
                                          ; Identifier - Vector<:Vector<:int:>:> elevations
                                             push qword [rbp - -16]
                                       ; RHS
                                          push qword [.__field____main____Vector__Vector____data] ; stored index associated with field that is being accessed
                                       pop rdx ; rhs
                                       pop rax ; lhs
                                       push qword [rax + 8*rdx] ; lhs.rhs
                                 ; OFFSET
                                    ; Member Accessor
                                       ; LHS
                                          ; Identifier - Vec pos
                                             push qword [rbp - 16]
                                       ; RHS
                                          push qword [.__field____main____Vec____i] ; stored index associated with field that is being accessed
                                       pop rdx ; rhs
                                       pop rax ; lhs
                                       push qword [rax + 8*rdx] ; lhs.rhs
                                 pop rdx ; __offset
                                 pop rax ; __pointer
                                 push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                           ; RHS
                              push qword [.__field____main____Vector__int____data] ; stored index associated with field that is being accessed
                           pop rdx ; rhs
                           pop rax ; lhs
                           push qword [rax + 8*rdx] ; lhs.rhs
                     ; OFFSET
                        ; Member Accessor
                           ; LHS
                              ; Identifier - Vec pos
                                 push qword [rbp - 16]
                           ; RHS
                              push qword [.__field____main____Vec____j] ; stored index associated with field that is being accessed
                           pop rdx ; rhs
                           pop rax ; lhs
                           push qword [rax + 8*rdx] ; lhs.rhs
                     pop rdx ; __offset
                     pop rax ; __pointer
                     push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
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
         cmp rax, rdx
         setle al
         movzx eax, al
         push rax
         pop rdx ; __cond
         cmp rdx, 0 ; ensure condition is true
         je .__endif__113 ; jump to end
         ; Body
         ; Method Call - LinkedList<:Vec:>::pushBack(Vec) -> void
         ; Make space for 1 arg(s) and object parameter
         sub rsp, 16
         ; LHS
            ; Identifier - LinkedList<:Vec:> frontier
               push qword [rbp - 8]
            pop rax ; object parameter
            mov qword [rsp + 0], rax ; place as first parameter
         ; RHS
         ; Arguments
            ; Eval arg0
               ; Constructor Call - Vec::Vec(int, int, int) -> Vec
                  ; Make space for 3 arg(s)
                  sub rsp, 24
                  ; Arguments
                     ; Eval arg0
                        ; Addition - int, int
                           ; LHS
                              ; Member Accessor
                                 ; LHS
                                    ; Identifier - Vec pos
                                       push qword [rbp - 16]
                                 ; RHS
                                    push qword [.__field____main____Vec____i] ; stored index associated with field that is being accessed
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
                     ; Move arg0's result to reverse order position on stack
                     pop rax
                     mov qword [rsp + 0], rax
                     ; Eval arg1
                        ; Member Accessor
                           ; LHS
                              ; Identifier - Vec pos
                                 push qword [rbp - 16]
                           ; RHS
                              push qword [.__field____main____Vec____j] ; stored index associated with field that is being accessed
                           pop rdx ; rhs
                           pop rax ; lhs
                           push qword [rax + 8*rdx] ; lhs.rhs
                     ; Move arg1's result to reverse order position on stack
                     pop rax
                     mov qword [rsp + 8], rax
                     ; Eval arg2
                        ; Addition - int, int
                           ; LHS
                              ; Member Accessor
                                 ; LHS
                                    ; Identifier - Vec pos
                                       push qword [rbp - 16]
                                 ; RHS
                                    push qword [.__field____main____Vec____time] ; stored index associated with field that is being accessed
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
                     ; Move arg2's result to reverse order position on stack
                     pop rax
                     mov qword [rsp + 16], rax
                  ; Call Vec::Vec(int, int, int)
                  call .__ctor____main____Vec____Vec__int__int__int
                  ; Remove args
                  add rsp, 24
                  ; Push return value
                  push rax
            ; Move arg0's result to reverse order position on stack
            pop rax
            mov qword [rsp + 8], rax
         call .__method____main____LinkedList__Vec____pushBack__Vec
         ; Remove args
         add rsp, 16
         ; Push return value
         push rax
         ; Statement results can be ignored
         pop rdx
         jmp .__endif__113 ; jump to end of condition chain
         ; End of if
.__endif__113:
;---------------------------------------------------------------------------------
         jmp .__endif__112 ; jump to end of condition chain
         ; End of if
.__endif__112:
;---------------------------------------------------------------------------------------
;---------------------------------------------------------------------------------------
         ; If-Statement
         ; Condition
         ; Greater Than or Equal to
         ; LHS
         ; Subtraction - int, int
         ; LHS
            ; Member Accessor
               ; LHS
                  ; Identifier - Vec pos
                     push qword [rbp - 16]
               ; RHS
                  push qword [.__field____main____Vec____j] ; stored index associated with field that is being accessed
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
         pop rdx ; __cond
         cmp rdx, 0 ; ensure condition is true
         je .__endif__114 ; jump to end
         ; Body
;---------------------------------------------------------------------------------
         ; If-Statement
         ; Condition
         ; Less Than or Equal to
         ; LHS
            ; Subtraction - int, int
               ; LHS
                  ; Subscript
                     ; LHS
                        ; Member Accessor
                           ; LHS
                              ; Subscript
                                 ; LHS
                                    ; Member Accessor
                                       ; LHS
                                          ; Identifier - Vector<:Vector<:int:>:> elevations
                                             push qword [rbp - -16]
                                       ; RHS
                                          push qword [.__field____main____Vector__Vector____data] ; stored index associated with field that is being accessed
                                       pop rdx ; rhs
                                       pop rax ; lhs
                                       push qword [rax + 8*rdx] ; lhs.rhs
                                 ; OFFSET
                                    ; Member Accessor
                                       ; LHS
                                          ; Identifier - Vec pos
                                             push qword [rbp - 16]
                                       ; RHS
                                          push qword [.__field____main____Vec____i] ; stored index associated with field that is being accessed
                                       pop rdx ; rhs
                                       pop rax ; lhs
                                       push qword [rax + 8*rdx] ; lhs.rhs
                                 pop rdx ; __offset
                                 pop rax ; __pointer
                                 push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                           ; RHS
                              push qword [.__field____main____Vector__int____data] ; stored index associated with field that is being accessed
                           pop rdx ; rhs
                           pop rax ; lhs
                           push qword [rax + 8*rdx] ; lhs.rhs
                     ; OFFSET
                        ; Subtraction - int, int
                           ; LHS
                              ; Member Accessor
                                 ; LHS
                                    ; Identifier - Vec pos
                                       push qword [rbp - 16]
                                 ; RHS
                                    push qword [.__field____main____Vec____j] ; stored index associated with field that is being accessed
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
               ; RHS
                  ; Subscript
                     ; LHS
                        ; Member Accessor
                           ; LHS
                              ; Subscript
                                 ; LHS
                                    ; Member Accessor
                                       ; LHS
                                          ; Identifier - Vector<:Vector<:int:>:> elevations
                                             push qword [rbp - -16]
                                       ; RHS
                                          push qword [.__field____main____Vector__Vector____data] ; stored index associated with field that is being accessed
                                       pop rdx ; rhs
                                       pop rax ; lhs
                                       push qword [rax + 8*rdx] ; lhs.rhs
                                 ; OFFSET
                                    ; Member Accessor
                                       ; LHS
                                          ; Identifier - Vec pos
                                             push qword [rbp - 16]
                                       ; RHS
                                          push qword [.__field____main____Vec____i] ; stored index associated with field that is being accessed
                                       pop rdx ; rhs
                                       pop rax ; lhs
                                       push qword [rax + 8*rdx] ; lhs.rhs
                                 pop rdx ; __offset
                                 pop rax ; __pointer
                                 push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                           ; RHS
                              push qword [.__field____main____Vector__int____data] ; stored index associated with field that is being accessed
                           pop rdx ; rhs
                           pop rax ; lhs
                           push qword [rax + 8*rdx] ; lhs.rhs
                     ; OFFSET
                        ; Member Accessor
                           ; LHS
                              ; Identifier - Vec pos
                                 push qword [rbp - 16]
                           ; RHS
                              push qword [.__field____main____Vec____j] ; stored index associated with field that is being accessed
                           pop rdx ; rhs
                           pop rax ; lhs
                           push qword [rax + 8*rdx] ; lhs.rhs
                     pop rdx ; __offset
                     pop rax ; __pointer
                     push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
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
         cmp rax, rdx
         setle al
         movzx eax, al
         push rax
         pop rdx ; __cond
         cmp rdx, 0 ; ensure condition is true
         je .__endif__115 ; jump to end
         ; Body
         ; Method Call - LinkedList<:Vec:>::pushBack(Vec) -> void
         ; Make space for 1 arg(s) and object parameter
         sub rsp, 16
         ; LHS
            ; Identifier - LinkedList<:Vec:> frontier
               push qword [rbp - 8]
            pop rax ; object parameter
            mov qword [rsp + 0], rax ; place as first parameter
         ; RHS
         ; Arguments
            ; Eval arg0
               ; Constructor Call - Vec::Vec(int, int, int) -> Vec
                  ; Make space for 3 arg(s)
                  sub rsp, 24
                  ; Arguments
                     ; Eval arg0
                        ; Member Accessor
                           ; LHS
                              ; Identifier - Vec pos
                                 push qword [rbp - 16]
                           ; RHS
                              push qword [.__field____main____Vec____i] ; stored index associated with field that is being accessed
                           pop rdx ; rhs
                           pop rax ; lhs
                           push qword [rax + 8*rdx] ; lhs.rhs
                     ; Move arg0's result to reverse order position on stack
                     pop rax
                     mov qword [rsp + 0], rax
                     ; Eval arg1
                        ; Subtraction - int, int
                           ; LHS
                              ; Member Accessor
                                 ; LHS
                                    ; Identifier - Vec pos
                                       push qword [rbp - 16]
                                 ; RHS
                                    push qword [.__field____main____Vec____j] ; stored index associated with field that is being accessed
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
                     ; Move arg1's result to reverse order position on stack
                     pop rax
                     mov qword [rsp + 8], rax
                     ; Eval arg2
                        ; Addition - int, int
                           ; LHS
                              ; Member Accessor
                                 ; LHS
                                    ; Identifier - Vec pos
                                       push qword [rbp - 16]
                                 ; RHS
                                    push qword [.__field____main____Vec____time] ; stored index associated with field that is being accessed
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
                     ; Move arg2's result to reverse order position on stack
                     pop rax
                     mov qword [rsp + 16], rax
                  ; Call Vec::Vec(int, int, int)
                  call .__ctor____main____Vec____Vec__int__int__int
                  ; Remove args
                  add rsp, 24
                  ; Push return value
                  push rax
            ; Move arg0's result to reverse order position on stack
            pop rax
            mov qword [rsp + 8], rax
         call .__method____main____LinkedList__Vec____pushBack__Vec
         ; Remove args
         add rsp, 16
         ; Push return value
         push rax
         ; Statement results can be ignored
         pop rdx
         jmp .__endif__115 ; jump to end of condition chain
         ; End of if
.__endif__115:
;---------------------------------------------------------------------------------
         jmp .__endif__114 ; jump to end of condition chain
         ; End of if
.__endif__114:
;---------------------------------------------------------------------------------------
         ; Free Operator
         ; RHS
         ; Identifier - Vec pos
         push qword [rbp - 16]
         ; Free pointer
         pop rdi   ; pointer
         call free ; free the pointer
         push rax  ; undefined return value
         ; Statement results can be ignored
         pop rdx
;------------------------------------------------------------------------------------------
         jmp .__while__104
         ; End of While
.__endwhile__104:
;------------------------------------------------------------------------------------------------
         ; Return
         ; Subscript
         ; LHS
         ; Member Accessor
         ; LHS
         ; Subscript
         ; LHS
         ; Member Accessor
         ; LHS
            ; Identifier - Vector<:Vector<:int:>:> board
               push qword [rbp - -24]
         ; RHS
            push qword [.__field____main____Vector__Vector____data] ; stored index associated with field that is being accessed
         pop rdx ; rhs
         pop rax ; lhs
         push qword [rax + 8*rdx] ; lhs.rhs
         ; OFFSET
         ; Member Accessor
         ; LHS
            ; Identifier - Vec end_pos
               push qword [rbp - -40]
         ; RHS
            push qword [.__field____main____Vec____i] ; stored index associated with field that is being accessed
         pop rdx ; rhs
         pop rax ; lhs
         push qword [rax + 8*rdx] ; lhs.rhs
         pop rdx ; __offset
         pop rax ; __pointer
         push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
         ; RHS
         push qword [.__field____main____Vector__int____data] ; stored index associated with field that is being accessed
         pop rdx ; rhs
         pop rax ; lhs
         push qword [rax + 8*rdx] ; lhs.rhs
         ; OFFSET
         ; Member Accessor
         ; LHS
         ; Identifier - Vec end_pos
         push qword [rbp - -40]
         ; RHS
         push qword [.__field____main____Vec____j] ; stored index associated with field that is being accessed
         pop rdx ; rhs
         pop rax ; lhs
         push qword [rax + 8*rdx] ; lhs.rhs
         pop rdx ; __offset
         pop rax ; __pointer
         push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
         pop rax ; return value (int)
         ; Clean up stack and return
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
;---------------------------------------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
.__end____main____bfs__Vector__tparam0__Vector__Vector__tparam0__Vector__Vec__Vec:
         ; End Function Declaration - bfs(Vector<:Vector<:int:>:>, Vector<:Vector<:int:>:>, Vec, Vec) -> int
; =========================================================================================================

         ; Assignment - '='
         ; RHS
         ; Multiplication - int, int
         ; LHS
         ; Member Accessor
         ; LHS
         ; Identifier - Vector<:Vector<:int:>:> elevations
         push qword [rbp - 24]
         ; RHS
         push qword [.__field____main____Vector__Vector____size] ; stored index associated with field that is being accessed
         pop rdx ; rhs
         pop rax ; lhs
         push qword [rax + 8*rdx] ; lhs.rhs
         ; RHS
         ; Member Accessor
         ; LHS
         ; Subscript
         ; LHS
         ; Member Accessor
         ; LHS
         ; Identifier - Vector<:Vector<:int:>:> elevations
         push qword [rbp - 24]
         ; RHS
         push qword [.__field____main____Vector__Vector____data] ; stored index associated with field that is being accessed
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
         ; RHS
         push qword [.__field____main____Vector__int____size] ; stored index associated with field that is being accessed
         pop rdx ; rhs
         pop rax ; lhs
         push qword [rax + 8*rdx] ; lhs.rhs
         pop rdx
         pop rax
         imul rax, rdx
         push rax
         ; LHS
         ; Variable Declaration - min_moves
         mov rax, qword [rbp - 104]  ; __main__min_moves
         pop rdx ; rhs value
         mov qword [rbp - 104], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
;---------------------------------------------------------------------------------------------------------
         ; While-Loop
.__while__116:
         ; Condition
         ; Negate - int
         ; RHS
         ; Method Call - LinkedList<:Vec:>::isEmpty() -> int
         ; Make space for 0 arg(s) and object parameter
         sub rsp, 8
         ; LHS
         ; Identifier - LinkedList<:Vec:> starting_positions
         push qword [rbp - 64]
         pop rax ; object parameter
         mov qword [rsp + 0], rax ; place as first parameter
         ; RHS
         ; Arguments
         call .__method____main____LinkedList__Vec____isEmpty
         ; Remove args
         add rsp, 8
         ; Push return value
         push rax
         pop rdx
         cmp rdx, 0
         sete al
         movzx eax, al
         push rax ; push result
         pop rax ; __cond
         cmp rax, 0 ; __cond
         je .__endwhile__116
         ; Body
;---------------------------------------------------------------------------------------------------
         ; Code Block
         ; Assignment - '='
         ; RHS
         ; Method Call - LinkedList<:Vec:>::popFront() -> Vec
         ; Make space for 0 arg(s) and object parameter
         sub rsp, 8
         ; LHS
         ; Identifier - LinkedList<:Vec:> starting_positions
         push qword [rbp - 64]
         pop rax ; object parameter
         mov qword [rsp + 0], rax ; place as first parameter
         ; RHS
         ; Arguments
         call .__method____main____LinkedList__Vec____popFront
         ; Remove args
         add rsp, 8
         ; Push return value
         push rax
         ; LHS
         ; Variable Declaration - starting_pos
         mov rax, qword [rbp - 112]  ; __main__while__116__block__117__starting_pos
         pop rdx ; rhs value
         mov qword [rbp - 112], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
;------------------------------------------------------------------------------------------------
         ; If-Statement
         ; Condition
         ; Greater Than or Equal to
         ; LHS
         ; Function Call - manhattan(int, int, int, int) -> int
         ; Make space for 4 arg(s)
         sub rsp, 32
         ; Arguments
         ; Eval arg0
         ; Member Accessor
         ; LHS
            ; Identifier - Vec starting_pos
               push qword [rbp - 112]
         ; RHS
            push qword [.__field____main____Vec____i] ; stored index associated with field that is being accessed
         pop rdx ; rhs
         pop rax ; lhs
         push qword [rax + 8*rdx] ; lhs.rhs
         ; Move arg0's result to reverse order position on stack
         pop rax
         mov qword [rsp + 0], rax
         ; Eval arg1
         ; Member Accessor
         ; LHS
            ; Identifier - Vec starting_pos
               push qword [rbp - 112]
         ; RHS
            push qword [.__field____main____Vec____j] ; stored index associated with field that is being accessed
         pop rdx ; rhs
         pop rax ; lhs
         push qword [rax + 8*rdx] ; lhs.rhs
         ; Move arg1's result to reverse order position on stack
         pop rax
         mov qword [rsp + 8], rax
         ; Eval arg2
         ; Member Accessor
         ; LHS
            ; Identifier - Vec end_pos
               push qword [rbp - 56]
         ; RHS
            push qword [.__field____main____Vec____i] ; stored index associated with field that is being accessed
         pop rdx ; rhs
         pop rax ; lhs
         push qword [rax + 8*rdx] ; lhs.rhs
         ; Move arg2's result to reverse order position on stack
         pop rax
         mov qword [rsp + 16], rax
         ; Eval arg3
         ; Member Accessor
         ; LHS
            ; Identifier - Vec end_pos
               push qword [rbp - 56]
         ; RHS
            push qword [.__field____main____Vec____j] ; stored index associated with field that is being accessed
         pop rdx ; rhs
         pop rax ; lhs
         push qword [rax + 8*rdx] ; lhs.rhs
         ; Move arg3's result to reverse order position on stack
         pop rax
         mov qword [rsp + 24], rax
         ; Call manhattan(int, int, int, int)
         call .__main____manhattan__int__int__int__int
         ; Remove args
         add rsp, 32
         ; Push return value
         push rax
         ; RHS
         ; Identifier - int min_moves
         push qword [rbp - 104]
         pop rdx ; rhs
         pop rax ; lhs
         cmp rax, rdx
         setge al
         movzx eax, al
         push rax
         pop rdx ; __cond
         cmp rdx, 0 ; ensure condition is true
         je .__endif__118 ; jump to end
         ; Body
;------------------------------------------------------------------------------------------
         ; Code Block
         ; Free Operator
         ; RHS
         ; Identifier - Vec starting_pos
         push qword [rbp - 112]
         ; Free pointer
         pop rdi   ; pointer
         call free ; free the pointer
         push rax  ; undefined return value
         ; Statement results can be ignored
         pop rdx
         ; Continue in __while__116
         jmp .__while__116
;------------------------------------------------------------------------------------------
         jmp .__endif__118 ; jump to end of condition chain
         ; End of if
.__endif__118:
;------------------------------------------------------------------------------------------------
;------------------------------------------------------------------------------------------------
         ; For-Loop
         ; Init
         ; Assignment - '='
         ; RHS
         ; Int Literal
         mov rax, 0
         push rax
         ; LHS
         ; Variable Declaration - i
         mov rax, qword [rbp - 120]  ; __main__while__116__block__117__for__120__i
         pop rdx ; rhs value
         mov qword [rbp - 120], rdx
         push rdx
         ; Loop init result can be discarded
         pop rax
         jmp .__forcond__120
.__for__120:
         ; Update
         ; Pre-Increment - int
         ; RHS
         ; Identifier - int i
         push qword [rbp - 120]
         pop rdx
         add qword [rbp - 120], 1
         mov rax, qword [rbp - 120]
         push rax ; push result
         ; Loop update result can be discarded
         pop rax
.__forcond__120:
         ; Condition
         ; Less Than
         ; LHS
         ; Identifier - int i
         push qword [rbp - 120]
         ; RHS
         ; Member Accessor
         ; LHS
         ; Identifier - Vector<:Vector<:int:>:> was_visited
         push qword [rbp - 32]
         ; RHS
         push qword [.__field____main____Vector__Vector____size] ; stored index associated with field that is being accessed
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
         je .__endfor__120
         ; Body
;------------------------------------------------------------------------------------------
         ; Code Block
;---------------------------------------------------------------------------------------
         ; For-Loop
         ; Init
         ; Assignment - '='
         ; RHS
         ; Int Literal
         mov rax, 0
         push rax
         ; LHS
         ; Variable Declaration - j
         mov rax, qword [rbp - 128]  ; __main__while__116__block__117__for__120__block__121__for__122__j
         pop rdx ; rhs value
         mov qword [rbp - 128], rdx
         push rdx
         ; Loop init result can be discarded
         pop rax
         jmp .__forcond__122
.__for__122:
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
.__forcond__122:
         ; Condition
         ; Less Than
         ; LHS
         ; Identifier - int j
         push qword [rbp - 128]
         ; RHS
         ; Member Accessor
         ; LHS
            ; Subscript
               ; LHS
                  ; Member Accessor
                     ; LHS
                        ; Identifier - Vector<:Vector<:int:>:> was_visited
                           push qword [rbp - 32]
                     ; RHS
                        push qword [.__field____main____Vector__Vector____data] ; stored index associated with field that is being accessed
                     pop rdx ; rhs
                     pop rax ; lhs
                     push qword [rax + 8*rdx] ; lhs.rhs
               ; OFFSET
                  ; Identifier - int i
                     push qword [rbp - 120]
               pop rdx ; __offset
               pop rax ; __pointer
               push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
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
         je .__endfor__122
         ; Body
;---------------------------------------------------------------------------------
         ; Code Block
         ; Assignment - '='
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
         ; LHS
         ; Subscript assignment
            ; LHS
               ; Member Accessor
                  ; LHS
                     ; Subscript
                        ; LHS
                           ; Member Accessor
                              ; LHS
                                 ; Identifier - Vector<:Vector<:int:>:> was_visited
                                    push qword [rbp - 32]
                              ; RHS
                                 push qword [.__field____main____Vector__Vector____data] ; stored index associated with field that is being accessed
                              pop rdx ; rhs
                              pop rax ; lhs
                              push qword [rax + 8*rdx] ; lhs.rhs
                        ; OFFSET
                           ; Identifier - int i
                              push qword [rbp - 120]
                        pop rdx ; __offset
                        pop rax ; __pointer
                        push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                  ; RHS
                     push qword [.__field____main____Vector__int____data] ; stored index associated with field that is being accessed
                  pop rdx ; rhs
                  pop rax ; lhs
                  push qword [rax + 8*rdx] ; lhs.rhs
            ; OFFSET
               ; Identifier - int j
                  push qword [rbp - 128]
            pop rdi ; __offset
            pop rbx ; __pointer
         pop rdx ; rhs value
         mov qword [rbx + 8*rdi], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
;---------------------------------------------------------------------------------
         ; Repeat
jmp .__for__122
         ; End of For
.__endfor__122:
;---------------------------------------------------------------------------------------
;------------------------------------------------------------------------------------------
         ; Repeat
jmp .__for__120
         ; End of For
.__endfor__120:
;------------------------------------------------------------------------------------------------
         ; Assignment - '='
         ; RHS
         ; Function Call - bfs(Vector<:Vector<:int:>:>, Vector<:Vector<:int:>:>, Vec, Vec) -> int
         ; Make space for 4 arg(s)
         sub rsp, 32
         ; Arguments
         ; Eval arg0
         ; Identifier - Vector<:Vector<:int:>:> elevations
         push qword [rbp - 24]
         ; Move arg0's result to reverse order position on stack
         pop rax
         mov qword [rsp + 0], rax
         ; Eval arg1
         ; Identifier - Vector<:Vector<:int:>:> was_visited
         push qword [rbp - 32]
         ; Move arg1's result to reverse order position on stack
         pop rax
         mov qword [rsp + 8], rax
         ; Eval arg2
         ; Identifier - Vec starting_pos
         push qword [rbp - 112]
         ; Move arg2's result to reverse order position on stack
         pop rax
         mov qword [rsp + 16], rax
         ; Eval arg3
         ; Identifier - Vec end_pos
         push qword [rbp - 56]
         ; Move arg3's result to reverse order position on stack
         pop rax
         mov qword [rsp + 24], rax
         ; Call bfs(Vector<:Vector<:int:>:>, Vector<:Vector<:int:>:>, Vec, Vec)
         call .__main____bfs__Vector__tparam0__Vector__Vector__tparam0__Vector__Vec__Vec
         ; Remove args
         add rsp, 32
         ; Push return value
         push rax
         ; LHS
         ; Variable Declaration - res
         mov rax, qword [rbp - 136]  ; __main__while__116__block__117__res
         pop rdx ; rhs value
         mov qword [rbp - 136], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
;------------------------------------------------------------------------------------------------
         ; If-Statement
         ; Condition
         ; Equal
         ; LHS
         ; Identifier - int res
         push qword [rbp - 136]
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
         sete al
         movzx eax, al
         push rax
         pop rdx ; __cond
         cmp rdx, 0 ; ensure condition is true
         je .__endif__124 ; jump to end
         ; Body
;------------------------------------------------------------------------------------------
         ; Code Block
         ; Free Operator
         ; RHS
         ; Identifier - Vec starting_pos
         push qword [rbp - 112]
         ; Free pointer
         pop rdi   ; pointer
         call free ; free the pointer
         push rax  ; undefined return value
         ; Statement results can be ignored
         pop rdx
         ; Continue in __while__116
         jmp .__while__116
;------------------------------------------------------------------------------------------
         jmp .__endif__124 ; jump to end of condition chain
         ; End of if
.__endif__124:
;------------------------------------------------------------------------------------------------
         ; Assignment - '='
         ; RHS
         ; Function Call - min(int, int) -> int
         ; Make space for 2 arg(s)
         sub rsp, 16
         ; Arguments
         ; Eval arg0
         ; Identifier - int res
         push qword [rbp - 136]
         ; Move arg0's result to reverse order position on stack
         pop rax
         mov qword [rsp + 0], rax
         ; Eval arg1
         ; Identifier - int min_moves
         push qword [rbp - 104]
         ; Move arg1's result to reverse order position on stack
         pop rax
         mov qword [rsp + 8], rax
         ; Call min(int, int)
         call .__main____min__int__int
         ; Remove args
         add rsp, 16
         ; Push return value
         push rax
         pop rdx ; rhs value
         mov qword [rbp - 104], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
         ; Free Operator
         ; RHS
         ; Identifier - Vec starting_pos
         push qword [rbp - 112]
         ; Free pointer
         pop rdi   ; pointer
         call free ; free the pointer
         push rax  ; undefined return value
         ; Statement results can be ignored
         pop rdx
;---------------------------------------------------------------------------------------------------
         jmp .__while__116
         ; End of While
.__endwhile__116:
;---------------------------------------------------------------------------------------------------------
         ; Function Call - println(int) -> void
         ; Make space for 1 arg(s)
         sub rsp, 8
         ; Arguments
         ; Eval arg0
         ; Identifier - int min_moves
         push qword [rbp - 104]
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
; =========================================================================================================
; ### END OF CODE #########################################################################################
; =========================================================================================================

         push 0
         call __builtin__exit__int
; =========================================================================================================
; ### DATA SECTION ########################################################################################
; =========================================================================================================

         section .data
.str0: db 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'S', 'E', 0
.float0: dq 0.0
.floatNegOne: dq -1.0
.floatZero: dq 0.0
.floatOne: dq 1.0
