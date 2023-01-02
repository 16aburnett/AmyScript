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
         ; [rbp - 24] - File root (<unset-scope-name>)
         ; [rbp - 32] - File workingdir (<unset-scope-name>)
         ; [rbp - 40] - Vector<:File:> all_files (<unset-scope-name>)
         ; [rbp - 48] - int i (<unset-scope-name>)
         ; [rbp - 56] - Vector<:char[]:> tokens (<unset-scope-name>)
         ; [rbp - 64] - int j (<unset-scope-name>)
         ; [rbp - 72] - Vector<:char[]:> tokens (<unset-scope-name>)
         ; [rbp - 80] - File dir (<unset-scope-name>)
         ; [rbp - 88] - int size (<unset-scope-name>)
         ; [rbp - 96] - File f (<unset-scope-name>)
         ; [rbp - 104] - int total_space (<unset-scope-name>)
         ; [rbp - 112] - int unused_space_needed (<unset-scope-name>)
         ; [rbp - 120] - int effective_space (<unset-scope-name>)
         ; [rbp - 128] - int min_space_to_remove (<unset-scope-name>)
         ; [rbp - 136] - int smallest (<unset-scope-name>)
         ; [rbp - 144] - int i (<unset-scope-name>)

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
         ; Class Declaration - __main____Vector__File inherits __builtin____main__Object
            ; Class data
            section .data
               ; Dispatch Table - this might need to be a malloc**
               .__dtable____main____Vector__File:
               ; Dispatch Table Entries
               dq .__method____main____Vector__File____pushBack__File ; 0
               dq .__method____main____Vector__File____popBack ; 1
               dq .__method____main____Vector__File____clear ; 2
               dq .__method____main____Vector__File____get__int ; 3
               dq .__method____main____Vector__File____set__int__File ; 4
            section .text
   ;---------------------------------------------------------------------
            ; Field - File[] Vector<:File:>::data
            section .data
            .__field____main____Vector__File____data: dq 1
            section .text
   ;---------------------------------------------------------------------
   ;---------------------------------------------------------------------
            ; Field - int Vector<:File:>::size
            section .data
            .__field____main____Vector__File____size: dq 2
            section .text
   ;---------------------------------------------------------------------
   ;---------------------------------------------------------------------
            ; Field - int Vector<:File:>::capacity
            section .data
            .__field____main____Vector__File____capacity: dq 3
            section .text
   ;---------------------------------------------------------------------
         ; skip over class methods
         jmp .__endclass____main____Vector__File
   ;---------------------------------------------------------------------
            ; Constructor Declaration - Vector<:File:>::Vector() -> Vector<:File:>
            jmp .__end__ctor____main____Vector__File____Vector
            .__ctor____main____Vector__File____Vector:
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
                  mov qword [rax + 0], .__dtable____main____Vector__File ; this[0] = &dtable
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
                              push qword [.__field____main____Vector__File____capacity] ; 
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
                              push qword [.__field____main____Vector__File____size] ; 
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
                                 push qword [.__field____main____Vector__File____capacity] ; stored index associated with field that is being accessed
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
                              push qword [.__field____main____Vector__File____data] ; 
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
         .__end__ctor____main____Vector__File____Vector:
         ; End Constructor Declaration - __ctor____main____Vector__File____Vector
;------------------------------------------------------------------------

;------------------------------------------------------------------------
         ; Constructor Declaration - Vector<:File:>::Vector(int) -> Vector<:File:>
         jmp .__end__ctor____main____Vector__File____Vector__int
         .__ctor____main____Vector__File____Vector__int:
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
               mov qword [rax + 0], .__dtable____main____Vector__File ; this[0] = &dtable
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
                           push qword [.__field____main____Vector__File____capacity] ; 
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
                           push qword [.__field____main____Vector__File____size] ; 
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
                              push qword [.__field____main____Vector__File____capacity] ; stored index associated with field that is being accessed
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
                           push qword [.__field____main____Vector__File____data] ; 
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
         .__end__ctor____main____Vector__File____Vector__int:
         ; End Constructor Declaration - __ctor____main____Vector__File____Vector__int
;---------------------------------------------------------------------------

;---------------------------------------------------------------------------
         ; Method Declaration - Vector<:File:>::pushBack(File) -> void
         jmp .__end__method____main____Vector__File____pushBack__File
         .__method____main____Vector__File____pushBack__File:
         ; Function Header:
         ; Setup stack frame
            push rbp
            mov rbp, rsp
            ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
               sub rsp, 32 ; space for local variables (16-byte aligned)
               ; [rbp - 8] - this - Reference to 'this' object instance
               mov rdx, qword [rbp + 16] ; param passed 'this'
               mov qword [rbp - 8], rdx ; save this to a local
               ; [rbp - 16] - File[] nData (<unset-scope-name>)
               ; [rbp - 24] - int i (<unset-scope-name>)
         ; Parameters
            ; Param: val [rbp + 24] (__main____Vector__File__pushBack__val)
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
                                       push qword [.__field____main____Vector__File____size] ; stored index associated with field that is being accessed
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
                                 push qword [.__field____main____Vector__File____capacity] ; stored index associated with field that is being accessed
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
                                          push qword [.__field____main____Vector__File____capacity] ; stored index associated with field that is being accessed
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
                                    push qword [.__field____main____Vector__File____capacity] ; 
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
                                       push qword [.__field____main____Vector__File____capacity] ; stored index associated with field that is being accessed
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
                                 mov rax, qword [rbp - 16]  ; __main____Vector__File__pushBack__block__14__if__15__block__16__nData
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
                                    mov rax, qword [rbp - 24]  ; __main____Vector__File__pushBack__block__14__if__15__block__16__for__17__i
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
                                          push qword [.__field____main____Vector__File____size] ; stored index associated with field that is being accessed
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
                                                   push qword [.__field____main____Vector__File____data] ; stored index associated with field that is being accessed
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
                                             ; Identifier - File[] nData
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
                                    push qword [.__field____main____Vector__File____data] ; stored index associated with field that is being accessed
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
                              ; Identifier - File[] nData
                                 push qword [rbp - 16]
                           ; LHS
                              ; Member Accessor Assignment
                                 ; LHS
                                    ; This keyword
                                       push qword [rbp - 8] ; __this
                                 ; RHS
                                    push qword [.__field____main____Vector__File____data] ; 
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
                     ; Identifier - File val
                        push qword [rbp - -24]
                  ; LHS
                     ; Subscript assignment
                        ; LHS
                           ; Member Accessor
                              ; LHS
                                 ; This keyword
                                    push qword [rbp - 8] ; __this
                              ; RHS
                                 push qword [.__field____main____Vector__File____data] ; stored index associated with field that is being accessed
                              pop rdx ; rhs
                              pop rax ; lhs
                              push qword [rax + 8*rdx] ; lhs.rhs
                        ; OFFSET
                           ; Member Accessor
                              ; LHS
                                 ; This keyword
                                    push qword [rbp - 8] ; __this
                              ; RHS
                                 push qword [.__field____main____Vector__File____size] ; stored index associated with field that is being accessed
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
                           push qword [.__field____main____Vector__File____size] ; stored index associated with field that is being accessed
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
                           push qword [.__field____main____Vector__File____size] ; size
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
         .__end__method____main____Vector__File____pushBack__File:
         ; End Method Declaration - .__method____main____Vector__File____pushBack__File
;---------------------------------------------------------------------------

;---------------------------------------------------------------------------
         ; Method Declaration - Vector<:File:>::popBack() -> File
         jmp .__end__method____main____Vector__File____popBack
         .__method____main____Vector__File____popBack:
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
                              push qword [.__field____main____Vector__File____data] ; stored index associated with field that is being accessed
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
                                    push qword [.__field____main____Vector__File____size] ; stored index associated with field that is being accessed
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
                                    push qword [.__field____main____Vector__File____size] ; size
                                 pop rdi ; rhs
                                 pop rbx ; lhs
                                 mov rax, qword [rbx + 8*rdi]
                                 sub rax, 1
                                 mov qword [rbx + 8*rdi], rax
                           push rax ; push result
                     pop rdx ; __offset
                     pop rax ; __pointer
                     push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                  pop rax ; return value (File)
                  ; Clean up stack and return
                  mov rsp, rbp ; remove local vars + unpopped pushes
                  pop rbp
                  ret
   ;---------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
         .__end__method____main____Vector__File____popBack:
         ; End Method Declaration - .__method____main____Vector__File____popBack
;---------------------------------------------------------------------------

;---------------------------------------------------------------------------
         ; Method Declaration - Vector<:File:>::clear() -> void
         jmp .__end__method____main____Vector__File____clear
         .__method____main____Vector__File____clear:
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
                                 push qword [.__field____main____Vector__File____size] ; stored index associated with field that is being accessed
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
                     ; Method Call - Vector<:File:>::popBack() -> File
                        ; Make space for 0 arg(s) and object parameter
                        sub rsp, 8
                        ; LHS
                           ; This keyword
                              push qword [rbp - 8] ; __this
                           pop rax ; object parameter
                           mov qword [rsp + 0], rax ; place as first parameter
                        ; RHS
                        ; Arguments
                        call .__method____main____Vector__File____popBack
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
         .__end__method____main____Vector__File____clear:
         ; End Method Declaration - .__method____main____Vector__File____clear
;---------------------------------------------------------------------------

;---------------------------------------------------------------------------
         ; Method Declaration - Vector<:File:>::get(int) -> File
         jmp .__end__method____main____Vector__File____get__int
         .__method____main____Vector__File____get__int:
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
            ; Param: index [rbp + 24] (__main____Vector__File__get__index)
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
                              push qword [.__field____main____Vector__File____data] ; stored index associated with field that is being accessed
                           pop rdx ; rhs
                           pop rax ; lhs
                           push qword [rax + 8*rdx] ; lhs.rhs
                     ; OFFSET
                        ; Identifier - int index
                           push qword [rbp - -24]
                     pop rdx ; __offset
                     pop rax ; __pointer
                     push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                  pop rax ; return value (File)
                  ; Clean up stack and return
                  mov rsp, rbp ; remove local vars + unpopped pushes
                  pop rbp
                  ret
   ;---------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
         .__end__method____main____Vector__File____get__int:
         ; End Method Declaration - .__method____main____Vector__File____get__int
;---------------------------------------------------------------------------

