from cffi import FFI

ffibuilder = FFI()

ffibuilder.cdef("unsigned long long factorial(int n);")

ffibuilder.set_source("_factorial",'''
    unsigned long long factorial(int n) {
        if (n < 0) return 0;
            
        if (n == 0 || n == 1) return 1;

        return n * factorial(n - 1);
    }
''')

ffibuilder.compile(verbose=True)
