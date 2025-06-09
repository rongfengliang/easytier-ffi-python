from cffi import FFI

ffibuilder = FFI()
ffibuilder.set_source("easytier.easytier_cffi", None)
with open("easytier.h") as f:
    ffibuilder.cdef(f.read())

if __name__ == '__main__':
    ffibuilder.compile(verbose=True)