;---------------------------------------------------------------------------
         ; Method Declaration - Vector<:File:>::set(int, File) -> void
         jmp .__end__method____main____Vector__File____set__int__File
         .__method____main____Vector__File____set__int__File:
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
            ; Param: index [rbp + 24] (__main____Vector__File__set__index)
            ; Param: value [rbp + 32] (__main____Vector__File__set__value)
         ; Body
   ;---------------------------------------------------------------------
            ; Code Block
               ; Assignment - '='
                  ; RHS
                     ; Identifier - File value
                        push qword [rbp - -32]
                  ; LHS
                     ; Subscript assignment
                        ; LHS
                           ; Member Accessor
                              ; LHS
                                 ; This keyword
                                    push qword [rbp - 8] ; __this
                              ; RHS
                                 push qword [.__field____main____Vector__File____data] ; stored index associated with field that is being accessed
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
         .__end__method____main____Vector__File____set__int__File:
         ; End Method Declaration - .__method____main____Vector__File____set__int__File
;---------------------------------------------------------------------------

.__endclass____main____Vector__File:
         ; End Class Declaration - __main____Vector__File
; ==============================================================================

         ; End Class Template - 
; ====================================================================================

; ====================================================================================
         ; Function Template - 
         ; Instances:
         ; End Function Template - 
; ====================================================================================

; ====================================================================================
         ; Function Template - 
         ; Instances:
         ; End Function Template - 
; ====================================================================================

; ====================================================================================
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
;------------------------------------------------------------------------------
         ; Code Block
;---------------------------------------------------------------------------
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
            je .__endif__25 ; jump to end
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
         jmp .__endif__25 ; jump to end of condition chain
         ; End of if
.__endif__25:
;---------------------------------------------------------------------------
         ; Assignment - '='
         ; RHS
            ; Int Literal
               mov rax, 0
               push rax
         ; LHS
            ; Variable Declaration - size
               mov rax, qword [rbp - 8]  ; __main__strlen__block__24__size
         pop rdx ; rhs value
         mov qword [rbp - 8], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
;---------------------------------------------------------------------------
         ; While-Loop
.__while__26:
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
            je .__endwhile__26
         ; Body
         jmp .__while__26
         ; End of While
.__endwhile__26:
;---------------------------------------------------------------------------
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
;------------------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
.__end____main____strlen__char__1:
         ; End Function Declaration - strlen(char[]) -> int
; ====================================================================================

; ====================================================================================
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
;------------------------------------------------------------------------------
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
               mov rax, qword [rbp - 8]  ; __main__strcmp__block__27__asize
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
               mov rax, qword [rbp - 16]  ; __main__strcmp__block__27__bsize
         pop rdx ; rhs value
         mov qword [rbp - 16], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
;---------------------------------------------------------------------------
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
            je .__endif__28 ; jump to end
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
         jmp .__endif__28 ; jump to end of condition chain
         ; End of if
.__endif__28:
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
               ; Variable Declaration - i
                  mov rax, qword [rbp - 24]  ; __main__strcmp__block__27__for__29__i
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
            je .__endfor__29
         ; Body
   ;---------------------------------------------------------------------
            ; Code Block
      ;------------------------------------------------------------------
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
                     je .__endif__31 ; jump to end
                  ; Body
            ;------------------------------------------------------------
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
            ;------------------------------------------------------------
                  jmp .__endif__31 ; jump to end of condition chain
                  ; End of if
.__endif__31:
      ;------------------------------------------------------------------
   ;---------------------------------------------------------------------
         ; Repeat
jmp .__for__29
         ; End of For
.__endfor__29:
;---------------------------------------------------------------------------
         ; Return
         ; Int Literal
            mov rax, 1
            push rax
         pop rax ; return value (int)
         ; Clean up stack and return
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
;------------------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
.__end____main____strcmp__char__1__char__1:
         ; End Function Declaration - strcmp(char[], char[]) -> int
; ====================================================================================

; ====================================================================================
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
;------------------------------------------------------------------------------
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
               mov rax, qword [rbp - 8]  ; __main__substr__block__33__res
         pop rdx ; rhs value
         mov qword [rbp - 8], rdx
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
                  mov rax, qword [rbp - 16]  ; __main__substr__block__33__for__34__i
            pop rdx ; rhs value
            mov qword [rbp - 16], rdx
            push rdx
         ; Loop init result can be discarded
         pop rax
         jmp .__forcond__34
.__for__34:
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
.__forcond__34:
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
            je .__endfor__34
         ; Body
   ;---------------------------------------------------------------------
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
   ;---------------------------------------------------------------------
         ; Repeat
jmp .__for__34
         ; End of For
.__endfor__34:
;---------------------------------------------------------------------------
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
;------------------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
.__end____main____substr__char__1__int__int:
         ; End Function Declaration - substr(char[], int, int) -> char[]
; ====================================================================================

; ====================================================================================
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
;------------------------------------------------------------------------------
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
               mov rax, qword [rbp - 8]  ; __main__first_index_of__block__36__size
         pop rdx ; rhs value
         mov qword [rbp - 8], rdx
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
                  mov rax, qword [rbp - 16]  ; __main__first_index_of__block__36__for__37__i
            pop rdx ; rhs value
            mov qword [rbp - 16], rdx
            push rdx
         ; Loop init result can be discarded
         pop rax
         jmp .__forcond__37
.__for__37:
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
.__forcond__37:
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
            je .__endfor__37
         ; Body
   ;---------------------------------------------------------------------
            ; Code Block
      ;------------------------------------------------------------------
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
                     je .__endif__39 ; jump to end
                  ; Body
                     ; Return
                        ; Identifier - int i
                           push qword [rbp - 16]
                        pop rax ; return value (int)
                        ; Clean up stack and return
                        mov rsp, rbp ; remove local vars + unpopped pushes
                        pop rbp
                        ret
                  jmp .__endif__39 ; jump to end of condition chain
                  ; End of if
.__endif__39:
      ;------------------------------------------------------------------
   ;---------------------------------------------------------------------
         ; Repeat
jmp .__for__37
         ; End of For
.__endfor__37:
;---------------------------------------------------------------------------
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
;------------------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
.__end____main____first_index_of__char__1__char:
         ; End Function Declaration - first_index_of(char[], char) -> int
; ====================================================================================

; ====================================================================================
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
;------------------------------------------------------------------------------
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
               mov rax, qword [rbp - 8]  ; __main__split__block__40__tokens
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
               mov rax, qword [rbp - 16]  ; __main__split__block__40__size
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
               mov rax, qword [rbp - 24]  ; __main__split__block__40__i
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
               mov rax, qword [rbp - 32]  ; __main__split__block__40__j
         pop rdx ; rhs value
         mov qword [rbp - 32], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
;---------------------------------------------------------------------------
         ; While-Loop
.__while__41:
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
            je .__endwhile__41
         ; Body
   ;---------------------------------------------------------------------
            ; Code Block
      ;------------------------------------------------------------------
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
                     je .__endif__43 ; jump to end
                  ; Body
            ;------------------------------------------------------------
                     ; Code Block
                        ; Assignment - '='
                           ; RHS
                              ; Int Literal
                                 mov rax, 0
                                 push rax
                           ; LHS
                              ; Variable Declaration - count
                                 mov rax, qword [rbp - 40]  ; __main__split__block__40__while__41__block__42__if__43__block__44__count
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
                                 mov rax, qword [rbp - 48]  ; __main__split__block__40__while__41__block__42__if__43__block__44__k
                           pop rdx ; rhs value
                           mov qword [rbp - 48], rdx
                           push rdx
                        ; Statement results can be ignored
                        pop rdx
               ;---------------------------------------------------------
                        ; While-Loop
.__while__45:
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
                              je .__endwhile__45
                           ; Body
                     ;---------------------------------------------------
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
                                    je .__else__46 ; jump to else
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
                                 jmp .__endif__46 ; jump to end of condition chain
                        ;------------------------------------------------
                                 ; Else-Statement
.__else__46:
                                 ; Break out of __while__45
                                 jmp .__endwhile__45
                        ;------------------------------------------------
                                 ; End of if
.__endif__46:
                     ;---------------------------------------------------
                           jmp .__while__45
                           ; End of While
.__endwhile__45:
               ;---------------------------------------------------------
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
               ;---------------------------------------------------------
                        ; For-Loop
                        ; Init
                           ; Assignment - '='
                              ; RHS
                                 ; Int Literal
                                    mov rax, 0
                                    push rax
                              ; LHS
                                 ; Variable Declaration - k
                                    mov rax, qword [rbp - 56]  ; __main__split__block__40__while__41__block__42__if__43__block__44__for__47__k
                              pop rdx ; rhs value
                              mov qword [rbp - 56], rdx
                              push rdx
                           ; Loop init result can be discarded
                           pop rax
                        jmp .__forcond__47
.__for__47:
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
.__forcond__47:
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
                              je .__endfor__47
                           ; Body
                     ;---------------------------------------------------
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
                     ;---------------------------------------------------
                           ; Repeat
jmp .__for__47
                           ; End of For
.__endfor__47:
               ;---------------------------------------------------------
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
            ;------------------------------------------------------------
                  jmp .__endif__43 ; jump to end of condition chain
                  ; End of if
.__endif__43:
      ;------------------------------------------------------------------
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
   ;---------------------------------------------------------------------
         jmp .__while__41
         ; End of While
.__endwhile__41:
;---------------------------------------------------------------------------
         ; Return
         ; Identifier - Vector<:char[]:> tokens
            push qword [rbp - 8]
         pop rax ; return value (Vector<:char[]:>)
         ; Clean up stack and return
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
;------------------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
.__end____main____split__char__1__char:
         ; End Function Declaration - split(char[], char) -> Vector<:char[]:>
; ====================================================================================

; ====================================================================================
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
;------------------------------------------------------------------------------
         ; Code Block
;---------------------------------------------------------------------------
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
            je .__endif__50 ; jump to end
         ; Body
            ; Return
               ; Identifier - int a
                  push qword [rbp - -16]
               pop rax ; return value (int)
               ; Clean up stack and return
               mov rsp, rbp ; remove local vars + unpopped pushes
               pop rbp
               ret
         jmp .__endif__50 ; jump to end of condition chain
         ; End of if
.__endif__50:
;---------------------------------------------------------------------------
         ; Return
         ; Identifier - int b
            push qword [rbp - -24]
         pop rax ; return value (int)
         ; Clean up stack and return
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
;------------------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
.__end____main____max__int__int:
         ; End Function Declaration - max(int, int) -> int
; ====================================================================================

; ====================================================================================
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
;------------------------------------------------------------------------------
         ; Code Block
;---------------------------------------------------------------------------
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
            je .__endif__52 ; jump to end
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
         jmp .__endif__52 ; jump to end of condition chain
         ; End of if
.__endif__52:
;---------------------------------------------------------------------------
         ; Return
         ; Identifier - float b
            push qword [rbp - -24]
         pop rax ; return value (float)
         movq xmm0, rax ; xmm0 is used for float return values
         ; Clean up stack and return
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
;------------------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
.__end____main____max__float__float:
         ; End Function Declaration - max(float, float) -> float
