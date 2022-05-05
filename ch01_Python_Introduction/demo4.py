import pip
import ipython_genutils
import sys

print("current module=", __name__)
print("pip moudle name=", pip.__name__)
print("ipython module name=", ipython_genutils.__name__)
# print(f"sys_path ={sys.path}")

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


if __name__ == '__main__':
    print(sys.argv)
    fib(int(sys.argv[1]))