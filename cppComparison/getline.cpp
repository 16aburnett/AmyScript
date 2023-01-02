#include <stdlib.h>
#include <stdio.h>

char* input ()
{
    char  *buffer = nullptr; //(char*) malloc (10*sizeof(char));
    size_t buflen = 0;
    getline(&buffer, &buflen, stdin);
    return buffer;
}

// Type your code here, or load an example.
int main ()
{
    char* line = input ();
    printf ("%s", line);
    free(line);
}