; ====================================================================================

; ====================================================================================
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
;------------------------------------------------------------------------------
         ; Code Block
;---------------------------------------------------------------------------
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
            je .__endif__54 ; jump to end
         ; Body
            ; Return
               ; Identifier - int a
                  push qword [rbp - -16]
               pop rax ; return value (int)
               ; Clean up stack and return
               mov rsp, rbp ; remove local vars + unpopped pushes
               pop rbp
               ret
         jmp .__endif__54 ; jump to end of condition chain
         ; End of if
.__endif__54:
;---------------------------------------------------------------------------
         ; Return
         ; Identifier - int b
            push qword [rbp - -24]
         pop rax ; return value (int)
         ; Clean up stack and return
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
;------------------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
.__end____main____min__int__int:
         ; End Function Declaration - min(int, int) -> int
; ====================================================================================

; ====================================================================================
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
;------------------------------------------------------------------------------
         ; Code Block
;---------------------------------------------------------------------------
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
            je .__endif__56 ; jump to end
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
         jmp .__endif__56 ; jump to end of condition chain
         ; End of if
.__endif__56:
;---------------------------------------------------------------------------
         ; Return
         ; Identifier - float b
            push qword [rbp - -24]
         pop rax ; return value (float)
         movq xmm0, rax ; xmm0 is used for float return values
         ; Clean up stack and return
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
;------------------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
.__end____main____min__float__float:
         ; End Function Declaration - min(float, float) -> float
; ====================================================================================

; ====================================================================================
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
;------------------------------------------------------------------------------
         ; Code Block
;---------------------------------------------------------------------------
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
            je .__endif__58 ; jump to end
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
         jmp .__endif__58 ; jump to end of condition chain
         ; End of if
.__endif__58:
;---------------------------------------------------------------------------
         ; Return
         ; Identifier - int v
            push qword [rbp - -16]
         pop rax ; return value (int)
         ; Clean up stack and return
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
;------------------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
.__end____main____abs__int:
         ; End Function Declaration - abs(int) -> int
; ====================================================================================

; ====================================================================================
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
;------------------------------------------------------------------------------
         ; Code Block
;---------------------------------------------------------------------------
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
            je .__endif__60 ; jump to end
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
         jmp .__endif__60 ; jump to end of condition chain
         ; End of if
.__endif__60:
;---------------------------------------------------------------------------
         ; Return
         ; Identifier - float v
            push qword [rbp - -16]
         pop rax ; return value (float)
         movq xmm0, rax ; xmm0 is used for float return values
         ; Clean up stack and return
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
;------------------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
.__end____main____abs__float:
         ; End Function Declaration - abs(float) -> float
; ====================================================================================

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
;------------------------------------------------------------------------------------
         ; While-Loop
.__while__61:
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
         je .__endwhile__61
         ; Body
;------------------------------------------------------------------------------
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
;------------------------------------------------------------------------------
         jmp .__while__61
         ; End of While
.__endwhile__61:
;------------------------------------------------------------------------------------
; ====================================================================================
         ; Class Declaration - __main____File inherits __builtin____main__Object
         ; Class data
         section .data
         ; Dispatch Table - this might need to be a malloc**
         .__dtable____main____File:
         ; Dispatch Table Entries
         section .text
;---------------------------------------------------------------------------------
         ; Field - char[] File::name
         section .data
         .__field____main____File____name: dq 1
         section .text
;---------------------------------------------------------------------------------
;---------------------------------------------------------------------------------
         ; Field - File File::parent
         section .data
         .__field____main____File____parent: dq 2
         section .text
;---------------------------------------------------------------------------------
;---------------------------------------------------------------------------------
         ; Field - Vector<:File:> File::children
         section .data
         .__field____main____File____children: dq 3
         section .text
;---------------------------------------------------------------------------------
;---------------------------------------------------------------------------------
         ; Field - int File::size
         section .data
         .__field____main____File____size: dq 4
         section .text
;---------------------------------------------------------------------------------
;---------------------------------------------------------------------------------
         ; Field - int File::is_dir
         section .data
         .__field____main____File____is_dir: dq 5
         section .text
;---------------------------------------------------------------------------------
         ; skip over class methods
         jmp .__endclass____main____File
;---------------------------------------------------------------------------------
         ; Constructor Declaration - File::File(char[]) -> File
         jmp .__end__ctor____main____File____File__char__1
         .__ctor____main____File____File__char__1:
         ; Function Header:
         ; Setup stack frame
         push rbp
         mov rbp, rsp
         ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
         sub rsp, 16 ; space for local variables (16-byte aligned)
         ; [rbp - 8] - this - Reference to 'this' object instance
         ; Creating Class Instance
         mov rdi, 48 ; [dtable, field0, field1, ..., fieldN] each 8 bytes
         call malloc
         mov qword [rbp - 8], rax ; save class instance as 'this'
         ; Add Dispatch Table
         mov rax, qword [rbp - 8] ; this
         mov qword [rax + 0], .__dtable____main____File ; this[0] = &dtable
         ; Parameters
         ; Param: name [rbp + 16]
         ; Body
;------------------------------------------------------------------------------
         ; Code Block
         ; Assignment - '='
         ; RHS
            ; Identifier - char[] name
               push qword [rbp - -16]
         ; LHS
            ; Member Accessor Assignment
               ; LHS
                  ; This keyword
                     push qword [rbp - 8] ; __this
               ; RHS
                  push qword [.__field____main____File____name] ; 
               pop rdi ; rhs
               pop rbx ; lhs
         pop rdx ; rhs value
         mov qword [rbx + 8*rdi], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
         ; RHS
            ; Null Literal
               push 0
         ; LHS
            ; Member Accessor Assignment
               ; LHS
                  ; This keyword
                     push qword [rbp - 8] ; __this
               ; RHS
                  push qword [.__field____main____File____parent] ; 
               pop rdi ; rhs
               pop rbx ; lhs
         pop rdx ; rhs value
         mov qword [rbx + 8*rdi], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
         ; RHS
            ; Constructor Call - Vector<:File:>::Vector() -> Vector<:File:>
               ; Make space for 0 arg(s)
               sub rsp, 0
               ; Arguments
               ; Call Vector<:File:>::Vector()
               call .__ctor____main____Vector__File____Vector
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
                  push qword [.__field____main____File____children] ; 
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
                  push qword [.__field____main____File____size] ; 
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
                  push qword [.__field____main____File____is_dir] ; 
               pop rdi ; rhs
               pop rbx ; lhs
         pop rdx ; rhs value
         mov qword [rbx + 8*rdi], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
;------------------------------------------------------------------------------
         mov rax, qword [rbp - 8] ; __this
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
         .__end__ctor____main____File____File__char__1:
         ; End Constructor Declaration - __ctor____main____File____File__char__1
;------------------------------------------------------------------------------------

.__endclass____main____File:
         ; End Class Declaration - __main____File
; =======================================================================================

         ; Assignment - '='
         ; RHS
         ; Constructor Call - File::File(char[]) -> File
         ; Make space for 1 arg(s)
         sub rsp, 8
         ; Arguments
         ; Eval arg0
         ; String Literal
            ; "/\n"
            mov rax, .str0
            push rax
         ; Move arg0's result to reverse order position on stack
         pop rax
         mov qword [rsp + 0], rax
         ; Call File::File(char[])
         call .__ctor____main____File____File__char__1
         ; Remove args
         add rsp, 8
         ; Push return value
         push rax
         ; LHS
         ; Variable Declaration - root
         mov rax, qword [rbp - 24]  ; __main__root
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
         ; Member Accessor Assignment
         ; LHS
         ; Identifier - File root
         push qword [rbp - 24]
         ; RHS
         push qword [.__field____main____File____is_dir] ; 
         pop rdi ; rhs
         pop rbx ; lhs
         pop rdx ; rhs value
         mov qword [rbx + 8*rdi], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
         ; RHS
         ; Identifier - File root
         push qword [rbp - 24]
         ; LHS
         ; Variable Declaration - workingdir
         mov rax, qword [rbp - 32]  ; __main__workingdir
         pop rdx ; rhs value
         mov qword [rbp - 32], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
         ; RHS
         ; Constructor Call - Vector<:File:>::Vector() -> Vector<:File:>
         ; Make space for 0 arg(s)
         sub rsp, 0
         ; Arguments
         ; Call Vector<:File:>::Vector()
         call .__ctor____main____Vector__File____Vector
         ; Remove args
         add rsp, 0
         ; Push return value
         push rax
         ; LHS
         ; Variable Declaration - all_files
         mov rax, qword [rbp - 40]  ; __main__all_files
         pop rdx ; rhs value
         mov qword [rbp - 40], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
         ; Method Call - Vector<:File:>::pushBack(File) -> void
         ; Make space for 1 arg(s) and object parameter
         sub rsp, 16
         ; LHS
         ; Identifier - Vector<:File:> all_files
         push qword [rbp - 40]
         pop rax ; object parameter
         mov qword [rsp + 0], rax ; place as first parameter
         ; RHS
         ; Arguments
         ; Eval arg0
         ; Identifier - File root
         push qword [rbp - 24]
         ; Move arg0's result to reverse order position on stack
         pop rax
         mov qword [rsp + 8], rax
         call .__method____main____Vector__File____pushBack__File
         ; Remove args
         add rsp, 16
         ; Push return value
         push rax
         ; Statement results can be ignored
         pop rdx
;---------------------------------------------------------------------------------------
         ; For-Loop
         ; Init
         ; Assignment - '='
         ; RHS
         ; Int Literal
         mov rax, 0
         push rax
         ; LHS
         ; Variable Declaration - i
         mov rax, qword [rbp - 48]  ; __main__for__64__i
         pop rdx ; rhs value
         mov qword [rbp - 48], rdx
         push rdx
         ; Loop init result can be discarded
         pop rax
         jmp .__forcond__64
.__for__64:
         ; Update
         ; Pre-Increment - int
         ; RHS
         ; Identifier - int i
         push qword [rbp - 48]
         pop rdx
         add qword [rbp - 48], 1
         mov rax, qword [rbp - 48]
         push rax ; push result
         ; Loop update result can be discarded
         pop rax
