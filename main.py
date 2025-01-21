from sys import exit

print('Welcome to The Fibonacci Sequence Generator!')

while True:
    user_input: str = input('Generate the Fibonacci sequence up to: ')

    if user_input == 'exit':
        print('Thanks for trying my program!')
        exit()
    if not user_input.isnumeric():
        print('Enter a whole number!')
        continue
    else:
        n: int = int(user_input)
        fib_num: int = 0
        count: int = 0
        fib_seq: list[int] = [fib_num]
        flag: bool = False
        while n != 0:
            if fib_num == 0:
                fib_num += 1
                fib_seq.append(fib_num)
                count += 1
            else:
                fib_num = fib_seq[count] + fib_seq[count-1]
                fib_seq.append(fib_num)
                count += 1
            if n in fib_seq:
                break
            if (fib_seq[-1] > n) and (len(fib_seq) > n):
                flag = True
                break
            
        if n in fib_seq:
            output: str = f'The Fibonacci sequence up to {n} is '
            for fib_num in fib_seq:
                if fib_seq.index(fib_num) != len(fib_seq)-1:
                    output += (str(fib_num) + ', ')
                else:
                    output += (str(fib_num) + '.')
                    
            print(output)
        
        if flag:
            output: str = f'The Fibonacci sequence up to the {n}th term is '
            for i in range(n):
                if i != n-1:
                    output += (str(fib_seq[i]) + ', ')
                else:
                    output += (str(fib_seq[i]) + '.')

            print(output)
