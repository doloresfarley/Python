def fibonacci(n):
    # Type your code here.
    if n <0:
        return -1
    elif n == 1 or n==0:
        print(n)
        return n
    elif n <0:
        return -1
    else:
       return fibonacci(n-1) + fibonacci(n-2)

if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')