.__forcond__64:
         ; Condition
         ; Less Than
         ; LHS
         ; Identifier - int i
         push qword [rbp - 48]
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
         je .__endfor__64
         ; Body
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
                        ; Identifier - int i
                           push qword [rbp - 48]
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
         ; Variable Declaration - tokens
            mov rax, qword [rbp - 56]  ; __main__for__64__block__65__tokens
         pop rdx ; rhs value
         mov qword [rbp - 56], rdx
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
                                 ; Identifier - Vector<:char[]:> lines
                                    push qword [rbp - 16]
                              ; RHS
                                 push qword [.__field____main____Vector__char__1____data] ; stored index associated with field that is being accessed
                              pop rdx ; rhs
                              pop rax ; lhs
                              push qword [rax + 8*rdx] ; lhs.rhs
                        ; OFFSET
                           ; Identifier - int i
                              push qword [rbp - 48]
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
                  push '$'
            pop rdx ; rhs
            pop rax ; lhs
            cmp rax, rdx
            sete al
            movzx eax, al
            push rax
         pop rdx ; __cond
         cmp rdx, 0 ; ensure condition is true
         je .__endif__66 ; jump to end
         ; Body
;------------------------------------------------------------------------
         ; Code Block
   ;---------------------------------------------------------------------
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
                                          ; Identifier - Vector<:char[]:> tokens
                                             push qword [rbp - 56]
                                       ; RHS
                                          push qword [.__field____main____Vector__char__1____data] ; stored index associated with field that is being accessed
                                       pop rdx ; rhs
                                       pop rax ; lhs
                                       push qword [rax + 8*rdx] ; lhs.rhs
                                 ; OFFSET
                                    ; Int Literal
                                       mov rax, 1
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
                           push 'c'
                     pop rdx ; rhs
                     pop rax ; lhs
                     cmp rax, rdx
                     sete al
                     movzx eax, al
                     push rax
                  pop rdx ; __cond
                  cmp rdx, 0 ; ensure condition is true
                  je .__elif__68x0 ; jump to first elif
               ; Body
         ;---------------------------------------------------------------
                  ; Code Block
            ;------------------------------------------------------------
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
                                                   ; Identifier - Vector<:char[]:> tokens
                                                      push qword [rbp - 56]
                                                ; RHS
                                                   push qword [.__field____main____Vector__char__1____data] ; stored index associated with field that is being accessed
                                                pop rdx ; rhs
                                                pop rax ; lhs
                                                push qword [rax + 8*rdx] ; lhs.rhs
                                          ; OFFSET
                                             ; Int Literal
                                                mov rax, 2
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
                                    push '/'
                              pop rdx ; rhs
                              pop rax ; lhs
                              cmp rax, rdx
                              sete al
                              movzx eax, al
                              push rax
                           pop rdx ; __cond
                           cmp rdx, 0 ; ensure condition is true
                           je .__elif__70x0 ; jump to first elif
                        ; Body
                  ;------------------------------------------------------
                           ; Code Block
                              ; Assignment - '='
                                 ; RHS
                                    ; Identifier - File root
                                       push qword [rbp - 24]
                                 pop rdx ; rhs value
                                 mov qword [rbp - 32], rdx
                                 push rdx
                              ; Statement results can be ignored
                              pop rdx
                  ;------------------------------------------------------
                        jmp .__endif__70 ; jump to end of condition chain
               ;---------------------------------------------------------
                        ; Elif-Statement
.__elif__70x0:
                           ; Condition
                           ; Equal
                              ; LHS
                                 ; Subscript
                                    ; LHS
                                       ; Subscript
                                          ; LHS
                                             ; Member Accessor
                                                ; LHS
                                                   ; Identifier - Vector<:char[]:> tokens
                                                      push qword [rbp - 56]
                                                ; RHS
                                                   push qword [.__field____main____Vector__char__1____data] ; stored index associated with field that is being accessed
                                                pop rdx ; rhs
                                                pop rax ; lhs
                                                push qword [rax + 8*rdx] ; lhs.rhs
                                          ; OFFSET
                                             ; Int Literal
                                                mov rax, 2
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
                                    push '.'
                              pop rdx ; rhs
                              pop rax ; lhs
                              cmp rax, rdx
                              sete al
                              movzx eax, al
                              push rax
                           pop rdx ; __cond
                           cmp rdx, 0 ; ensure condition is true
                           je .__else__70
                           ; Body
                  ;------------------------------------------------------
                           ; Code Block
                              ; Assignment - '='
                                 ; RHS
                                    ; Member Accessor
                                       ; LHS
                                          ; Identifier - File workingdir
                                             push qword [rbp - 32]
                                       ; RHS
                                          push qword [.__field____main____File____parent] ; stored index associated with field that is being accessed
                                       pop rdx ; rhs
                                       pop rax ; lhs
                                       push qword [rax + 8*rdx] ; lhs.rhs
                                 pop rdx ; rhs value
                                 mov qword [rbp - 32], rdx
                                 push rdx
                              ; Statement results can be ignored
                              pop rdx
                  ;------------------------------------------------------
                           jmp .__endif__70
               ;---------------------------------------------------------
               ;---------------------------------------------------------
                        ; Else-Statement
.__else__70:
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
                                    ; Variable Declaration - j
                                       mov rax, qword [rbp - 64]  ; __main__for__64__block__65__if__66__block__67__if__68__block__69.__else__70__block__73__for__74__j
                                 pop rdx ; rhs value
                                 mov qword [rbp - 64], rdx
                                 push rdx
                              ; Loop init result can be discarded
                              pop rax
                           jmp .__forcond__74
.__for__74:
                              ; Update
                                 ; Pre-Increment - int
                                    ; RHS
                                       ; Identifier - int j
                                          push qword [rbp - 64]
                                    pop rdx
                                    add qword [rbp - 64], 1
                                    mov rax, qword [rbp - 64]
                                    push rax ; push result
                                 ; Loop update result can be discarded
                                 pop rax
.__forcond__74:
                              ; Condition
                                 ; Less Than
                                    ; LHS
                                       ; Identifier - int j
                                          push qword [rbp - 64]
                                    ; RHS
                                       ; Member Accessor
                                          ; LHS
                                             ; Member Accessor
                                                ; LHS
                                                   ; Identifier - File workingdir
                                                      push qword [rbp - 32]
                                                ; RHS
                                                   push qword [.__field____main____File____children] ; stored index associated with field that is being accessed
                                                pop rdx ; rhs
                                                pop rax ; lhs
                                                push qword [rax + 8*rdx] ; lhs.rhs
                                          ; RHS
                                             push qword [.__field____main____Vector__File____size] ; stored index associated with field that is being accessed
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
                                 je .__endfor__74
                              ; Body
                        ;------------------------------------------------
                                 ; Code Block
                           ;---------------------------------------------
                                    ; If-Statement
                                       ; Condition
                                          ; Function Call - strcmp(char[], char[]) -> int
                                             ; Make space for 2 arg(s)
                                             sub rsp, 16
                                             ; Arguments
                                                ; Eval arg0
                                                   ; Subscript
                                                      ; LHS
                                                         ; Member Accessor
                                                            ; LHS
                                                               ; Identifier - Vector<:char[]:> tokens
                                                                  push qword [rbp - 56]
                                                            ; RHS
                                                               push qword [.__field____main____Vector__char__1____data] ; stored index associated with field that is being accessed
                                                            pop rdx ; rhs
                                                            pop rax ; lhs
                                                            push qword [rax + 8*rdx] ; lhs.rhs
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
                                                ; Eval arg1
                                                   ; Member Accessor
                                                      ; LHS
                                                         ; Subscript
                                                            ; LHS
                                                               ; Member Accessor
                                                                  ; LHS
                                                                     ; Member Accessor
                                                                        ; LHS
                                                                           ; Identifier - File workingdir
                                                                              push qword [rbp - 32]
                                                                        ; RHS
                                                                           push qword [.__field____main____File____children] ; stored index associated with field that is being accessed
                                                                        pop rdx ; rhs
                                                                        pop rax ; lhs
                                                                        push qword [rax + 8*rdx] ; lhs.rhs
                                                                  ; RHS
                                                                     push qword [.__field____main____Vector__File____data] ; stored index associated with field that is being accessed
                                                                  pop rdx ; rhs
                                                                  pop rax ; lhs
                                                                  push qword [rax + 8*rdx] ; lhs.rhs
                                                            ; OFFSET
                                                               ; Identifier - int j
                                                                  push qword [rbp - 64]
                                                            pop rdx ; __offset
                                                            pop rax ; __pointer
                                                            push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                                                      ; RHS
                                                         push qword [.__field____main____File____name] ; stored index associated with field that is being accessed
                                                      pop rdx ; rhs
                                                      pop rax ; lhs
                                                      push qword [rax + 8*rdx] ; lhs.rhs
                                                ; Move arg1's result to reverse order position on stack
                                                pop rax
                                                mov qword [rsp + 8], rax
                                             ; Call strcmp(char[], char[])
                                             call .__main____strcmp__char__1__char__1
                                             ; Remove args
                                             add rsp, 16
                                             ; Push return value
                                             push rax
                                          pop rdx ; __cond
                                          cmp rdx, 0 ; ensure condition is true
                                          je .__endif__76 ; jump to end
                                       ; Body
                                 ;---------------------------------------
                                          ; Code Block
                                             ; Assignment - '='
                                                ; RHS
                                                   ; Subscript
                                                      ; LHS
                                                         ; Member Accessor
                                                            ; LHS
                                                               ; Member Accessor
                                                                  ; LHS
                                                                     ; Identifier - File workingdir
                                                                        push qword [rbp - 32]
                                                                  ; RHS
                                                                     push qword [.__field____main____File____children] ; stored index associated with field that is being accessed
                                                                  pop rdx ; rhs
                                                                  pop rax ; lhs
                                                                  push qword [rax + 8*rdx] ; lhs.rhs
                                                            ; RHS
                                                               push qword [.__field____main____Vector__File____data] ; stored index associated with field that is being accessed
                                                            pop rdx ; rhs
                                                            pop rax ; lhs
                                                            push qword [rax + 8*rdx] ; lhs.rhs
                                                      ; OFFSET
                                                         ; Identifier - int j
                                                            push qword [rbp - 64]
                                                      pop rdx ; __offset
                                                      pop rax ; __pointer
                                                      push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                                                pop rdx ; rhs value
                                                mov qword [rbp - 32], rdx
                                                push rdx
                                             ; Statement results can be ignored
                                             pop rdx
                                             ; Break out of __for__74
                                             jmp .__endfor__74
                                 ;---------------------------------------
                                       jmp .__endif__76 ; jump to end of condition chain
                                       ; End of if
.__endif__76:
                           ;---------------------------------------------
                        ;------------------------------------------------
                              ; Repeat
jmp .__for__74
                              ; End of For
.__endfor__74:
                  ;------------------------------------------------------
               ;---------------------------------------------------------
               ;---------------------------------------------------------
                        ; End of if
.__endif__70:
            ;------------------------------------------------------------
         ;---------------------------------------------------------------
               jmp .__endif__68 ; jump to end of condition chain
      ;------------------------------------------------------------------
               ; Elif-Statement
