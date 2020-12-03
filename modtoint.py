#import sys
#input = sys.stdin.readline

def get_original(x,Q,root):
    if x == 0:
        return "0"
    for i in range(1,root):
        if x*i%Q <= root:
            return str(x*i%Q) + "/" + str(i)
    return "we cannot expect"

def start_loop(Q):
    root = int( Q**(1/2))
    while True:
        x = int( input("Please input an integer mod Q: \n"))
        print("estimated of " + str(x) + ": " + get_original(x,Q,root))
    
def is_prime(N): #素因数
    middle = int( N**(1/2))
    for i in range(2, middle+1):
        if N%i == 0:
            return False
    return True

        
def main():
    # Q = 10**9+7
    # Q = 998244353
    Q = 10**9+7
    input_text = """please input a devisor Q:
1) 10**9+7(default)
2) 998244353
3) other
"""
    t = 1
    try:
        t = int( input(input_text))
    except ValueError:
        pass
    
    if t == 2:
        Q = 998244353
    if t == 3:
        print("please input a devisor Q:")
        while True:
            Q = int( input(""))
            if is_prime(Q):
                break
            print("please input a prime number")
    print("Q = " + str(Q))        
    start_loop(Q)
if __name__ == '__main__':
    main()
