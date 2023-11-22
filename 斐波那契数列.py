def fibonacci(n):
    fib_list = [0, 1]  # 前两个数为0和1
    
    if n <= 1:
        return fib_list[:n+1]
    
    while len(fib_list) <= n:
        next_num = fib_list[-1] + fib_list[-2]  # 下一个数为前两个数的和
        fib_list.append(next_num)
    
    return fib_list

# 测试输出斐波那契数列前10个数
n = 10
fib_seq = fibonacci(n)
print(fib_seq)