.__elif__68x0:
                  ; Condition
                  ; Equal
                     ; LHS
                        ; Subscript
                           ; LHS
                              ; Subscript
                                 ; LHS
                                    ; Member Accessor
                                       ; LHS
                                          ; Identifier - Vector<:char[]:> tokens
                                             push qword [rbp - 56]
                                       ; RHS
                                          push qword [.__field____main____Vector__char__1____data] ; stored index associated with field that is being accessed
                                       pop rdx ; rhs
                                       pop rax ; lhs
                                       push qword [rax + 8*rdx] ; lhs.rhs
                                 ; OFFSET
                                    ; Int Literal
                                       mov rax, 1
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
                           push 'l'
                     pop rdx ; rhs
                     pop rax ; lhs
                     cmp rax, rdx
                     sete al
                     movzx eax, al
                     push rax
                  pop rdx ; __cond
                  cmp rdx, 0 ; ensure condition is true
                  je .__endif__68
                  ; Body
         ;---------------------------------------------------------------
                  ; Code Block
                     ; Pre-Increment - int
                        ; RHS
                           ; Identifier - int i
                              push qword [rbp - 48]
                        pop rdx
                        add qword [rbp - 48], 1
                        mov rax, qword [rbp - 48]
                        push rax ; push result
                     ; Statement results can be ignored
                     pop rdx
            ;------------------------------------------------------------
                     ; While-Loop
.__while__79:
                        ; Condition
                           ; Less Than
                              ; LHS
                                 ; Identifier - int i
                                    push qword [rbp - 48]
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
                           je .__endwhile__79
                        ; Body
                  ;------------------------------------------------------
                           ; Code Block
                     ;---------------------------------------------------
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
                                                            ; Identifier - Vector<:char[]:> lines
                                                               push qword [rbp - 16]
                                                         ; RHS
                                                            push qword [.__field____main____Vector__char__1____data] ; stored index associated with field that is being accessed
                                                         pop rdx ; rhs
                                                         pop rax ; lhs
                                                         push qword [rax + 8*rdx] ; lhs.rhs
                                                   ; OFFSET
                                                      ; Identifier - int i
                                                         push qword [rbp - 48]
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
                                             push '$'
                                       pop rdx ; rhs
                                       pop rax ; lhs
                                       cmp rax, rdx
                                       sete al
                                       movzx eax, al
                                       push rax
                                    pop rdx ; __cond
                                    cmp rdx, 0 ; ensure condition is true
                                    je .__endif__81 ; jump to end
                                 ; Body
                                    ; Break out of __while__79
                                    jmp .__endwhile__79
                                 jmp .__endif__81 ; jump to end of condition chain
                                 ; End of if
.__endif__81:
                     ;---------------------------------------------------
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
                                                   ; Identifier - int i
                                                      push qword [rbp - 48]
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
                                    ; Variable Declaration - tokens
                                       mov rax, qword [rbp - 72]  ; __main__for__64__block__65__if__66__block__67__elif__68x1__block__78__while__79__block__80__tokens
                                 pop rdx ; rhs value
                                 mov qword [rbp - 72], rdx
                                 push rdx
                              ; Statement results can be ignored
                              pop rdx
                     ;---------------------------------------------------
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
                                                            ; Identifier - Vector<:char[]:> tokens
                                                               push qword [rbp - 72]
                                                         ; RHS
                                                            push qword [.__field____main____Vector__char__1____data] ; stored index associated with field that is being accessed
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
                                             push 'd'
                                       pop rdx ; rhs
                                       pop rax ; lhs
                                       cmp rax, rdx
                                       sete al
                                       movzx eax, al
                                       push rax
                                    pop rdx ; __cond
                                    cmp rdx, 0 ; ensure condition is true
                                    je .__else__82 ; jump to else
                                 ; Body
                           ;---------------------------------------------
                                    ; Code Block
                                       ; Assignment - '='
                                          ; RHS
                                             ; Constructor Call - File::File(char[]) -> File
                                                ; Make space for 1 arg(s)
                                                sub rsp, 8
                                                ; Arguments
                                                   ; Eval arg0
                                                      ; Subscript
                                                         ; LHS
                                                            ; Member Accessor
                                                               ; LHS
                                                                  ; Identifier - Vector<:char[]:> tokens
                                                                     push qword [rbp - 72]
                                                               ; RHS
                                                                  push qword [.__field____main____Vector__char__1____data] ; stored index associated with field that is being accessed
                                                               pop rdx ; rhs
                                                               pop rax ; lhs
                                                               push qword [rax + 8*rdx] ; lhs.rhs
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
                                                ; Call File::File(char[])
                                                call .__ctor____main____File____File__char__1
                                                ; Remove args
                                                add rsp, 8
                                                ; Push return value
                                                push rax
                                          ; LHS
                                             ; Variable Declaration - dir
                                                mov rax, qword [rbp - 80]  ; __main__for__64__block__65__if__66__block__67__elif__68x1__block__78__while__79__block__80__if__82__block__83__dir
                                          pop rdx ; rhs value
                                          mov qword [rbp - 80], rdx
                                          push rdx
                                       ; Statement results can be ignored
                                       pop rdx
                                       ; Assignment - '='
                                          ; RHS
                                             ; Identifier - File workingdir
                                                push qword [rbp - 32]
                                          ; LHS
                                             ; Member Accessor Assignment
                                                ; LHS
                                                   ; Identifier - File dir
                                                      push qword [rbp - 80]
                                                ; RHS
                                                   push qword [.__field____main____File____parent] ; 
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
                                                mov rax, 1
                                                push rax
                                          ; LHS
                                             ; Member Accessor Assignment
                                                ; LHS
                                                   ; Identifier - File dir
                                                      push qword [rbp - 80]
                                                ; RHS
                                                   push qword [.__field____main____File____is_dir] ; 
                                                pop rdi ; rhs
                                                pop rbx ; lhs
                                          pop rdx ; rhs value
                                          mov qword [rbx + 8*rdi], rdx
                                          push rdx
                                       ; Statement results can be ignored
                                       pop rdx
                                       ; Method Call - Vector<:File:>::pushBack(File) -> void
                                          ; Make space for 1 arg(s) and object parameter
                                          sub rsp, 16
                                          ; LHS
                                             ; Member Accessor
                                                ; LHS
                                                   ; Identifier - File workingdir
                                                      push qword [rbp - 32]
                                                ; RHS
                                                   push qword [.__field____main____File____children] ; stored index associated with field that is being accessed
                                                pop rdx ; rhs
                                                pop rax ; lhs
                                                push qword [rax + 8*rdx] ; lhs.rhs
                                             pop rax ; object parameter
                                             mov qword [rsp + 0], rax ; place as first parameter
                                          ; RHS
                                          ; Arguments
                                             ; Eval arg0
                                                ; Identifier - File dir
                                                   push qword [rbp - 80]
                                             ; Move arg0's result to reverse order position on stack
                                             pop rax
                                             mov qword [rsp + 8], rax
                                          call .__method____main____Vector__File____pushBack__File
                                          ; Remove args
                                          add rsp, 16
                                          ; Push return value
                                          push rax
                                       ; Statement results can be ignored
                                       pop rdx
                                       ; Method Call - Vector<:File:>::pushBack(File) -> void
                                          ; Make space for 1 arg(s) and object parameter
                                          sub rsp, 16
                                          ; LHS
                                             ; Identifier - Vector<:File:> all_files
                                                push qword [rbp - 40]
                                             pop rax ; object parameter
                                             mov qword [rsp + 0], rax ; place as first parameter
                                          ; RHS
                                          ; Arguments
                                             ; Eval arg0
                                                ; Identifier - File dir
                                                   push qword [rbp - 80]
                                             ; Move arg0's result to reverse order position on stack
                                             pop rax
                                             mov qword [rsp + 8], rax
                                          call .__method____main____Vector__File____pushBack__File
                                          ; Remove args
                                          add rsp, 16
                                          ; Push return value
                                          push rax
                                       ; Statement results can be ignored
                                       pop rdx
                           ;---------------------------------------------
                                 jmp .__endif__82 ; jump to end of condition chain
                        ;------------------------------------------------
                                 ; Else-Statement
