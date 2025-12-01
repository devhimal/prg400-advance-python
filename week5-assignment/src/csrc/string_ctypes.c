/* string_ctypes.c
   Builds a shared library with reverse(const char*) that returns malloc'd string.
*/
#include <string.h>
#include <stdlib.h>

char* reverse(const char* input) {
    if (!input) return NULL;
    int n = (int)strlen(input);
    char* out = (char*)malloc((size_t)n + 1);
    if (!out) return NULL;
    for (int i = 0; i < n; i++) {
        out[i] = input[n - i - 1];
    }
    out[n] = '\0';
    return out;
}

/* expose free to allow caller to free the returned pointer */
void free_ptr(void* p) {
    free(p);
}