.__else__82:
                        ;------------------------------------------------
                                 ; Code Block
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
                                                               ; Identifier - Vector<:char[]:> tokens
                                                                  push qword [rbp - 72]
                                                            ; RHS
                                                               push qword [.__field____main____Vector__char__1____data] ; stored index associated with field that is being accessed
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
                                             ; Call stringToInt(char[])
                                             call __builtin__stringToInt__char__1
                                             ; Remove args
                                             add rsp, 8
                                             ; Push return value
                                             push rax
                                       ; LHS
                                          ; Variable Declaration - size
                                             mov rax, qword [rbp - 88]  ; __main__for__64__block__65__if__66__block__67__elif__68x1__block__78__while__79__block__80.__else__82__block__84__size
                                       pop rdx ; rhs value
                                       mov qword [rbp - 88], rdx
                                       push rdx
                                    ; Statement results can be ignored
                                    pop rdx
                                    ; Assignment - '='
                                       ; RHS
                                          ; Constructor Call - File::File(char[]) -> File
                                             ; Make space for 1 arg(s)
                                             sub rsp, 8
                                             ; Arguments
                                                ; Eval arg0
                                                   ; Subscript
                                                      ; LHS
                                                         ; Member Accessor
                                                            ; LHS
                                                               ; Identifier - Vector<:char[]:> tokens
                                                                  push qword [rbp - 72]
                                                            ; RHS
                                                               push qword [.__field____main____Vector__char__1____data] ; stored index associated with field that is being accessed
                                                            pop rdx ; rhs
                                                            pop rax ; lhs
                                                            push qword [rax + 8*rdx] ; lhs.rhs
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
                                             ; Call File::File(char[])
                                             call .__ctor____main____File____File__char__1
                                             ; Remove args
                                             add rsp, 8
                                             ; Push return value
                                             push rax
                                       ; LHS
                                          ; Variable Declaration - f
                                             mov rax, qword [rbp - 96]  ; __main__for__64__block__65__if__66__block__67__elif__68x1__block__78__while__79__block__80.__else__82__block__84__f
                                       pop rdx ; rhs value
                                       mov qword [rbp - 96], rdx
                                       push rdx
                                    ; Statement results can be ignored
                                    pop rdx
                                    ; Assignment - '='
                                       ; RHS
                                          ; Identifier - int size
                                             push qword [rbp - 88]
                                       ; LHS
                                          ; Member Accessor Assignment
                                             ; LHS
                                                ; Identifier - File f
                                                   push qword [rbp - 96]
                                             ; RHS
                                                push qword [.__field____main____File____size] ; 
                                             pop rdi ; rhs
                                             pop rbx ; lhs
                                       pop rdx ; rhs value
                                       mov qword [rbx + 8*rdi], rdx
                                       push rdx
                                    ; Statement results can be ignored
                                    pop rdx
                                    ; Assignment - '='
                                       ; RHS
                                          ; Identifier - File workingdir
                                             push qword [rbp - 32]
                                       ; LHS
                                          ; Member Accessor Assignment
                                             ; LHS
                                                ; Identifier - File f
                                                   push qword [rbp - 96]
                                             ; RHS
                                                push qword [.__field____main____File____parent] ; 
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
                                                ; Identifier - File f
                                                   push qword [rbp - 96]
                                             ; RHS
                                                push qword [.__field____main____File____is_dir] ; 
                                             pop rdi ; rhs
                                             pop rbx ; lhs
                                       pop rdx ; rhs value
                                       mov qword [rbx + 8*rdi], rdx
                                       push rdx
                                    ; Statement results can be ignored
                                    pop rdx
                                    ; Method Call - Vector<:File:>::pushBack(File) -> void
                                       ; Make space for 1 arg(s) and object parameter
                                       sub rsp, 16
                                       ; LHS
                                          ; Member Accessor
                                             ; LHS
                                                ; Identifier - File workingdir
                                                   push qword [rbp - 32]
                                             ; RHS
                                                push qword [.__field____main____File____children] ; stored index associated with field that is being accessed
                                             pop rdx ; rhs
                                             pop rax ; lhs
                                             push qword [rax + 8*rdx] ; lhs.rhs
                                          pop rax ; object parameter
                                          mov qword [rsp + 0], rax ; place as first parameter
                                       ; RHS
                                       ; Arguments
                                          ; Eval arg0
                                             ; Identifier - File f
                                                push qword [rbp - 96]
                                          ; Move arg0's result to reverse order position on stack
                                          pop rax
                                          mov qword [rsp + 8], rax
                                       call .__method____main____Vector__File____pushBack__File
                                       ; Remove args
                                       add rsp, 16
                                       ; Push return value
                                       push rax
                                    ; Statement results can be ignored
                                    pop rdx
                                    ; Method Call - Vector<:File:>::pushBack(File) -> void
                                       ; Make space for 1 arg(s) and object parameter
                                       sub rsp, 16
                                       ; LHS
                                          ; Identifier - Vector<:File:> all_files
                                             push qword [rbp - 40]
                                          pop rax ; object parameter
                                          mov qword [rsp + 0], rax ; place as first parameter
                                       ; RHS
                                       ; Arguments
                                          ; Eval arg0
                                             ; Identifier - File f
                                                push qword [rbp - 96]
                                          ; Move arg0's result to reverse order position on stack
                                          pop rax
                                          mov qword [rsp + 8], rax
                                       call .__method____main____Vector__File____pushBack__File
                                       ; Remove args
                                       add rsp, 16
                                       ; Push return value
                                       push rax
                                    ; Statement results can be ignored
                                    pop rdx
                        ;------------------------------------------------
                        ;------------------------------------------------
                                 ; End of if
.__endif__82:
                     ;---------------------------------------------------
                              ; Pre-Increment - int
                                 ; RHS
                                    ; Identifier - int i
                                       push qword [rbp - 48]
                                 pop rdx
                                 add qword [rbp - 48], 1
                                 mov rax, qword [rbp - 48]
                                 push rax ; push result
                              ; Statement results can be ignored
                              pop rdx
                  ;------------------------------------------------------
                        jmp .__while__79
                        ; End of While
.__endwhile__79:
            ;------------------------------------------------------------
                     ; Pre-Decrement - int
                        ; RHS
                           ; Identifier - int i
                              push qword [rbp - 48]
                        pop rdx
                        sub qword [rbp - 48], 1
                        mov rax, qword [rbp - 48]
                        push rax ; push result
                     ; Statement results can be ignored
                     pop rdx
         ;---------------------------------------------------------------
                  jmp .__endif__68
      ;------------------------------------------------------------------
               ; End of if
.__endif__68:
   ;---------------------------------------------------------------------
;------------------------------------------------------------------------
         jmp .__endif__66 ; jump to end of condition chain
         ; End of if
.__endif__66:
;------------------------------------------------------------------------------
;---------------------------------------------------------------------------------
         ; Repeat
jmp .__for__64
         ; End of For
.__endfor__64:
;---------------------------------------------------------------------------------------
; =======================================================================================
         ; Function Declaration - printfs(File, int) -> void
         ; Skip over function declaration
         jmp .__end____main____printfs__File__int
.__main____printfs__File__int:
         ; Function Header:
         ; Setup stack frame
         push rbp
         mov rbp, rsp
         sub rsp, 16
         ; Parameters
         ; Param: fs [rbp + 16]
         ; Param: indent [rbp + 24]
         ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
         ; [rbp - 8] - int i (<unset-scope-name>)
         ; [rbp - 16] - int i (<unset-scope-name>)

         ; Body
;---------------------------------------------------------------------------------
         ; Code Block
;------------------------------------------------------------------------------
         ; If-Statement
         ; Condition
         ; Equal
            ; LHS
               ; Identifier - File fs
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
         je .__endif__86 ; jump to end
         ; Body
         ; Return
            mov rax, 0
            ; Clean up stack and return
            mov rsp, rbp ; remove local vars + unpopped pushes
            pop rbp
            ret
         jmp .__endif__86 ; jump to end of condition chain
         ; End of if
.__endif__86:
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
            ; Variable Declaration - i
               mov rax, qword [rbp - 8]  ; __main__printfs__block__85__for__87__i
         pop rdx ; rhs value
         mov qword [rbp - 8], rdx
         push rdx
         ; Loop init result can be discarded
         pop rax
         jmp .__forcond__87
.__for__87:
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
.__forcond__87:
         ; Condition
         ; Less Than
            ; LHS
               ; Identifier - int i
                  push qword [rbp - 8]
            ; RHS
               ; Identifier - int indent
                  push qword [rbp - -24]
            pop rdx ; rhs
            pop rax ; lhs
            cmp rax, rdx
            setl al
            movzx eax, al
            push rax
         pop rax ; __cond
         cmp rax, 0 ; __cond
         je .__endfor__87
         ; Body
;------------------------------------------------------------------------
         ; Code Block
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
;------------------------------------------------------------------------
         ; Repeat
jmp .__for__87
         ; End of For
.__endfor__87:
;------------------------------------------------------------------------------
         ; Function Call - print(char[]) -> void
         ; Make space for 1 arg(s)
         sub rsp, 8
         ; Arguments
         ; Eval arg0
            ; Member Accessor
               ; LHS
                  ; Identifier - File fs
                     push qword [rbp - -16]
               ; RHS
                  push qword [.__field____main____File____name] ; stored index associated with field that is being accessed
               pop rdx ; rhs
               pop rax ; lhs
               push qword [rax + 8*rdx] ; lhs.rhs
         ; Move arg0's result to reverse order position on stack
         pop rax
         mov qword [rsp + 0], rax
         ; Call print(char[])
         call __builtin__print__char__1
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
                  ; Identifier - File fs
                     push qword [rbp - -16]
               ; RHS
                  push qword [.__field____main____File____size] ; stored index associated with field that is being accessed
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
                  ; Identifier - File fs
                     push qword [rbp - -16]
               ; RHS
                  push qword [.__field____main____File____is_dir] ; stored index associated with field that is being accessed
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
;------------------------------------------------------------------------------
         ; For-Loop
         ; Init
         ; Assignment - '='
         ; RHS
            ; Int Literal
               mov rax, 0
               push rax
         ; LHS
            ; Variable Declaration - i
               mov rax, qword [rbp - 16]  ; __main__printfs__block__85__for__89__i
         pop rdx ; rhs value
         mov qword [rbp - 16], rdx
         push rdx
         ; Loop init result can be discarded
         pop rax
         jmp .__forcond__89
.__for__89:
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
.__forcond__89:
         ; Condition
         ; Less Than
            ; LHS
               ; Identifier - int i
                  push qword [rbp - 16]
            ; RHS
               ; Member Accessor
                  ; LHS
                     ; Member Accessor
                        ; LHS
                           ; Identifier - File fs
                              push qword [rbp - -16]
                        ; RHS
                           push qword [.__field____main____File____children] ; stored index associated with field that is being accessed
                        pop rdx ; rhs
                        pop rax ; lhs
                        push qword [rax + 8*rdx] ; lhs.rhs
                  ; RHS
                     push qword [.__field____main____Vector__File____size] ; stored index associated with field that is being accessed
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
         je .__endfor__89
         ; Body
;------------------------------------------------------------------------
         ; Code Block
            ; Function Call - printfs(File, int) -> void
               ; Make space for 2 arg(s)
               sub rsp, 16
               ; Arguments
                  ; Eval arg0
                     ; Subscript
                        ; LHS
                           ; Member Accessor
                              ; LHS
                                 ; Member Accessor
                                    ; LHS
                                       ; Identifier - File fs
                                          push qword [rbp - -16]
                                    ; RHS
                                       push qword [.__field____main____File____children] ; stored index associated with field that is being accessed
                                    pop rdx ; rhs
                                    pop rax ; lhs
                                    push qword [rax + 8*rdx] ; lhs.rhs
                              ; RHS
                                 push qword [.__field____main____Vector__File____data] ; stored index associated with field that is being accessed
                              pop rdx ; rhs
                              pop rax ; lhs
                              push qword [rax + 8*rdx] ; lhs.rhs
                        ; OFFSET
                           ; Identifier - int i
                              push qword [rbp - 16]
                        pop rdx ; __offset
                        pop rax ; __pointer
                        push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                  ; Move arg0's result to reverse order position on stack
                  pop rax
                  mov qword [rsp + 0], rax
                  ; Eval arg1
                     ; Addition - int, int
                        ; LHS
                           ; Identifier - int indent
                              push qword [rbp - -24]
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
               ; Call printfs(File, int)
               call .__main____printfs__File__int
               ; Remove args
               add rsp, 16
               ; Push return value
               push rax
            ; Statement results can be ignored
            pop rdx
;------------------------------------------------------------------------
         ; Repeat
jmp .__for__89
         ; End of For
.__endfor__89:
;------------------------------------------------------------------------------
;---------------------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
.__end____main____printfs__File__int:
         ; End Function Declaration - printfs(File, int) -> void
; =======================================================================================

; =======================================================================================
         ; Function Declaration - sum_sizes(File) -> void
         ; Skip over function declaration
         jmp .__end____main____sum_sizes__File
.__main____sum_sizes__File:
         ; Function Header:
         ; Setup stack frame
         push rbp
         mov rbp, rsp
         sub rsp, 16
         ; Parameters
         ; Param: fs [rbp + 16]
         ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
         ; [rbp - 8] - int i (<unset-scope-name>)

         ; Body
;---------------------------------------------------------------------------------
         ; Code Block
;------------------------------------------------------------------------------
         ; If-Statement
         ; Condition
         ; Equal
            ; LHS
               ; Identifier - File fs
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
         je .__endif__92 ; jump to end
         ; Body
         ; Return
            mov rax, 0
            ; Clean up stack and return
            mov rsp, rbp ; remove local vars + unpopped pushes
            pop rbp
            ret
         jmp .__endif__92 ; jump to end of condition chain
         ; End of if
.__endif__92:
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
            ; Variable Declaration - i
               mov rax, qword [rbp - 8]  ; __main__sum_sizes__block__91__for__93__i
         pop rdx ; rhs value
         mov qword [rbp - 8], rdx
         push rdx
         ; Loop init result can be discarded
         pop rax
         jmp .__forcond__93
.__for__93:
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
.__forcond__93:
         ; Condition
         ; Less Than
            ; LHS
               ; Identifier - int i
                  push qword [rbp - 8]
            ; RHS
               ; Member Accessor
                  ; LHS
                     ; Member Accessor
                        ; LHS
                           ; Identifier - File fs
                              push qword [rbp - -16]
                        ; RHS
                           push qword [.__field____main____File____children] ; stored index associated with field that is being accessed
                        pop rdx ; rhs
                        pop rax ; lhs
                        push qword [rax + 8*rdx] ; lhs.rhs
                  ; RHS
                     push qword [.__field____main____Vector__File____size] ; stored index associated with field that is being accessed
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
         je .__endfor__93
         ; Body
;------------------------------------------------------------------------
         ; Code Block
            ; Function Call - sum_sizes(File) -> void
               ; Make space for 1 arg(s)
               sub rsp, 8
               ; Arguments
                  ; Eval arg0
                     ; Subscript
                        ; LHS
                           ; Member Accessor
                              ; LHS
                                 ; Member Accessor
                                    ; LHS
                                       ; Identifier - File fs
                                          push qword [rbp - -16]
                                    ; RHS
                                       push qword [.__field____main____File____children] ; stored index associated with field that is being accessed
                                    pop rdx ; rhs
                                    pop rax ; lhs
                                    push qword [rax + 8*rdx] ; lhs.rhs
                              ; RHS
                                 push qword [.__field____main____Vector__File____data] ; stored index associated with field that is being accessed
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
               ; Call sum_sizes(File)
               call .__main____sum_sizes__File
               ; Remove args
               add rsp, 8
               ; Push return value
               push rax
            ; Statement results can be ignored
            pop rdx
            ; Assignment - '+='
               ; RHS
                  ; Member Accessor
                     ; LHS
                        ; Subscript
                           ; LHS
                              ; Member Accessor
                                 ; LHS
                                    ; Member Accessor
                                       ; LHS
                                          ; Identifier - File fs
                                             push qword [rbp - -16]
                                       ; RHS
                                          push qword [.__field____main____File____children] ; stored index associated with field that is being accessed
                                       pop rdx ; rhs
                                       pop rax ; lhs
                                       push qword [rax + 8*rdx] ; lhs.rhs
                                 ; RHS
                                    push qword [.__field____main____Vector__File____data] ; stored index associated with field that is being accessed
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
                        push qword [.__field____main____File____size] ; stored index associated with field that is being accessed
                     pop rdx ; rhs
                     pop rax ; lhs
                     push qword [rax + 8*rdx] ; lhs.rhs
               ; LHS
                  ; Member Accessor Assignment
                     ; LHS
                        ; Identifier - File fs
                           push qword [rbp - -16]
                     ; RHS
                        push qword [.__field____main____File____size] ; 
                     pop rdi ; rhs
                     pop rbx ; lhs
               pop rdx ; rhs value
               mov rax, qword [rbx + 8*rdi] ; read lhs value
               add rax, rdx      ; add lhs and rhs
               mov qword [rbx + 8*rdi], rax ; write back to lhs
               push rax          ; push result for other expressions
            ; Statement results can be ignored
            pop rdx
;------------------------------------------------------------------------
         ; Repeat
jmp .__for__93
         ; End of For
.__endfor__93:
;------------------------------------------------------------------------------
;---------------------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
.__end____main____sum_sizes__File:
         ; End Function Declaration - sum_sizes(File) -> void
; =======================================================================================

         ; Function Call - sum_sizes(File) -> void
         ; Make space for 1 arg(s)
         sub rsp, 8
         ; Arguments
         ; Eval arg0
         ; Identifier - File root
         push qword [rbp - 24]
         ; Move arg0's result to reverse order position on stack
         pop rax
         mov qword [rsp + 0], rax
         ; Call sum_sizes(File)
         call .__main____sum_sizes__File
         ; Remove args
         add rsp, 8
         ; Push return value
         push rax
         ; Statement results can be ignored
         pop rdx
; =======================================================================================
         ; Function Declaration - sum_small_dirs(File) -> int
         ; Skip over function declaration
         jmp .__end____main____sum_small_dirs__File
.__main____sum_small_dirs__File:
         ; Function Header:
         ; Setup stack frame
         push rbp
         mov rbp, rsp
         sub rsp, 16
         ; Parameters
         ; Param: fs [rbp + 16]
         ; Local Variables - Each variable is currently 64-bit (sorry not sorry)
         ; [rbp - 8] - int sum (<unset-scope-name>)
         ; [rbp - 16] - int i (<unset-scope-name>)

         ; Body
;---------------------------------------------------------------------------------
         ; Code Block
;------------------------------------------------------------------------------
         ; If-Statement
         ; Condition
         ; Equal
            ; LHS
               ; Identifier - File fs
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
         je .__endif__96 ; jump to end
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
         jmp .__endif__96 ; jump to end of condition chain
         ; End of if
.__endif__96:
;------------------------------------------------------------------------------
;------------------------------------------------------------------------------
         ; If-Statement
         ; Condition
         ; Negate - int
            ; RHS
               ; Member Accessor
                  ; LHS
                     ; Identifier - File fs
                        push qword [rbp - -16]
                  ; RHS
                     push qword [.__field____main____File____is_dir] ; stored index associated with field that is being accessed
                  pop rdx ; rhs
                  pop rax ; lhs
                  push qword [rax + 8*rdx] ; lhs.rhs
            pop rdx
            cmp rdx, 0
            sete al
            movzx eax, al
            push rax ; push result
         pop rdx ; __cond
         cmp rdx, 0 ; ensure condition is true
         je .__endif__97 ; jump to end
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
         jmp .__endif__97 ; jump to end of condition chain
         ; End of if
.__endif__97:
;------------------------------------------------------------------------------
         ; Assignment - '='
         ; RHS
         ; Int Literal
            mov rax, 0
            push rax
         ; LHS
         ; Variable Declaration - sum
            mov rax, qword [rbp - 8]  ; __main__sum_small_dirs__block__95__sum
         pop rdx ; rhs value
         mov qword [rbp - 8], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
;------------------------------------------------------------------------------
         ; If-Statement
         ; Condition
         ; Less Than
            ; LHS
               ; Member Accessor
                  ; LHS
                     ; Identifier - File fs
                        push qword [rbp - -16]
                  ; RHS
                     push qword [.__field____main____File____size] ; stored index associated with field that is being accessed
                  pop rdx ; rhs
                  pop rax ; lhs
                  push qword [rax + 8*rdx] ; lhs.rhs
            ; RHS
               ; Int Literal
                  mov rax, 100000
                  push rax
            pop rdx ; rhs
            pop rax ; lhs
            cmp rax, rdx
            setl al
            movzx eax, al
            push rax
         pop rdx ; __cond
         cmp rdx, 0 ; ensure condition is true
         je .__endif__98 ; jump to end
         ; Body
         ; Assignment - '+='
            ; RHS
               ; Member Accessor
                  ; LHS
                     ; Identifier - File fs
                        push qword [rbp - -16]
                  ; RHS
                     push qword [.__field____main____File____size] ; stored index associated with field that is being accessed
                  pop rdx ; rhs
                  pop rax ; lhs
                  push qword [rax + 8*rdx] ; lhs.rhs
            pop rdx ; rhs value
            mov rax, qword [rbp - 8] ; read lhs value
            add rax, rdx      ; add lhs and rhs
            mov qword [rbp - 8], rax ; write back to lhs
            push rax          ; push result for other expressions
         ; Statement results can be ignored
         pop rdx
         jmp .__endif__98 ; jump to end of condition chain
         ; End of if
.__endif__98:
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
            ; Variable Declaration - i
               mov rax, qword [rbp - 16]  ; __main__sum_small_dirs__block__95__for__99__i
         pop rdx ; rhs value
         mov qword [rbp - 16], rdx
         push rdx
         ; Loop init result can be discarded
         pop rax
         jmp .__forcond__99
.__for__99:
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
.__forcond__99:
         ; Condition
         ; Less Than
            ; LHS
               ; Identifier - int i
                  push qword [rbp - 16]
            ; RHS
               ; Member Accessor
                  ; LHS
                     ; Member Accessor
                        ; LHS
                           ; Identifier - File fs
                              push qword [rbp - -16]
                        ; RHS
                           push qword [.__field____main____File____children] ; stored index associated with field that is being accessed
                        pop rdx ; rhs
                        pop rax ; lhs
                        push qword [rax + 8*rdx] ; lhs.rhs
                  ; RHS
                     push qword [.__field____main____Vector__File____size] ; stored index associated with field that is being accessed
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
;------------------------------------------------------------------------
         ; Code Block
            ; Assignment - '+='
               ; RHS
                  ; Function Call - sum_small_dirs(File) -> int
                     ; Make space for 1 arg(s)
                     sub rsp, 8
                     ; Arguments
                        ; Eval arg0
                           ; Subscript
                              ; LHS
                                 ; Member Accessor
                                    ; LHS
                                       ; Member Accessor
                                          ; LHS
                                             ; Identifier - File fs
                                                push qword [rbp - -16]
                                          ; RHS
                                             push qword [.__field____main____File____children] ; stored index associated with field that is being accessed
                                          pop rdx ; rhs
                                          pop rax ; lhs
                                          push qword [rax + 8*rdx] ; lhs.rhs
                                    ; RHS
                                       push qword [.__field____main____Vector__File____data] ; stored index associated with field that is being accessed
                                    pop rdx ; rhs
                                    pop rax ; lhs
                                    push qword [rax + 8*rdx] ; lhs.rhs
                              ; OFFSET
                                 ; Identifier - int i
                                    push qword [rbp - 16]
                              pop rdx ; __offset
                              pop rax ; __pointer
                              push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                        ; Move arg0's result to reverse order position on stack
                        pop rax
                        mov qword [rsp + 0], rax
                     ; Call sum_small_dirs(File)
                     call .__main____sum_small_dirs__File
                     ; Remove args
                     add rsp, 8
                     ; Push return value
                     push rax
               pop rdx ; rhs value
               mov rax, qword [rbp - 8] ; read lhs value
               add rax, rdx      ; add lhs and rhs
               mov qword [rbp - 8], rax ; write back to lhs
               push rax          ; push result for other expressions
            ; Statement results can be ignored
            pop rdx
;------------------------------------------------------------------------
         ; Repeat
jmp .__for__99
         ; End of For
.__endfor__99:
;------------------------------------------------------------------------------
         ; Return
         ; Identifier - int sum
         push qword [rbp - 8]
         pop rax ; return value (int)
         ; Clean up stack and return
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
;---------------------------------------------------------------------------------
         ; Function Epilogue
         mov rsp, rbp ; remove local vars + unpopped pushes
         pop rbp
         ret
.__end____main____sum_small_dirs__File:
         ; End Function Declaration - sum_small_dirs(File) -> int
; =======================================================================================

         ; Assignment - '='
         ; RHS
         ; Int Literal
         mov rax, 70000000
         push rax
         ; LHS
         ; Variable Declaration - total_space
         mov rax, qword [rbp - 104]  ; __main__total_space
         pop rdx ; rhs value
         mov qword [rbp - 104], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
         ; RHS
         ; Int Literal
         mov rax, 30000000
         push rax
         ; LHS
         ; Variable Declaration - unused_space_needed
         mov rax, qword [rbp - 112]  ; __main__unused_space_needed
         pop rdx ; rhs value
         mov qword [rbp - 112], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
         ; RHS
         ; Subtraction - int, int
         ; LHS
         ; Identifier - int total_space
         push qword [rbp - 104]
         ; RHS
         ; Identifier - int unused_space_needed
         push qword [rbp - 112]
         pop rdx ; rhs
         pop rax ; lhs
         sub rax, rdx
         push rax
         ; LHS
         ; Variable Declaration - effective_space
         mov rax, qword [rbp - 120]  ; __main__effective_space
         pop rdx ; rhs value
         mov qword [rbp - 120], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
         ; RHS
         ; Subtraction - int, int
         ; LHS
         ; Member Accessor
         ; LHS
            ; Identifier - File root
               push qword [rbp - 24]
         ; RHS
            push qword [.__field____main____File____size] ; stored index associated with field that is being accessed
         pop rdx ; rhs
         pop rax ; lhs
         push qword [rax + 8*rdx] ; lhs.rhs
         ; RHS
         ; Identifier - int effective_space
         push qword [rbp - 120]
         pop rdx ; rhs
         pop rax ; lhs
         sub rax, rdx
         push rax
         ; LHS
         ; Variable Declaration - min_space_to_remove
         mov rax, qword [rbp - 128]  ; __main__min_space_to_remove
         pop rdx ; rhs value
         mov qword [rbp - 128], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
         ; Assignment - '='
         ; RHS
         ; Identifier - int total_space
         push qword [rbp - 104]
         ; LHS
         ; Variable Declaration - smallest
         mov rax, qword [rbp - 136]  ; __main__smallest
         pop rdx ; rhs value
         mov qword [rbp - 136], rdx
         push rdx
         ; Statement results can be ignored
         pop rdx
;---------------------------------------------------------------------------------------
         ; For-Loop
         ; Init
         ; Assignment - '='
         ; RHS
         ; Int Literal
         mov rax, 0
         push rax
         ; LHS
         ; Variable Declaration - i
         mov rax, qword [rbp - 144]  ; __main__for__101__i
         pop rdx ; rhs value
         mov qword [rbp - 144], rdx
         push rdx
         ; Loop init result can be discarded
         pop rax
         jmp .__forcond__101
.__for__101:
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
.__forcond__101:
         ; Condition
         ; Less Than
         ; LHS
         ; Identifier - int i
         push qword [rbp - 144]
         ; RHS
         ; Member Accessor
         ; LHS
            ; Identifier - Vector<:File:> all_files
               push qword [rbp - 40]
         ; RHS
            push qword [.__field____main____Vector__File____size] ; stored index associated with field that is being accessed
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
;---------------------------------------------------------------------------------
         ; Code Block
;------------------------------------------------------------------------------
         ; If-Statement
         ; Condition
         ; Member Accessor
            ; LHS
               ; Subscript
                  ; LHS
                     ; Member Accessor
                        ; LHS
                           ; Identifier - Vector<:File:> all_files
                              push qword [rbp - 40]
                        ; RHS
                           push qword [.__field____main____Vector__File____data] ; stored index associated with field that is being accessed
                        pop rdx ; rhs
                        pop rax ; lhs
                        push qword [rax + 8*rdx] ; lhs.rhs
                  ; OFFSET
                     ; Identifier - int i
                        push qword [rbp - 144]
                  pop rdx ; __offset
                  pop rax ; __pointer
                  push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
            ; RHS
               push qword [.__field____main____File____is_dir] ; stored index associated with field that is being accessed
            pop rdx ; rhs
            pop rax ; lhs
            push qword [rax + 8*rdx] ; lhs.rhs
         pop rdx ; __cond
         cmp rdx, 0 ; ensure condition is true
         je .__endif__103 ; jump to end
         ; Body
;------------------------------------------------------------------------
         ; Code Block
   ;---------------------------------------------------------------------
            ; If-Statement
               ; Condition
                  ; Greater Than or Equal to
                     ; LHS
                        ; Member Accessor
                           ; LHS
                              ; Subscript
                                 ; LHS
                                    ; Member Accessor
                                       ; LHS
                                          ; Identifier - Vector<:File:> all_files
                                             push qword [rbp - 40]
                                       ; RHS
                                          push qword [.__field____main____Vector__File____data] ; stored index associated with field that is being accessed
                                       pop rdx ; rhs
                                       pop rax ; lhs
                                       push qword [rax + 8*rdx] ; lhs.rhs
                                 ; OFFSET
                                    ; Identifier - int i
                                       push qword [rbp - 144]
                                 pop rdx ; __offset
                                 pop rax ; __pointer
                                 push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                           ; RHS
                              push qword [.__field____main____File____size] ; stored index associated with field that is being accessed
                           pop rdx ; rhs
                           pop rax ; lhs
                           push qword [rax + 8*rdx] ; lhs.rhs
                     ; RHS
                        ; Identifier - int min_space_to_remove
                           push qword [rbp - 128]
                     pop rdx ; rhs
                     pop rax ; lhs
                     cmp rax, rdx
                     setge al
                     movzx eax, al
                     push rax
                  pop rdx ; __cond
                  cmp rdx, 0 ; ensure condition is true
                  je .__endif__105 ; jump to end
               ; Body
         ;---------------------------------------------------------------
                  ; Code Block
            ;------------------------------------------------------------
                     ; If-Statement
                        ; Condition
                           ; Less Than
                              ; LHS
                                 ; Member Accessor
                                    ; LHS
                                       ; Subscript
                                          ; LHS
                                             ; Member Accessor
                                                ; LHS
                                                   ; Identifier - Vector<:File:> all_files
                                                      push qword [rbp - 40]
                                                ; RHS
                                                   push qword [.__field____main____Vector__File____data] ; stored index associated with field that is being accessed
                                                pop rdx ; rhs
                                                pop rax ; lhs
                                                push qword [rax + 8*rdx] ; lhs.rhs
                                          ; OFFSET
                                             ; Identifier - int i
                                                push qword [rbp - 144]
                                          pop rdx ; __offset
                                          pop rax ; __pointer
                                          push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                                    ; RHS
                                       push qword [.__field____main____File____size] ; stored index associated with field that is being accessed
                                    pop rdx ; rhs
                                    pop rax ; lhs
                                    push qword [rax + 8*rdx] ; lhs.rhs
                              ; RHS
                                 ; Identifier - int smallest
                                    push qword [rbp - 136]
                              pop rdx ; rhs
                              pop rax ; lhs
                              cmp rax, rdx
                              setl al
                              movzx eax, al
                              push rax
                           pop rdx ; __cond
                           cmp rdx, 0 ; ensure condition is true
                           je .__endif__107 ; jump to end
                        ; Body
                  ;------------------------------------------------------
                           ; Code Block
                              ; Assignment - '='
                                 ; RHS
                                    ; Member Accessor
                                       ; LHS
                                          ; Subscript
                                             ; LHS
                                                ; Member Accessor
                                                   ; LHS
                                                      ; Identifier - Vector<:File:> all_files
                                                         push qword [rbp - 40]
                                                   ; RHS
                                                      push qword [.__field____main____Vector__File____data] ; stored index associated with field that is being accessed
                                                   pop rdx ; rhs
                                                   pop rax ; lhs
                                                   push qword [rax + 8*rdx] ; lhs.rhs
                                             ; OFFSET
                                                ; Identifier - int i
                                                   push qword [rbp - 144]
                                             pop rdx ; __offset
                                             pop rax ; __pointer
                                             push qword [rax + 8*rdx] ; pointer + sizeof(data_t) * offset
                                       ; RHS
                                          push qword [.__field____main____File____size] ; stored index associated with field that is being accessed
                                       pop rdx ; rhs
                                       pop rax ; lhs
                                       push qword [rax + 8*rdx] ; lhs.rhs
                                 pop rdx ; rhs value
                                 mov qword [rbp - 136], rdx
                                 push rdx
                              ; Statement results can be ignored
                              pop rdx
                  ;------------------------------------------------------
                        jmp .__endif__107 ; jump to end of condition chain
                        ; End of if
.__endif__107:
            ;------------------------------------------------------------
         ;---------------------------------------------------------------
               jmp .__endif__105 ; jump to end of condition chain
               ; End of if
.__endif__105:
   ;---------------------------------------------------------------------
;------------------------------------------------------------------------
         jmp .__endif__103 ; jump to end of condition chain
         ; End of if
.__endif__103:
;------------------------------------------------------------------------------
;---------------------------------------------------------------------------------
         ; Repeat
jmp .__for__101
         ; End of For
.__endfor__101:
;---------------------------------------------------------------------------------------
         ; Function Call - println(int) -> void
         ; Make space for 1 arg(s)
         sub rsp, 8
         ; Arguments
         ; Eval arg0
         ; Identifier - int smallest
         push qword [rbp - 136]
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
; =======================================================================================
; ### END OF CODE #######################################################################
; =======================================================================================

         push 0
         call __builtin__exit__int
; =======================================================================================
; ### DATA SECTION ######################################################################
; =======================================================================================

         section .data
.str0: db '/', 10, 0
.float0: dq 0.0
.floatNegOne: dq -1.0
.floatZero: dq 0.0
.floatOne: dq 1.0
